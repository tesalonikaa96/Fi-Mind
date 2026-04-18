import streamlit as st

st.set_page_config(page_title="Fi-Mind", page_icon="🧠", layout="wide")

# --- SIDEBAR ---
st.sidebar.success("Select a feature above.")
st.sidebar.title("Fi-vengers Team")
st.sidebar.info("Jakarta International University | AD-CARE Project")

# --- MAIN PAGE LAYOUT ---
# Create two columns: Left for text, Right for a welcome image/logo
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🖋️ The Fi-Mind Anthology")
    st.subheader("Where Literature Meets Mental Wellness")
    st.write("""
        Welcome to the heart of the Fi-vengers project. 
        As English Literature students, we know that words have power. 
        Whether you are analyzing Shakespeare or studying for SLA, 
        Fi-Mind is here to support your mind and soul.
    """)
    
with col2:
    # You can put a logo or an illustration here
    st.image("https://via.placeholder.com/200", caption="Fi-Mind Logo")

st.divider()

# --- TABS FOR QUICK INFO ---
tab1, tab2, tab3 = st.tabs(["Daily Verse", "Project Goals", "Contact Us"])

with tab1:
    st.write("*'For I know the plans I have for you,' declares the Lord...*")
    
with tab2:
    st.write("Our goal is to improve student well-being through AI-driven peer support.")

with tab3:
    st.write("Reach out to Tesa and the team at JIU!")