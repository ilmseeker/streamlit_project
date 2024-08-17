import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="About Page", 
                   page_icon="🎈️", 
                   layout="wide",
                   initial_sidebar_state="collapsed")

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

# Define custom CSS for button styling
button_style = """
    <style>
    .stButton>button {
        color: white;
        background-color: #4CAF50; /* Green */
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stButton.red-button>button {
        background-color: #f44336; /* Red */
    }
    .stButton.red-button>button:hover {
        background-color: #da190b; /* Darker red on hover */
    }
    </style>
    """
st.markdown(button_style, unsafe_allow_html=True)


