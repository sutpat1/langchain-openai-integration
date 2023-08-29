from langchain.llms import OpenAI
import os

print('Hello World')
OPENAI_API_KEY="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"
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY
llm = OpenAI(temperature = 0.2)
response = llm.predict("what is population of united states?")
print(response)