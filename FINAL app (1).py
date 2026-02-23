import streamlit as st
import time

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

    {
        "question": "हाल ही में 78वां जोमी राष्ट्रीय दिवस कहाँ मनाया गया?",
        "options": ["नागालैंड", "मिजोरम", "मणिपुर", "असम"],
        "answer": "मणिपुर"
    },

    {
        "question": "विश्व शांति और समझ दिवस कब मनाया जाता है?",
        "options": ["21 फरवरी", "23 फरवरी", "25 फरवरी", "1 मार्च"],
        "answer": "23 फरवरी"
    },

    {
        "question": "‘अटल बिहारी वाजपेयी: शाश्वत राजनेता’ पुस्तक किसने लिखी?",
        "options": ["नवीन कुंडू", "विजय गोयल", "उर्जित पटेल", "सिकंदर कुमार"],
        "answer": "विजय गोयल"
    },

    {
        "question": "वसई कैथडरल को संरक्षण के लिए UNESCO अवार्ड किस राज्य को मिला?",
        "options": ["गोवा", "कर्नाटक", "गुजरात", "महाराष्ट्र"],
        "answer": "महाराष्ट्र"
    },

    {
        "question": "WAMS एशिया कप राइजिंग स्टार्स खिताब किसने जीता?",
        "options": ["जापान", "ऑस्ट्रेलिया", "भारत", "दक्षिण कोरिया"],
        "answer": "भारत"
    },

    {
        "question": "बाल चिकित्सा जीन थेरेपी परियोजना का ऐतिहासिक शुभारंभ किस देश ने किया?",
        "options": ["सऊदी अरब", "यूएई", "कतर", "ओमान"],
        "answer": "यूएई"
    },

    {
        "question": "हाल ही में निधन हुए मणिशंकर मुखोपाध्याय किस क्षेत्र से जुड़े थे?",
        "options": ["खिलाड़ी", "वैज्ञानिक", "लेखक", "राजनेता"],
        "answer": "लेखक"
    },

    {
        "question": "भारत और किस देश के बीच बागवानी पर पहला संयुक्त कार्य समूह आयोजित हुआ?",
        "options": ["ऑस्ट्रेलिया", "कनाडा", "न्यूजीलैंड", "फ्रांस"],
        "answer": "न्यूजीलैंड"
    },

    {
        "question": "ऑल इंडिया मैनेजमेंट एसोसिएशन बिजनेस लीडर अवार्ड किसने जीता?",
        "options": ["गौतम अडानी", "करण अडानी", "आनंद महिंद्रा", "मुकेश अंबानी"],
        "answer": "करण अडानी"
    },

    {
        "question": "सोनपुर इंटरनेशनल एयरपोर्ट प्रोजेक्ट को किस राज्य ने मंजूरी दी?",
        "options": ["बिहार", "झारखंड", "उत्तर प्रदेश", "पश्चिम बंगाल"],
        "answer": "बिहार"
    },

    {
        "question": "इंडिया एआई इंपैक्ट समिट 2026 में सबसे कम उम्र के स्पीकर कौन बने?",
        "options": ["आरव शर्मा", "वेदांत मिश्रा", "रणबीर सचदेवा", "कृष चौधरी"],
        "answer": "रणबीर सचदेवा"
    },

    {
        "question": "पंजाब स्टेट पावर कॉरपोरेशन लिमिटेड का डायरेक्टर किसे नियुक्त किया गया?",
        "options": ["नीतू वर्मा", "हरशरण कौर", "अमृता सिंह", "जसप्रीत कौर"],
        "answer": "हरशरण कौर"
    },

    {
        "question": "भारत में वर्तमान कुल रामसर स्थल कितने हैं?",
        "options": ["90", "95", "96", "98"],
        "answer": "98"
    },

    {
        "question": "प्रोजेक्ट चीता की शुरुआत किस वर्ष हुई?",
        "options": ["2019", "2020", "2021", "2022"],
        "answer": "2022"
    },

    {
        "question": "प्रोजेक्ट टाइगर कब शुरू हुआ?",
        "options": ["1980", "1992", "1973", "2000"],
        "answer": "1973"
    },

    {
        "question": "अंतरराष्ट्रीय महिला दिवस कब मनाया जाता है?",
        "options": ["13 फरवरी", "21 मार्च", "8 मार्च", "5 जून"],
        "answer": "8 मार्च"
    },

    {
        "question": "विश्व मानसिक स्वास्थ्य दिवस कब मनाया जाता है?",
        "options": ["10 सितंबर", "10 अक्टूबर", "9 अक्टूबर", "21 जून"],
        "answer": "10 अक्टूबर"
    },

    {
        "question": "अंतरराष्ट्रीय मातृभाषा दिवस कब मनाया जाता है?",
        "options": ["20 फरवरी", "21 फरवरी", "22 फरवरी", "23 फरवरी"],
        "answer": "21 फरवरी"
    },

    {
        "question": "विश्व पर्यटन दिवस कब मनाया जाता है?",
        "options": ["21 सितंबर", "23 सितंबर", "27 सितंबर", "30 सितंबर"],
        "answer": "27 सितंबर"
    },

    {
        "question": "हाल ही में लोसार उत्सव किस राज्य में मनाया गया?",
        "options": ["उत्तराखंड", "सिक्किम", "अरुणाचल प्रदेश", "हिमाचल प्रदेश"],
        "answer": "हिमाचल प्रदेश"
    }

]

# ================== SESSION INIT ==================
if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(questions)

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "finished" not in st.session_state:
    st.session_state.finished = False

# ================== NAME INPUT ==================
name = st.text_input("Enter Your Name:")

if name and not st.session_state.finished:
    st.success(f"✨ Welcome {name}! Best of Luck 🎯")

    # ================== TIMER ==================
    remaining = 120 - int(time.time() - st.session_state.start_time)
    st.markdown(f"<h2>⏰ Time Left: {max(0, remaining)} sec</h2>", unsafe_allow_html=True)

    if remaining <= 0:
        st.error("⛔ Time's Up!")
        st.session_state.finished = True
        st.stop()

    # ================== QUIZ ==================
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


# ================== RESULT SECTION ==================
if st.session_state.finished and name:

    st.markdown("---")
    st.success(f"🎉 {name}, Your Final Score: {st.session_state.score} / {len(questions)}")

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
