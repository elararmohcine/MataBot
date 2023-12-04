import streamlit as st
import soundfile as sf
import numpy as np
import os
import tempfile
import sounddevice as sd
import speech_recognition as sr

# Fonction principale de l'application Streamlit
def main():
    st.title("Enregistrement Audio")

    # Utiliser des variables de session pour suivre l'état de l'enregistrement
    if "recording" not in st.session_state:
        st.session_state.recording = False

    # Créer un bouton pour commencer ou arrêter l'enregistrement
    if st.button("Commencer/Arrêter l'enregistrement"):
        if st.session_state.recording:
            st.session_state.recording = False
        else:
            st.session_state.recording = True

    # Enregistrement de l'audio
    if st.session_state.recording:
        st.info("Enregistrement en cours...")
        audio_data = record_audio()
        st.success("Enregistrement terminé!")

        # Convertir l'audio en texte en utilisant la bibliothèque SpeechRecognition
        text_result = convert_audio_to_text(audio_data)
        if text_result is not None:
            st.write("Résultat de la transcription audio :")
            st.write(text_result)

def record_audio():
    # Paramètres d'enregistrement
    sample_rate = 44100
    channels = 1
    duration = 5  # Vous pouvez ajuster la durée d'enregistrement selon vos besoins

    # Enregistrement de l'audio
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=channels, dtype=np.int16)
    sd.wait()

    return audio_data

def convert_audio_to_text(audio_data):
    # Sauvegarder les données audio dans un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        sf.write(temp_audio_file.name, audio_data, 44100)

    # Convertir l'audio en texte en utilisant la bibliothèque SpeechRecognition
    recognizer = sr.Recognizer()
    audio_file_path = temp_audio_file.name

    with sr.AudioFile(audio_file_path) as source:
        audio_text = recognizer.record(source)

    try:
        text_result = recognizer.recognize_google(audio_text, language='fr-FR')
        return text_result
    except sr.UnknownValueError:
        st.warning("Impossible de transcrire l'audio. Aucune parole détectée.")
        return None
    except sr.RequestError as e:
        st.error(f"Erreur lors de la demande à l'API Google : {e}")
        return None
    finally:
        # Supprimer le fichier temporaire après utilisation
        os.remove(temp_audio_file.name)

if __name__ == "__main__":
    main()
