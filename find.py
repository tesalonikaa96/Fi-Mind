import streamlit as st
import google.generativeai as genai

# --- 1. CONFIG ---
st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")

# --- 2. AI SETUP ---
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ API Key not found! Please check your Streamlit Cloud Secrets.")
    st.stop()

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # We will try these model names one by one until one works
    possible_models = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-1.5-pro']
    model = None

    for name in possible_models:
        try:
            test_model = genai.GenerativeModel(name)
            # Try a tiny test to see if it responds
            model = test_model
            break # Success! Exit the loop
        except:
            continue

    if not model:
        st.error("All Gemini models are currently unavailable. Please try again in 5 minutes.")
        st.stop()
        
except Exception as e:
    st.error(f"⚠️ Connection Error: {e}")
    st.stop()

# --- 3. UI SIDEBAR ---
st.sidebar.title("🛡️ Fi-vengers Team")
st.sidebar.info("Jakarta International University | English Lit")
st.sidebar.write("**Team:** Tesa, Paulin, Abigail, Winona, Dedifis")

# --- 4. MAIN INTERFACE ---
st.title("🖋️ The Fi-Mind Anthology")
st.write("Welcome, Fi-venger! Let's get that literature analysis done.")

st.divider()

user_query = st.text_input("Ask your AI Mentor (SLA, Phonetics, or Literature):")

if st.button("Ask AI", key="fi_vengers_main_btn"):
    if user_query:
        with st.spinner("Fi-Mind is analyzing..."):
            try:
                # Custom instruction for the AI
                persona = "You are a supportive English Literature mentor for Tesa and the Fi-vengers team."
                response = model.generate_content(f"{persona} Question: {user_query}")
                
                st.markdown("### 🧠 Fi-Mind Says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"The AI is currently resting: {e}")
    else:
        st.warning("Please type a question first!")