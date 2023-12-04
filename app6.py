import streamlit as st
import streamlit_authenticator as stauth
import traceback
from dependancies import sign_up, fetch_users




if __name__ == '__main__':
    try:
        st.title("Authentication App")

        # Button to choose between Sign Up and Login
        selected_option = st.radio("Choose an option:", ["Sign Up", "Login"])

        if selected_option == "Sign Up":
            sign_up()
        elif selected_option == "Login":
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
                        st.success('Great !')
                    elif not authentication_status:
                        with info:
                            st.error('Incorrect Password or username')
                    else:
                        with info:
                            st.warning('Please feed in your credentials')
                else:
                    with info:
                        st.warning('Username does not exist, Please Sign up')

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.write(traceback.format_exc())
