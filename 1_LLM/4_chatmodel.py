from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model = "Fable-5")

result = llm.invoke("what is AI all about?")

print(result.content)