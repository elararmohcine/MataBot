# login.py
import streamlit as st
from dependancies import sign_up, fetch_users
import traceback
import streamlit_authenticator as stauth
import os
from io import BytesIO
import base64
from Mata import main, transition_video
from home import show_home_page
def show_login_page():
    session_state = st.session_state

    if 'transition_displayed' not in session_state:
        session_state.transition_displayed = False
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='email', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':black[Login]', 'main')

    info, info1 = st.columns(2)

    if username:
        if username in usernames:
            if authentication_status:

                if not session_state.transition_displayed:
                    transition_video()
                    session_state.transition_displayed = True
                main()
                Authenticator.logout('Log Out', 'sidebar')

            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')


