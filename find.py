import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Fi-Mind AI Studio", page_icon="🧠", layout="wide")

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("🚨 API Key missing! Check your Streamlit Secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- 2. STITCH-STYLE SIDEBAR SETTINGS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3426/3426653.png", width=80)
    st.title("⚙️ Stitch Settings")
    
    st.markdown("**1. System Instructions (Persona)**")
    # You can change the AI's personality anytime right from the sidebar!
    sys_instruct = st.text_area(
        "AI Instructions:", 
        value="You are an expert English Literature and Linguistics mentor at Jakarta International University. You are assisting a junior student named Tesa and the Fi-vengers team.",
        height=120
    )
    
    st.markdown("**2. Model Parameters**")
    # Slider to adjust creativity (0 = Strict/Factual, 1 = Highly Creative)
    temperature = st.slider("Temperature (Creativity)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    
    # Button to wipe the AI's memory and start fresh
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_session = None
        st.rerun()

    st.divider()
    st.caption("🛡️ Project Fi-vengers | AD-CARE JIU")

# --- 3. MODEL INITIALIZATION & MEMORY ---
# Create the model using the settings from your sidebar
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=sys_instruct,
    generation_config=genai.GenerationConfig(temperature=temperature)
)

# st.session_state ensures the website remembers your chat history
if "chat_session" not in st.session_state or st.session_state.chat_session is None:
    st.session_state.chat_session = model.start_chat(history=[])

# --- 4. MAIN UI CHAT (Stitch Layout) ---
st.title("🖋️ The Fi-Mind Anthology")
st.markdown("Let's discuss Second Language Acquisition theories or 19th-Century Literature!")
st.divider()

# Display the entire chat history on the screen
for message in st.session_state.chat_session.history:
    # Assign the correct icon based on who is talking
    role = "assistant" if message.role == "model" else "user"
    avatar = "🧠" if role == "assistant" else "👩‍🎓"
    
    with st.chat_message(role, avatar=avatar):
        st.markdown(message.parts[0].text)

# --- 5. CHAT INPUT BAR ---
# st.chat_input creates a sleek typing bar at the bottom of the screen
if prompt := st.chat_input("Type your question here (e.g., What is the Input Hypothesis?)..."):
    
    # 1. Show the user's message
    with st.chat_message("user", avatar="👩‍🎓"):
        st.markdown(prompt)
        
    # 2. Send the message to the AI and show the response
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Analyzing literature..."):
            try:
                # Using send_message ensures the AI remembers the context of the chat
                response = st.session_state.chat_session.send_message(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Connection lost: {e}")