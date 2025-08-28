# Setup simple agent

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv() # load the environment variable we created in env 

# Setup in LLM, give it to an agent and then give the agent some tools

llm = ChatOpenAI(model= "gpt-4o-mini") # use can use openai key or anything
# llm = ChatAnthropic(model = "claude-3-5-sonnet-20241022") # add the model with version

# Test your API key
response = llm.invoke("What is the meaning of life?")
print(response)