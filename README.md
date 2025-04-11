# LangChain OpenAI Question Answering

A simple Python application that uses **LangChain** and **OpenAI** to answer questions with natural language processing.

## 🤖 Overview
This application demonstrates how to set up and use the LangChain library with OpenAI's language models to create a basic question-answering system.

---

## 🚀 Features
- 🔗 **LangChain Integration**: Utilizes the LangChain framework for working with large language models.
- 🧠 **OpenAI API**: Connects to OpenAI's powerful language models for question answering.
- 🌡️ **Temperature Control**: Configurable temperature parameter to control response creativity.
- 🔑 **API Key Management**: Example of how to set environment variables for API access.

---

## 🛠️ Tech Stack
- **Language**: Python
- **Framework**: LangChain
- **AI Provider**: OpenAI
- **Dependencies**: langchain, openai

---

## 📁 File Structure
<pre lang="markdown">
├── main.py                 # Main script that runs the question-answering functionality
└── README.md               # Project documentation
</pre>

---

## 🚀 Getting Started

### Prerequisites
* Python 3.7 or higher
* OpenAI API key

### Installation

1. Clone the repository

   `git clone https://github.com/yourusername/langchain-openai-qa.git`
   `cd langchain-openai-qa`

2. Install dependencies

   `pip install langchain openai`

3. Set up your OpenAI API key
   
   Either add it directly to the script (not recommended for production) or set it as an environment variable:
   
   `# On Linux/Mac`
   `export OPENAI_API_KEY="your-api-key-here"`
   
   `# On Windows`
   `set OPENAI_API_KEY=your-api-key-here`

4. Run the application

   `python main.py`

## 💻 Usage Example

The current script is configured to ask OpenAI about the population of the United States:

```python
from langchain.llms import OpenAI
import os

# Set your API key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# Initialize the language model with a temperature of 0.2 (more factual)
llm = OpenAI(temperature=0.2)

# Ask a question
response = llm.predict("what is population of united states?")
print(response)
