import streamlit as st
import os
from gtts import gTTS

from io import BytesIO
import base64

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def clicked():
    st.session_state.clicked = True
def audio(text, lang='fr'):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)

    # Save audio data to a temporary file
    temp_filename = r"C:\Users\mohci\PycharmProjects\MataBot/temp.mp3"
    with open(temp_filename, "wb") as f:
        f.write(audio_bytes.getvalue())
    if os.path.exists(temp_filename):
        with open(temp_filename, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio controls autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(
                md,
                unsafe_allow_html=True,
            )
    else:
        st.warning("Le fichier audio n'existe pas.")
    os.remove(temp_filename)
# Button with callback function
st.button('Button', on_click=clicked)


if st.session_state.clicked:
    audio("Bonjour")
