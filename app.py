import streamlit as st
from bot import chatbot

st.title("AI Internship Chatbot")
st.write("Chatbot with Memory + Calendar")

user_id = "student_001"
msg = st.text_input("Enter your message")

if st.button("Send"):
    if msg:
        response = chatbot(user_id, msg)
        st.write("Bot:", response)
