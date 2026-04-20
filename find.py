import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")

# --- 2. AI CONFIGURATION ---
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ API Key not found! Please check your Streamlit Cloud Secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- 3. DIAGNOSIS: FINDING THE RIGHT MODEL ---
@st.cache_resource
def get_working_model():
    # This list contains common names for Gemini in 2026
    test_names = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
    for name in test_names:
        try:
            m = genai.GenerativeModel(name)
            # A tiny test to see if Google accepts the name
            m.generate_content("test", generation_config={"max_output_tokens": 1})
            return m
        except Exception:
            continue
    return None

model = get_working_model()

# --- 4. SIDEBAR & UI ---
st.sidebar.title("🛡️ Fi-vengers Team")
st.sidebar.info("Jakarta International University | English Lit")
st.sidebar.write("**Members:** Tesa, Paulin, Abigail, Winona, Dedifis")

st.title("🖋️ The Fi-Mind Anthology")
st.write("Welcome back, Tesa! Let's get your study session started.")
st.divider()

# --- 5. THE AI CHAT ---
if model is None:
    st.error("🚨 404 Error: Google cannot find a compatible model for your key yet. Please wait 10 minutes for your key to activate fully.")
else:
    user_query = st.text_input("Ask about SLA, Phonetics, or Literature:")
    
    if st.button("Ask AI", key="fi_mind_final_btn"):
        if user_query:
            with st.spinner("Fi-Mind is analyzing..."):
                try:
                    persona = "You are a supportive English Literature mentor for Tesa and the Fi-vengers team."
                    response = model.generate_content(f"{persona} Question: {user_query}")
                    st.markdown("### 🧠 Fi-Mind Says:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"The AI is having a moment: {e}")
        else:
            st.warning("Please type a question first!")