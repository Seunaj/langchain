from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano")

result = llm.invoke("Do you know anything about HPC research in Argonne? Give a short summary.")

print(result.content)

