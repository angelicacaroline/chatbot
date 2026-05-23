import os
from groq import Groq
import streamlit as st
import yaml

with open("config.yaml", "r", encoding="utf-8") as arquivo:
    config = yaml.safe_load(arquivo)

client = Groq(api_key=config["api_key"])

st.set_page_config(page_title="Carbot")
st.title("Carbot friend")

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Olá, me ajude a escolher um carro. Eu gosto de carros velozes",
        }
    ],
    model="llama-3.3-70b-versatile",
)
print(chat.choices[0].message.content)