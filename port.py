import streamlit as st
from PIL import Image

# Set up page configuration
st.set_page_config(
    page_title="Ankit Raj - Portfolio",
    page_icon="🎯",
    layout="centered"
)

# Header section with image (you can add your own profile image)
profile_image = Image.open("image.jpg")  # Add a profile picture here
st.image(profile_image, width=150, caption="Ankit Raj")

st.title("Ankit Raj")
st.write("**AI & Data Science Enthusiast**")
st.write("📍 *Jamshedpur, India* | ✉️ ankit.raj91100@gmail.com | [LinkedIn](https://www.linkedin.com/in/ankit-raj-4512a1107) | [GitHub](https://github.com/arawesome1)")
st.write("---")

# About Section with icons and styled text
st.header("About Me")
st.write("""
Hi, I'm **Ankit Raj**, a passionate AI, Machine Learning, and Data Science practitioner. I enjoy creating intelligent solutions and tools to solve real-world problems. My technical expertise includes **Deep Learning, NLP, Machine Learning**, and **Generative AI**.
""")
st.write("---")

# Highlight Key Skills
st.subheader("Key Skills")
st.write("""
- **AI & Machine Learning:** Deep Learning, CNN, NLP, RNN, TensorFlow
- **Web Development:** HTML, CSS, JavaScript, Streamlit
- **Data Science:** Pandas, NumPy, Scikit-Learn, SQL, Data Visualization
- **Generative AI:** Langchain, API Integration, HuggingFace
""")
st.write("---")

# Projects Section (Professional formatting)
st.header("📁 Projects")

# Project 1: QnA Bot (Conversation with PDF)
st.subheader("1. 📄 QnA AI ChatBot ")
st.write("""
This **AI-powered chatbot** delivers real-time answers using **advanced language models**. Unlike other chatbots, it operates independently of external databases, including **Retrieval-Augmented Generation (RAG)** or vector stores. Everything is generated directly from the AI’s built-in knowledge..
- **Technologies Used:** Langchain, AI, Groq
""")
st.markdown("[Live Demo](https://ankitaichatbot.streamlit.app/)", unsafe_allow_html=True)
st.markdown("[GitHub Repository](https://github.com/arawesome1/ai_chatbot/blob/main/app.py)", unsafe_allow_html=True)
st.write("---")

# Project 2: PDF Reader
st.subheader("2. 📚 PDF Reader")
st.write("""
A **PDF reading tool** with AI capabilities that allows users to interact with PDF contents in real time.
- **Technologies Used:** Streamlit, Langchain, NLP
""")
st.markdown("[Live Demo](https://pdfreaderbot.streamlit.app/)", unsafe_allow_html=True)
st.markdown("[GitHub Repository](https://github.com/arawesome1/pdfbot)", unsafe_allow_html=True)
st.write("---")

# Project 3: Gender Classification using CNN
st.subheader("3. 👥 Gender Classification using CNN")
st.write("""
A **deep learning model** that classifies gender based on image inputs. Achieved **94% accuracy** in classifying gender.
- **Technologies Used:** Deep Learning, CNN
""")
st.markdown("[GitHub Repository](https://github.com/arawesome1/Gender_Classification)", unsafe_allow_html=True)
st.write("---")

# Project 4: Hate Speech Detection using Machine Learning
st.subheader("4. 🚨 Hate Speech Detection Using ML")
st.write("""
A machine learning model that classifies text as hateful or non-hateful using **TF-IDF** and **Naive Bayes**.
- **Technologies Used:** NLP, ML, Feature Engineering
""")
st.markdown("[GitHub Repository](https://github.com/arawesome1/hate-speech-detection)", unsafe_allow_html=True)
st.write("---")

# Footer with contact links
st.write("### 📫 Contact Me")
st.write("Feel free to reach out via email or connect with me on [LinkedIn](https://www.linkedin.com/in/ankit-raj-4512a1107). Check out more of my work on [GitHub](https://github.com/arawesome1).")

# Footer with copyright
st.write("---")
st.write("© 2024 Ankit Raj | Made with ❤️ using [Streamlit](https://streamlit.io)")
