
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

# 画像ファイルのパス
IMAGE_PATH = "aaa.jpg" # ここにイメージファイルのパスを設定してください

st.title("Embedding Dify app in Streamlit")

img = Image.open('aaa.jpg')
st.image(img)

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

# CSSで枠のスタイルを定義（背景画像を含む）
BOX_STYLE = f"""
<style>
.box {{
    border: 2px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    background-image: url('{img_url}');
    background-size: cover; /* 画像を枠全体にフィットさせる */
    background-repeat: no-repeat; /* 画像を繰り返さない */
}}
</style>
"""

# CSSを適用
st.markdown(BOX_STYLE, unsafe_allow_html=True)

# 枠付きコンテンツ
st.markdown("""
<div class="box">
    <h3>タイトル</h3>
    <p>ここにコンテンツを記述します。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box" style="background-color: rgba(255, 255, 255, 0.5);">
    <h3>半透明な背景</h3>
    <p>文字を読みやすくするために背景色を調整できます。</p>
</div>
""", unsafe_allow_html=True)






