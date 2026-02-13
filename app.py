import streamlit as st
import datetime
import random

# --- 1. ページの設定 ---
st.set_page_config(page_title="My Daily Cheerleader", layout="centered")

# --- 2. 背景色をランダムに生成する関数（100色以上のパステルカラー） ---
def get_random_color():
    # 明るく優しい色合いになるようにRGBを調整
    r = random.randint(225, 255)
    g = random.randint(225, 255)
    b = random.randint(225, 255)
    return f"rgb({r}, {g}, {b})"

# セッション状態（背景色の保持）
if 'bg_color' not in st.session_state:
    st.session_state.bg_color = "#FFFDE7" # 初期色は優しいイエロー

# --- 3. カスタムデザイン設定（CSS） ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 1.5s ease; /* 色がふわっと変わるアニメーション */
    }}
    h1, h2, h3, p {{
        color: #FFB300 !important; /* 濃いイエロー・ゴールド */
        text-align: center;
        font-family: 'Arial', sans-serif;
    }}
    /* 黄色の星ボタンのデザイン */
    div.stButton > button:first-child {{
        background-color: #FFD700;
        color: #4A4A4A;
        border-radius: 50px;
        font-size: 26px;
        font-weight: bold;
        padding: 15px;
        width: 100%;
        border: 2px solid #FFB300;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        cursor: pointer;
    }}
    div.stButton > button:hover {{
        background-color: #FFEA00;
        border-color: #FFD700;
    }}
    /* メッセージエリアのスタイル */
    .stSuccess {{
        background-color: rgba(255, 255, 255, 0.5) !important;
        border: 1px solid #FFD700 !important;
        color: #4A4A4A !important;
        font-size: 20px !important;
        text-align: center !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. タイトルと日付の表示 ---
st.title("🌟 My Daily Cheerleader")
now = datetime.datetime.now()
st.header(f"✨ {now.strftime('%Y')} ✨")
st.markdown(f"<h1 style='font-size: 100px; margin: 0;'>{now.strftime('%b %d')}</h1>", unsafe_allow_html=True)

# --- 5. 自分を褒めるハイブリッド・メッセージリスト ---
cheer_messages = [
    "You are absolutely brilliant today! (今日のあなたは最高に輝いてるよ！)",
    "I'm so proud of everything you do! (あなたの頑張り、私が一番知ってるよ！)",
    "Your smile makes the world brighter! (あなたの笑顔は世界を明るくする魔法だよ！)",
    "You are a superstar in the making! (あなたは未来のスーパースターだよ！)",
    "Trust yourself, you are incredible! (自分を信じて、あなたは本当にすごいんだから！)",
    "Today is another day to shine like a diamond! (今日もダイヤモンドみたいに輝こう！)",
    "Keep going, you are unstoppable! (その調子！今のあなたを止められる人はいないよ！)",
    "You are enough just as you are! (あなたは、そのままで十分素晴らしいんだよ。)",
    "You make a difference just by being you! (あなたがそこにいるだけで、みんなハッピーだよ！)",
    "You are doing an amazing job! (本当によくやってるよ！天才！)",
    "Believe in the magic within you! (自分の中にある可能性を信じて！)",
    "You deserve all the happiness! (あなたは幸せになる権利しかないよ！)",
    "Every small step counts! (一歩ずつ進むあなたは最高にかっこいい！)",
    "You are brave and strong! (あなたは強くて、とっても勇敢だよ！)",
    "You've got a heart of gold! (あなたは本当に優しい心を持っているね！)",
    "Your hard work will pay off! (あなたの努力は必ず最高の結果になるよ！)",
    "Everything is going to be amazing! (すべては最高の方向に進んでいるよ！)",
    "You are a ray of sunshine! (あなたはみんなを照らす太陽みたいだね！)"
]

st.write("---")

# --- 6. ボタンのアクション ---
if st.button('⭐ Click for your cheer! ✨'):
    st.session_state.bg_color = get_random_color()
    st.session_state.current_msg = random.choice(cheer_messages)
    st.balloons() # 風船を飛ばす演出
    st.rerun()

# 初回訪問時のメッセージ
if 'current_msg' not in st.session_state:
    st.session_state.current_msg = "Are you ready to shine today? (さあ、今日も輝く準備はいい？)"

# メッセージを画面に表示
st.success(st.session_state.current_msg)