import streamlit as st
import datetime
import random

# --- 1. ページの設定 ---
st.set_page_config(page_title="My Daily Cheerleader", page_icon="🌟")

# --- 2. 応援メッセージのリスト（200種類） ---
base_cheers = [
    "You're a genius! (天才！)", "Keep shining! (輝き続けて！)", "You've got this! (君ならできる！)",
    "Believe in you! (自分を信じて！)", "So proud of you! (誇りに思うよ！)", "Victory is yours! (勝利は君の手に！)",
    "Amazing work! (素晴らしい仕事！)", "You are magic! (君は魔法だ！)", "Stay positive! (前向きにいこう！)",
    "Love your smile! (笑顔が素敵！)", "Unstoppable! (誰にも止められない！)", "Pure talent! (純粋な才能！)",
    "Dream big! (大きな夢を！)", "Bravo! (ブラボー！)", "You are enough! (そのままで完璧！)",
    "Keep growing! (成長し続けよう！)", "Simply the best! (最高だよ！)", "Future looks bright! (未来は明るい！)",
    "You inspire me! (刺激を受けるよ！)", "Today is special! (今日は特別な日！)"
]
cheers = (base_cheers * 10)[:200] 

# --- 3. カラー生成 ---
def get_random_color():
    return f"#{random.randint(200, 255):02x}{random.randint(200, 255):02x}{random.randint(200, 255):02x}"

if 'bg_color' not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

# --- 4. デザイン (CSS) ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.5s ease;
    }}
    /* 時計の箱をあらかじめ作っておく */
    .clock-box {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 80px; font-weight: bold;
        color: #FF8C00; text-align: center;
        background: rgba(255, 255, 255, 0.9);
        padding: 20px; border-radius: 20px; border: 5px solid #FFD700;
        margin: 20px auto; width: 80%;
    }}
    .date-box {{
        font-size: 40px; text-align: center; font-weight: bold; color: #5C4033;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. メイン画面の表示 ---
st.markdown("<h2 style='text-align: center;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# HTML要素を配置（ここにJavaScriptで書き込む）
st.markdown('<div id="my-clock" class="clock-box">--:--:--</div>', unsafe_allow_html=True)
st.markdown('<div id="my-date" class="date-box">Loading...</div>', unsafe_allow_html=True)

# 🛠 修正版：ブラウザの時間を確実に拾うJavaScript
st.components.v1.html("""
    <script>
    function update() {
        const now = new Date();
        
        // 24時間表記の作成
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        const timeStr = h + ':' + m + ':' + s;
        
        // 日付の作成
        const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        const dateStr = "✨ " + now.getFullYear() + " ✨<br>" + months[now.getMonth()] + " " + now.getDate();

        // 親画面（Streamlit）の要素を探して書き換える
        const clock = window.parent.document.querySelector('#my-clock');
        const date = window.parent.document.querySelector('#my-date');
        
        if (clock) clock.innerText = timeStr;
        if (date) date.innerHTML = dateStr;
    }
    // 0.5秒ごとにチェック（ズレ防止）
    setInterval(update, 500);
    update();
    </script>
    """, height=0)

st.write("---")

# --- 6. 応援ボタン ---
if st.button("✨ Click for your cheer! ✨", use_container_width=True):
    st.session_state.bg_color = get_random_color()
    st.balloons()
    st.success(random.choice(cheers))
    st.rerun()
else:
    st.info("Are you ready to shine today? (さあ、今日も輝く準備はいい？)")
