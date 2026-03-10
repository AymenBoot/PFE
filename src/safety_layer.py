def check_emergency(user_query):
    # Liste de mots-cles pour la detection automatique des situations critiques
    critical_keywords = ["inconscient", "hemorragie", "etouffement", "arret cardiaque", "ne respire plus"]
    
    query_lower = user_query.lower()
    for word in critical_keywords:
        if word in query_lower:
            return True
    return False

def get_medical_disclaimer():
    # Disclaimer obligatoire pour la reduction des risques
    return "\n(Note: Cette reponse est generee par une IA. En cas d'urgence, contactez les secours au 15 ou 112.)"