import streamlit as st

# --- Profile Section ---
st.set_page_config(page_title="My Resume", layout="wide")
st.title("🌟 Fatin Syazana Binti Azhar")
st.image("profile.jpg", width=150)  # optional profile picture
st.markdown("---")

# --- Contact Information ---
st.header("📞 Contact Information")
st.write("**Email:** fatin.azhar@example.com")
st.write("**Phone:** +60 12-345 6789")
st.write("[LinkedIn](https://linkedin.com/in/fatinazhar)")
st.write("[GitHub](https://github.com/fatinazhar)")

# --- Education ---
st.header("🎓 Education")
st.write("**Bachelor of Computer Science (Data Science)** - Universiti Teknologi MARA (UiTM)")
st.write("_Expected Graduation: 2026_")

# --- Work Experience ---
st.header("💼 Work Experience")
st.write("**Intern, Tech Solutions Sdn Bhd (June 2024 – Aug 2024)**")
st.write("""
- Assisted in developing a data analytics dashboard using Python and Streamlit.
- Cleaned and visualized company data to improve reporting efficiency.
""")

# --- Skills ---
st.header("🧠 Skills")
cols = st.columns(2)
with cols[0]:
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Data Visualization")
with cols[1]:
    st.write("- SQL")
    st.write("- Machine Learning (Scikit-learn)")
    st.write("- Communication")

# --- Projects ---
st.header("🚀 Projects & Achievements")
st.write("**Smart Automated Clothesline (IoT Project)**")
st.write("Designed a system using ESP8266, rain sensor, and Blynk app for smart drying automation.")
st.write("**Resume Craft (Digital Entrepreneurship Project)**")
st.write("Developed a web-based resume builder with AI-assisted customization.")

# --- Footer ---
st.markdown("---")
st.markdown("✨ _This webpage was built using Streamlit as part of a tutorial assignment._")
