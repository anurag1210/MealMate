"""MealMate — Streamlit UI for family meal planning."""
import streamlit as st
import tempfile
import os
from src.agent import create_agent

st.set_page_config(page_title="MealMate", layout="centered")
st.title("🍽️ MealMate — Family Meal Planner")

# Sidebar — Family Setup & Photo Upload
with st.sidebar:
    st.header("📸 Snap Your Fridge")
    uploaded_photo = st.file_uploader("Upload a fridge photo", type=["jpg", "jpeg", "png"])
    
    if uploaded_photo:
        st.image(uploaded_photo, caption="Your fridge", use_container_width=True)
        
        if st.button("🔍 Identify Ingredients"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                tmp.write(uploaded_photo.getbuffer())
                tmp_path = tmp.name
            
            st.session_state.fridge_photo_path = tmp_path
            st.session_state.pending_photo = True
    
    st.divider()
    st.header("👨‍👩‍👧‍👦 Family Setup")
    if st.button("Reset Memory"):
        import shutil
        if os.path.exists("data/memory"):
            shutil.rmtree("data/memory")
        if os.path.exists("data/sessions"):
            shutil.rmtree("data/sessions")
        st.session_state.messages = []
        st.success("Memory cleared!")

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = create_agent(session_id="mealmate-ui")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle fridge photo analysis
if st.session_state.get("pending_photo"):
    photo_path = st.session_state.fridge_photo_path
    prompt = f"I have a photo of my fridge at {photo_path} — identify all the ingredients you can see and suggest what I can cook tonight."
    
    with st.chat_message("user"):
        st.markdown("📸 *Uploaded fridge photo for analysis*")
    st.session_state.messages.append({"role": "user", "content": "📸 Uploaded fridge photo for analysis"})
    
    with st.chat_message("assistant"):
        with st.spinner("Scanning your fridge..."):
            response = st.session_state.agent(prompt)
            response_text = str(response)
            st.markdown(response_text)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.session_state.pending_photo = False
    
    # Cleanup temp file
    os.unlink(photo_path)

# Chat input
if query := st.chat_input("What should we cook tonight?"):
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent(query)
            response_text = str(response)
            st.markdown(response_text)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})