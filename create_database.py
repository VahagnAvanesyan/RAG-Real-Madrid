from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


BASE_DIR = Path(__file__).resolve().parent

DOCUMENT_PATH = BASE_DIR / "documents" / "real_madrid_rag_dataset.txt"
DB_PATH = BASE_DIR / "chroma_db_v2"


if not DOCUMENT_PATH.exists():
    raise FileNotFoundError(
        f"Файл базы знаний не найден: {DOCUMENT_PATH}"
    )


loader = TextLoader(
    str(DOCUMENT_PATH),
    encoding="utf-8"
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print("Created chunks:", len(chunks))


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=str(DB_PATH)
)

print("Documents saved:", vectorstore._collection.count())
print("Database created:", DB_PATH)