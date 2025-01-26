
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

# 画像ファイルのパス
IMAGE_PATH = "./aaa.jpeg" # ここにイメージファイルのパスを設定してください

st.title("Embedding Dify app in Streamlit")

# img = Image.open('aaa.jpg')
# st.image(img)

# 画像を読み込み
try:
  image = Image.open(IMAGE_PATH)
except FileNotFoundError:
    st.error(f"エラー：画像ファイル '{IMAGE_PATH}' が見つかりませんでした。")
    st.stop()

# 画像をバイト列に変換
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()
img_url = f"data:image/jpeg;base64,{img_str}"








