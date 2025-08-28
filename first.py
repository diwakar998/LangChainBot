#pip install -U langchain langchain-openai
import streamlit as st
LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY=st.secrets["LANGSMITH_API_KEY"]
#"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"
LANGSMITH_PROJECT="firstLangAgent"
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
#OPENAI_API_KEY="<your-openai-api-key>"

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")

