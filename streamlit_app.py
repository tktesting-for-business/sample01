import streamlit as st
import streamlit.components.v1 as stc
import base64
from PIL import Image,ImageDraw

# インプット画像ファイルのパス
IMAGE_PATH = "aaa.jpg"
# アウトプット画像ファイルのパス
OUTPUT_PATH = "output_image.jpeg"

st.title("Embedding Dify app in Streamlit")
st.write("元の画像")
# 画像を読み込み
try:
    img = Image.open(IMAGE_PATH)
    st.image(img)
    # 画像サイズを取得
    width, height = img.size
    st.write(str(width) + "," + str(height))

except FileNotFoundError:
    st.error(f"エラー：画像ファイル '{IMAGE_PATH}' が見つかりませんでした。")
    st.stop()

# リサイズ後の最大サイズ
MAX_WIDTH = width
MAX_HEIGHT = height

#box_x = 123
#box_y = 136
#box_w = 114
#box_h = 23

if __name__ == "__main__":
    # テキストボックス
    box_x = st.text_input("x")
    box_y = st.text_input("y")
    box_w = st.text_input("w")
    box_h = st.text_input("h")
    # ボタン
    if st.button("Dify APIを呼び出す"):

        # 画像を読み込み
        try:
            image = Image.open(IMAGE_PATH).convert("RGB") # RGBに変換
            # resized_image = resize_image(image, max_width, max_height) #リサイズ
        except FileNotFoundError:
            st.error(f"エラー：画像ファイル '{IMAGE_PATH}' が見つかりませんでした。")
            st.stop()
        
        # 画像サイズを取得
        width, height = image.size
        
        # ImageDraw オブジェクトを作成
        draw = ImageDraw.Draw(image)
        # 赤枠を描画
        draw.rectangle(
          [(box_x, box_y), (box_x + box_w, box_y + box_h)], outline="red", width=2
        )
  
        # 加工後の画像を保存
        image.save(OUTPUT_PATH, "JPEG")
    
        # 画面に表示
        st.write("文字を赤枠で囲った画像")
        st.image(image, caption='赤枠が追加された画像', use_column_width=True)



# 画像をリサイズする関数
def resize_image(image, max_width, max_height):
    image.thumbnail((max_width, max_height), Image.LANCZOS)  # Lanczosフィルタを使用
    return image





  
