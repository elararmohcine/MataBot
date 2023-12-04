import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
from dotenv import load_dotenv
import os


DETA_KEY = st.secrets["DETA_KEY"]
# Load the environment variables
load_dotenv(".env")


deta = Deta(DETA_KEY)

db = deta.Base('Mata') # Creer une base dans https://deta.space/collections


def insert_user(email, username, tel, num, pro, password):
    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
    date_joined = str(datetime.datetime.now())

    return db.put({'username': username, 'key': email, 'tel': tel,'num': num, 'pro':pro, 'password': password, 'date_joined': date_joined})


def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items


def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user['key'])
    return emails


def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['key'])
    return usernames


def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        return True
    return False


def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """

    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False


def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':black[Sign Up]')
        username = st.text_input(':black[Nom complet]', placeholder='Entrez votre nom complet')
        email = st.text_input(':black[Email]', placeholder='Entrez votre adresse e-mail.')
        tel = st.text_input(':black[Tél]', placeholder='Entrez votre numéro de téléphone')
        num = st.text_input(':black[RPPS]', placeholder='Entrez votre numéro RPPS (facultatif)')
        pro = st.text_input(':black[Profession]', placeholder='Entrez votre Profession')
        password1 = st.text_input(':black[Password]', placeholder='Entrez votre mot de passe', type='password')
        password2 = st.text_input(':black[Confirm Password]', placeholder='Confirmez votre mot de passe', type='password')

        if email:
            if validate_email(email):
                if email not in get_user_emails():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >= 2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        # Add User to DB
                                        hashed_password = stauth.Hasher([password2]).generate()
                                        insert_user(username, email, tel, num, pro, hashed_password[0])
                                        st.success('Account created successfully!!')
                                        # st.balloons()
                                    else:
                                        st.warning('Passwords Do Not Match')
                                else:
                                    st.warning('Password is too Short')
                            else:
                                st.warning('Username Too short')
                        else:
                            st.warning('Username Already Exists')

                    else:
                        st.warning('Invalid Username')
                else:
                    st.warning('Email Already exists!!')
            else:
                st.warning('Invalid Email')

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            st.form_submit_button('Sign Up')

# sign_uo()



# sign_up()


