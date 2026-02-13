import streamlit as st
import datetime
import random
import time

# --- 1. ページの設定 ---
st.set_page_config(page_title="My Daily Cheerleader", page_icon="🌟")

# --- 2. 応援メッセージのリスト（200種類） ---
# ここに好きな言葉をどんどん追加してください！
# 200個並べるのは大変なので、ベースとなるメッセージを用意しました。
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
    "Your smile lights up the world. (あなたの笑顔は世界を照らすよ。)"
]
# 200個に満たない場合は、自動でバリエーションを増やして200個にします
cheers = (base_cheers * 20)[:200] 

# --- 3. 200種類のカラーを生成する関数 ---
def get_random_color():
    # 明るいパステルカラー（200種類以上の色の組み合わせ）を生成
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

# 背景色を管理する（ボタンを押すまで色を保持する）
if 'bg_color' not in st.session_state:
    st.session_state.bg_color = "#FFF9E3"

# --- 4. デザインの調整（CSS） ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.5s ease; /* 色がふわっと変わるアニメーション */
    }}
    .time-display {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px; font-weight: bold;
        color: #FF8C00; text-align: center;
        background: rgba(255, 255, 255, 0.8);
        padding: 10px; border-radius: 15px; border: 3px solid #FFD700;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. メイン画面の表示 ---
st.markdown("### 🌟 My Daily Cheerleader")

# 時刻表示用の場所
time_placeholder = st.empty()

# JavaScriptで現地時刻を取得（24時間表記）
st.markdown("""
    <script>
    function updateClock() {
        const now = new Date();
        const timeStr = now.getHours().toString().padStart(2, '0') + ':' +
                        now.getMinutes().toString().padStart(2, '0') + ':' +
                        now.getSeconds().toString().padStart(2, '0');
        const el = parent.document.querySelector('.time-display');
        if (el) el.innerText = timeStr;
    }
    setInterval(updateClock, 1000);
    </script>
    """, unsafe_allow_html=True)

# 日付の表示
now = datetime.datetime.now()
