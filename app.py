import streamlit as st
from PIL import Image

st.title("Hola Mundo!!")

st.header("Wow guys puse texto en una página web")
st. write("ahora que")
image = Image.open('IMG_1936.jpg')

st.image(image, caption='miren a mi gata')


texto = st.text_input('bueno pero', 'y se sabe el chiste del bus')
st.write('pero', texto)
