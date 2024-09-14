import streamlit as st
import google.generativeai as genai


st.title("Welcome to GENERATIVE AI application")

genai.configure(api_key='AIzaSyBhjLCdOAiu9xMv_Q2uy_tJf3PbDpIlJD4')  

text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click here to Generate"):
    response = chat.send_message(text)
    st.write(response.text)
