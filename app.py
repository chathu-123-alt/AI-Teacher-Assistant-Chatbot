import streamlit as st
from utils.rag_utils import search_knowledge
from utils.web_utils import open_google
from utils.ml_utils import predict_score

st.set_page_config(page_title="AI Teacher Assistant", layout="wide")

st.title("🎓 AI Teacher Assistant Chatbot")

with st.sidebar:
    st.header("📄 Knowledge Base")
    uploaded_file = st.file_uploader("Upload Document (TXT/PDF)", type=["txt", "pdf"])
    if uploaded_file:
        from utils.rag_utils import process_uploaded_file
        process_uploaded_file(uploaded_file)
        st.success("Knowledge Base Updated!")
        
    st.markdown("---")
    st.markdown("### 📊 Enter Details for Prediction")
    class_size = st.slider("Class Size", 10, 100, 30)
    student_score = st.slider("Student Score", 0, 100, 75)
    
    st.markdown("---")
    mode = st.radio("Response Mode", ["Concise", "Detailed"], horizontal=True)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask your question...")

def get_rule_based_response(question, mode):
    question = question.lower()

    if "teacher effectiveness" in question:
        return "Teacher effectiveness improves student outcomes." if mode == "Concise" else \
               """Teacher effectiveness refers to how well a teacher enhances student learning and performance.

🔍 Key Points:
• Teaching quality  
• Student engagement  
• Performance measurement"""

    if "class size" in question:
        return "Class size affects attention." if mode == "Concise" else \
               """Class size plays a crucial role in learning.

🔍 Key Points:
• Smaller classes improve interaction  
• More individual attention  
• Better student engagement"""

    return None

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # 🔥 1. ML Prediction
    if "predict" in user_input.lower():
        try:
            features = [class_size, student_score]
            result = predict_score(features)
            response = f"📊 Predicted Teacher Effectiveness Score: {result}"
        except:
            response = "⚠️ Error in prediction model."

    else:
        # 🔍 2. RAG
        rag_response = search_knowledge(user_input, mode)

        if rag_response:
            response = rag_response
        else:
            # 🧠 3. Rule-based
            rule_response = get_rule_based_response(user_input, mode)

            if rule_response:
                response = rule_response
            else:
                # 🌐 4. Web fallback
                response = "🌐 Searching on Google..."
                open_google(user_input)

    # Show bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)