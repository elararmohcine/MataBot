import streamlit as st
import speech_recognition as sr
import time


def process_voice_input():
    # Streamlit app
    st.title("Application de traitement vocal")

    # Message for recording state
    recording_message = None  # Initial message state

    # Voice input
    r = sr.Recognizer()

    # Layout options to position the button at the bottom right
    col1, col2, col3 = st.columns([1, 1, 1])

    with col3:
        record_question = st.button("Enregistrer une question via la voix", key="record_button")



    st.markdown("""
                <style>
                div.stButton > button:first-child {
                    
                    position: fixed;
                    bottom: 15px;
                    right: 15px;
                    margin: 15px;
                }
                div.stButton > button:hover {
                    background-color: #FAB6AD;
                    color:##ff99ff;
                    }
                </style>""", unsafe_allow_html=True)

    if record_question:
        with st.container():
            # Voice input
            with sr.Microphone() as source:
                recording_message = st.empty()
                recording_message.write("Enregistrement en cours... Parlez maintenant...")
                audio = r.listen(source, phrase_time_limit=8)

            try:
                # Use Google Web Speech API to recognize speech
                user_question = r.recognize_google(audio, language="fr-FR")

                # Display the recognized text
                st.write(f"Texte obtenu depuis l'audio: {user_question}")



            except sr.UnknownValueError:
                # If speech is not recognized
                st.warning("Désolé, la parole n'a pas pu être reconnue.")





# Run the Streamlit app
if __name__ == "__main__":
    process_voice_input()
