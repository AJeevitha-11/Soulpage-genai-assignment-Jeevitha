# Conversational Knowledge Bot

## Overview
This project implements a Conversational Knowledge Bot using LangChain.

Features:
- Conversational memory
- Wikipedia tool integration
- Streamlit chat interface
- Context-aware follow-up responses

## Architecture

User → Streamlit UI → LangChain Agent  
Agent → Memory + Wikipedia Tool  

## Installation

1. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run application:
   streamlit run app.py

## Example Interaction

User: Who is Elon Musk?  
Bot: (Wikipedia response)

User: When was he born?  
Bot: (Context-aware answer)

