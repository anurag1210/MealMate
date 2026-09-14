# 🍽️ MealMate — AI Family Meal Planning Agent

An AI-powered meal planning agent that knows your family, scans your fridge, 
and plans personalised meals — so you never have to answer "what's for dinner?" again.

Built with [AWS Strands Agents SDK](https://strandsagents.com/) and 
[Amazon Bedrock](https://aws.amazon.com/bedrock/) (Claude) for the 
AWS Strands Agents Hackathon — Track 1: Everyday Agents.

## The Problem

Every family has the same daily conversation: "What should we cook tonight?" 
It sounds simple, but it's actually a complex optimisation problem — dietary 
restrictions, kids' preferences, what's in the fridge, avoiding repeats, 
budget, and time constraints. Multiply that by 3 meals × 7 days × different 
family members, and it's 20-30 minutes of daily decision fatigue.

## Who It's For

Any family that's tired of the daily meal planning debate. Especially families 
with mixed dietary needs — a diabetic parent, a vegetarian spouse, kids who 
only eat chicken — where every meal has to work for everyone at the table.

## What It Does

**Snap your fridge → get a week of meals → shopping list ready.**

MealMate is a single AI agent with multiple tools that handles meal planning 
end-to-end:

### 📸 Fridge Scanning
Upload a photo of your fridge. MealMate identifies visible ingredients using 
Claude's vision capabilities and plans meals around what you already have — 
reducing waste and unnecessary shopping.

### 🧠 Family Memory
Tell MealMate about your family once. It remembers dietary restrictions, 
preferences, and feedback across sessions. "I'm diabetic, my wife is 
vegetarian, my daughters love chicken and eggs" — saved permanently, 
applied to every future meal plan automatically.

### 🍛 Smart Meal Planning
Generates weekly meal plans that respect everyone's needs simultaneously. 
Low-GI options for the diabetic family member, vegetarian dishes for the 
spouse, chicken and egg dishes for the kids — all in the same plan, with 
Indian and Chinese cuisine preferences honoured.

### 🎒 School Lunchbox Planning
Plans 5-day school lunchboxes with real constraints: no heating required, 
leak-proof, finger-friendly, under 5 minutes to pack. Uses leftovers from 
last night's dinner. Includes protein + fruit + vegetable + carb + treat 
for every box.

### 🛒 Shopping List
Generates categorised shopping lists that exclude what you already have. 
Grouped by supermarket section, quantities combined across meals.

### 📦 Pantry Tracking
Maintains an inventory of your available ingredients. Updated from fridge 
photos and manual input. The agent checks the pantry before suggesting 
meals and only adds missing items to the shopping list.

## Architecture

![MealMate Architecture](docs/mealmate_architecture.png)

User (text / fridge photo / feedback)
│
▼
┌─────────────────────────────────────────┐
│ MealMate Agent (Strands SDK) │
│ Amazon Bedrock (Claude Sonnet 4.6) │
│ │
│ Tools: │
│ ├── 📸 Vision (ingredient detection) │
│ ├── 🍽️ Meal Planner │
│ ├── 🛒 Shopping List Builder │
│ ├── 📦 Pantry Tracker │
│ └── 🔍 Memory Search / Add │
└────────────┬───────────────┬────────────┘
│ │
┌──────┘ └──────┐
▼ ▼
Session Manager Memory Manager
(FileSessionManager) (TestMemoryStore)
Conversation history Family preferences
across sessions dietary needs, feedback


## Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | AWS Strands Agents SDK |
| LLM | Amazon Bedrock — Claude Sonnet 4.6 |
| Vision | Bedrock Converse API (multimodal) |
| Session Persistence | Strands FileSessionManager |
| Long-term Memory | Strands TestMemoryStore |
| Frontend | Streamlit |
| Language | Python 3.11 |

## Setup

### Prerequisites
- Python 3.11+
- AWS account with Bedrock access (Claude Sonnet enabled)
- AWS CLI configured (`aws login`)

### Install

```bash
git clone https://github.com/anurag1210/MealMate.git
cd MealMate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure

```bash
cp .env.example .env
# Edit .env with your AWS region
```

### Run

```bash
# Streamlit UI
PYTHONPATH=$(pwd) streamlit run ui/app.py

# Or command line
python -m src.agent
```

## Demo Screenshots

### Fridge Photo → Meal Plan
![Fridge scan to meal plan](docs/screenshot/fridge-scan.png)

### Family Memory Recall
![Memory working across sessions](docs/screenshot/memory-recall.png)

### School Lunchbox Planning
![5-day lunchbox plan](docs/screenshot/lunchbox.png)

## How It Works

1. **First visit:** Tell MealMate about your family — dietary needs, preferences, 
   who likes what. The agent saves this to long-term memory.

2. **Snap your fridge:** Upload a photo. Claude's vision identifies ingredients. 
   The pantry tracker stores them.

3. **Get your plan:** Ask for dinner ideas, a full weekly plan, or school lunchboxes. 
   The agent checks memory (your family's needs), checks the pantry (what you have), 
   and generates a plan that works for everyone.

4. **Give feedback:** "Kids loved the chicken tacos" or "the soup was too spicy." 
   The agent remembers and adjusts future suggestions.

5. **Shop smart:** Generate a shopping list that only includes what you're missing. 
   Grouped by aisle, quantities combined.

## What Makes This Different

- **Not a recipe app.** MealMate doesn't just find recipes — it solves the 
  decision problem. It knows your family, sees your fridge, and makes the 
  choice for you.
- **Memory that matters.** Most chatbots forget you between sessions. MealMate 
  remembers your family permanently — preferences, restrictions, and feedback 
  compound over time.
- **Real constraints.** School lunchboxes that survive a backpack. Weeknight 
  dinners under 30 minutes. Diabetic-friendly meals that taste good. These 
  aren't afterthoughts — they're the core design.

## License

MIT