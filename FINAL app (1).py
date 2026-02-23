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
quiz_questions = [

    ("अंतरराष्ट्रीय मातृभाषा दिवस कब मनाया जाता है?",
     ["20 फरवरी", "21 फरवरी", "22 फरवरी", "23 फरवरी"],
     "21 फरवरी"),

    ("विश्व कैंसर दिवस कब मनाया जाता है?",
     ["2 फरवरी", "4 फरवरी", "5 फरवरी", "6 फरवरी"],
     "4 फरवरी"),

    ("विश्व दलहन दिवस कब मनाया जाता है?",
     ["8 फरवरी", "9 फरवरी", "10 फरवरी", "11 फरवरी"],
     "10 फरवरी"),

    ("प्रोजेक्ट टाइगर किस वर्ष शुरू हुआ था?",
     ["1972", "1973", "1992", "2022"],
     "1973"),

    ("प्रोजेक्ट एलीफेंट किस वर्ष शुरू हुआ था?",
     ["1990", "1992", "1995", "2000"],
     "1992"),

    ("प्रोजेक्ट चीता किस वर्ष शुरू हुआ था?",
     ["2020", "2021", "2022", "2023"],
     "2022"),

    ("विश्व पर्यटन दिवस कब मनाया जाता है?",
     ["25 सितंबर", "26 सितंबर", "27 सितंबर", "28 सितंबर"],
     "27 सितंबर"),

    ("विश्व आत्महत्या रोकथाम दिवस कब मनाया जाता है?",
     ["9 सितंबर", "10 सितंबर", "10 अक्टूबर", "11 जुलाई"],
     "10 सितंबर"),

    ("विश्व जनसंख्या दिवस कब मनाया जाता है?",
     ["10 जुलाई", "11 जुलाई", "12 जुलाई", "13 जुलाई"],
     "11 जुलाई"),

    ("विश्व रेडियो दिवस कब मनाया जाता है?",
     ["12 फरवरी", "13 फरवरी", "14 फरवरी", "15 फरवरी"],
     "13 फरवरी"),

    ("विश्व सामाजिक न्याय दिवस कब मनाया जाता है?",
     ["18 फरवरी", "19 फरवरी", "20 फरवरी", "21 फरवरी"],
     "20 फरवरी"),

    ("लोसार उत्सव किस राज्य में मनाया जाता है?",
     ["सिक्किम", "असम", "झारखंड", "बिहार"],
     "सिक्किम")

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
    elif st.session_state.score >= 10:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")

    st.markdown("---")
    st.markdown("### 📺 Watch More Quizzes On YouTube")
    st.link_button("🔴 Visit My YouTube Channel",
                   "https://www.youtube.com/watch?v=tqYnGxO9gCU")
