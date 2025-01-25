
import streamlit as st
from PIL import Image


img = Image.open('aaa.jpg')

st.title("Embedding Dify app in Streamlit")

st.image(img)

# Dify APIのベースURL
BASE_URL = 'https://api.dify.ai/v1/workflows/run'
API_KEY = 'app-esamNSyt3DcelD4o6yM9uH4U'  # 取得したAPIキーに置き換えてください





