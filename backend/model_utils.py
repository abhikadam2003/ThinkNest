from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.settings import Settings

# ✅ Use lightweight model compatible with your system RAM
embed_model = OllamaEmbedding(model_name="tinyllama")  # Small and fast embedding model
llm_model = Ollama(model="tinyllama")  # Small and fast LLM

# Apply to global settings (optional but recommended)
Settings.embed_model = embed_model
Settings.llm = llm_model

def create_vector_index(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    return index

def search_from_index(index, query):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return str(response)
