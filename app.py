import streamlit as st
import datetime
import random
import time

# --- 1. ページの設定（タブに表示される名前やアイコン） ---
st.set_page_config(page_title="My Daily Cheerleader", page_icon="🌟")

# --- 2. 応援メッセージのリスト ---
cheers = [
    "You are doing an amazing job! (本当によくやってるよ！天才！)",
    "Believe in yourself! (自分を信じて！あなたならできる！)",
    "Every step counts. (どんな一歩も無駄じゃないよ。)",
    "You shine brighter than the stars! (あなたは星よりも輝いてる！)",
    "Take a deep breath and smile. (深呼吸して、笑ってみて。)",
    "I'm so proud of you! (あなたのことを本当に誇りに思うよ！)",
    "Today is going to be a great day! (今日はきっと最高の1日になる！)"
]

# --- 3. デザインの調整（CSS） ---
st.markdown("""
    <style>
    .main {
        background-color: #FFF9E3;
    }
    .stButton>button {
        background-color: #FFD700;
        color: #5C4033;
        font-weight: bold;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #FFC400;
        color: #5C4033;
    }
    h1, h2, h3 {
        color: #D4AF37;
        text-align: center;
    }
    .time-display {
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px;
        font-weight: bold;
        color: #FF8C00;
        text-align: center;
        background: #FFFFFF;
        padding: 10px;
        border-radius: 15px;
        border: 3px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. メイン画面の表示 ---
st.markdown("### 🌟 My Daily Cheerleader")

# 時刻表示用のコンテナ（ここが1秒ごとに書き換わります）
time_placeholder = st.empty()

# 日付の表示
now = datetime.datetime.now()
st.header(f"✨ {now.strftime('%Y')} ✨")
st.markdown(f"<h1 style='font-size: 80px; margin: 0;'>{now.strftime('%b %d')}</h1>", unsafe_allow_html=True)

st.write("---")

# --- 5. 応援ボタンの機能 ---
if st.button("✨ Click for your cheer! ✨"):
    st.balloons()
    selected_cheer = random.choice(cheers)
    st.success(selected_cheer)
else:
    st.info("Are you ready to shine today? (さあ、今日も輝く準備はいい？)")

# --- 6. リアルタイム時計の処理（無限ループ） ---
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    # プレースホルダーの中身だけを書き換える
    time_placeholder.markdown(f"<div class='time-display'>{current_time}</div>", unsafe_allow_html=True)
    time.sleep(1) # 1秒待機