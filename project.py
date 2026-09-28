import streamlit as st

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080c18, #18213b);
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #312e81, #164e63);
    padding: 35px 20px;
    border-radius: 25px;
    text-align: center;
    border: 1px solid #6366f1;
    margin-bottom: 25px;
}

.hero h1 {
    color: white !important;
    font-size: 42px;
}

.hero p {
    color: #dbeafe !important;
    font-size: 17px;
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 10px !important;
}

.stButton button {
    background: linear-gradient(90deg, #7c3aed, #0891b2);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton button:hover {
    border: 1px solid #a78bfa;
    color: white;
}

label, .stMarkdown {
    color: #f3f4f6;
}
</style>
""", unsafe_allow_html=True)

# Visible chatbot interface
st.markdown("""
<div class="hero">
    <h1>🤖 AI CHATBOT</h1>
    <p>Welcome! Your personal AI assistant is here.</p>
    <p>Ask questions, explore ideas, and learn something new.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("💬 How can I help you?")

st.write(
    "You can ask me anything, from general knowledge "
    "to writing, summarizing, and coding."
)

name = st.text_input("Enter your name")
message = st.text_area("Enter your message")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)

value = st.slider("Select a value", 0, 100, 50)

option = st.selectbox(
    "Select an option",
    ["General Knowledge", "Writing", "Coding"]
)

options = st.multiselect(
    "Select your interests",
    ["Technology", "Science", "Business", "Education"]
)

if st.button("Submit"):
    st.success(f"Welcome {name or 'there'}! Your details have been submitted.")

st.caption("Powered by Streamlit | AI Chatbot")