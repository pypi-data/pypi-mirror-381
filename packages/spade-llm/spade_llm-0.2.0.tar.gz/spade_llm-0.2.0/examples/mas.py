import asyncio, json, getpass, os,spade, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from spade_llm import LLMTool, load_env_vars
from spade_llm.agent import LLMAgent
from spade_llm.providers import LLMProvider
from spade.message import Message
from datetime import datetime
from prompts import *
from typing import Dict, Any

# para mostrar la información sobre los agentes
import logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("spade_llm").setLevel(logging.INFO)

def save_output(llm_output, id):
    """Safely save the output of a LLM in a JSON file by adding a new entry [id] = llm_output"""
    filepath = "datasets/results.json"
    print(f"\n\n\n Saving Output with id... ", id)
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                data = json.load(f)
        else:
            data = {}

        data[id] = llm_output # update dictionary, new entry

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

        return "Output saved successfully."

    except Exception as e:
        return f"Error: {str(e)}"


import aiofiles

async def write_to_file(content: str, mode: str = "w", filepath: str = "datasets/results.txt") -> str:
    """
    Write content to a text file (or append). 
    - filepath: path to the file to write
    - content: the text to write
    - mode: "w" (overwrite) or "a" (append)
    Returns a status message or error.
    """
    try:
        async with aiofiles.open(filepath, mode) as f:
            await f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing to file: {e}"

write_tool = LLMTool(
    name="write_to_file",
    description="Write (or append) text content to a file",
    parameters={
        "type": "object",
        "properties": {
            # "filepath": {"type": "string", "description": "Path to the file"},
            "content": {"type": "string", "description": "Text content to write"},
            "mode": {
                "type": "string",
                "enum": ["w", "a"],
                "description": "File mode: 'w' for overwrite, 'a' for append"
            }
        },
        "required": [
            # "filepath",
              "content"]
    },
    func=write_to_file
)


async def send_initial_messages_to_agents(specialised_agents_jid, q, d, sheet_name, index):
    from spade.agent import Agent
    from spade.behaviour import OneShotBehaviour

    class SenderAgent(Agent):
        class SendBehaviour(OneShotBehaviour):
            def __init__(self, recipients, message_body, thread_id):
                super().__init__()
                self.recipients = recipients
                self.message_body = message_body
                self.thread_id = thread_id

            async def run(self):
                for recipient in self.recipients:
                    msg = Message(to=recipient)
                    msg.body = self.message_body
                    msg.thread = self.thread_id
                    msg.set_metadata("message_type", "llm")
                    await self.send(msg)
                    print(f"Message sent to {recipient}")

        async def setup(self):
            message_body = self.get("message_body")
            recipients = self.get("recipients")
            thread_id = self.get("thread_id")
            behaviour = self.SendBehaviour(recipients, message_body, thread_id)
            self.add_behaviour(behaviour)

    sender = SenderAgent("sender@localhost", "sender_password")
    sender.set("thread_id", f"{sheet_name}_{index}")
    sender.set("message_body", f"ID:{sheet_name}_{index}; Question:{q}; Document:{d}")
    sender.set("recipients", specialised_agents_jid)
    await sender.start()
    await asyncio.sleep(15)
    await sender.stop()

async def main():
    print()
    
    tools = [
        write_tool
        # LLMTool(
        #     name="save_output_to_json",
        #     description="Safely saves LLM outputs into existing .json by their id",
        #     parameters={
        #         "type": "object",
        #         "properties": {
        #             "llm_output":{"type":"string", "description":"The output of a LLMAgent"},
        #             "id":{"type":"string", "description":"The identifyier of the conversation"},
        #             # "type_of_agent":{"type":"string", "description":"The type of agent that executres"},
        #         },
        #         "required": ["llm_output","id"
        #                      ]
        #     },
        #     func=save_output
        # )
    ]
    load_env_vars()

    # API Key (with fallback to input)
    api_key = os.environ.get("OPENAI_API_KEY")
    provider = LLMProvider.create_openai(
        api_key=api_key,
        model="gpt-4o-mini"
    )

    relevancy = LLMAgent(
        jid="rel@localhost",
        password="relevancy",
        provider=provider,
        reply_to="coor@localhost",
        system_prompt=relatedness_prompt,
        # tools=tools
    )

    coordinator = LLMAgent(
        jid="coor@localhost",
        password="coordinator",
        provider=provider,
        system_prompt="You receive a score and a justification and provide a response (YES/NO) based on the following threshold: if the received score is higher than 0.7 you respond YES and, otherwirse, return NO. ALWAYS USE THE TOOL TO SAVE THE RESULTS IN A JSON FORMAT. ",
        tools=tools
    )

    with open("datasets/json_ragbench.json", "r", encoding="utf-8") as f:
        datasets = json.load(f)
        for dataset, dic in datasets.items():
            for sample in dic:
                q = sample["question"] # question
                index = sample["id"] # sample identifier - row
                for p, doc in enumerate(sample["documents"]): # p identifies the document number to be analysed
                    print("\n\n\n\n--------------------------------------------\n\n")
                    print(f"- Combination of (q, doc) with id {index}_{p}:\n\n -   Query:{q} \n\n -   Document:{doc} \n\n\n")
                
                    try:
                        await relevancy.start()
                        await coordinator.start()
                        print("\n\n ✅ Agents started successfully!\n")
                        await asyncio.sleep(1)
                        specialised_agents_jid = ["rel@localhost"]

                        # Send initial messages to all specialized agents
                        await send_initial_messages_to_agents(
                            specialised_agents_jid=specialised_agents_jid,
                            q=q,
                            d=doc,
                            sheet_name=dataset,
                            index=f"{index}_{p}"
                        )

                        # print(f"\n\n - Messages sent to {len(specialised_agents_jid)} agents. \n\n")

                        await asyncio.sleep(250)

                    except KeyboardInterrupt:
                        print("\n👋 Shutting down...")
                    
                    # finally:
                    #     await relevancy.stop()
                    #     await coordinator.stop()
                    #     # print("\n\n ✅ Agents stopped successfully!")

                    #     await asyncio.sleep(2)

                break # solo queremos 4 iteraciones por el momento para ver que funciona
            break  

if __name__ == "__main__":

    spade.run(main())
 