import streamlit as st
from chat import chat_inference

st.title("Bot Chat Sederhana dengan Gemini")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("ketik pesan disini")
if prompt:
    # kirim response ke chat_inference
    response = chat_inference(prompt)
    # tampilkan pesan dari user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({
        "role": "user", "content": prompt
    })
    # tampilkan response dari bot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({
        "role": "assistant", "content": response
    })

