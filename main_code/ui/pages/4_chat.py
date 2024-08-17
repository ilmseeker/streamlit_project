import streamlit as st
from st_pages import Page, add_page_title, show_pages_from_config
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="Chat Page", 
                   page_icon=":robot_face:", 
                   layout="wide",
                   initial_sidebar_state="collapsed")
# add_page_title()

st.title("Chat")

show_pages_from_config("main_code//ui//pages.toml")

left, right = st.columns(2, vertical_alignment="top")
with left:
    button1 = st.button('Home', key=1, use_container_width=True)
with right:
    button2 = st.button('About', key=2, use_container_width=True)
if button1:
    switch_page("home")
if button2:
    switch_page("about")