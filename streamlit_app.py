
import streamlit as st
import streamlit.components.v1 as stc
import base64
from PIL import Image,ImageDraw
from io import BytesIO

# 画像ファイルのパス
IMAGE_PATH = "aaa.jpg" # ここにイメージファイルのパスを設定してください

st.title("Embedding Dify app in Streamlit")

img = Image.open('aaa.jpg')
st.image(img)

# 画像サイズを取得
width, height = img.size
st.write(str(width) + "," + str(height))

# 画像を読み込み
try:
  image = Image.open(IMAGE_PATH)
except FileNotFoundError:
    st.error(f"エラー：画像ファイル '{IMAGE_PATH}' が見つかりませんでした。")
    st.stop()

# 画像をリサイズする関数
def resize_image(image, max_width, max_height):
    image.thumbnail((max_width, max_height), Image.LANCZOS)  # Lanczosフィルタを使用
    return image

# リサイズ後の最大サイズ
MAX_WIDTH = width
MAX_HEIGHT = height
resized_image = resize_image(image, MAX_WIDTH, MAX_HEIGHT)


# 画像をバイト列に変換
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()
img_url = f"data:image/jpeg;base64,{img_str}"

# st.write(img_url)
# st.write(img_str)

# CSSで枠のスタイルを定義（背景画像を含む）
BOX_STYLE = f"""
<style>
.box {{
    border: 2px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    background-image: url('{img_url}');
    background-size: contain; /* 画像を枠内に収める */
    background-repeat: no-repeat; /* 画像を繰り返さない */
    background-position: center; /* 画像を中央に配置 */
    min-width: {MAX_WIDTH}px;
    min-height: {MAX_HEIGHT}px;
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
<div class="box" style="background-color: rgba(255, 255, 0, 0.5);">
    <h3>半透明な背景</h3>
    <p>文字を読みやすくするために背景色を調整できます。</p>
</div>
""", unsafe_allow_html=True)



# 画像を読み込み
try:
    image = Image.open(IMAGE_PATH).convert("RGB") # RGBに変換
except FileNotFoundError:
    print(f"エラー：画像ファイル '{IMAGE_PATH}' が見つかりませんでした。")
    exit()

# 画像サイズを取得
width, height = image.size

# 赤枠のサイズと位置を定義 (例：画像の中央)
box_size = 50
box_x = (width - box_size) // 2
box_y = (height - box_size) // 2
box_coords = (box_x, box_y, box_x + box_size, box_y + box_size)

# ImageDraw オブジェクトを作成
draw = ImageDraw.Draw(image)

# 赤枠を描画
draw.rectangle(box_coords, outline="red", width=2)

# 結果を保存するファイルパス
OUTPUT_PATH = "output_image.jpeg"

# 加工後の画像を保存
image.save(OUTPUT_PATH, "JPEG")

# 画面に表示する場合 (Streamlitを使う場合)
# import streamlit as st
st.image(image, caption='赤枠が追加された画像', use_column_width=True)
