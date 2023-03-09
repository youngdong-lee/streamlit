import streamlit as st
from streamlit_chat import message
import requests
import openai
import toml
import os
currentpath = os.getcwd()
print(currentpath)

with open('secrets.toml', 'r') as f:
    config = toml.load(f)

openai.api_type = "azure"
openai.api_key = config['fb64bf7c663d41efb288da7573a9e3f6']
openai.api_base = "https://young-openai.openai.azure.com/"
openai.api_version = "2022-12-01"


st.set_page_config(page_title="Custom ChatGPT", page_icon="💬")

st.markdown("# Custom ChatGPT")
st.sidebar.header("Custom ChatGPT")

#generating 2 empty lists to store past and generated value in the conversation

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = st.text_input("You: ","Hello, how are you?", key="input")

if user_input:
    output = openai.Completion.create(
          engine="test1",
          prompt=f"{st.session_state.past}\n{user_input}",
          temperature=0,
          max_tokens=1041,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          best_of=1,
          stop=None)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["choices"][0]["text"].strip())

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], avatar_style = 'bottts', key=str(i))
        message(st.session_state['past'][i], avatar_style = 'big-ears',is_user=True, key=str(i) + '_user')
