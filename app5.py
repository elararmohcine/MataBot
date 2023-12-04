import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import tempfile
import os
def convert_audio_to_text(audio_data):
    # Sauvegarder les données audio dans un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_audio_file.write(audio_data)

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
        # st.write(f"Le fichier temporaire est sauvegardé à l'emplacement : {temp_audio_file.name}")
        os.remove(temp_audio_file.name)
# Définissez une variable pour stocker les données audio
audio_data = None

# Utilisez l'audio_recorder pour capturer les données audio
audio_bytes = audio_recorder(
    text="",
    recording_color="#BF0A0A",
    neutral_color="#FFFFFF",
    icon_size="2x",
)

# Vérifiez si des données audio ont été capturées
if audio_bytes:
    # Stockez les données audio dans la variable audio_data
    audio_data = audio_bytes

    # Appeler la fonction pour convertir l'audio en texte
    text_result = convert_audio_to_text(audio_data)

    # Afficher le résultat
    if text_result:
        st.write("Texte extrait de l'audio:", text_result)
