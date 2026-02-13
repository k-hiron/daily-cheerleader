import streamlit as st
import datetime
import random
import time
from streamlit_javascript import st_javascript

# 1. ページ構成
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# 2. セッション状態の初期化
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"
if "current_message" not in st.session_state:
    st.session_state.current_message = "Ready to shine? (さあ、輝く準備はいい？)"

# メッセージリスト
base_messages = [
    "You're doing amazing! (最高に輝いてるよ！)",
    "Believe in yourself! (自分を信じて！)",
    "Every step counts! (一歩ずつ、確実に進んでるよ！)",
    "You've got this! (あなたならできる！)",
    "Proud of you for living today! (今日も生きててえらい！)",
    "Take a deep breath and relax. (深呼吸して、リラックス。)",
    "Your smile is your best weapon. (笑顔が一番の武器だよ。)",
    "Don't push yourself too hard. (無理しすぎないでね。)",
    "Someone is watching your hard work. (あなたの努力、誰かが見てるよ。)",
    "Celebrate small wins! (小さな成功を祝おう！)",
    "Tomorrow will be even better. (明日はもっと良くなる。)",
    "You are perfect as you are. (今のままで完璧だよ。)",
    "You are one of a kind. (あなたは唯一無二の存在。)",
    "It's okay to stop and rest. (止まってもいい、また歩き出せば。)",
    "Love yourself more. (自分を愛してあげて。)",
    "Eat something yummy! (美味しいもの食べて元気出そう！)",
    "Dreams don't run away. (夢は逃げないよ。)",
    "You are a hero! (あなたはヒーローだ！)",
    "Go at your own pace. (焦らず、自分のペースで。)",
    "I'm always on your side. (応援してるよ、ずっと。)",
    "Your kindness is a treasure. (あなたの優しさは宝物。)",
    "You've worked so hard. (よく頑張ってるね。)",
    "Treat yourself today. (今日は自分を甘やかして。)",
    "Everything's gonna be alright. (大丈夫、すべては上手くいく。)"
]
cheer_pool = (base_messages * 8)[:200]

# 背景色の適用CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.8s ease;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* 2重表示を絶対に許さないためのCSS設定 */
    div[data-testid="stMarkdownContainer"] > div.cheer-box:nth-child(n+2) {{
        display: none !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# 3. 🌍 タイムゾーン自動取得
tz_offset = st_javascript("""new Date().getTimezoneOffset();""")
local_now = datetime.datetime.utcnow() - datetime.timedelta(minutes=(tz_offset if tz_offset else -540))

current_time = local_now.strftime("%H:%M:%S")
current_date = local_now.strftime("%Y / %b %d")

# 時計表示
st.markdown(f"""
    <div style="border: 5px solid #FFD700; border-radius: 25px; padding: 15px; margin: 15px 0; text-align: center; background-color: rgba(255, 255, 255, 0.6);">
        <h1 style="color: #FF8C00; margin: 0; font-size: min(16vw, 100px); font-family: 'Courier New', Courier, monospace; font-weight: bold;">{current_time}</h1>
        <h3 style="color: #666; margin-top: 10px;">✨ {current_date} ✨</h3>
    </div>
""", unsafe_allow_html=True)

# 4. 応援ボタン
if st.button("✨ Click for your Cheer! ✨", use_container_width=True):
    # ボタンが押されたときだけ、セッション状態を直接更新
    r = lambda: random.randint(200, 255)
    st.session_state.bg_color = f'#%02X%02X%02X' % (r(), r(), r())
    st.session_state.current_message = random.choice(cheer_pool)
    st.balloons()
    # ボタン押下直後の2重描画を防ぐため、即座にリラン
    st.rerun()

# 5. 【修正の核心】CSSクラスを付与したメッセージ表示
st.markdown(f"""
    <div class="cheer-box" style="background-color: #ffffff; border-radius: 15px; padding: 20px; text-align: center; font-size: 1.1rem; color: #FF4B4B; border: 2px solid #FF4B4B; margin-top: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); line-height: 1.6;">
        {st.session_state.current_message}
    </div>
""", unsafe_allow_html=True)

# 6. 自動更新
time.sleep(1)
st.rerun()
