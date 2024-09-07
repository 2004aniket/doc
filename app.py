from transformers import pipeline
# import tokenizers
import streamlit as st

st.title("chatbot")
model=pipeline(model='Aniket2004/Llama_doctor_v1',task="text-generation")


prompt=st.text_input("enter the query")
if prompt:
    result=model(f"[INST] {prompt} [/INST]")
    st.write(result[0]['generated_text'])
    st.write(prompt)
