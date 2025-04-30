import streamlit as st

st.set_page_config(page_title="Growth Mindset App", layout="centered")
st.title("🌱 Growth Mindset Challenge")

st.write("""
Welcome! This app is designed to inspire and support your journey toward developing a **growth mindset**.  
A growth mindset means believing your abilities can improve with effort, learning, and persistence.
""")

with st.expander("📘 What is a Growth Mindset?"):
    st.write("""
    A **growth mindset** is the belief that your abilities and intelligence can be developed with hard work, perseverance, and learning from mistakes.
    
    Coined by psychologist **Carol Dweck**, this mindset encourages us to see challenges as opportunities to grow.
    """)

with st.expander("🌟 Why Adopt a Growth Mindset?"):
    st.markdown("""
    - **Embrace Challenges** – Obstacles help you learn.
    - **Learn from Mistakes** – Mistakes are part of the process.
    - **Persist Through Difficulties** – Keep going even when it's tough.
    - **Celebrate Effort** – Focus on the effort, not just outcomes.
    - **Stay Curious** – Be open to new ideas and feedback.
    """)

with st.expander("💡 How to Practice It?"):
    st.markdown("""
    - **Set Learning Goals** – Focus on learning, not just grades.
    - **Reflect Regularly** – Learn from success and failure.
    - **Seek Feedback** – Use criticism to grow.
    - **Stay Positive** – Believe in yourself and help others do the same.
    """)

st.subheader("🚀 Ready to Commit?")
commit = st.checkbox("I want to adopt a growth mindset!")

if commit:
    st.success("Awesome! You're on the path to continuous growth. 💪")
    feedback = st.text_input("What's one area where you want to grow?")
    if feedback:
        st.write(f"🌱 Great! You want to grow in: **{feedback}**. Keep going!")

st.write("---")

