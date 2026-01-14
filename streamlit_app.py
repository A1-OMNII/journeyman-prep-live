codespace-shiny-funicular-r4q9j4q7qq99cx9p6
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
        "answer": "Provide a low-impedance path",
"explanation": "This ensures fault current can safely return to the source and trip the breaker quickly.",
"reference": "NEC 250.4(A)(5)"
    }
]

# Session state = st.radio("Choose an answer:", q["options"])

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

"""\nStreamlit frontend for Journeyman Prep\n- Trial mode (sample questions)\n- License unlock input (checks backend /verify)\n- Timed exam behavior for licensed users\n- Uses environment variable APP_BASE_URL to locate backend verify endpoint\n"""\n\nimport streamlit as st\nimport time\nimport os\nimport requests\nimport json\n\n# CONFIG\nst.set_page_config(\n    page_title="Journeyman Electrician Exam Prep",\n    page_icon="⚡",\n    layout="centered",\n)\n\nAPP_BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:8000")\n\n# Small sample question bank (replace with import feature or load from file)\nquestions = [\n    {\n        "id": 1,\n        "question": "Which agency regulates electrician licensing in Texas?",\n        "options": ["TWC", "TDLR", "OSHA", "ICC"],\n        "answer": "TDLR",\n        "explanation": "TDLR (Texas Department of Licensing and Regulation) oversees electrician licensing and exams in Texas.",\n        "reference": "Texas Occupations Code",\n    },\n    {\n        "id": 2,\n        "question": "According to NEC, what is the standard minimum conductor ampacity adjustment for ambient temperatures above 30°C?",\n        "options": ["No adjustment", "Reduce by 10%", "Reduce according to NEC tables", "Increase by 25%"],\n        "answer": "Reduce according to NEC tables",\n        "explanation": "The NEC provides ampacity correction factors in tables that must be applied when ambient temperatures exceed rating conditions.",\n        "reference": "NEC ampacity adjustment tables",\n    },\n]\n\n# SESSION STATE\nif "licensed" not in st.session_state:\n    st.session_state.licensed = False\n\nif "start_time" not in st.session_state:\n    st.session_state.start_time = time.time()\n\nif "q_index" not in st.session_state:\n    st.session_state.q_index = 0\n\nif "score" not in st.session_state:\n    st.session_state.score = 0\n\nif "answered" not in st.session_state:\n    st.session_state.answered = False\n\nif "question_start" not in st.session_state:\n    st.session_state.question_start = time.time()\n\n# HEADER\nst.title("⚡ Journeyman Electrician Exam Prep")\nst.markdown("NEC-Based • Timed Exams • Real Test Logic")\nst.markdown("---")\n\n# NOTICE (from owner)\nst.info(\n    "⚠️ IMPORTANT – READ FIRST\n\n"\n    "This product provides access to a WEB-BASED app.\n"\n    "It is NOT an Apple App Store or Google Play download.\n\n"\n    "✅ After purchase, you will receive a secure link to access the app.\n"\n    "📱 Works on iPhone, Android, tablet, and desktop\n"\n    "🌐 Open using Safari or Chrome\n"\n    "⭐ Bookmark the link for future access\n\n"\n    "If you have any issues accessing the app, contact: A1 Omni Creations"\n)\n\nst.markdown("---")\n\n# LICENSE / ACCESS UI\nst.subheader("🔐 Exam Access")\n\ncol1, col2 = st.columns([3, 1])\nwith col1:\n    license_key = st.text_input(\n        "Enter your license key",\n        type="password",\n        placeholder="XXXX-XXXX-XXXX",\n    )\nwith col2:\n    if st.button("Unlock Access"):\n        if license_key.strip() != "":\n            # Verify with backend\n            try:\n                resp = requests.post(\n                    f"{APP_BASE_URL}/verify",\n                    json={"license_key": license_key.strip()},\n                    timeout=8,\n                )\n                if resp.status_code == 200:\n                    data = resp.json()\n                    if data.get("valid"):\n                        st.session_state.licensed = True\n                        st.success("Access unlocked successfully.")\n                        # reset exam state for a fresh start\n                        st.session_state.q_index = 0\n                        st.session_state.score = 0\n                        st.session_state.answered = False\n                        st.session_state.question_start = time.time()\n                    else:\n                        st.error("Invalid license key. Please check your license or contact support.")\n                else:\n                    st.error("License verification failed (server error). Try again later.")\n            except Exception as e:\n                st.error(f"Error verifying license: {e}")\n        else:\n            st.error("Please enter a valid license key.")\n\nACCESS_TIER = "PRO" if st.session_state.licensed else "TRIAL"\n\n# TRIAL VIEW\nif not st.session_state.licensed:\n    st.warning("🔒 Full access requires a license. You have Trial access to sample questions.")\n    st.markdown("If you purchased through the funnel, paste your license key above.\n\n"\n                "If you have not purchased yet, complete checkout in your funnel to receive access.")\n    st.markdown("---")\n\n# TIMER (paid users)\nQUESTION_TIME_LIMIT = 60\nif ACCESS_TIER != "TRIAL":\n    elapsed = int(time.time() - st.session_state.question_start)\n    remaining = max(0, QUESTION_TIME_LIMIT - elapsed)\n    st.markdown(f"### ⏱️ Time Remaining: **{remaining}s**")\n    if remaining <= 0 and not st.session_state.answered:\n        st.error("⏰ Time expired for this question!")\n        st.session_state.answered = True\n\n# MAIN FLOW\nif st.session_state.q_index >= len(questions):\n    st.success("🎉 Exam Complete")\n    st.write(f"Final Score: {st.session_state.score} / {len(questions)}")\n    st.markdown("---")\n    st.markdown("## 🏆 Pass Guarantee")\n    st.markdown(\n        """\n        • **Free Trial** – Limited sample questions  \n        • **Pro Exam Mode** – **$49**  \n        • **Lifetime Access** – **$129** (Best Value)\n        """\n    )\n    st.markdown("👉 **Complete purchase through your funnel to receive a license key.**")\n    st.info(\n        "After purchase, you will receive your license key by email. "\n        "Enter it above to unlock full access."\n    )\n    st.stop()\n\nq = questions[st.session_state.q_index]\nst.markdown(f"### Question {st.session_state.q_index + 1} of {len(questions)}")\nst.write(q["question"])\n\nchoice = st.radio("Select an answer:", q["options"], index=0, key=f"choice_{st.session_state.q_index}")\n\ncol_submit, col_next = st.columns([1, 1])\nwith col_submit:\n    if st.button("Submit Answer") and not st.session_state.answered:\n        st.session_state.answered = True\n        if choice == q["answer"]:\n            st.success("✅ Correct")\n            st.session_state.score += 1\n        else:\n            st.error(f"❌ Incorrect — Correct answer: **{q['answer']}**")\n        st.markdown(f"**Explanation:** {q.get('explanation','')}")\n        st.markdown(f"**Reference:** {q.get('reference','')}")\nwith col_next:\n    if st.button("Next Question") and st.session_state.answered:\n        st.session_state.q_index += 1\n        st.session_state.answered = False\n        st.session_state.question_start = time.time()\n\nif not st.session_state.licensed and st.session_state.q_index == 0:\n    st.info("This is a sample trial question. Unlock full access after purchase to access the full bank and timed exams.")\n\n# FOOTER\nst.markdown("---")\nst.markdown(\n    "<div style='text-align:center; color: gray; font-size: 0.9em;'>"\n    "Designed & Developed by Saul Hernandez<br>"\n    "A1 Omni Creations<br><br>"\n    "This application is a study and practice tool and does not guarantee licensure."\n    "</div>",\n    unsafe_allow_html=True,\n)\n

