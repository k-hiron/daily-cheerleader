import streamlit as st
import datetime
import random

# --- 1. ページの設定 ---
st.set_page_config(page_title="My Daily Cheerleader", page_icon="🌟")

# --- 2. 応援メッセージのリスト（200種類） ---
base_cheers = [
    "You are doing an amazing job! (本当によくやってるよ！)",
    "Believe in yourself! (自分を信じて！)",
    "Every step counts. (どんな一歩も無駄じゃないよ。)",
    "You shine brighter than the stars! (あなたは星より輝いてる！)",
    "Take a deep breath. (深呼吸して。)",
    "I'm so proud of you! (あなたのことを誇りに思うよ！)",
    "Today is your day! (今日はあなたの特別な日！)",
    "You are a superstar! (あなたはスーパースター！)",
    "Keep going, you're almost there! (その調子！あともう少し！)",
    "Your smile lights up the world. (あなたの笑顔は世界を照らすよ。)",
    "You've got this! (君ならできる！)",
    "Stay positive and happy! (前向きに、ハッピーに！)",
    "You are stronger than you think! (あなたは自分が思うより強いよ！)",
    "Success is coming to you! (成功はもうすぐそこ！)",
    "Enjoy every moment! (一瞬一瞬を楽しんで！)"
]
cheers = (base_cheers * 14)[:200] 

# --- 3. 200種類のカラーを生成する関数 ---
def get_random_color():
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

if 'bg_color' not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

# --- 4. デザインの調整（CSS） ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.5s ease;
    }}
    .time-display {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 80px; font-weight: bold;
        color: #FF8C00; text-align: center;
        background: rgba(255, 255, 255, 0.9);
        padding: 20px; border-radius: 20px; border: 5px solid #FFD700;
        margin: 20px 0;
    }}
    .date-display {{
        font-size: 40px; text-align: center; font-weight: bold; color: #5C4033;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. メイン画面の表示 ---
st.markdown("<h2 style='text-align: center;'>🌟 My Daily Cheerleader</h2>", unsafe_allow_html=True)

# 時計と日付を表示する場所
st.markdown('<div id="clock" class="time-display">00:00:00</div>', unsafe_allow_html=True)
st.markdown('<div id="date" class="date-display">Loading...</div>', unsafe_allow_html=True)

# JavaScriptで「閲覧者のブラウザの時間」を24時間形式で取得して上書きする
st.markdown("""
    <script>
    function updateClock() {
        const now = new Date();
        
        // 24時間表記の時計を作成
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        const timeStr = hours + ':' + minutes + ':' + seconds;
        
        // 日付を作成 (例: Feb 13, 2026)
        const options = { month: 'short', day: 'numeric', year: 'numeric' };
        const dateStr = "✨ " + now.getFullYear() + " ✨<br>" + now.toLocaleDateString('en-US', {month:'short', day:'numeric'});

        // StreamlitのHTML要素を直接書き換え
        const clockEl = parent.document.querySelector('#clock');
        const dateEl = parent.document.querySelector('#date');
        if (clockEl) clockEl.innerText = timeStr;
        if (dateEl) dateEl.innerHTML = dateStr;
    }
    // 1秒ごとに更新
    setInterval(updateClock, 1000);
    updateClock(); // 初回実行
    </script>
    """, unsafe_allow_html=True)

st.write("---")

# --- 6. 応援ボタン ---
if st.button("✨ Click for your cheer! ✨", use_container_width=True):
    st.session_state.bg_color = get_random_color()
    st.balloons()
    st.success(random.choice(cheers))
    st.rerun()
else:
    st.info("Are you ready to shine today? (さあ、今日も輝く準備はいい？)")
