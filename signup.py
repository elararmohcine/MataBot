# signup.py
import streamlit as st
from dependancies import sign_up, fetch_users
import traceback
import streamlit_authenticator as stauth
import os
from io import BytesIO
import base64
def get_video_base64(video_path):
    if os.path.exists(video_path):
        with open(video_path, "rb") as file:
            video_base64 = base64.b64encode(file.read()).decode("utf-8")
        return video_base64
    else:
        st.error("Video file not found.")



video_path_sign_up = "animations/untitled-video-made-with-clipchamp-1_VX3IUxCI.mp4"

video_base64_sign_up = get_video_base64(video_path_sign_up)
def show_signup_page():
    st.title("")
    # Define column widths
    video_column_width = 1
    form_column_width = 3

    # Create columns
    video_col, form_col = st.columns([video_column_width, form_column_width])

    # Left column (video)
    with video_col:
        video_html_sign_up = f"""
                        <style>
                            #videoLeft {{
                                position: fixed;
                                left: 50px;
                                bottom: 200px;
                                width: 40%;
                                height: 40%;
                                border: 1px solid #010136; /* Add border to the video */
                                box-shadow: 7px 7px 12px rgba(0, 0, 0, 0.5); /* Add shadow to the video */

                            }}
                        </style>
                        <video autoplay muted loop id="videoLeft">
                            <source src="data:video/mp4;base64,{video_base64_sign_up}" type="video/mp4">
                            Your browser does not support HTML5 video.
                        </video>
                    """
        st.markdown(video_html_sign_up, unsafe_allow_html=True)

    # Right column (form)
    with form_col:
        sign_up_html = """
                        <style>
                            [class="st-emotion-cache-o7kwkx e1f1d6gn2"] {
                                width: 100%;
                                position: relative;
                                justify-content: flex-end;
                                right: -195px;
                                top: -100px;


                            }
                        </style>
                    """
        st.markdown(sign_up_html, unsafe_allow_html=True)
        sign_up()


    if st.sidebar.button("Login"):
        st.session_state.page = 'login'
    if st.sidebar.button("home"):
        st.session_state.page = 'home'