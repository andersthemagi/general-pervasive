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
    You can enter any post code for a GP in the UK.
    
    We have included all GPs per [a public registry](https://digital.nhs.uk/services/organisation-data-service/export-data-files/csv-downloads/gp-and-gp-practice-related-data) provided by the NHS.
    
    To find a specific GP with a UK postcode, you can search for a UK postcode (per this link)[https://ukpostcode.org/location/GB-ENG/City%20and%20County%20of%20the%20City%20of%20London] and enter the postcode per the (NHS GP site)[https://www.nhs.uk/service-search/find-a-gp] to find the closest GP.                  
    """)
    default_value = st.session_state.postal_code or "E1 7JJ"
    st.sidebar.text_input("Postal Code", value=default_value, key="_postal_code", on_change=keep, args=["postal_code"]) # Bishopsgate
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/audio.py", label="Audio Example")
    st.sidebar.page_link("pages/text.py", label="Text Example")

def menu_with_redirect():
    if "postal_code" not in st.session_state:
        st.switch_page("app.py")