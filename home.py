# home.py
import streamlit as st

# Utilisez st.session_state.get pour obtenir la valeur par défaut si la clé n'existe pas
clicked_1 = st.session_state.get('clicked_1', False)
clicked_2 = st.session_state.get('clicked_2', False)

def clicked(button_id):
    if button_id == 1:
        st.session_state.clicked_1 = True
    elif button_id == 2:
        st.session_state.clicked_2 = True

def show_home_page():
    st.title("Bienvenue chez Mata bot, votre assistance en radiologie !")
    st.button('Sign Up', on_click=clicked, args=[1])
    st.button('Login', on_click=clicked, args=[2])

    # Utilisez st.session_state.get pour obtenir la valeur par défaut si la clé n'existe pas
    if st.session_state.get('clicked_1', False):
        st.session_state.page = 'signup'
    elif st.session_state.get('clicked_2', False):
        st.session_state.page = 'login'
