import streamlit as st
import datetime
import random

# ページの設定
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# --- 200色のパステルカラー背景設定 ---
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

def change_color():
    r = lambda: random.randint(200, 255)
    st.session_state.bg_color = f'#%02X%02X%02X' % (r(), r(), r())

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

# --- ブラウザの現地時刻を表示するJavaScript ---
# サーバーの時刻ではなく、ユーザーが見ているデバイスの時刻を表示します
st.markdown("""
    <div id="clock-container" style="
        border: 5px solid #FFD700; 
        border-radius: 20px; 
        padding: 10px; 
        margin: 10px 0;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.5);
    ">
        <h1 id="clock" style="
            color: #FF8C00; 
            margin: 0;
            font-size: min(15vw, 90px);
            white-space: nowrap;
            font-family: 'Courier New', Courier, monospace;
        ">
            --:----
        </h1>
        <h3 id="date" style="color: #555; margin-top: 10px;">---- / -- --</h3>
    </div>

    <script>
    function updateClock() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        
        const options = { year: 'numeric', month: 'short', day: '2-digit' };
        const dateStr = now.toLocaleDateString('en-US', options).replace(',', ' /');

        document.getElementById('clock').textContent = hours + ':' + minutes + ':' + seconds;
        document.getElementById('date').textContent = '✨ ' + dateStr + ' ✨';
    }
    setInterval(updateClock, 1000);
    updateClock();
    </script>
""", unsafe_allow_html=True)

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
