import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY не найден. Проверь файл .env или Environment Variables."
    )
app = Flask(__name__)


# =========================================================
# LOAD RAG SYSTEM
# =========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db_v2",
    embedding_function=embeddings
)
print("Documents in Chroma:", vectorstore._collection.count())

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 6}
)

prompt = ChatPromptTemplate.from_template("""
You are Real Madrid AI, an expert assistant specialized in
Real Madrid Club de Fútbol.

Use only the provided knowledge-base context.

Rules:
- Answer clearly and accurately.
- Check all context passages carefully.
- Do not invent facts.
- Answer in the same language as the user's question.
- If the answer is not in the context, say:
  "I couldn't find that information in my knowledge base."

Context:
{context}

Question:
{question}

Answer:
""")

llm = ChatGoogleGenerativeAI(
    # Put here the Gemini model that worked in your notebook
    model="gemini-3.1-flash-lite-preview",
    temperature=0
)

answer_chain = prompt | llm | StrOutputParser()


def format_documents(documents):
    return "\n\n".join(
        document.page_content
        for document in documents
    )


# =========================================================
# ROUTES
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask_question():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is empty."
            }), 400

        question = data.get("question", "").strip()

        if not question:
            return jsonify({
                "error": "Please enter a question."
            }), 400

        source_documents = retriever.invoke(question)

        context = format_documents(source_documents)

        answer = answer_chain.invoke({
            "context": context,
            "question": question
        })

        sources = []

        for index, document in enumerate(source_documents, start=1):
            content = document.page_content.strip()

            if len(content) > 500:
                content = content[:500] + "..."

            sources.append({
                "number": index,
                "source": document.metadata.get(
                    "source",
                    "Real Madrid Knowledge Base"
                ),
                "content": content
            })

        return jsonify({
            "answer": answer,
            "sources": sources
        })

    except Exception as error:
        print("ERROR:", error)

        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )