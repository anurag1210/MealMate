Day 1 (Today): Foundation

Project structure + dependencies
Basic Strands agent with system prompt
First tool: meal planner (text-based, no photo yet)
Test end-to-end: "Plan dinner for a family of 4"

Day 2: Memory + Preferences

Memory layer (SQLite for simplicity, swap to DynamoDB later)
Family profile storage (members, dietary restrictions, dislikes)
Meal history tracking (no repeats)
Test: agent remembers preferences across calls

Day 3: Vision + Pantry

Fridge photo tool (Bedrock Claude vision)
Pantry tracker (stores identified ingredients)
Shopping list tool (gaps between pantry and meal plan)
Test: snap photo → agent plans around what you have

Day 4: Lunchbox + Polish

Kids lunchbox planner tool
Weekly planning flow (full week output)
Streamlit UI
Feedback mechanism ("kids loved it" / "didn't eat it")

Day 5: Deploy + Submit

Deploy to AgentCore (bonus points) or Docker
README with architecture diagram, screenshots
Record demo video
Submit to hackathon

Let's start Day 1. First — verify your AWS setup: