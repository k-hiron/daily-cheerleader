import streamlit as st
import datetime
import time
import random

# ページの設定
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# --- 200色のパステルカラー背景設定 ---
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"  # 初期色

def change_color():
    # 200色に近いバリエーションを生むランダムパステルカラー
    r = lambda: random.randint(200, 255)
    st.session_state.bg_color = f'#%02X%02X%02X' % (r(), r(), r())

# 背景色を適用するCSS
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.5s ease;
    }}
    </style>
""", unsafe_allow_html=True)

# --- メインコンテンツ ---
st.write(f"<h2 style='text-align: center;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# 時刻と日付の取得
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y / %b %d")

# --- スマホ・PC両対応の時刻表示 ---
st.markdown(f"""
    <div style="
        border: 5px solid #FFD700; 
        border-radius: 20px; 
        padding: 10px; 
        margin: 10px 0;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.5);
    ">
        <h1 style="
            color: #FF8C00; 
            margin: 0;
            font-size: min(15vw, 90px);
            white-space: nowrap;
            font-family: 'Courier New', Courier, monospace;
        ">
            {current_time}
        </h1>
    </div>
""", unsafe_allow_html=True)

st.write(f"<h3 style='text-align: center;'>✨ {current_date} ✨</h3>", unsafe_allow_html=True)

# 応援ボタン
if st.button("✨ Click for your cheer! ✨", on_click=change_color, use_container_width=True):
    st.balloons()
    messages = [
        "You're doing amazing! (最高に輝いてるよ！)",
        "Believe in yourself! (自分を信じて！)",
        "Every step counts! (一歩一歩が力になるよ！)",
        "You've got this! (あなたならできる！)",
        "Keep shining today! (今日も輝き続けよう！)"
    ]
    st.info(random.choice(messages))

# 1秒ごとに更新
time.sleep(1)
st.rerun()
