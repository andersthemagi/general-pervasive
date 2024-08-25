import streamlit as st
from menu import menu
from openai import OpenAI

if "example" not in st.session_state:
    st.session_state.example = None

if "gp_data" not in st.session_state:
    with open("epraccur.csv") as file:
        gp_data = file.read()
    st.session_state.gp_data = gp_data

if "client" not in st.session_state:
    st.session_state.client = None
    
st.session_state.client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("General Pervasiveness: An experiment on trust using LLMs in medical practice.")
st.markdown("""
We aim to focus on a potential scam based on a fake interaction between a parent and their doctor/GP.

In the UK, the NHS has a publicly available database of all GPs (https://www.nhs.uk/service-search/find-a-gp) with all the GPs’ data potentially available for web scraping

This demo simulates fake messages sent to those residents living close to each GP with a seemingly urgent message that requests for some private/sensitive data. By continuing the interaction, the message could eventually ask to ‘verify’ payment details to then capture this data

Given that parents are 1) busy, and 2) care about their child, they would more likely review and respond to messages from a trusted source like a GP

[See the full writeup.](https://docs.google.com/document/d/1Dcgzd_EklA9TRJbxDIdWvoqg0xErH9UyTglZjFfi2Lg/edit?usp=sharing)
            
---
            
Created by Andres Sepulveda Morales and Patrick Huang

Built for the [AI Capabilities and Risks Demo-Jam](https://www.apartresearch.com/event/ai-capabilities-and-risks-demo-jam)       
""")

menu()
