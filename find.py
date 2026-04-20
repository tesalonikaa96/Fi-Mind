import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Fi-Mind AI Studio", page_icon="🧠", layout="wide")

# Cek API Key dari Streamlit Secrets
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("🚨 API Key hilang! Pastikan kamu sudah memasukkannya di pengaturan Streamlit Cloud (Secrets).")
    st.stop()

# Menghubungkan ke Google Stitch
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- 2. FITUR AUTO-DISCOVER MODELS (ANTI-404) ---
# Fitur ini akan bertanya ke Google: "Model apa saja yang bisa dipakai oleh kunci rahasia ini?"
@st.cache_data(ttl=300)
def get_allowed_models():
    try:
        available = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # Bersihkan namanya agar tidak ada kata 'models/' yang ganda
                clean_name = m.name.replace('models/', '')
                available.append(clean_name)
        return available
    except Exception as e:
        st.error(f"Gagal mengambil daftar model dari Google: {e}")
        return []

allowed_models = get_allowed_models()

# --- 3. SIDEBAR (STITCH SETTINGS & TEAM INFO) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3426/3426653.png", width=80)
    st.title("⚙️ Stitch Settings")
    
    if not allowed_models:
        st.error("Google sedang memproses API Key barumu. Tunggu 5-10 menit, lalu Refresh web ini.")
        selected_model = None
    else:
        # Pilihan Model Otomatis
        selected_model = st.selectbox("🤖 Active Google Model:", allowed_models)
    
    st.markdown("**1. System Instructions (Persona)**")
    # Tesa bisa mengubah sifat AI langsung dari web!
    sys_instruct = st.text_area(
        "Instruksi Khusus untuk AI:", 
        value="You are an expert English Literature and Linguistics mentor at Jakarta International University. You are assisting the Student Union (SU) AD-CARE team (Tesa, Paulin, Abigail, Winona, Dedifis).",
        height=120
    )
    
    st.markdown("**2. Model Parameters**")
    # Slider kreativitas
    temperature = st.slider("Temperature (Creativity)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    
    # Tombol hapus ingatan
    if st.button("🗑️ Hapus Riwayat Obrolan"):
        st.session_state.chat_session = None
        st.rerun()

    st.divider()
    st.caption("🛡️ Project Fi-vengers | AD-CARE JIU")

# --- 4. INISIALISASI AI & MEMORI OBROLAN ---
if selected_model:
    model = genai.GenerativeModel(
        model_name=selected_model,
        system_instruction=sys_instruct,
        generation_config=genai.GenerationConfig(temperature=temperature)
    )

    # Membuat 'ingatan' agar AI tidak lupa obrolan sebelumnya
    if "chat_session" not in st.session_state or st.session_state.chat_session is None:
        st.session_state.chat_session = model.start_chat(history=[])

# --- 5. MAIN UI (RUANG OBROLAN) ---
st.title("🖋️ The Fi-Mind Anthology")
st.markdown("Mari berdiskusi soal *Second Language Acquisition* atau analisis Sastra 19th-Century!")
st.divider()

if not selected_model:
    st.warning("⏳ Menunggu aktivasi dari Google Stitch... Silakan refresh halaman ini sebentar lagi.")
    st.stop()

# Menampilkan semua riwayat obrolan di layar
for message in st.session_state.chat_session.history:
    role = "assistant" if message.role == "model" else "user"
    avatar = "🧠" if role == "assistant" else "👩‍🎓"
    with st.chat_message(role, avatar=avatar):
        st.markdown(message.parts[0].text)

# --- 6. KOLOM KETIK (CHAT INPUT) ---
if prompt := st.chat_input("Ketik pertanyaanmu di sini (Contoh: Apa inti dari cerita 'The Necklace'?)..."):
    # Tampilkan pesan dari Tesa
    with st.chat_message("user", avatar="👩‍🎓"):
        st.markdown(prompt)
        
    # Proses dan tampilkan balasan dari AI
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Fi-Mind sedang menganalisis..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Koneksi AI terputus: {e}")www