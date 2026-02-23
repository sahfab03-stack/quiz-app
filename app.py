import streamlit as st

st.set_page_config(page_title="Luxury Quiz App", page_icon="🔥", layout="centered")

# ================== THEME ==================
st.markdown("""
<style>

.stApp {
    background-color: #F3EDE6;
    font-family: 'Georgia', serif;
}

h1 {
    color: #0F3D3E;
    text-align: center;
    font-weight: bold;
}

h2 {
    color: #7A1E1E;
}

.stRadio > div {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #D8CFC4;
}

.stButton>button {
    background-color: #0F3D3E;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #145A5A;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title("🔥 Current Affairs Luxury Quiz")

# ================== QUESTIONS ==================
questions = [
    ("G20 शिखर सम्मेलन 2023 किस देश में हुआ?",
     ["जापान", "भारत", "ब्राज़ील", "जर्मनी"], "भारत"),

    ("चंद्रयान-3 किस वर्ष लॉन्च हुआ?",
     ["2021", "2022", "2023", "2024"], "2023"),

    ("भारत के वर्तमान राष्ट्रपति कौन हैं?",
     ["रामनाथ कोविंद", "द्रौपदी मुर्मू", "नरेंद्र मोदी", "जगदीप धनखड़"], "द्रौपदी मुर्मू"),

    ("विश्व पर्यावरण दिवस कब मनाया जाता है?",
     ["5 जून", "15 जून", "21 मार्च", "22 अप्रैल"], "5 जून"),

    ("BRICS में मूल रूप से कितने देश थे?",
     ["3", "4", "5", "6"], "5"),
]

# ================== SESSION INIT ==================
if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(questions)

if "finished" not in st.session_state:
    st.session_state.finished = False

# ================== QUIZ ==================
if not st.session_state.finished:

    for i, (q, options, answer) in enumerate(questions):

        st.markdown(f"### Question {i+1}")

        choice = st.radio(q, options, key=f"q{i}", disabled=st.session_state.answered[i])

        if not st.session_state.answered[i]:
            if st.button(f"Submit {i+1}", key=f"btn{i}"):

                if choice == answer:
                    st.success("✅ Correct Answer!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong! Correct Answer: {answer}")

                st.session_state.answered[i] = True

    st.markdown("---")

    if st.button("🏁 Finish Quiz"):
        st.session_state.finished = True


# ================== RESULT ==================
if st.session_state.finished:

    st.markdown("---")
    st.success(f"🎉 Your Final Score: {st.session_state.score} / {len(questions)}")

    if st.session_state.score == len(questions):
        st.balloons()
        st.success("🔥 Excellent Performance!")
    elif st.session_state.score >= 3:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")

    # ================== YOUTUBE LINK ==================
    st.markdown("---")
    st.markdown("### 📺 Watch More Quizzes On YouTube")
    st.link_button("🔴 Visit My YouTube Channel",
                   "https://www.youtube.com/watch?v=tqYnGxO9gCU")
