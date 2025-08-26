import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo, ModelFamily, SystemMessage, UserMessage, AssistantMessage
from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

async def main():
    print("\n" + "═" * 60)
    print("🤖 AI CODING AGENT WITH CODE EXECUTION")
    print("│")
    print("│  💻 Programmer: GAP_Coder")
    print("│  ⚡ Executor: LocalCommandLineCodeExecutor")
    print("│  🔧 Model: GPT-4.1 with OpenAI")
    print("═" * 60 + "\n")

    model_client_openai = OpenAIChatCompletionClient(
        model="gpt-4.1", 
        api_key=os.environ["OPENAI_API_KEY"],
        model_info=ModelInfo(
            vision=True,        
            function_calling=True,
            json_output=True,
            family=ModelFamily.GPT_41,
        )
    )

    programmer_agent = AssistantAgent(
        name="GAP_Coder",
        system_message="""
You're a senior and creative programmer who writes practical codes.
IMPORTANT: Wait for execute your code and then you can reply with the word "TERMINATE".
DO NOT OUTPUT "TERMINATE" after your code block.
""",
        model_client=model_client_openai, 
    )

    code_executor = CodeExecutorAgent(
        name="code_executor",
        code_executor=LocalCommandLineCodeExecutor(work_dir="coding")
    )

    termination = TextMentionTermination(text="TERMINATE")

    team = RoundRobinGroupChat(
        participants=[programmer_agent, code_executor],
        termination_condition=termination,
    )

    print("🚀 Starting coding session...\n")
    stream = team.run_stream(task="Provide code to create a Python function that can add multiply three numbers and return the result.")
    await Console(stream)
    print("\n✅ Coding session complete.\n")

if __name__ == "__main__":
    asyncio.run(main())