import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIGURATION ---
# This MUST be the very first Streamlit command in your script
st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")

# --- 2. DEBUGGING & SECRETS CHECK ---
# We check if the key exists before trying to use it
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ The Website can't find your Key. Please check the Streamlit Cloud Dashboard Secrets or your .streamlit/secrets.toml file!")
    st.stop() # This stops the app here so it doesn't crash trying to load the AI

# --- 3. AI SETUP ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    # Using gemini-1.5-flash is perfect for quick, text-based chat!
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"⚠️ Connection Error during AI setup: {e}")
    st.stop()

# --- 4. SIDEBAR ---
st.sidebar.title("Fi-vengers Team")
st.sidebar.info("Jakarta International University | Fi-vengers Project")
st.sidebar.write("**Members:** Tesa, Paulin, Abigail, Winona, Dedifis")

# --- 5. MAIN HEADER UI ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("🖋️ The Fi-Mind Anthology")
    st.subheader("Where Literature Meets Mental Wellness")
    st.write("Welcome, Fi-venger! Let's analyze literature together.")
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3426/3426653.png", width=150)

st.divider()

# --- 6. THE AI FEATURE (STUDY BUDDY) ---
st.subheader("💬 Fi-Mind AI Study Buddy")
user_query = st.text_input("Ask me about SLA, Phonetics, or Literature:")

if st.button("Ask AI", key="fi_vengers_ai_button"):
    if user_query:
        with st.spinner("Fi-Mind is analyzing..."):
            try:
                # Adding the persona so the AI knows who it's talking to
                persona = "You are a supportive English Literature mentor for Tesa and the Fi-vengers team."
                response = model.generate_content(f"{persona} Question: {user_query}")
                
                st.markdown("### Fi-Mind Says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"The AI is currently resting: {e}")
    else:
        st.warning("Please enter a question first!")