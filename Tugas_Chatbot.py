import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

API_KEY = "AIzaSyDh7sAqxYIUzWajFP2jC5i95uFq_CgE-_4"

def chat(history, question):
    """Mengirimkan riwayat chat dan pertanyaan baru ke model AI"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.7,
        api_key=API_KEY
    )
    # Gabungkan history dengan pertanyaan baru
    messages = [
        (
            "system",
            "You are a helpful assistant. Always answer in Indonesian language.",
        ),
        (
            "human",
            f"Riwayat percakapan:\n{history}\n\nPertanyaan baru: {question}",
        ),
    ]
    # Panggil model AI
    ai_msg = llm.invoke(messages)
    return ai_msg

st.title("Halo DIMAS")

# Inisialisasi chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat chat pada setiap refresh halaman
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Menangani input dari pengguna
if prompt := st.chat_input("Apa yang ingin Anda tanyakan?"):
    # Menyusun riwayat percakapan sebagai string
    history = "\n".join([f'{msg["role"]}: {msg["content"]}' for msg in st.session_state.messages])

    # Tampilkan input pengguna di antarmuka
    st.chat_message("user").markdown(prompt)
    # Tambahkan input pengguna ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Dapatkan respons dari model AI
    response = chat(history, prompt)
    answer = response.content

    # Tampilkan respons AI di antarmuka
    with st.chat_message("assistant"):
        st.markdown(answer)
    # Tambahkan respons AI ke riwayat
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Tambahkan opsi untuk melihat riwayat chat
with st.expander("Lihat Riwayat Chat"):
    st.write("**Riwayat Chat:**")
    for msg in st.session_state.messages:
        st.write(f'{msg["role"].capitalize()}: {msg["content"]}')
