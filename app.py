import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# --- 背景色のセッション管理 ---
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

def change_color():
    # 200色以上のパステルバリエーション
    r = lambda: random.randint(200, 255)
    st.session_state.bg_color = f'#%02X%02X%02X' % (r(), r(), r())

# 背景色とアニメーションのCSS
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.8s ease;
    }}
    /* ストリームリットの標準メニューを少し隠してアプリ感を出す */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- メインコンテンツ ---
st.markdown("<h2 style='text-align: center; font-family: sans-serif;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# --- 世界時刻対応・レスポンシブ時計 (JavaScript) ---
st.markdown("""
    <div id="clock-container" style="
        border: 5px solid #FFD700; 
        border-radius: 25px; 
        padding: 15px; 
        margin: 15px 0;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.6);
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    ">
        <h1 id="clock" style="
            color: #FF8C00; 
            margin: 0;
            font-size: min(16vw, 100px); /* iPhoneの幅に合わせて自動縮小 */
            white-space: nowrap;         /* 改行を防止 */
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
        ">
            00:00:00
        </h1>
        <h3 id="date" style="color: #666; margin-top: 10px; font-family: sans-serif;">
            ---- / -- --
        </h3>
    </div>

    <script>
    function updateClock() {
        const now = new Date(); // アクセスしたデバイスの現地時刻を取得
        
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        
        const options = { year: 'numeric', month: 'short', day: '2-digit' };
        const dateStr = now.toLocaleDateString('en-US', options).replace(',', ' /');

        document.getElementById('clock').textContent = h + ':' + m + ':' + s;
        document.getElementById('date').textContent = '✨ ' + dateStr + ' ✨';
    }
    // 1秒ごとに更新
    setInterval(updateClock, 1000);
    updateClock(); // 初回実行
    </script>
""", unsafe_allow_html=True)

# --- 応援ボタン ---
st.write("") # スペース
if st.button("✨ Click for your cheer! ✨", on_click=change_color, use_container_width=True):
    st.balloons()
    messages = [
        "You're doing amazing! (最高に輝いてるよ！)",
        "Believe in yourself! (自分を信じて！)",
        "Every step counts! (一歩一歩が力になるよ！)",
        "You've got this! (あなたならできる！)",
        "Keep shining today! (今日も輝き続けよう！)",
        "You are your own hero! (君は君自身のヒーローだ！)",
        "Take a deep breath and smile! (深呼吸して笑って！)"
    ]
    st.success(random.choice(messages))
