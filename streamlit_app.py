
import streamlit as st
import base64
import sys
from PIL import Image


st.title("Embedding Dify app in Streamlit")

# img = Image.open('aaa.jpg')
# st.image(img)


# 画像ファイルをbase64エンコードしてCSSに埋め込む
def get_base64_of_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
    except FileNotFoundError as e:
        st.write(e)
    
    
    return encoded_string

# 画像ファイルのパス
IMAGE_PATH = "aaa.jpeg" # ここにイメージファイルのパスを設定してください

# 画像をbase64エンコード
image_base64 = get_base64_of_image('aaa.jpeg')

# CSSで枠のスタイルを定義（背景画像を含む）
BOX_STYLE = f"""
<style>
.box {
    border: 2px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    background-image: url('data:image/jpeg;base64,{image_base64}');
    background-size: cover; /* 画像を枠全体にフィットさせる */
    background-repeat: no-repeat; /* 画像を繰り返さない */
}
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



