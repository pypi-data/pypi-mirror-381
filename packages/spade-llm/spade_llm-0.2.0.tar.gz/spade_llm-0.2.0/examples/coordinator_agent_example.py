"""
CoordinatorAgent Example

This example demonstrates how to use the CoordinatorAgent class to coordinate
multiple subordinate agents in a shared conversation context.

PREREQUISITES:
1. Start SPADE built-in server in another terminal:
   spade run

2. Install dependencies:
   pip install spade_llm

DEBUGGING:
- Default: INFO level logging for main coordination flow
- Verbose: Set environment variable DEBUG=true for detailed SPADE_LLM debug logs

This example uses SPADE's default built-in server (localhost:5222) - no account registration needed!
"""

import asyncio
import logging
import time
import os
import spade
from spade.message import Message
from spade_llm.agent.coordinator_agent import CoordinatorAgent
from spade_llm.agent.llm_agent import LLMAgent
from spade_llm.agent.chat_agent import ChatAgent
from spade_llm.providers.llm_provider import LLMProvider
from spade_llm.utils import load_env_vars

# Configure logging for debugging
DEBUG_MODE = os.environ.get("DEBUG", "false").lower() == "true"

logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("spade_llm").setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)
logging.getLogger("spade").setLevel(logging.INFO if DEBUG_MODE else logging.WARNING)

logger = logging.getLogger("coordinator_example")


async def run_coordination_example():
    """
    Example showing CoordinatorAgent coordinating multiple subagents
    """
    logger.info("*** Starting CoordinatorAgent example...")

    load_env_vars()
    api_key = os.environ.get("OPENAI_API_KEY") or input("OpenAI API key: ")
    provider = LLMProvider.create_openai(
        api_key=api_key,
        model="gpt-4o-mini"
    )

    logger.info("*** Creating LLM provider with OpenAI")

    # 1. Create subordinate agents (isolated - they don't see coordination context)
    logger.info("*** Creating subordinate agents...")
    data_processor = LLMAgent(
        jid="dataprocessor@localhost",
        password="dataprocessor_pass",
        system_prompt="""You are a fake  data processing agent.

When asked to analyze a dataset:
1. Acknowledge the request
2. Provide fake analysis results with realistic metrics
3. Be concise and end your response clearly

Example: "Analysis complete. Dataset 'sales_2024.csv' contains 1000 rows, 5 columns. Total sales: $50,000. Top product: Widget A."
""",
        provider=provider,
        verify_security=False
    )

    file_manager = LLMAgent(
        jid="filemanager@localhost",
        password="filemanager_pass",
        system_prompt="""You are a file management agent.

When asked to save results:
1. Acknowledge the file and location
2. Confirm the save operation
3. Be concise

Example: "File saved successfully to 'analysis_results.json'."
""",
        provider=provider,
        verify_security=False
    )

    notifier = LLMAgent(
        jid="notifier@localhost",
        password="notifier_pass",
        system_prompt="""You are a fake notification agent.

When asked to send alerts:
1. Acknowledge the notification request
2.  FAke and Confirm the alert was sent
3. Be concise

Example: "Alert sent to user: Task completed successfully."
""",
        provider=provider,
        verify_security=False
    )

    # 2. Create coordinator agent
    logger.info("*** Creating coordinator agent...")
    coordinator = CoordinatorAgent(
        jid="coordinator@localhost",
        password="coordinator_pass",
        subagent_ids=[
            "dataprocessor@localhost",
            "filemanager@localhost",
            "notifier@localhost"
        ],
        coordination_session="project_alpha",
        provider=provider
    )

    # 3. Start all agents
    agents = [data_processor, file_manager, notifier, coordinator]
    logger.info(f"*** Starting {len(agents)} agents...")

    for agent in agents:
        await agent.start()
        logger.info(f"*** Started agent: {agent.jid}")

    logger.info("*** All agents started. Waiting for connections...")
    await asyncio.sleep(2)

    # 4. Send coordination request to coordinator
    logger.info("*** Preparing coordination request...")

    coordination_request = """
    Please coordinate the following task think how to coordinate each action step by step. Ensure that each one is completed before start another:
    1. Have the data processor analyze dataset 'sales_2024.csv'
    2. Have the file manager save the results to 'analysis_results.json'
    3. Have the notifier send an alert to the user when complete

    Use your coordination tools to orchestrate this workflow.
    
    Once the job is done, end your response with this : 
    
     <TASK_COMPLETE>
    """

    # Create ChatAgent to send initial coordination request
    # ChatAgent handles XMPP messaging properly with metadata for LLMAgent
    logger.info("*** Creating ChatAgent to send coordination request...")

    # Track completion with an event
    completion_event = asyncio.Event()

    # Display callback to capture responses and detect completion
    def display_response(message: str, sender: str):
        logger.info(f"*** Response from {sender}: {message[:100]}...")
        if "<TASK_COMPLETE>" in message:
            logger.info("*** TASK COMPLETION DETECTED!")
            completion_event.set()

    user_chat = ChatAgent(
        jid="user@localhost",
        password="user_pass",
        target_agent_jid="coordinator@localhost",
        display_callback=display_response,
        verify_security=False
    )

    await user_chat.start()
    logger.info("*** ChatAgent started")

    # Wait a moment for connection
    await asyncio.sleep(1)

    # Send the coordination request
    logger.info("*** Sending coordination request...")
    user_chat.send_message(coordination_request)
    logger.info("*** Coordination request sent!")

    logger.info("*** Waiting for coordination to complete...")
    logger.info("*** Watch the logs to see coordination in action!")

    # Wait for completion (with timeout)
    try:
        await asyncio.wait_for(completion_event.wait(), timeout=180)  # 3 minute timeout
        logger.info("*** Coordination completed successfully!")
    except asyncio.TimeoutError:
        logger.warning("*** Coordination timed out after 3 minutes")

    # Stop all agents cleanly
    logger.info("*** Stopping all agents...")
    await user_chat.stop()
    for agent in agents:
        await agent.stop()
        logger.info(f"*** Stopped agent: {agent.jid}")

    logger.info("*** Example finished!")






if __name__ == "__main__":
    print("*** Starting CoordinatorAgent Example...")
    print("*** This example shows how a coordinator manages multiple agents in shared context.")
    print(f"*** Debug mode: {'ENABLED' if DEBUG_MODE else 'INFO level'} (set DEBUG=true for verbose logs)")
    print("*** Make sure to have SPADE server running: 'spade run'")
    print()

    asyncio.run(run_coordination_example())