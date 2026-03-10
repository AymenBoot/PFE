import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_response(query, retriever):
    # Utilisation du modele LLM Online (OpenAI GPT) via API [cite: 8, 12]
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        temperature=0, 
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Definition du prompt pour reduire les hallucinations [cite: 3, 9]
    template = """Utilisez les extraits de documents fournis pour repondre a la question. 
    Si vous ne connaissez pas la reponse, dites que vous ne savez pas.
    
    Contexte: {context}
    
    Question: {question}
    """
    
    prompt = ChatPromptTemplate.from_template(template)

    # Creation de la chaine RAG moderne (Architecture technique) [cite: 7, 11]
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Generation de la reponse [cite: 32]
    return rag_chain.invoke(query)