import streamlit as st
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Journeyman Electrician Exam Prep",
    page_icon="⚡",
    layout="centered"
)

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

# =========================
# LICENSE ACCESS
# =========================
st.subheader("🔐 Exam Access")

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

# =========================
# TRIAL / LOCKED VIEW
# =========================
if not st.session_state.licensed:
    st.warning("🔒 Access Required")

    st.markdown("### 🚀 Get Instant Access")
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
