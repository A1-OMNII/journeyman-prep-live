import streamlit as st
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Journeyman Electrician Exam Prep",
    page_icon="⚡",
    layout="centered"
GUMROAD_PRODUCT_ID = "exsnqw"
GUMROAD_LINK = "https://a1omnicreation.gumroad.com/l/exsnqw"

# =========================
# SESSION STATE
# =========================
if "licensed" not in st.session_state:
    st.session_state.licensed = False

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# =========================
# HEADER
# =========================
st.title("⚡ Journeyman Electrician Exam Prep")
st.markdown(
    "NEC-Based • Timed Exams • Real Test Logic",
)

st.markdown("---")

<<<<<<< HEAD
# =========================================================
# QUESTION BANK (EXPAND FREELY)
# =========================================================
texas_questions ",
        "question": "Which agency regulates electrician licensing in Texas?",
        "options": ["TWC", "TDLR", "OSHA", "ICC"],
        "a
        "explanation": "TDLR oversees electrician licensing and exams in Texas.",
        "reference": "Texas Occupations Code"
    }
]
=======
# =========================
# LICENSE ACCESS
# =========================
st.subheader("🔐 Exam Access")
>>>>>>> 7327be7ceadef49368fa71317043d450ff9cde0b

license_key = st.text_input(
    "Enter your license key",
    type="password",
    placeholder="XXXX-XXXX-XXXX"
)

if st.button("Unlock Access"):
    if license_key.strip() != "":
        # Placeholder logic (real Gumroad verification can be added later)
        st.session_state.licensed = True
        st.success("Access unlocked successfully.")
    else:
        st.error("Please enter a valid license key.")

<<<<<<< HEAD
# =========================================================
# EXAM MODE TIMER (PAID ONLY)
# =========================================================
if ACCESS_TIER != "TRIAL":
    QUESTION_TIME_LIMIT = 60
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, QUESTION_TIME_LIMIT - elapsed)
    st.markdown(f"### ⏱️ Time Remaining: **{remaining}s**")
    if remaining =
        st.error("⏰ Time expired!")
        st.session_state.answered = True
=======
# =========================
# TRIAL / LOCKED VIEW
# =========================
if not st.session_state.licensed:
    st.warning("🔒 Access Required")
>>>>>>> 7327be7ceadef49368fa71317043d450ff9cde0b

<<<<<<< HEAD
# ==========
# =========================================================
if st.session_state.q_index >= len(questions):
    st.success("🎉 Exam Complete")
    st.write(f"Final Score: {st.session_state.score} / {len(questions)}")

    st.markdown("---")
    st.markdown("## 🏆 Pass Guarantee")
=======
    st.markdown("### 🚀 Get Instant Access")
>>>>>>> 7327be7ceadef49368fa71317043d450ff9cde0b
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
# MAIN APP (UNLOCKED)
# =========================
st.success("✅ Full Access Enabled")

st.markdown("### 🧠 Exam Dashboard")

st.markdown("""
This system is designed to simulate real Journeyman Electrician exam conditions.

<<<<<<< HEAD
if st.button("Submit Answer") and not st.session_state.answered:
    st.session_state.answered = True
    if choice == q["answer"]:
        st.success(
=======
**Features included:**
- Timed practice exams  
- NEC-style questions  
- Real exam logic  
- Score tracking (coming next)  
""")

st.markdown("🚧 **Exam engine and questions load here**")

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
    unsafe_allow_html=True
)

>>>>>>> 7327be7ceadef49368fa71317043d450ff9cde0b
