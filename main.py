import streamlit as st
from PIL import Image

st.title('Kana Flash cards')
st.markdown('#### Profitez de votre temps libre pour pratiquer les hiragana et les katakana !')

image = Image.open("kana_renshuu.png")
st.image(image)
