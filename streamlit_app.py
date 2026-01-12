import streamlit as st
import time

# -------------------------------------------------
# Page Configuration (MUST be first Streamlit command)
# -------------------------------------------------
st.set_page_config(
    page_title="A1 Omni Journeyman Prep",
    page_icon="⚡",
    layout="centered"
)

# -------------------------------------------------
# Session State Initialization (ONE TIME ONLY)
# -------------------------------------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "time_up" not in st.session_state:
    st.session_state.time_up = False

# -------------------------------------------------
# App Header
# -------------------------------------------------
st.title("⚡ A1 Omni Journeyman License Practice")
st.subheader("Electrical Exam Prep")

# -------------------------------------------------
# Question Bank (sample – you can expand this)
# -------------------------------------------------
questions = [
    {
        "question": "A continuous load must be calculated at what percentage?",
        "options": [
            "100%",
            "110%",
            "125%",
            "150%"
        ],
        "answer": "125%"
    },
    {
        "question": "What NEC article covers grounding and bonding?",
        "options": [
            "Article 100",
            "Article 110",
            "Article 250",
            "Article 300"
        ],
        "answer": "Article 250"
    }
]

# -------------------------------------------------
# End of Exam Check
# -------------------------------------------------
if st.session_state.q_index >= len(questions):
    st.success("✅ Exam Complete!")
    st.write(f"Final Score: {st.session_state.score} / {len(questions)}")
    st.stop()

# -------------------------------------------------
# Timer Configuration
# -------------------------------------------------
QUESTION_TIME_LIMIT = 30  # seconds

elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, QUESTION_TIME_LIMIT - elapsed)

st.markdown(f"### ⏳ Time Remaining: **{remaining}s**")

# -------------------------------------------------
# Time-Up Detection (NO rerun here)
# -------------------------------------------------
if remaining == 0 and not st.session_state.time_up:
    st.session_state.time_up = True

# -------------------------------------------------
# Display Current Question
# -------------------------------------------------
current_q = questions[st.session_state.q_index]

st.markdown(f"### Question {st.session_state.q_index + 1}")
st.write(current_q["question"])

choice = st.radio(
    "Select your answer:",
    current_q["options"],
    key=f"q_{st.session_state.q_index}"
)

# -------------------------------------------------
# Submit Answer Button
# -------------------------------------------------
if st.button("Submit Answer") and not st.session_state.answered:
    st.session_state.answered = True

    if choice == current_q["answer"]:
        st.session_state.score += 1
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. Correct answer: {current_q['answer']}")

# -------------------------------------------------
# Auto-Advance Logic (Answer OR Time-Up)
# -------------------------------------------------
if st.session_state.answered or st.session_state.time_up:
    time.sleep(1)

    st.session_state.q_index += 1
    st.session_state.start_time = time.time()
    st.session_state.answered = False
    st.session_state.time_up = False

    st.rerun()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.write(f"Score: {st.session_state.score}")
