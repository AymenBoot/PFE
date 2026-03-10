import os
import shutil

# Définition de l'arborescence cible
folders = [
    "data/raw",
    "data/processed",
    "vector_db/faiss_index",
    "src",
    "notebooks"
]

files = {
    "src/ingestion.py": "# Extraction PDF et Indexation FAISS\n",
    "src/retrieval.py": "# Recherche sémantique\n",
    "src/generation.py": "# Appel API OpenAI\n",
    "src/safety_layer.py": "# Détection d'urgence et Disclaimer\n",
    "requirements.txt": "langchain\nfaiss-cpu\nsentence-transformers\npypdf\nopenai\npython-dotenv\n",
    ".env": "OPENAI_API_KEY=votre_cle_ici\n",
    "main.py": "import os\nprint('Chatbot Premiers Secours Ready')\n"
}

def setup():
    # 1. Créer les dossiers
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # 2. Déplacer tes PDF existants vers data/raw
    for item in os.listdir('data'):
        if item.endswith('.pdf'):
            old_path = os.path.join('data', item)
            new_path = os.path.join('data/raw', item)
            shutil.move(old_path, new_path)
            print(f"✔️ Déplacé: {item} -> data/raw/")

    # 3. Créer les fichiers de code
    for path, content in files.items():
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📄 Créé: {path}")

if __name__ == "__main__":
    setup()