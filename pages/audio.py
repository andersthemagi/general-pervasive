import streamlit as st 
from menu import menu_with_redirect
from pathlib import Path
import common

menu_with_redirect()

st.title("Audio Example")

if st.button("Return to Home", type="primary"):
    st.switch_page("app.py")

st.markdown(common.SYSTEM_PROMPT)

with st.chat_message("assistant"):
    try:
        stream = st.session_state.client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": common.SYSTEM_PROMPT}
            ],
            stream=True,
            temperature=1,
        )
        response = st.write_stream(stream)
    except:
        response = st.write(common.DEFAULT_AUDIO_PROMPT)

    speech_file_path = None
    
    try:
        speech_file_path = Path(__file__).parent.parent / "speech.mp3"
        with st.session_state.client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="nova",
            input=response
        ) as response:
            with open(speech_file_path, 'wb') as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        st.audio("speech.mp3")
    except:
        st.audio("default_speech.mp3")

menu_with_redirect()