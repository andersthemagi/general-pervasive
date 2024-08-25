import streamlit as st

def keep(key):
    st.session_state[key] = st.session_state['_' + key]

def unkeep(key):
    st.session_state['_' + key] = st.session_state[key]

def menu():
    if "postal_code" not in st.session_state:
        st.session_state.postal_code = None
    st.sidebar.header("Instructions.")
    st.sidebar.markdown("""
    Enter a postcode in the UK (here are some [examples](https://ukpostcode.org/location/GB-ENG/City%20and%20County%20of%20the%20City%20of%20London)). You should see a GP name that is closest to the postcode. You can compare your results with the [NHS GP website](https://www.nhs.uk/service-search/find-a-gp).

    Once you have a postal code entered, please choose either an audio or text example.                    
    """)
    default_value = st.session_state.postal_code or "E1 7JJ"
    st.sidebar.text_input("Postal Code", value=default_value, key="_postal_code", on_change=keep, args=["postal_code"]) # Bishopsgate
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/audio.py", label="Audio Example")
    st.sidebar.page_link("pages/text.py", label="Text Example")

def menu_with_redirect():
    if "postal_code" not in st.session_state:
        st.switch_page("app.py")