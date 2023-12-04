# home.py
import streamlit as st

if 'clicked_1' not in st.session_state:
    st.session_state.clicked_1 = False
if 'clicked_2' not in st.session_state:
    st.session_state.clicked_2 = False

def clicked(button_id):
    if button_id == 1:
        st.session_state.clicked_1 = True
    elif button_id == 2:
        st.session_state.clicked_2 = True

def show_home_page():
    st.title("Bienvenue chez Mata bot, votre assistance en radiologie !")
    st.button('Sign Up', on_click=clicked, args=[1])
    st.button('Login', on_click=clicked, args=[2])

    if st.session_state.clicked_1:
        st.session_state.page = 'signup'
    elif st.session_state.clicked_2:
        st.session_state.page = 'login'
