🚀 Features
Predictive Analytics: Uses a Machine Learning model to estimate Teacher Effectiveness Scores based on class size and student performance.

Dynamic Knowledge Base: Upload PDF or TXT documents to power a RAG (Retrieval-Augmented Generation) system for context-aware answers.

Intelligent Fallback: A 4-tier response hierarchy:

ML Prediction (Triggered by "predict" keywords)

RAG Search (Context from uploaded documents)

Rule-Based Logic (Pre-defined pedagogical insights)

Web Fallback (Automated Google search for external queries)

Customizable Modes: Toggle between Concise and Detailed responses via the sidebar.

📁 Project Structure

├── app.py              # Main Streamlit application entry point
├── config/
│   └── config.py       # Environment variables and API keys (Internal)
├── utils/
│   ├── rag_utils.py    # Document processing and vector search logic
│   ├── ml_utils.py     # Machine Learning model inference
│   └── web_utils.py    # External search and web integration
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

🛠️ Installation & Setup
Clone the Repository:
git clone https://github.com/your-username/ai-teacher-assistant.git
cd ai-teacher-assistant

Set Up Environment Variables:
Create a config/config.py file. Do not commit your actual API keys.

# config/config.py
import os
API_KEY = "your_secret_key_here"

Install Dependencies:
pip install -r requirements.txt

Run the App:
streamlit run app.py
