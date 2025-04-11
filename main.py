from langchain.llms import OpenAI
import os

print('Hello World')
OPENAI_API_KEY="hiddenKey"
#replace hiddenKey with your own OpenAI API key
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY
llm = OpenAI(temperature = 0.2)
response = llm.predict("what is population of united states?")
print(response)

