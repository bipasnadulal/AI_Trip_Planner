import streamlit as st
import asyncio

from agent_code import trip_planner_agent, session_service
from google.adk.runners import Runner
from google.genai.types import Content, Part

st.title("AI Trip Planner")

if "session" not in st.session_state:
    st.session_state.session = asyncio.run(
        session_service.create_session(
            app_name=trip_planner_agent.name,
            user_id="user1"
        )
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask for a trip plan")

if user_input:

    st.session_state.messages.append(("user", user_input))

    runner = Runner(
        agent=trip_planner_agent,
        session_service=session_service,
        app_name=trip_planner_agent.name
    )

    async def run_agent():
        async for event in runner.run_async(
            user_id="user1",
            session_id=st.session_state.session.id,
            new_message=Content(parts=[Part(text=user_input)], role="user")
        ):
            if event.is_final_response():
                return event.content.parts[0].text

    response = asyncio.run(run_agent())

    st.session_state.messages.append(("assistant", response))

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)