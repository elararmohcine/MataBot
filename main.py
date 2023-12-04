# main.py
import streamlit as st
from home import show_home_page
from signup import show_signup_page
from login import show_login_page

# Initialisez les clés clicked_1 et clicked_2 si elles ne sont pas présentes dans st.session_state
if 'clicked_1' not in st.session_state:
    st.session_state.clicked_1 = False
if 'clicked_2' not in st.session_state:
    st.session_state.clicked_2 = False

# Initialisez la clé 'page' si elle n'est pas présente dans st.session_state
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
