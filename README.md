# GenAI using LangChain

Welcome to my **Generative AI Learning Journey** using **LangChain**, one of the most powerful frameworks for building with LLMs. This project documents my weekly learning, experiments, and mini-apps during the summer break while exploring key concepts of Large Language Models (LLMs), Chat Models, Embedding Models, and inference techniques.

> ⚠️ **Note:** This repository is a **work in progress** and will be updated weekly as I continue to learn and build with LangChain. Stay tuned for more updates!

## 🧠 Project Overview

The primary goal is to **understand and build foundational GenAI components** using LangChain, APIs like OpenAI/Gemini, and local inference with HuggingFace models. The weekly structure allows me to gradually master concepts from simple prompts to complete retrieval-augmented generation (RAG) systems.

Here’s what’s included:

1. **📘 Week-wise Study Notes**
   - Organized in the `Study_Notes/` folder
   - Includes handwritten explanations, flowcharts, and breakdowns of models
   - Format: `Week_1_GenAI_LangChain`, `Week_2_RAG_Systems`, etc.

2. **🔍 LLMs and Chat Models**
   - Used OpenAI’s `gpt-3.5-turbo-instruct`, Gemini’s `gemini-1.5-pro`, and open-source local models like `TinyLlama-1.1B-Chat`
   - Explored temperature, top_p, and token limits for controlled generation

3. **🧮 Embedding Models**
   - Used both API-based and local embedding models
   - Compared semantic similarity using OpenAI (`text-embedding-3-large`) and HuggingFace (`all-MiniLM-L6-v2`)

4. **🔧 Mini Projects**
   - A small app for semantic similarity and document embedding using LangChain
   - Demonstrated invoking models, chaining responses, and memory handling

---

## 📁 Repository Structure

```

GenAI-using-LangChain/
├── ChatModels/                   # LLM & Chat Model Examples
├── Embedding Models/             # Semantic search and embeddings
├── LLMs/                         # LangChain LLMs logic
├── ER/                           # Evaluation & Retrieval modules
├── Study\_Notes/                 # Weekly learning notes (handwritten + images)
│   └──Week_1_GenAI_LangChain/    # Keeps the folder in version control
├── requirements.txt              # Project dependencies
├── .env                          # API keys and environment variables
├── README.md                     # Project documentation

````

---

## 🛠️ Getting Started

1. **Clone the Repository**
git clone
```bash
https://github.com/MTalhaZafar32/GenAI-using-LangChain.git
````

2. **Create a Virtual Environment**

```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# or on macOS/Linux
source venv/bin/activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Run Sample Scripts**

```bash
python test.py
```

---

## 📝 Study Notes (Weekly)

The `Study_Notes` folder will be updated weekly with new learnings including:

* ✍️ Handwritten breakdowns (PDF)
* 🔁 Model workflows
* 💡 Concepts & use cases from GenAI world

Examples:

* Week\_1: GenAI Foundations, LLMs vs ChatModels, API vs Local Inference

---


## 🤝 Contributions

If you're exploring LangChain or building similar GenAI projects, feel free to fork this repo, open issues, or share ideas through pull requests. Collaboration = Innovation 🤝

---

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for more details.
