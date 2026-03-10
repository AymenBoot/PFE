import os
from src.retrieval import get_retriever
from src.generation import generate_response
from src.safety_layer import check_emergency, get_medical_disclaimer

def main():
    print("--- Chatbot Intelligent d'Aide aux Premiers Secours (Architecture RAG) ---")
    
    # 1. Initialisation du Retriever local
    try:
        retriever = get_retriever()
        print("Systeme pret. Tapez 'quitter' pour fermer.")
    except Exception as e:
        print(f"Erreur de chargement : {e}")
        return
    
    while True:
        user_input = input("\nUtilisateur : ")
        
        if user_input.lower() in ["quitter", "exit", "stop"]:
            break
            
        # 2. Safety Layer : Detection automatique des urgences
        if check_emergency(user_input):
            print("\nALERTE : Situation critique detectee !")
            print("Appelez les secours (15 ou 112) immediatement.")
            
        # 3. Generation RAG
        try:
            answer = generate_response(user_input, retriever)
            print(f"\nAssistant : {answer}")
            print(get_medical_disclaimer())
        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()