import streamlit as st
import datetime
import random
import time

# --- 1. ページの設定 ---
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
    .main { background-color: #FFF9E3; }
    .stButton>button {
        background-color: #FFD700; color: #5C4033;
        font-weight: bold; border-radius: 20px;
    }
    .time-display {
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px; font-weight: bold;
        color: #FF8C00; text-align: center;
        background: #FFFFFF; padding: 10px;
        border-radius: 15px; border: 3px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. メイン画面の表示 ---
st.markdown("### 🌟 My Daily Cheerleader")

# 時刻表示用の場所を確保
time_placeholder = st.empty()

# --- 5. アクセスした人の国の時刻を取得する仕組み ---
# ブラウザの現在時刻を表示するためのJavaScript
st.markdown("""
    <script>
    function updateClock() {
        const now = new Date();
        const timeStr = now.getHours().toString().padStart(2, '0') + ':' +
                        now.getMinutes().toString().padStart(2, '0') + ':' +
                        now.getSeconds().toString().padStart(2, '0');
        // Streamlitの要素に書き込むための処理（簡易版）
        parent.document.querySelector('.time-display').innerText = timeStr;
    }
    setInterval(updateClock, 1000);
    </script>
    """, unsafe_allow_html=True)

# --- 6. 日付の表示 (24時間表記対応) ---
now = datetime.datetime.now()
st.header(f"✨ {now.strftime('%Y')} ✨")
st.markdown(f"<h1 style='font-size: 80px; margin: 0;'>{now.strftime('%b %d')}</h1>", unsafe_allow_html=True)

# デジタル時計の初期表示（24時間表記）
current_time = now.strftime("%H:%M:%S")
time_placeholder.markdown(f"<div class='time-display'>{current_time}</div>", unsafe_allow_html=True)

st.write("---")

# --- 7. 応援ボタン ---
if st.button("✨ Click for your cheer! ✨"):
    st.balloons()
    st.success(random.choice(cheers))
else:
    st.info("Are you ready to shine today? (さあ、今日も輝く準備はいい？)")