# =========================================================
# A1 OMNI JOURNEYMAN EXAM PREP — FINAL LAUNCH BUILD
# =========================================================

import streamlit as st
import time
import requests

# =========================================================
# PAGE CONFIG (MUST BE FIRST STREAMLIT CALL)
# =========================================================
st.set_page_config(
    page_title="A1 Omni Journeyman Exam Prep",
    page_icon="⚡",
    layout="centered"
)

# =========================================================
# PREMIUM BLACK & GOLD DESIGN
# =========================================================
st.markdown("""
<style>
:root {
  --gold:#d4af37;
  --black:#0b0b0b;
}
html, body, [class*="css"] {
  background-color: var(--black);
  color: #f5f5f5;
}
h1, h2, h3 { color: var(--gold); }
.stButton>button {
  background: linear-gradient(90deg, #b8962e, #f2d675);
  color: #000;
  border-radius: 10px;
  font-weight: 700;
}
.stRadio label, .stCheckbox label { color:#f5f5f5; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# GUMROAD LICENSE VERIFICATION (LIVE)
# =========================================================
st.markdown("## 🔒 A1 Omni Journeyman Exam Prep Access")

license_key = st.text_input("Enter your license key", type="password")

# 🔴 CHANGE ONLY THESE TWO LINES 🔴
GUMROAD_PRODUCT_ID = "PASTE_YOUR_GUMROAD_PRODUCT_ID_HERE"
GUMROAD_LINK = "https://gumroad.com/PASTE_YOUR_PRODUCT_LINK_HERE"
# 🔴 DO NOT CHANGE ANYTHING ELSE 🔴

def verify_license(key):
    url = "https://api.gumroad.com/v2/licenses/verify"
    payload = {
        "product_id": GUMROAD_PRODUCT_ID,
        "license_key": key
    }
    r = requests.post(url, data=payload)
    if r.status_code != 200:
        return None
    data = r.json()
    return data if data.get("success") else None

license_data = verify_license(license_key) if license_key else None

if not license_data:
    st.warning("🔐 Access required")
    st.markdown(f"""
### 💳 Get Instant Access
- Trial (Free)
- Pro Exam Mode ($49)
- Lifetime Access ($129)

👉 **Purchase here:**  
{GUMROAD_LINK}
""")
    st.stop()

purchase = license_data["purchase"]

if purchase.get("refunded"):
    st.error("❌ License refunded")
    st.stop()

variant = purchase.get("variant", "").lower()
if "trial" in variant:
    ACCESS_TIER = "TRIAL"
elif "lifetime" in variant:
    ACCESS_TIER = "LIFETIME"
else:
    ACCESS_TIER = "PRO"

st.success(f"✅ Access Granted — {ACCESS_TIER}")

# =========================================================
# HEADER
# =========================================================
st.title("⚡ A1 Omni Journeyman Exam Prep")
st.subheader("Train like the exam. Pass with confidence.")
st.markdown("---")

# =========================================================
# EXAM FOCUS (BUYER CHOICE)
# =========================================================
exam_focus = st.radio(
    "Choose your exam focus:",
    ["Texas Journeyman (TDLR)", "National NEC"]
)

# =========================================================
# SESSION STATE
# =========================================================
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# =========================================================
# QUESTION BANK (EXPAND FREELY)
# =========================================================
texas_questions = [
    {
        "topic": "Texas Licensing",
        "question": "Which agency regulates electrician licensing in Texas?",
        "options": ["TWC", "TDLR", "OSHA", "ICC"],
        "answer": "TDLR",
        "explanation": "TDLR oversees electrician licensing and exams in Texas.",
        "reference": "Texas Occupations Code"
    }
]

national_questions = [
    {
        "topic": "NEC Basics",
        "question": "Which NEC article contains definitions?",
        "options": ["90", "100", "110", "250"],
        "answer": "100",
        "explanation": "Article 100 contains NEC definitions.",
        "reference": "NEC Article 100"
    }
]

questions = texas_questions if "Texas" in exam_focus else national_questions

# =========================================================
# EXAM MODE TIMER (PAID ONLY)
# =========================================================
if ACCESS_TIER != "TRIAL":
    QUESTION_TIME_LIMIT = 60
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, QUESTION_TIME_LIMIT - elapsed)
    st.markdown(f"### ⏱️ Time Remaining: **{remaining}s**")
    if remaining == 0:
        st.error("⏰ Time expired!")
        st.session_state.answered = True

# =========================================================
# END OF EXAM
# =========================================================
if st.session_state.q_index >= len(questions):
    st.success("🎉 Exam Complete")
    st.write(f"Final Score: {st.session_state.score} / {len(questions)}")

    st.markdown("---")
    st.markdown("## 🏆 Pass Guarantee")
    st.markdown("""
If you complete this prep and **do not pass your Journeyman exam**:
- Continued free access
- Bonus practice questions
- Retest strategy support

📧 support@a1omnicreations.com
""")
    st.stop()

# =========================================================
# DISPLAY QUESTION
# =========================================================
q = questions[st.session_state.q_index]

st.markdown(f"### 📘 Topic: {q['topic']}")
st.markdown(f"**Question:** {q['question']}")

choice = st.radio("Choose an answer:", q["options"], key=st.session_state.q_index)

if st.button("Submit Answer") and not st.session_state.answered:
    st.session_state.answered = True
    if choice == q["answer"]:
        st.success("✅ Correct")
        st.session_state.score += 1
    else:
        st.error("❌ Incorrect")
    st.info(q["explanation"])
    st.caption(f"📖 {q['reference']}")

if st.session_state.answered:
    if st.button("Next Question"):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.session_state.start_time = time.time()
        st.experimental_rerun()

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.write(f"Score: {st.session_state.score}")
st.write(f"Question {st.session_state.q_index + 1} of {len(questions)}")
