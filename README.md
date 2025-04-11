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
```

To modify the question, simply change the text inside the llm.predict() function.

### Adjusting Temperature

The temperature parameter controls how creative the model's responses will be:
- Lower values (0.0-0.3): More deterministic, factual responses
- Higher values (0.7-1.0): More creative, varied responses

```python
# For more creative responses
llm = OpenAI(temperature=0.8)

# For more factual responses
llm = OpenAI(temperature=0.1)
```

---

## 📝 Notes on API Keys

- Never commit your API keys to version control
- For production applications, use environment variables or a secure secrets manager
- The current implementation in main.py is for demonstration purposes only

---

## 🔍 Further Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Security Best Practices for API Keys](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Acknowledgements

* LangChain team for the excellent framework
* OpenAI for providing the language model API
