import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
import time


recording_message = None  # Initial message state
record_question = st.button("Enregistrer une question via la voix")
if record_question:
    # Voice input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        recording_message = st.empty()
        recording_message.write("Enregistrement en cours... Parlez maintenant...")
        # recording_message = st.write("Enregistrement en cours... Parlez maintenant...")
        audio = r.listen(source, phrase_time_limit=8)

        start_time = time.time()  # Record the start time before starting to listen
        if time.time() - start_time > 5:  # Check if time limit is exceeded
            recording_message.empty()  # Remove the recording message

    try:
        # Use Google Web Speech API to recognize speech
        user_question = r.recognize_google(audio, language="fr-FR")

        # Display the recognized text in the text input area
        # user_question = st.text_area("Question (Entrée vocale)", value=user_question, height=100)
        user_question = st.chat_input(user_question)
    except sr.UnknownValueError:
        # If speech is not recognized
        st.warning("Désolé, la parole n'a pas pu être reconnue.")
        user_question = st.chat_input("")
    finally:
        if recording_message is not None:
            recording_message.empty()  # Remove the message after audio detection


else:
    # Option to enter question manually (text)
    user_question = st.chat_input("Comment puis-je vous assister, Docteur ?")