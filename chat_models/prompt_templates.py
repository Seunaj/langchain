from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano")

# Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system", "You are an {role} in {organization}."),
    ("human", "Tell me something about {division} in {organization}."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"role": "AI assistant", "organization": "Argonne", "division": "ALCF"})
result = llm.invoke(prompt)
print(result.content)

