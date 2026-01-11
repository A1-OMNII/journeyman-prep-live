import streamlit as st
# -----------------------
# Session State Setup
# -----------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False
st.set_page_config(page_title="Journeyman Prep App", layout="centered")

st.title("Journeyman License Practice App")
st.subheader("Electrical Exam Prep")

# Question bank (NEC-style, original wording)
questions = [
    {
        "topic": "Electrical Theory / Branch Circuits",
        "question": "A continuous load is supplied by a branch circuit. What is the minimum required ampacity of the branch-circuit conductors?",
        "options": [
            "100% of the continuous load",
            "110% of the continuous load",
            "125% of the continuous load",
            "150% of the continuous load"
        ],
        "answer": "125% of the continuous load",
        "explanation": "Branch-circuit conductors supplying a continuous load must be sized at not less than 125% of the continuous load.",
        "reference": "NEC Article 210"
    },
    {
        "topic": "Calculations",
        "question": "What is the minimum ampacity required for a conductor supplying a 16-amp continuous load?",
        "options": [
            "16 amps",
            "18 amps",
            "20 amps",
            "22 amps"
        ],
        "answer": "20 amps",
        "explanation": "Continuous loads must be multiplied by 125%. 16A × 1.25 = 20A.",
        "reference": "NEC 210 / Load Calculations"
    },
    {
        "topic": "Grounding & Bonding",
        "question": "What is the primary purpose of equipment grounding conductors?",
        "options": [
            "Carry normal load current",
            "Reduce voltage drop",
            "Provide a low-impedance fault path",
            "Bond grounded conductors"
        ],
        "answer": "Provide a low-impedance fault path",
        "explanation": "Equipment grounding conductors provide a low-impedance path for fault current to facilitate overcurrent device operation.",
        "reference": "NEC Article 250"
    }
]

# Session state
if "index" not in st.session_state:
    st.session_state.index = 0

q = questions[st.session_state.index]

st.markdown(f"### Topic: {q['topic']}")
st.markdown(f"**Question:** {q['question']}")

choice = st.radio("Choose an answer:", q["options"])

if st.button("Submit Answer"):
    if choice == q["answer"]:
        st.success("✅ Correct")
    else:
        st.error("❌ Incorrect")

    st.info(f"**Explanation:** {q['explanation']}")
    st.caption(f"📘 Reference: {q['reference']}")

if st.button("Next Question"):
    st.session_state.index = (st.session_state.index + 1) % len(questions)
    st.rerun()
st.markdown("---")
st.subheader("📊 Score & Progress")

st.write(f"Score: {st.session_state.score}")
st.write(f"Question {st.session_state.q_index + 1} of {len(questions)}")