
# 🧠 Bruce Agent

**AgentX** is a lightweight, extensible agentic framework for building custom LLM agents with structured tool use, prompt templates, and integration with OpenAI and Gemini models.

## 🚀 Features

- 🔁 Custom reasoning loop (`AgentRunner`)
- 🧩 Structured tool execution (Pydantic-based)
- 💬 Prompt templating and management
- 🔌 LLM-agnostic: supports **OpenAI function calling** and **Google Gemini**
- 🪄 Easy-to-use API for building agents

## 📦 Installation

published to PyPI:

```sh
pip install AgentX-Dev
```

## Example use

```python
from AgentXL import AgentRunner, AgentType,ChatModel
from pydantic import BaseModel
from AgentXL.Tools import StructuredTool,StandardTool
# Define a sample Stuctured tool
class MultiplyTool(BaseModel):
    a: int
    b: int

def multiply(a: int, b: int) -> int:
    return a * b

# Define a sample Standard tool
def Weather(weather:str):
    return f"{weather} is currently at 28 degree with a high of 32 and a low of 18 "

# Create chat model and agent
ReAct=AgentType.ReAct
chat_model = ChatModel.GPT(model="gpt-4", temperature=0.7)
tools = [StructuredTool(name="MultiplyTool",
                        description="useful when you need to add two numbers",
                        func=multiply,
                        args_schema=MultiplyTool
                        ),
         StandardTool(name="Weather",
                      description="when you need to check the weather of a location, input should be the str of the location",
                      func=Weather)]
# Create an AgentRunner instance
agent = AgentRunner(model=chat_model,Agent=ReAct, tools=tools)

# Initialize the agent with user input
response = agent.Initialize("What is 5 times 8?")

# Print the result
print(response.content)


# output the Agent completion
agent.Initialize("i need the weather in Barrie")


```

``` bruce_framework/
├── src/
│   └── bruce_framework/
│       ├── __init__.py
│       ├── agent/
│       │   ├── __init__.py
│       │   └── agent.py
│       ├── runner/
│       │   ├── __init__.py
│       │   └── agent_run.py
│       └── chatmodel.py
├── README.md
├── LICENSE
└── pyproject.toml

```

## 📚 Documentation (Coming Soon)
### More tutorials, tool examples, and structured prompting guides coming soon.

## 🧑‍💻 Author
#### Bruce-Arhin Shadrach
#### 📧 brucearhin098@gmail.com
#### 🌐 GitHub

📝 License
MIT License



