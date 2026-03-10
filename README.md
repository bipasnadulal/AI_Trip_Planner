# AI Trip Planner

AI Trip Planner is a smart travel itinerary creator that uses generative AI to build personalized day‑trip plans based on user input.  
Tell the system where you want to go along with things like your mood, interests, and budget, and it will generate a travel plan that covers morning, afternoon, and evening activities. 
The plans include real places and up‑to‑date info using web search tools integrated with Google’s Generative AI models.

---

## What This Project Does

- Creates customized travel plans using natural language prompts.
- Uses a combination of an AI agent and real‑time search tools to gather place information.
- Provides an interactive Streamlit UI where users can ask for itineraries in a chat‑like interface.

---

## Key Features

**Interactive Trip Planning**  
Enter a destination or travel idea in everyday language, and the AI will suggest a full day itinerary.

**Real‑World Info**  
Uses live search (Google Search API) to find up‑to‑date details about places and activities.

**Conversational UI**  
The Streamlit app works like a chat, users can type questions and get responses just like talking to a travel assistant.

**Session Memory**  
The planner remembers the conversation so follow‑ups are meaningful (e.g., clarifying mood or budget).

---

## Simple Visualization
```text
            +---------------------+
            |  User Input         |
            | (Destination, Mood, |
            | Interests, Budget) |
            +----------+----------+
                       |
                       v
            +---------------------+
            |  Trip Planner Agent  |
            |  (Gemini AI Model)  |
            +----------+----------+
                       |
       +---------------+-----------------+
       |                                 |
       v                                 v
+--------------+                  +-----------------+
| Google Search|                  | Internal Reasoning|
| Tool fetches |                  | (interprets mood,|
| real-time    |                  | interests, budget|
| info/events  |                  | & plans itinerary)|
+--------------+                  +-----------------+
       |                                 |
       +---------------+-----------------+
                       |
                       v
            +---------------------+
            | Formatted Itinerary |
            | (Morning,Afternoon, |       
            | Evening)            |
            +---------------------+
                       |
                       v
            +---------------------+
            | Display in UI       |
            | (Streamlit Chat)   |
            +---------------------+
```
[AI Trip Planner](https://aitripplanner-8ywl5ytnuenugpmok5w6r4.streamlit.app/)
