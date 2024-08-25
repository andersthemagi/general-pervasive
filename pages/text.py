import streamlit as st
from menu import menu_with_redirect
import common

menu_with_redirect()

st.title("Text Example")

if st.button("Return to Home", type="primary"):
    st.switch_page("app.py")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini-2024-07-18"

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system", "content": common.SYSTEM_PROMPT})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Talk with your GP." ):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

with st.chat_message("assistant"):
    try:
        stream = st.session_state.client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            temperature=1,
        )
        response = st.write_stream(stream)
    except:
        response = st.write(common.DEFAULT_TEXT_RESPONSE)
    st.session_state.messages.append({"role": "assistant", "content": response})

    menu_with_redirect()



