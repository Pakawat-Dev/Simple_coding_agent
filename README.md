# AI Coding Agent

🤖 AI-powered coding assistant with automatic code execution using AutoGen and OpenAI.

## Features

- **Smart Programmer**: Senior-level AI coder (GAP_Coder)
- **Code Execution**: Automatic local command line execution
- **Interactive Workflow**: Code generation → execution → feedback loop
- **Work Directory**: Isolated `coding/` folder for safe execution

## Setup

1. Install dependencies:
```bash
pip install autogen-agentchat autogen-ext[openai] python-dotenv
```

2. Create `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

```bash
python simple_coding_agent.py
```

The agent will automatically:
1. Generate Python code based on the given task
2. Execute the code in the `coding/` directory
3. Provide feedback and results

## Configuration

- **Model**: GPT-4.1 with OpenAI
- **Execution**: LocalCommandLineCodeExecutor
- **Work Directory**: `./coding/`
- **Termination**: Text mention "TERMINATE"

## Agents

- **GAP_Coder**: Senior programmer agent that writes practical code
- **code_executor**: Executes code locally and provides output

## Example Task

Default task: "Provide code to create a Python function that can add multiply three numbers and return the result."
