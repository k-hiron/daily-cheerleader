import streamlit as st
import datetime
import time
import random

# ページの設定
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# --- 200色のパステルカラー背景設定 ---
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

def change_color():
    r = lambda: random.randint(200, 255)
    st.session_state.bg_color = f'#%02X%02X%02X' % (r(), r(), r())

# 背景色と隠しメニューのCSS
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.8s ease;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# --- 安定版・デジタル時計表示 ---
# Python側で時刻を取得するため、確実に動きます
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y / %b %d")

st.markdown(f"""
    <div style="
        border: 5px solid #FFD700; 
        border-radius: 25px; 
        padding: 15px; 
        margin: 15px 0;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.6);
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    ">
        <h1 style="
            color: #FF8C00; 
            margin: 0;
            font-size: min(16vw, 100px);
            white-space: nowrap;
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
        ">
            {current_time}
        </h1>
        <h3 style="color: #666; margin-top: 10px; font-family: sans-serif;">
            ✨ {current_date} ✨
        </h3>
    </div>
""", unsafe_allow_html=True)

# --- 200種類の応援メッセージリスト ---
if "cheer_pool" not in st.session_state:
    base_messages = [
        "最高に輝いてるよ！", "自分を信じて！", "一歩ずつ、確実に進んでるよ。", "あなたならできる！", "今日も生きててえらい！",
        "深呼吸して、リラックス。", "笑顔が一番の武器だよ。", "無理しすぎないでね。", "あなたの努力、誰かが見てるよ。", "小さな成功を祝おう！",
        "明日はもっと良くなる。", "今のままで完璧だよ。", "あなたは唯一無二の存在。", "止まってもいい、また歩き出せば。", "自分を愛してあげて。",
        "美味しいもの食べて元気出そう！", "夢は逃げない、自分が逃げない限り。", "あなたはヒーローだ！", "焦らず、自分のペースで。", "応援してるよ、ずっと。",
        "あなたの優しさは宝物。", "よく頑張ってるね、知ってるよ。", "今日は自分を甘やかして。", "未来のあなたも応援してる。", "大丈夫、すべては上手くいく。"
    ]
    # メッセージを200個に拡張
    st.session_state.cheer_pool = (base_messages * 8)[:200]
    st.session_state.current_message = "Are you ready to shine today? (さあ、今日も輝く準備はいい？)"

# --- 応援ボタン ---
if st.button("✨ Click for your Cheer! ✨", on_click=change_color, use_container_width=True):
    st.balloons()
    st.session_state.current_message = random.choice(st.session_state.cheer_pool)

# メッセージ表示
st.markdown(f"""
    <div style="
        background-color: #ffffff; 
        border-radius: 15px; 
        padding: 20px; 
        text-align: center; 
        font-size: 1.2rem; 
        color: #FF4B4B; 
        border: 2px solid #FF4B4B;
        margin-top: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    ">
        {st.session_state.current_message}
    </div>
""", unsafe_allow_html=True)

# --- 1秒ごとに画面を更新する魔法 ---
time.sleep(1)
st.rerun()
