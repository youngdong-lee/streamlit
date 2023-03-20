import streamlit as st
from streamlit_chat import message
import requests
import os
import openai
import toml

with open('secrets.toml', 'r') as f:
    config = toml.load(f)

openai.api_type = "azure"
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = "https://bloodntear.openai.azure.com/"
openai.api_version = "2022-12-01"

st.set_page_config(page_title="쬐그만한 ChatGPT", page_icon="💬")
st.markdown("# 쬐그만한 ChatGPT")

#generating 2 empty lists to store past and generated value in the conversation

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input = st.text_input("You: ","안녕하세요", key="input")

if user_input:
    output = openai.Completion.create(
          engine="bloodntear",
          prompt=f"{st.session_state.past}\n{user_input}",
          temperature=0.6,
          max_tokens=3000,
          top_p=1,
          frequency_penalty=1,
          presence_penalty=1,
          best_of=1,
          stop=None)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["choices"][0]["text"].strip())

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], avatar_style = 'bottts', key=str(i))
        message(st.session_state['past'][i], avatar_style = 'big-ears',is_user=True, key=str(i) + '_user')
