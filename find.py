import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")

# --- 2. AI SETUP (SECURITY) ---
try:
    # This pulls your API key safely from the "Secrets" vault
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ API Key not found! Please check your Streamlit Cloud Secrets.")

# --- 3. SIDEBAR (TEAM PROFILE) ---
st.sidebar.title("Fi-vengers Team")
st.sidebar.info("Jakarta International University | AD-CARE Project")
st.sidebar.write("**Members:** Tesa, Paulin, Abigail, Winona, Dedifis")

# --- 4. MAIN INTERFACE ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🖋️ The Fi-Mind Anthology")
    st.subheader("Where Literature Meets Mental Wellness")
    st.write("Welcome, Fi-venger! Let's analyze literature and stay mindful together.")

with col2:
    # Team Logo or Illustration
    st.image("https://cdn-icons-png.flaticon.com/512/3426/3426653.png", width=150)

st.divider()

# --- 5. THE AI FEATURE (STUDY BUDDY) ---
st.subheader("💬 Fi-Mind AI Study Buddy")
user_query = st.text_input("Ask me about SLA, Phonetics, or Literature:", placeholder="e.g., Explain Universal Grammar...")

if st.button("Ask AI"):
    if user_query:
        with st.spinner("Fi-Mind is analyzing..."):
            try:
                # Custom Persona: Telling the AI how to behave
                persona = "You are an empathetic English Literature mentor for Tesa and the Fi-vengers team. Answer kindly."
                response = model.generate_content(f"{persona} Question: {user_query}")
                
                st.markdown("### Fi-Mind Says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"The AI is currently resting: {e}")
    else:
        st.warning("Please enter a question first!")

# --- 6. INFORMATION TABS ---
st.divider()
tab1, tab2, tab3 = st.tabs(["🙏 Daily Verse", "🎯 Project Goals", "📞 Contact"])

with tab1:
    st.info("'For I know the plans I have for you,' declares the Lord...")

with tab2:
    st.write("Supporting the well-being of JIU students through literature and AI.")

with tab3:
    st.write("Contact the AD-CARE division for support.")