# 📄 RAG with Docling + Ollama 

A Streamlit-based RAG (Retrieval-Augmented Generation) app that lets you upload PDFs or excelsheets, index them with Docling, and chat with them using Ollama LLMs and HuggingFace embeddings.

---

## 🚀 Features

* Upload and preview  documents
* Index document using `DoclingReader`
* Use HuggingFace embeddings (BGE models) for retrieval
* Query document with Ollama models
* Interactive Streamlit chat UI

---

## ⚡ Quick Start

1.  **Install dependencies**
    ```bash
    pip install streamlit llama-index-llms-ollama llama-index-embeddings-huggingface llama-index-readers-docling pdfplumber
    ```

2.  **Run Streamlit app**
    ```bash
    streamlit run app.py
    ```

3.  **Pull a model in Ollama**- here `qwen3` used for pdfs and `mistral:latest` used for excelsheets.
    ```bash
    ollama pull qwen3
    ```
    *(or use any smaller model like `llama3.2:1b`, `mistral:7b-instruct-q4_K_M`)*

---

## 🐞 Issues Faced & Solutions

### 1. Duplicate Validator Error
You might encounter the following error:
`duplicate validator function "langchain_community.chat_models.openai.ChatOpenAI.validate_environment"`

> ✅ **Solution**: Uninstall `langchain` as it's not needed here:
> ```bash
> pip uninstall -y langchain langchain-community
> ```
> Or, add the following at the top of `app.py`:
> ```python
> import os
> os.environ["PYDANTIC_ALLOW_DUPLICATE_VALIDATORS"] = "1"
> ```

### 2. App Extremely Slow / Stuck for 10+ Mins
This often happens due to high memory usage. `ollama` was observed using 10+ GB RAM on an 8 GB Mac, leading to heavy swapping. Large embedding models like `bge-large-en-v1.5` also consume significant memory.

> ✅ **Solution**:
> * **Use smaller Ollama models**:
>     * `qwen2:1.5b`
>     * `llama3.2:1b`
>     * `mistral:7b-instruct-q4_K_M`
> * **Use smaller embeddings**:
>     ```python
>     HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
>     ```

---

## ✅ Recommended Setup for an 8 GB Mac

* **LLM**: `qwen2:1.5b`
* **Embeddings**: `bge-small-en-v1.5`
* **Caching**: Use `st.session_state` for caching models.
* **Monitor memory usage with**:
    ```bash
    ollama ps
    ```

---

## 📌 Notes

* The initial PDF indexing may take some time due to Docling parsing.
* After caching, subsequent queries should be fast (typically < 30 seconds).
* If your GPU (like Apple's MPS) causes memory issues, you can force CPU execution:
    ```bash
    OLLAMA_USE_MPS=0 streamlit run app.py
    ```