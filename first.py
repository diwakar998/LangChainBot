pip install -U langchain langchain-openai

LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="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"
LANGSMITH_PROJECT="firstLangAgent"
OPENAI_API_KEY = "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"
#OPENAI_API_KEY="<your-openai-api-key>"

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")

