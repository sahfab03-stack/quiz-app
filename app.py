import streamlit as st
import time

st.set_page_config(page_title="Quiz App", page_icon="🔥", layout="centered")

st.markdown("<h1 style='text-align: center; color: orange;'>🔥 Current Affairs Quiz 2026 🔥</h1>", unsafe_allow_html=True)

# Name input
name = st.text_input("Enter Your Name:")

questions = [
    ("G20 शिखर सम्मेलन 2023 किस देश में हुआ?",
     ["जापान", "भारत", "ब्राज़ील", "जर्मनी"], "भारत"),

    ("चंद्रयान-3 किस वर्ष लॉन्च हुआ?",
     ["2021", "2022", "2023", "2024"], "2023"),

    ("विश्व पर्यावरण दिवस कब मनाया जाता है?",
     ["5 जून", "15 जून", "21 मार्च", "22 अप्रैल"], "5 जून"),
]

if "score" not in st.session_state:
    st.session_state.score = 0

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

score = 0

for i, (q, options, answer) in enumerate(questions):

    st.markdown(f"### Question {i+1}")
    choice = st.radio(q, options, key=i)

    if st.button(f"Submit Answer {i+1}"):

        # Timer simulation
        with st.spinner("⏳ Checking answer..."):
            time.sleep(2)

        if choice == answer:
            st.success("✅ Correct Answer!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct Answer is: {answer}")

st.markdown("---")

if st.button("🏁 Finish Quiz"):

    final_score = st.session_state.score

    st.markdown(f"## 🎉 {name}, Your Final Score: {final_score} / {len(questions)}")

    # Performance message
    if final_score == len(questions):
        st.balloons()
        st.success("🔥 Excellent Performance!")
    elif final_score >= 2:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")

    # Leaderboard update
    if name:
        st.session_state.leaderboard.append((name, final_score))

    st.markdown("## 🏆 Leaderboard")
    sorted_board = sorted(st.session_state.leaderboard, key=lambda x: x[1], reverse=True)

    for player, pts in sorted_board:
        st.write(f"{player} - {pts}")
