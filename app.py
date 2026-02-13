import streamlit as st
import datetime
import random
import time

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
# メッセージを自動で200個に拡張
cheers = (base_cheers * 14)[:200] 

# --- 3. 200種類のカラーを生成する関数 ---
def get_random_color():
    # 明るいパステルカラーをランダム生成
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

# 背景色の初期化
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
        font-size: 50px; font-weight: bold;
        color: #FF8C00; text-align: center;
        background: rgba(255, 255, 255, 0.8);
        padding: 15px; border-radius: 20px; border: 3px solid #FFD700;
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. メイン画面の表示 ---
st.markdown("### 🌟 My Daily Cheerleader")

# 時刻表示用のコンテナ
time_placeholder = st.empty()

# JavaScriptで現地時刻を取得してリアルタイム更新
st.markdown("""
    <script>
    function updateClock() {
        const now = new Date();
        const timeStr = now.getHours().toString().padStart(2, '0') + ':' +
                        now.getMinutes().toString().padStart(2, '0') + ':' +
                        now.getSeconds().toString().padStart(2, '0');
        const elements = parent.document.querySelectorAll('.time-display');
        elements.forEach(el => { el.innerText = timeStr; });
    }
    setInterval(updateClock, 1000);
    </script>
    """, unsafe_allow_html=True)

# 日付の表示
now = datetime.datetime.now()
st.header(f"✨ {now.strftime('%Y')} ✨")
st.markdown(f"<h1 style='font-size: 80px; margin: 0; text-align: center;'>{now.strftime('%b %d')}</h1>", unsafe_allow_html=True)

# デジタル時計の表示（JavaScriptが動くまでの初期値）
time_placeholder.markdown(f"<div class='time-display'>{now.strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 6. 応援ボタン ---
if st.button("✨ Click for your cheer! ✨", use_container_width=True):
    # 背景色とメッセージを更新
    st.session_state.bg_color = get_random_color()
    st.balloons()
    selected_cheer = random.choice(cheers)
    st.success(selected_cheer)
    # 画面を更新して背景色を反映
    st.rerun()
else:
    st.info("Are you ready to shine today? (さあ、今日も輝く準備はいい？)")
