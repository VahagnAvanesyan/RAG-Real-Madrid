<div align="center">

# ⚽ Real Madrid AI Assistant

### 🤖 AI-powered RAG Chatbot for Real Madrid Fans

Ask anything about the history, legends, trophies, stadium, players, coaches, and achievements of the greatest football club in history.

<img src="static/images/logo.jpg" width="180">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-blue)
![Gemini](https://img.shields.io/badge/Gemini-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-red)

</div>

---

# 📖 Overview

This project is an AI-powered chatbot built using **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on the language model, the assistant searches through a custom Real Madrid knowledge base using semantic search and generates accurate responses with Google's Gemini model.

The chatbot can answer questions about:

- 🏆 Club History
- 👑 Legendary Players
- ⚽ Current Squad
- 🏟 Santiago Bernabéu Stadium
- 🧠 Coaches
- 🥇 Trophies
- 📅 Important Matches
- ⭐ Club Legends
- 📚 Interesting Facts

---

# 🚀 Demo

<img width="1917" height="801" alt="image" src="https://github.com/user-attachments/assets/2a888559-3678-4cb7-b8d8-22c140a9675c" />


# 🛠 Tech Stack

- Python
- Flask
- LangChain
- Google Gemini
- ChromaDB
- HuggingFace Embeddings
- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```text
RAG_Football/
│
├── app.py
├── create_database.py
├── requirements.txt
├── .env
│
├── documents/
│   └── real_madrid_rag_dataset.txt
│
├── chroma_db_v2/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│       ├── logo.jpg
│       ├── bernabeu_1.jpg
│       └── bernabeu_2.jpg
│
└── real_madrid.ipynb
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/RAG-Real-Madrid.git
```

Go to the project

```bash
cd RAG-Real-Madrid
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 💬 Example Questions

- When was Real Madrid founded?
- Who has scored the most goals?
- How many Champions League trophies does Real Madrid have?
- Tell me about Cristiano Ronaldo.
- Who is Santiago Bernabéu?
- Where does Real Madrid play?
- Who is the current coach?
- Tell me about La Fábrica.

---

# 🧠 How It Works

```text
User Question
      │
      ▼
Flask Backend
      │
      ▼
LangChain
      │
      ▼
ChromaDB
      │
      ▼
Relevant Documents
      │
      ▼
Gemini LLM
      │
      ▼
Final Answer
```

---

# ✨ Features

- AI-powered answers
- Retrieval-Augmented Generation (RAG)
- Semantic search
- Beautiful responsive UI
- Suggested questions
- Stadium background animation
- Real Madrid knowledge base
- Fast responses

---

# 📊 Future Improvements

- Voice Chat
- Player Images
- Match Statistics
- Live Fixtures
- Transfer News
- Dark / Light Theme
- Multi-language Support

---

# 👨‍💻 Author

**Vahagn Avanesyan**

AI / Machine Learning Enthusiast

GitHub:
https://github.com/VahagnAvanesyan

---

<div align="center">

### ⭐ If you like this project, don't forget to leave a star!

**Hala Madrid! 🤍⚽**

</div>
