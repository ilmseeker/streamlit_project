import streamlit as st
from st_pages import Page, add_page_title, show_pages_from_config
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.app_logo import add_logo
# from streamlit_extras.stateful_button import button

st.set_page_config(page_title="Home Page", 
                   page_icon="🏠", 
                   layout="wide", 
                #    initial_sidebar_state="collapsed"
                   )

show_pages_from_config("main_code//ui//pages.toml")

# add_page_title()

url = "main_code\\images\\images.png"

# st.logo("https://github.com/ilmseeker/images/blob/23b228a94ea9b11e7467495b0b5e8455bbfeefb1/ilmseeker.png")
# add_logo("https://github.com/ilmseeker/images/blob/86530031c7f918bd6f84793e3e62fa6912bf2d31/images.png")
# add_logo(url)
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
## Welcome to your RAG Chatbot

### Click one of the buttons at the :top: to proceed.

**Streamlit is an open-source app framework built specifically for
Machine Learning and Data Science projects.**
**👈 Select a demo from the sidebar** to see some examples
of what Streamlit can do!
### Want to learn more?
- Check out [streamlit.io](https://streamlit.io)
- Jump into our [documentation](https://docs.streamlit.io)
- Ask a question in our [community
    forums](https://discuss.streamlit.io)
"""
)


# pg.run()



# file_path = "main_code/ui/pages.toml"
# print(f"Attempting to read from: {os.path.abspath(file_path)}")
# nav = get_nav_from_toml(file_path)

# script_dir = os.path.dirname(os.path.abspath(__file__))
# toml_path = os.path.join(script_dir, "ui", "pages.toml")
# nav = get_nav_from_toml(toml_path)