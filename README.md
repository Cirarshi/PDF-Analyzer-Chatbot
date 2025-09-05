# 📚 PDF Analyzer Chatbot

An interactive chatbot that lets you **chat with your PDFs** using **LlamaIndex**, **Ollama**, and **HuggingFace embeddings**.  

The project loads your PDF files, indexes them, and allows you to ask questions. Answers are generated with **detailed context**, and sources (file names and page numbers) are displayed for full transparency.  

---

## 🚀 Features
- 📂 **Upload PDFs** into the `data/` folder and chat with them.  
- 🤖 **Ollama LLM (Llama 3)** for answering your queries.  
- 🔍 **HuggingFace Embeddings** (`all-MiniLM-L6-v2`) for efficient PDF search.  
- 📖 **Detailed responses** powered by `tree_summarize` query mode.  
- 📝 Source references (file name + page numbers).  
- 🖥️ Simple command-line interface for Q&A.  

---

## 📦 Requirements
- Python **3.9+**
- [Ollama](https://ollama.com/) installed and running locally  
- Virtual environment (recommended)

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Cirarshi/PDF-Analyzer-Chatbot.git
cd pdf-analyzer-chatbot
```
###2. Create a virtual environment
```bash
python -m venv .venv
```
Activate it:

Windows (PowerShell):
```bash
.venv\Scripts\activate
```
Linux/macOS:
```bash
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Install and run Ollama
   
Download Ollama from Ollama’s website

Once installed, pull the Llama 3 model
```bash
ollama pull llama3
```
Keep Ollama running in the background:
```bash
ollama run llama3
```

5. Place all your PDFs inside the data/ folder:
```bash
data/
 ├── sample1.pdf
 ├── sample2.pdf
```

6. Run the chatbot
```bash
python app.py
```

---

## 📖 Usage
Once started, the program will continuously ask for your input.

---

## 📑 Project Structure
```bash
.
├── app.py                # Main chatbot code
├── requirements.txt      # Project dependencies
├── data/                 # Folder containing your PDFs
├── .venv/                # Virtual environment (ignored in git)
└── README.md             # Project documentation
```

---

## 📝 Notes
You can use model of your choice based on your preference out of the mentioned below
  - "compact" → short answer (default earlier).
  - "tree_summarize" → merges context from multiple sources, detailed + structured.
  - "refine" → builds answer step by step, refining it each time (more nuanced).
  - "accumulate" → dumps relevant chunks without much summarization (great for research).

---

## 📌 Roadmap
- Add Streamlit UI for web interface
- Enable multiple embedding models selection
- Support for summarizing entire PDFs in one command

---

## 🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss any major changes.

---

## 🚀 Future Implementations
Here are some ideas to take this project further:
1. Interactive Web UI
  - Build a frontend using Streamlit, Gradio, or React for a more user-friendly interface.
  - Allow drag-and-drop PDF uploads and a live chat experience.

2. Multi-Modal Support
  - Extend beyond PDFs to support Word docs, Excel sheets, and images (OCR).

3. Improved Citation Handling
  - Highlight exact text snippets from the PDF instead of just page numbers.
  - Add clickable links to jump directly to the referenced section.

4. Customizable LLM Options
  - Let users pick between different local models (e.g., Mistral, Gemma, Llama2/3) depending on hardware.

5. Enhanced Search
  - Add a hybrid keyword + semantic search for faster and more accurate retrieval.

6. Multi-User / Study Group Mode
  - Deploy as a local or cloud-based service where multiple users can query the same knowledge base.

7. Memory & Notes
  - Add a feature for saving queries and answers for future revision.
  - Option to export results into a personal study notebook.

8. Voice Interface
  - Integrate speech-to-text and text-to-speech for hands-free usage.

9. Fine-Tuned Models
  - Train embeddings or fine-tune the LLM on domain-specific study material (e.g., law, medicine, engineering).

---
