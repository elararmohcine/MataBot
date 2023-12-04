import streamlit as st
from gtts import gTTS
import os
from io import BytesIO
import base64

def text_to_speech(text, lang='fr'):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)

    # Save audio data to a temporary file
    temp_filename = r"C:\Users\mohci\PycharmProjects\MataBot/temp.mp3"
    with open(temp_filename, "wb") as f:
        f.write(audio_bytes.getvalue())

    return temp_filename

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
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

def main():
    st.title("Text to Speech en Français avec Streamlit")

    # Text area for entering the text
    input_text = st.text_area("Saisissez votre texte en français")

    # Button to trigger text-to-speech
    if st.button("Lire le texte"):
        if input_text:
            st.success("Synthèse vocale en cours...")
            audio_file = text_to_speech(input_text)
            print(audio_file)

            # Display and autoplay the audio
            autoplay_audio(audio_file)
            os.remove(audio_file)

            st.info("Synthèse vocale terminée!")
        else:
            st.warning("Veuillez saisir du texte à lire.")

if __name__ == "__main__":
    main()
