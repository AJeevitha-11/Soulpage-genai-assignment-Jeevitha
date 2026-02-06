Overview
--------
This project implements a Conversational Knowledge Bot using LangChain.

The bot is capable of:
- Maintaining conversational memory
- Fetching real-time factual data using the Wikipedia tool
- Providing context-aware follow-up responses
- Running through an interactive Streamlit chat interface

Features
--------
- Conversational Memory using ConversationBufferMemory
- Wikipedia Tool Integration for factual information retrieval
- Context-aware follow-up handling
- Streamlit-based Chat UI
- Live Deployment on Streamlit Cloud

Architecture
------------
User  
  ↓  
Streamlit Chat UI  
  ↓  
LangChain Agent (AgentExecutor)  
  ↓  
ConversationBufferMemory  
  ↓  
Wikipedia Tool  
  ↓  
LLM (OpenAI)  
  ↓  
Final Response to User

Memory Used
-----------
- ConversationBufferMemory (LangChain)
- Maintains previous conversation context
- Enables follow-up questions like:

User: Who is Elon Musk?
User: When was he born?

Tools Integrated
----------------
WikipediaQueryRun
   ~ Fetches factual and updated information from Wikipedia

LLM Used
--------
OpenAI GPT Model (e.g., GPT-3.5 / GPT-4)

Installation & Setup

1)Clone the repository:
-----------------------
git clone https://github.com/AJeevitha-11/Soulpage-genai-assignment-Jeevitha
        
2)Create a virtual environment:
-------------------------------
 python -m venv venv
 venv\Scripts\activate

3)Install dependencies:
 pip install -r requirements.txt

4)Run the application:
 streamlit run app.py

Example Interaction
-------------------
User: Who is Elon Musk?
Bot: (Fetches information using Wikipedia tool)

User: When was he born?
Bot: (Uses memory to understand "he" refers to Elon Musk and responds correctly)

Live Demo
---------
Streamlit Deployment:
👉 https://soulpage-genai-assignment-jeevitha-kuya24l4pxbvaogwfkta6s.streamlit.app/

Main Libraries Used
-------------------
langchain==0.1.16
langchain-openai==0.0.8
openai==1.14.3
streamlit==1.32.2
wikipedia==1.4.0
python-dotenv==1.0.1
huggingface_hub==0.23.0

This project fulfills the requirements of Task-2 by integrating LangChain tools, conversational memory, and a context-aware chat interface.
