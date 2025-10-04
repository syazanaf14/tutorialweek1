import streamlit as st

# --- Profile Section ---
st.set_page_config(page_title="My Resume", layout="wide")

# Create two columns
col1, col2 = st.columns([1, 3])  # 1:3 ratio (image smaller, text wider)

with col1:
    st.image("formalfatin.JPG", width=150) 
with col2:
    st.title("Fatin Syazana Binti Azhar")
    st.subheader("Final Year Student of Bachelor of Information Technology with Honours Track in Artificial Intelligence")

st.markdown("---")

# --- Contact Information ---
st.header("📞 Contact Information")
st.write("**Email:** s23b0125@umk.edu.my")
st.write("**Phone:** +60 11-6366 0289")
st.write("[LinkedIn](https://linkedin.com/in/fatin-syazana-azhar)")
st.write("[GitHub](https://github.com/syazanaf14)")

# --- Education ---
st.header("🎓 Education")
st.write("**Currently in fifth semester : Bachelor of Information Technology with Honours Track in Artificial Intelligence** - Universiti Malaysia Kelantan (UMK)")
st.write("Expected Graduation: 2027")
st.write("**Diploma in Database Management System Technology and Web Applications** - Kolej Vokasional Perdagangan Johor Bahru (KVPJB)")
st.write("Graduated: 2023")

# --- Work Experience ---
st.header("💼 Work Experience")
st.write("**Full Time Shop Assistant, Printcept Services (December 2022 – August 2023)**")
st.write("""
- Assisted in packing shopee order and shop order.
- Assisted in sorting products.
- Assisted in printing and cutting stickers, flyers, cards and etc.
- Managed to sort out all the products in the store. 
""")
st.write("**Intern, Dreamztech Sdn Bhd (April 2022 – Aug 2022)**")
st.write("""
- Assisted in designing a web dashboard (front end).
- Assisted in handling project (back end).
- Assited in  group developing project for multiple project in various company of customers.
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
