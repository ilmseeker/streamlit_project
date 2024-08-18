import os, sys
# Get the path to the 'Streamlit_Project' directory
project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

# Add the project root to sys.path if it's not already there
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
st.set_page_config(page_title="Page Title", 
                   page_icon="Icon", 
                   layout="wide", 
                   initial_sidebar_state="collapsed"
                   )


from main_code.css.css import button_style

st.markdown( 
    """ <style> [data-testid="collapsedControl"] { display: none } </style> """, 
    unsafe_allow_html=True, )

rain(
    emoji="❄️",
    font_size=36,
    falling_speed=20,
    animation_length="infinite",
    )

# Use an empty column and the button in the rightmost column
cols = st.columns([9, 1])
with cols[0]:
    st.title("This is About Us page")
with cols[1]:
    button2 = st.button('Home', key=1, use_container_width=True)
if button2:
    switch_page("home")

st.markdown(button_style, unsafe_allow_html=True)