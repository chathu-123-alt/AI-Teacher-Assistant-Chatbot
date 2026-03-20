import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key) if api_key else None

def load_knowledge():
    try:
        with open("data/knowledge.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def search_knowledge(query, mode="Concise"):
    context = load_knowledge()
    
    if not context:
        return None

    # Helper function for basic keyword matching if API fails
    def get_basic_match():
        lines = context.split("\n")
        query_words = query.lower().split()
        best_match = ""
        max_score = 0
        for line in lines:
            score = sum(1 for word in query_words if word in line.lower())
            if score > max_score:
                max_score = score
                best_match = line
        return best_match if max_score > 0 else None
        
    if not client:
        return get_basic_match()
        
    length_instruction = "Keep your answer brief and concise (a few sentences at most)." if mode == "Concise" else "Provide a detailed and thorough explanation with bullet points if helpful."

    prompt = f"""You are a helpful AI Teacher Assistant. 
Use the following knowledge base context to answer the user's question accurately and conversationally.
{length_instruction}
If the context doesn't contain the answer, you can use your general knowledge, but prioritize the provided context.

Context:
{context}

Question: {query}
"""
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant"
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq API Error: {e}")
        # Fallback to basic keyword matching
        return get_basic_match()

import PyPDF2

def process_uploaded_file(uploaded_file):
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    else:
        text = uploaded_file.getvalue().decode("utf-8")
        
    with open("data/knowledge.txt", "w") as f:
        f.write(text)