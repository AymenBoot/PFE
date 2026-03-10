from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def get_retriever():
    # Chargement du modele d'embeddings et de la base locale
    vector_db_path = "vector_db/faiss_index"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Chargement de l'index avec autorisation de deserialisation
    vectorstore = FAISS.load_local(
        vector_db_path, 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    
    # Configuration du moteur de recherche (Top-3 passages)
    return vectorstore.as_retriever(search_kwargs={"k": 3})