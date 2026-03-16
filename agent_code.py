import os
import asyncio
import streamlit as st
# from dotenv import load_dotenv

import google.generativeai as genai
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai.types import Content, Part


#We configure the API Key so that the Google allows the program to access it and use the AI models
# load_dotenv()

#use API key as an environment variable
# api_key=os.environ["GOOGLE_API_KEY"]
# genai.configure(api_key=api_key)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

print("API Key configured successfully")

#Defining Agent:

def create_trip_planner_agent():
  return Agent(
      name="Trip_Planner_Agent",
      model="gemini-2.5-flash",
      description="This is the Trip Planner agent which plans a day trip based on the user’s mood, interests, and budget.",
      instruction="""
      You are a Day Trip Planner – an AI that makes fun, full-day trip plans for users.
      Ask the user for missing information: mood, budget, interests, before planning.
If all info is present, generate the plan.
      
        Your Task:
Turn a user’s mood, interests, and budget into a complete day-trip plan with real, up-to-date details.

How to Do It:

Follow the Budget: Suggest activities that match the user’s budget, whether cheap, moderate, or splurge. Use Google Search to find relevant places or events.

Plan the Full Day: Include ideas for morning, afternoon, and evening.

Check Real-Time Info: Look up current opening hours, events, or special happenings.

Match the Mood: Make sure activities fit the mood, like adventurous, relaxing, or artsy.

Output Format:
Give the plan in Markdown, with clear time sections and actual venue names.
      """,
      tools=[google_search]
  )

trip_planner_agent = create_trip_planner_agent()
print(f"{trip_planner_agent.name} is created and ready to go!")

async def run_agent_query(agent:Agent, query:str, session:Session, user_id:str, is_router:bool=False):
  print(f"Running query for agent: {agent.name} in session: {session.id}")

  runner = Runner(
      agent=agent,
      session_service=session_service,
      app_name=agent.name
  )

  final_response=""
  try:
    async for event in runner.run_async(
        user_id=user_id,
      session_id=session.id,
      new_message=Content(parts=[Part(text=query)], role="user")
    ):
      # if not is_router:
      #   print(f"EVENT: {event}")
      if event.is_final_response():
        final_response=event.content.parts[0].text
  except Exception as e:
    final_response=f"An error occurred: {e}"

  if not is_router:
    print("\n" + "-"*50)
    print("Final Response: ")
    print(final_response)
    #display(Markdown(final_response))
    print("-"*50 + "\n")

  return final_response

#Initializing our Session service
session_service=InMemorySessionService()
my_user_id="user_001"

async def run_day_trip_agent():
  day_trip_session=await session_service.create_session(
    app_name=trip_planner_agent.name,
    user_id=my_user_id
  )
  while True:
    query=input("Enter your query (or type 'exit' to quit): ")

    if query.lower() in ["exit", "quit", "cancel"]:
      print("Exiting the trip planner. Bye!")
      break
  #Query can be Plan a relaxing and artsy day trip near Sunnyvale, CA. Keep it affordable!
  # query=input("Enter your query: ")
  # print(f"User's query: {query}")

    await run_agent_query(trip_planner_agent, query, day_trip_session, my_user_id)

if __name__ == "__main__":
    asyncio.run(run_day_trip_agent())