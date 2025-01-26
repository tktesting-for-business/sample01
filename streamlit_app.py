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

# 画面サイズを調整
resized_image = resize_image(image, MAX_WIDTH, MAX_HEIGHT)

# 画面に表示する場合 (Streamlitを使う場合)
st.image(resized_image, caption='赤枠が追加された画像', use_column_width=True)
