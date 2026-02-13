import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# --- 背景色のセッション管理 ---
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

def change_color():
    r = lambda: random.randint(200, 255)
    st.session_state.bg_color = f'#%02X%02X%02X' % (r(), r(), r())

# 背景色とスタイルの適用
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.8s ease;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .message-box {{
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 20px;
        color: #444;
        line-height: 1.6;
        font-size: 1rem;
        text-align: left;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }}
    </style>
""", unsafe_allow_html=True)

# --- メインコンテンツ ---
st.markdown("<h2 style='text-align: center;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# --- 世界時刻対応・時計表示 (JavaScript) ---
st.markdown("""
    <div id="clock-container" style="
        border: 5px solid #FFD700; 
        border-radius: 25px; 
        padding: 15px; 
        margin: 15px 0;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.6);
    ">
        <h1 id="clock-display" style="
            color: #FF8C00; 
            margin: 0;
            font-size: min(16vw, 100px);
            white-space: nowrap;
            font-family: 'Courier New', Courier, monospace;
        ">--:--:--</h1>
        <h3 id="date-display" style="color: #666; margin-top: 10px;">---- / -- --</h3>
    </div>

    <script>
    function updateClock() {
        const now = new Date();
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        const options = { year: 'numeric', month: 'short', day: '2-digit' };
        const dateStr = now.toLocaleDateString('en-US', options).replace(',', ' /');
        
        document.getElementById('clock-display').textContent = h + ':' + m + ':' + s;
        document.getElementById('date-display').textContent = '✨ ' + dateStr + ' ✨';
    }
    setInterval(updateClock, 1000);
    updateClock();
    </script>
""", unsafe_allow_html=True)

# --- 200字のメッセージセクション ---
st.markdown("""
    <div class="message-box">
        <strong>💌 あなたへのメッセージ</strong><br>
        今日という日は、世界にたった一度きり。あなたが今、この画面を見ているその瞬間も、一歩ずつ未来へ進んでいる証拠です。
        たとえ大きな成果が見えない日でも、深呼吸をして、今日を生き抜いている自分を誇りに思ってください。
        完璧じゃなくていい、少しずつでいい。あなたの歩むスピードが、あなたにとっての正解です。
        この時計が刻む一秒一秒が、あなたの努力と優しさを静かに見守っています。今日も本当にお疲れ様。あなたは、そのままで十分に素晴らしい存在です。
    </div>
""", unsafe_allow_html=True)

st.write("") # スペース

# --- 応援ボタン ---
if st.button("✨ Click for your cheer! ✨", on_click=change_color, use_container_width=True):
    st.balloons()
    messages = [
        "You're doing amazing!",
        "Believe in yourself!",
        "Every step counts!",
        "You've got this!",
        "Keep shining today!"
    ]
    st.success(random.choice(messages))
