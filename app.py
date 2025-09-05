from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# Load PDFs
documents = SimpleDirectoryReader("Content", recursive=True).load_data()

# Use Ollama for both LLM and Embeddings
llm = Ollama(model="llama3")  

# Use HuggingFace for embeddings (local, no API key needed)
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Set defaults for LlamaIndex
Settings.llm = llm
Settings.embed_model = embed_model

# Build the index
index = VectorStoreIndex.from_documents(documents)

# Query engine
query_engine = index.as_query_engine(response_mode="accumulate")  

# Use model based on your preference
# "compact" → short answer (default earlier).
# "tree_summarize" → merges context from multiple sources, detailed + structured.
# "refine" → builds answer step by step, refining it each time (more nuanced).
# "accumulate" → dumps relevant chunks without much summarization (great for research).

while True:
    query = input("Ask a question (or type 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        break

    response = query_engine.query(query)

    print("\n📖 Detailed Answer:\n", response.response, "\n")

    if response.source_nodes:
        print("📂 Sources:")
        for idx, source in enumerate(response.source_nodes, start=1):
            file_name = source.metadata.get("file_name", "Unknown file")
            page = source.metadata.get("page_label", source.metadata.get("page_number", "N/A"))
            print(f"  {idx}. {file_name}, Page {page}")
    else:
        print("No sources found.")

    print("\n" + "=" * 80 + "\n")

