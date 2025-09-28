import os
from dotenv import load_dotenv
from typing import Annotated, Literal, TypedDict
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph,MessagesState,END,START
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from tools import get_job, get_resume


load_dotenv()

tools = [get_job, get_resume]

llm = ChatOpenAI(model=os.getenv("MODEL_NAME", "gpt-4o"), temperature=0).bind_tools(tools)

def expert(state:MessagesState):
    system_message  = """ Youa are a resume expert. You have access to a job posting and a resume.
    Your task is to evaluate how well the resume matches the job posting.
    You should provide a score from 1 to 10, where 10 means the resume is a perfect match for the job posting, and 1 means it is not a match at all.
    You should also provide a brief explanation for the score, highlighting the strengths and weaknesses of the resume in relation to the job posting.
    """
    messages = state['messages']
    response = llm.invoke([system_message] + messages)

    return {"messages":[response]}

tool_node = ToolNode(tools)

def should_continue(state:MessagesState) ->Literal["tools","end"]:
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "END"

graph = StateGraph(MessagesState)
graph.add_node("expert",expert)
graph.add_node("tools",tool_node)
graph.add_edge(START,"expert")
graph.add_conditional_edges("expert",should_continue)



graph.add_edge("tools","expert")
checkpointer = MemorySaver()
app =graph.compile(checkpointer=checkpointer)

while True:
    user_input = input("Enter your message (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    response = app.invoke({"messages":[HumanMessage(content=user_input)]},config={"configurable":{"thread_id":1}})
    print("Response:", response['messages'][-1].content)
