
import streamlit as st
import base64
import sys
from PIL import Image


st.title("Embedding Dify app in Streamlit")

# img = Image.open('aaa.jpg')
# st.image(img)


# 画像ファイルをbase64エンコードしてCSSに埋め込む
def get_base64_of_image(image_path):
    encoded_string = base64.b64encode(image_file.read()).decode()
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = "test"
            # encoded_string = base64.b64encode(image_file.read()).decode()
    except FileNotFoundError as e:
        sencoded_string = e
        
    return encoded_string

# 画像ファイルのパス
IMAGE_PATH = "aaa.jpeg" # ここにイメージファイルのパスを設定してください

# 画像をbase64エンコード
image_base64 = get_base64_of_image('aaa.jpeg')





