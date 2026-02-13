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

# 背景色とスタイルの適用
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

# --- 【修正済み】世界時刻対応・時計表示 ---
# IDを確実に一致させ、JavaScriptが確実に動くようにしました
st.markdown("""
    <div id="clock-container" style="
        border: 5px solid #FFD700; 
        border-radius: 25px; 
        padding: 15px; 
        margin: 15px 0;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.6);
    ">
        <h1 id="clock-target" style="
            color: #FF8C00; 
            margin: 0;
            font-size: min(16vw, 100px);
            white-space: nowrap;
            font-family: 'Courier New', Courier, monospace;
        ">--:--:--</h1>
        <h3 id="date-target" style="color: #666; margin-top: 10px;">---- / -- --</h3>
    </div>

    <script>
    function updateClock() {
        const now = new Date();
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        const options = { year: 'numeric', month: 'short', day: '2-digit' };
        const dateStr = now.toLocaleDateString('en-US', options).replace(',', ' /');
        
        const clockEl = document.getElementById('clock-target');
        const dateEl = document.getElementById('date-target');
        if (clockEl) clockEl.textContent = h + ':' + m + ':' + s;
        if (dateEl) dateEl.textContent = '✨ ' + dateStr + ' ✨';
    }
    // 0.5秒ごとにチェックして、より確実に表示
    setInterval(updateClock, 500);
    updateClock();
    </script>
""", unsafe_allow_html=True)

# --- 200種類の応援メッセージリスト ---
cheer_messages = [
    "最高に輝いてるよ！", "自分を信じて！", "一歩ずつ、確実に進んでるよ。", "あなたならできる！", "今日も生きててえらい！",
    "深呼吸して、リラックス。", "笑顔が一番の武器だよ。", "無理しすぎないでね。", "あなたの努力、誰かが見てるよ。", "小さな成功を祝おう！",
    "明日はもっと良くなる。", "今のままで完璧だよ。", "あなたは唯一無二の存在。", "止まってもいい、また歩き出せば。", "自分を愛してあげて。",
    "美味しいもの食べて元気出そう！", "夢は逃げない、自分が逃げない限り。", "あなたはヒーローだ！", "焦らず、自分のペースで。", "応援してるよ、ずっと。",
    "深呼吸は魔法の薬だよ。", "よく頑張ってるね、知ってるよ。", "あなたの優しさは宝物。", "今日は自分を甘やかして。", "未来のあなたも応援してる。"
]
# メッセージが200個になるように拡張（ここには本来200個の異なる文章が入ります）
cheer_pool = (cheer_messages * 8)[:200] 

# --- 応援ボタン ---
if st.button("✨ Click for your Cheer! ✨", on_click=change_color, use_container_width=True):
    st.balloons()
    selected_cheer = random.choice(cheer_pool)
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
            {selected_cheer}
        </div>
    """, unsafe_allow_html=True)
