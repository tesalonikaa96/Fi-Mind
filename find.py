import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")
# --- 2. AI SETUP (SECURITY) ---
model = None  # We start with nothing

try:
    # 1. Try to get the key and configure
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # 2. Try to start the model (This must be INSIDE the try block or AFTER the except)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
except Exception as e:
    # 3. This tells Python what to do if things go wrong
    st.error(f"⚠️ Connection Error: {e}")
else:
    st.error("⚠️ API Key not found! Please check your .streamlit/secrets.toml file.")
st.sidebar.title("Fi-vengers Team")
st.sidebar.info("Jakarta International University | Fi-vengers Project")
st.sidebar.write("**Members:** Tesa, Paulin, Abigail, Winona, Dedifis")
col1, col2 = st.columns([2, 1])
with col1:
    st.title("🖋️ The Fi-Mind Anthology")
    st.subheader("Where Literature Meets Mental Wellness")
    st.write("Welcome, Fi-venger! Let's analyze literature together.")
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3426/3426653.png", width=150)

st.divider()

# --- 5. THE AI FEATURE (STUDY BUDDY) ---
st.subheader("💬 Fi-Mind AI Study Buddy")
user_query = st.text_input("Ask me about SLA, Phonetics, or Literature:")

if st.button("Ask AI"):
    if not model:
        st.error("The AI cannot start because the API Key is missing.")
    elif user_query:
        with st.spinner("Fi-Mind is analyzing..."):
            try:
                persona = "You are a supportive English Literature mentor for Tesa and the Fi-vengers team."
                response = model.generate_content(f"{persona} Question: {user_query}")
                st.markdown("### Fi-Mind Says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"The AI is currently resting: {e}")
    else:
        st.warning("Please enter a question first!")