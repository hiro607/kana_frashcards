import streamlit as st
import random

# 平仮名とその読みの辞書
hiragana_dict = {
    'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo', 'シャ': 'sha', 'シュ': 'shu',
    'ショ': 'sho', 'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho', 'ニャ': 'nya',
    'ニュ': 'nyu', 'ニョ': 'nyo', 'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
    'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo', 'リャ': 'rya', 'リュ': 'ryu',
    'リョ': 'ryo', 'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo', 'ジャ': 'ja',
    'ジュ': 'ju', 'ジョ': 'jo', 'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
    'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}

# ランダムに平仮名を選ぶ関数
def get_random_hiragana():
    hiragana, romanji = random.choice(list(hiragana_dict.items()))
    return hiragana, romanji

# セッション情報の初期化
if 'remaining_quiz' not in st.session_state:
    st.session_state.remaining_quiz = 10
    st.session_state.score = 0
    st.session_state.hiragana, st.session_state.romanji = get_random_hiragana()
    st.session_state.show_answer = False
    st.session_state.incorrect_answers = []

remaining_quiz = st.session_state.remaining_quiz
score = st.session_state.score

# Streamlitのアプリ
st.title('Katakana Flash cards Quiz 3')

# クイズが終了したかどうかを確認
if remaining_quiz == 0:
    st.markdown(f'### Votre score est {score} points sur 10')
    st.markdown('### Les kanas incorrects et leur prononciation :')
    for hiragana, romanji in st.session_state.incorrect_answers:
        st.markdown(f'- {hiragana}: {romanji}')

    if st.button('Commencez un nouveau quiz'):
        st.session_state.remaining_quiz = 10
        st.session_state.score = 0
        st.session_state.hiragana, st.session_state.romanji = get_random_hiragana()
        st.session_state.show_answer = False
        st.session_state.incorrect_answers = []
        st.experimental_rerun()  # アプリを再実行して新しいクイズを開始

else:
    st.markdown(f'### Nombre de questions restantes : {remaining_quiz}')

    hiragana = st.session_state.hiragana
    romanji = st.session_state.romanji

    st.write(f"""
        <div style="text-align: center; font-size: 250px; font-family: 'Noto Sans JP';">
            {hiragana}
        </div>
    """, unsafe_allow_html=True)

    if st.button('Voir la réponse'):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.markdown(f'### Le hiragana {hiragana} se lit "{romanji}"')

    if st.button('Correct'):
        st.session_state.remaining_quiz -= 1
        st.session_state.score += 1
        st.session_state.hiragana, st.session_state.romanji = get_random_hiragana()
        st.session_state.show_answer = False
        st.experimental_rerun()

    if st.button('Incorrect'):
        st.session_state.incorrect_answers.append((hiragana, romanji))  # 間違った答えを記録
        st.session_state.remaining_quiz -= 1
        st.session_state.hiragana, st.session_state.romanji = get_random_hiragana()
        st.session_state.show_answer = False
        st.experimental_rerun()

    st.markdown(f'### Score actuel: {score}points')
