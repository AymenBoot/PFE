import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def run_ingestion():
    # Configuration des chemins selon l'architecture technique
    raw_data_path = "data/raw"
    vector_db_path = "vector_db/faiss_index"
    
    if not os.path.exists("vector_db"):
        os.makedirs("vector_db")
    
    documents = []
    
    # 1. Extraction PDF (OMS, Croix-Rouge)
    print("--- Etape 1: Chargement des documents PDF ---")
    pdf_files = [f for f in os.listdir(raw_data_path) if f.endswith(".pdf")]
    
    for file in pdf_files:
        loader = PyPDFLoader(os.path.join(raw_data_path, file))
        documents.extend(loader.load())
    
    # 2. Decoupage en chunks (Methodologie Scientifique)
    print("--- Etape 2: Decoupage en segments (Chunking) ---")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )
    final_docs = text_splitter.split_documents(documents)
    print(f"Nombre de segments crees: {len(final_docs)}")

    # 3. Generation des Embeddings (Sentence-Transformers)
    print("--- Etape 3: Creation des vecteurs (Embeddings) ---")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Sauvegarde locale FAISS (Adaptation RAM limitee)
    print("--- Etape 4: Indexation et sauvegarde FAISS ---")
    vectorstore = FAISS.from_documents(final_docs, embeddings)
    vectorstore.save_local(vector_db_path)
    
    print("Succes: Base de donnees vectorielle prete.")

if __name__ == "__main__":
    run_ingestion()