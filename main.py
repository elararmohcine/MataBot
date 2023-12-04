# app.py
import streamlit as st
from home import show_home_page
from signup import show_signup_page
from login import show_login_page


# if 'sidebar_state' not in st.session_state:
#     st.session_state.sidebar_state = 'collapsed'
# st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)

if 'page' not in st.session_state:
    st.session_state.page = 'home'


# Page principale
if st.session_state.page == 'home':
    show_home_page()

elif st.session_state.page == 'signup':
    show_signup_page()

elif st.session_state.page == 'login':
    show_login_page()

    if st.sidebar.button("home"):
        st.session_state.page = 'home'


