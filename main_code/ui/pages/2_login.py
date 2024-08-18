import streamlit as st

from st_pages import Page, add_page_title, show_pages_from_config
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.mention import mention

st.set_page_config(page_title="Chat Page", 
                   page_icon=":closed_lock_with_key:", 
                   layout="wide", 
                #    initial_sidebar_state="collapsed"
                )

show_pages_from_config("main_code\\ui\\pages.toml")

cols = st.columns([6,2,2])
with cols[0]:
    mention(
        label="Hi Sajjad!!!",
        icon="streamlit",  # Some icons are available... like Streamlit!
        url="https://extras.streamlitapp.com",
    )
with cols[1]:
    button1 = st.button('Home', key=1, use_container_width=True)
with cols[2]:
    button2 = st.button('Upload', key=2, use_container_width=True)
if button1:
    switch_page("home")
if button2:
    switch_page("upload")

st.title("Login")

