import os
from typing import List, Union,TypedDict
from langchain_core.messages import HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv # used to store secret stuff like API keys or configuration values

load_dotenv()

class Agentstate(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


llm =ChatOpenAI(model="gpt-4o")

def process(state:Agentstate) -> Agentstate:
    """This node will solve the request you input"""

    response = llm.invoke(state["messages"])
    print(f"\nAI: {response.content}")
    state["messages"].append(AIMessage(content=response.content))
    return state


graph = StateGraph(Agentstate)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()


conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    print(f"Result: {result}")
    conversation_history = result["messages"]
    user_input = input("Enter: ")

with open("logging.txt","w") as file:
    file.write("Your Conversation log:\n")

    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"Human: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    file.write("End of Conversation ")

print("Conversation log saved to logging.txt")
