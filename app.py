import os
import time
import requests
import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Journeyman Electrician Exam Prep",
    page_icon="⚡",
    layout="centered",
)

GUMROAD_PRODUCT_ID = "exsnqw"
GUMROAD_LINK = "https://a1omnicreation.gumroad.com/l/exsnqw"
# Optional: set LICENSE_SERVER_URL as an environment variable or in Streamlit secrets
LICENSE_SERVER_URL = os.environ.get("LICENSE_SERVER_URL") or (st.secrets.get("LICENSE_SERVER_URL") if "LICENSE_SERVER_URL" in st.secrets else None)

# =========================
# SIMPLE QUESTION BANK (expand as needed)
# =========================
questions = [
    {
        "question": "Which agency regulates electrician licensing in Texas?",
        "options": ["TWC", "TDLR", "OSHA", "ICC"],
        "answer": "TDLR",
        "explanation": "TDLR oversees electrician licensing and exams in Texas.",
        "reference": "Texas Occupations Code",
    },
    {
        "question": "What is the minimum conductor size for a 30A branch circuit?",
        "options": ["#14 AWG", "#12 AWG", "#10 AWG", "#8 AWG"],
        "answer": "#10 AWG",
        "explanation": "A 30A branch circuit typically requires #10 AWG copper conductors.",
        "reference": "NEC conductor ampacity tables",
    },
    {
        "question": "Which color is typically used for equipment grounding conductors?",
        "options": ["Black", "Red", "Green or Green with Yellow Stripe", "White"],
        "answer": "Green or Green with Yellow Stripe",
        "explanation": "Green (or green with yellow stripe) denotes grounding conductors.",
        "reference": "NEC grounding conductor identification",
    },
]

# =========================
# SESSION STATE
# =========================
if "licensed" not in st.session_state:
    st.session_state.licensed = False

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "question_start_time" not in st.session_state:
    st.session_state.question_start_time = time.time()

# =========================
# HEADER
# =========================
st.title("⚡ Journeyman Electrician Exam Prep")
st.markdown("NEC-Based • Timed Exams • Real Test Logic")
st.markdown("---")

# =========================
# LICENSE INPUT (server-side verification optional)
# =========================
st.subheader("🔐 Exam Access")
license_key = st.text_input(
    "Enter your license key",
    type="password",
    placeholder="XXXX-XXXX-XXXX",
)

if st.button("Unlock Access"):
    if license_key.strip() == "":
        st.error("Please enter a license key.")
    else:
        # If a license server is configured, verify server-side
        if LICENSE_SERVER_URL:
            try:
                resp = requests.post(
                    f"{LICENSE_SERVER_URL.rstrip('/')}/verify",
                    json={"license_key": license_key, "product_id": GUMROAD_PRODUCT_ID},
                    timeout=10,
                )
                data = resp.json()
                if resp.status_code == 200 and data.get("valid"):
                    st.session_state.licensed = True
                    st.success("Access unlocked successfully.")
                else:
                    st.error(data.get("message", "License verification failed."))
            except Exception as e:
                st.error(f"License server error: {e}")
        else:
            # Placeholder: accept any non-empty key locally (replace with real verification for production)
            st.session_state.licensed = True
            st.success("Access unlocked locally (no license server configured).")

st.markdown("---")

# =========================
# TRIAL / PURCHASE PROMPT
# =========================
TRIAL_QUESTIONS = 1  # number of free/trial questions allowed
QUESTION_TIME_LIMIT = 60  # seconds per question for licensed users

if not st.session_state.licensed:
    st.warning("🔒 Access Required — Free trial available for a limited number of questions.")
    st.info(f"Try {TRIAL_QUESTIONS} sample question(s) for free. Purchase full access: [Buy on Gumroad]({GUMROAD_LINK})")

# Ensure we don't index past the question list
if st.session_state.q_index >= len(questions):
    st.success("🎉 Exam Complete")
    st.write(f"Final Score: {st.session_state.score} / {len(questions)}")
    st.markdown("---")
    st.markdown("## 🏆 Pass Guarantee")
    st.markdown("""
    • **Free Trial** – Limited sample questions  
    • **Pro Exam Mode** – **$49**  
    • **Lifetime Access** – **$129** (Best Value)
    """)
    st.markdown(f"👉 **[Purchase access here]({GUMROAD_LINK})**")
    st.info(
        "After purchase, you will receive your license key by email. "
        "Enter it above to unlock full access."
    )
    st.stop()

# =========================
# MAIN APP (QUESTION DISPLAY)
# =========================
st.success("✅ Full Access Enabled" if st.session_state.licensed else "🔎 Trial Mode")
st.markdown("### 🧠 Exam Dashboard")
st.markdown("This system is designed to simulate real Journeyman Electrician exam conditions.")
st.markdown("---")

# Make sure current index is valid
q = questions[st.session_state.q_index]
st.markdown(f"### Question {st.session_state.q_index + 1}")
st.write(q["question"])

choice = st.radio("Select an answer:", q["options"], key=f"choice_{st.session_state.q_index}")

# Timer for licensed users
if st.session_state.licensed:
    elapsed = int(time.time() - st.session_state.question_start_time)
    remaining = max(0, QUESTION_TIME_LIMIT - elapsed)
    st.markdown(f"### ⏱️ Time Remaining: **{remaining}s**")
    # auto-expire
    if remaining <= 0 and not st.session_state.answered:
        st.session_state.answered = True
        st.warning("⏰ Time expired for this question.")

# Trial limitation
if not st.session_state.licensed and st.session_state.q_index >= TRIAL_QUESTIONS:
    st.info("Trial complete. Purchase full access to continue.")
    st.markdown(f"[Purchase access here]({GUMROAD_LINK})")
    st.stop()

# =========================
# SUBMIT / FEEDBACK / NAVIGATION
# =========================
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Submit Answer") and not st.session_state.answered:
        st.session_state.answered = True
        selected = choice
        if selected == q["answer"]:
            st.session_state.score += 1
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
        st.markdown(f"**Explanation:** {q.get('explanation', 'No explanation provided.')}")
        if q.get("reference"):
            st.markdown(f"**Reference:** {q['reference']}")

with col2:
    if st.button("Next Question") and st.session_state.answered:
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.session_state.question_start_time = time.time()
        st.experimental_rerun()

# =========================
# DISPLAY progress and partial score
# =========================
st.markdown("---")
st.write(f"Progress: {min(st.session_state.q_index + (0 if st.session_state.answered else 1), len(questions))} / {len(questions)}")
st.write(f"Score: {st.session_state.score}")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color: gray; font-size: 0.9em;'>"
    "Designed & Developed by Saul Hernandez<br>"
    "A1 Omni Creations<br><br>"
    "This application is a study and practice tool and does not guarantee licensure."
    "</div>",
    unsafe_allow_html=True,
)
