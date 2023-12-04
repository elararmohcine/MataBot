# import streamlit as st
# import base64
#
# file_path = r"C:\Users\mohci\Downloads/AdobeStock_95385826_Video_HD_Preview.gif"
#
# # Lecture du fichier GIF
# file_ = open(file_path, "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()
#
# # Personnalisation de la taille du GIF
# width = 400  # spécifiez la largeur souhaitée en pixels
# height = 300  # spécifiez la hauteur souhaitée en pixels
#
# # Affichage du GIF avec la taille personnalisée
# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="{width}" height="{height}">',
#     unsafe_allow_html=True,
# )


import streamlit as st
import base64

file_path = r"C:\Users\mohci\Downloads/AdobeStock_95385826_Video_HD_Preview.gif"

# Lecture du fichier GIF
file_ = open(file_path, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

# Affichage du GIF avec la taille personnalisée pour occuper toute la largeur et être centré
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <img src="data:image/gif;base64,{data_url}" alt="cat gif" style="width:100%; max-width: 100%; max-height: 100vh;">
    </div>
    """,
    unsafe_allow_html=True,
)
