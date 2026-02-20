import streamlit as st
import time
import uuid

st.set_page_config(page_title="Ultimate Quiz App", page_icon="🔥")

st.markdown("<h1 style='text-align:center; color:orange;'>🔥 Current Affairs Quiz 2026 🔥</h1>", unsafe_allow_html=True)

# Unique ID
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())[:8]

st.write(f"🆔 Your Unique ID: {st.session_state.user_id}")

name = st.text_input("Enter Your Name:")

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

    ("भारतीय संविधान कब लागू हुआ?",
     ["15 अगस्त 1947", "26 जनवरी 1950", "2 अक्टूबर 1948", "26 नवंबर 1949"], "26 जनवरी 1950"),

    ("RBI का मुख्यालय कहाँ है?",
     ["दिल्ली", "मुंबई", "चेन्नई", "कोलकाता"], "मुंबई"),

    ("एशियाई खेल 2022 कहाँ आयोजित हुए?",
     ["टोक्यो", "बीजिंग", "हांगझोउ", "सियोल"], "हांगझोउ"),

    ("भारत का राष्ट्रीय पशु कौन सा है?",
     ["शेर", "बाघ", "हाथी", "गैंडा"], "बाघ"),

    ("डिजिटल इंडिया अभियान कब शुरू हुआ?",
     ["2013", "2014", "2015", "2016"], "2015"),
]

# Initialize states
if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(questions)

# Timer (120 seconds for 10 questions)
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

remaining = 120 - int(time.time() - st.session_state.start_time)

st.markdown(f"## ⏰ Time Left: {max(0, remaining)} sec")

if remaining <= 0:
    st.error("⛔ Time's Up!")
    st.stop()

# Quiz Questions
for i, (q, options, answer) in enumerate(questions):

    st.markdown(f"### Question {i+1}")

    choice = st.radio(q, options, key=i, disabled=st.session_state.answered[i])

    if not st.session_state.answered[i]:
        if st.button(f"Submit {i+1}"):

            if choice == answer:
                st.success("✅ Correct Answer!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct Answer: {answer}")

            st.session_state.answered[i] = True

st.markdown("---")

# Finish Button
if st.button("🏁 Finish Quiz"):

    st.success(f"🎉 {name} ({st.session_state.user_id}) | Final Score: {st.session_state.score} / {len(questions)}")

    if st.session_state.score == len(questions):
        st.balloons()
        st.success("🔥 Excellent Performance!")
    elif st.session_state.score >= 6:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")

# Restart Button
if st.button("🔄 Restart Quiz"):
    st.session_state.score = 0
    st.session_state.answered = [False] * len(questions)
    st.session_state.start_time = time.time()
