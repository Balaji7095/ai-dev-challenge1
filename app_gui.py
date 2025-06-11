
import streamlit as st
from utils.llm_utils import expand_prompt
from utils.memory import save_to_memory

st.title("AI Developer Challenge Demo")

user_input = st.text_input("Enter a creative prompt:")

if user_input:
    expanded = expand_prompt(user_input)
    save_to_memory(user_input, expanded)
    st.success("Prompt expanded and saved!")
    st.write("Expanded Prompt:", expanded)
