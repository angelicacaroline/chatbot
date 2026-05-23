import os
from groq import Groq
import streamlit as st
import yaml

with open("config.yaml", "r", encoding="utf-8") as arquivo:
    config = yaml.safe_load(arquivo)

client = Groq(api_key=config["api_key"])

st.set_page_config(page_title="Carbot")
st.title("Carbot friend")

input = st.text_input("Digite sua pergunta sobre carros:")

if st.button("Enviar"):
    if input:
        with st.spinner("Vrum vrumm..."):
            chat = client.chat.completions.create(
            messages=[{"role": "user", "content": input}],
            model="llama-3.3-70b-versatile",
            )
            resposta = chat.choices[0].message.content
            st.write("Resposta do Carbot:")
            st.info(resposta)
    else:
        st.warning("Por favor, me diga qual é a sua dúvida?")