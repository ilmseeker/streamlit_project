import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from st_pages import Page, add_page_title, show_pages_from_config, hide_pages
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Page Title", 
                   page_icon="Icon", 
                   layout="wide", 
                #    initial_sidebar_state="collapsed"
                   )

hide_pages(["Upload", "Chat"])

show_pages_from_config("main_code\\ui\\pages.toml")

url = "main_code\\images\\images.png"

st.sidebar.image(url, use_column_width=True)

cols = st.columns([6,2,2])
with cols[1]:
    button1 = st.button('Login', key=1, use_container_width=True)
with cols[2]:
    button2 = st.button('About', key=2, use_container_width=True)
if button1:
    switch_page("login")
if button2:
    switch_page("about")

st.markdown( 
    """ <style> [data-testid="collapsedControl"] { display: none } </style> """, 
    unsafe_allow_html=True)

st.markdown(
    """ <div style="text-align: center"> 
    <h1 style="font-size:5vw"><b><strong>Welcome to QnA Chatbot!!</b></strong></h1> 
    <h1 style="font-size:3vw"><b><strong>Chat with your documents</b></strong></h1>
    </div>""",
    unsafe_allow_html=True,
)

st.divider()

st.markdown(
"""
<h1 style='text-align:center; color:tomato; font-size:2vw; font-style:italic; font-weight:bold'>Welcome to custom QnA Chatbot</h1>
<h1 style='text-align:center; color:tomato; font-size:2vw; font-style:italic'>Powered by LLM</h1> 

### Click one of the buttons at the :top: to proceed.

**Streamlit is an open-source app framework built specifically for
Machine Learning and Data Science projects.**
**👈 Select a page from the sidebar** to navigate to this web app pages!
### Want to learn more?
- Check out [streamlit.io](https://streamlit.io)
- Jump into the [documentation](https://docs.streamlit.io)
- Ask a question in Streamlit [community
    forums](https://discuss.streamlit.io)
""", unsafe_allow_html=True
)