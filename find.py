import streamlit as st
from google import genai

# --- 1. CONFIG ---
st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")

# --- 2. SETUP CLIENT (MODERN VERSION) ---
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ API Key tidak ditemukan di Secrets!")
    st.stop()

# Inisialisasi Client Baru
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# --- 3. UI SIDEBAR & HEADER ---
st.sidebar.title("Fi-vengers Team")
st.sidebar.info("Jakarta International University | Fi-vengers Project")

st.title("🖋️ The Fi-Mind Anthology")
st.write("Welcome, Fi-venger! Let's analyze literature together.")

st.divider()

# --- 4. AI FEATURE ---
st.subheader("💬 Fi-Mind AI Study Buddy")
user_query = st.text_input("Tanyakan sesuatu (SLA, Phonetics, Literature):")

if st.button("Ask AI", key="fi_vengers_ai_button"):
    if user_query:
        with st.spinner("Fi-Mind sedang berpikir..."):
            try:
                # Cara panggil AI yang baru di tahun 2026
                response = client.models.generate_content(
                    model='gemini-1.5-flash', 
                    contents=f"You are a supportive English Lit mentor. Question: {user_query}"
                )
                
                st.markdown("### Fi-Mind Says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Terjadi kendala teknis: {e}")
    else:
        st.warning("Silakan masukkan pertanyaan dulu!")