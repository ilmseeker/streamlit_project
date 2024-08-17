import streamlit as st
from streamlit_msal import Msal

with st.sidebar:
    auth_data = Msal.initialize_ui(
        client_id=client_id,
        authority=authority,
        scopes=[], # Optional
        # Customize (Default values):
        connecting_label="Connecting",
        disconnected_label="Disconnected",
        sign_in_label="Sign in",
        sign_out_label="Sign out"
    )

if not auth_data:
    st.write("Authenticate to access protected content")
    st.stop()

st.write("Protected content available")
