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
st.write("**Address:** No. 35, Jalan Setia 8/4, Taman Setia Indah, 81100, Johor Bahru, Johor.")
st.write("**Email:** s23b0125@umk.edu.my")
st.write("**Phone:** +60 11-6366 0289")
st.write("[LinkedIn](https://linkedin.com/in/fatin-syazana-azhar)")
st.write("[GitHub](https://github.com/syazanaf14)")

# --- Education ---
st.header("🎓 Education")
st.write("**Currently in fifth semester : Bachelor of Information Technology with Honours Track in Artificial Intelligence** - Universiti Malaysia Kelantan (UMK)")
st.write("""
- Expected Graduation: 2027
""")
st.write("**Diploma in Database Management System Technology and Web Applications** - Kolej Vokasional Perdagangan Johor Bahru (KVPJB)")
st.write("""
- Graduated: 2023
""")
st.write("**Sekolah Menengah Kebangsaan Taman Daya**")
st.write("""
- Pentaksiran Tingkatan Tiga (PT3) | 2017
""")
st.write("**Sekolah Kebangsaan Taman Daya 3**")
st.write("""
- Ujian Pencapaian Sekolah Rendah (UPSR) | 2014
""")

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
    st.write("- PHP")
    st.write("- SQL")
    st.write("- C++")
with cols[1]:
    st.write("- Adobe Illustrator")
    st.write("- Microsoft Excel")
    st.write("- Microsoft Word")
    st.write("- Android Studio")

# --- Projects ---
st.header("🚀 Projects & Achievements")
st.write("""
- Smart Rain Clothesline (IoT Project)
- GOLDEN AWARD IN NATIONAL INNOVATION COMPETITION OF EDUCATION AND TECHNOLOGY 2021 (NICETECH21)
- Golden Award in e-Seminar Penyelidikan Dan Inovasi Dalam Pendidikan 2021 (e-SPeDIP2021) 
- Silver Award in Innovation Development Through Educatonal Activities (iDEA21)
- WEBINAR STRATEGI PEMASARAN DIGITAL PERINGKAT KEBANGSAAN 2021
- KURSUS JANGKA PENDEK MS PROJECT ANJURAN KOLEJ KOMUNITI PASIR GUDANG
- Ceramah Kepimpinan Pelajar Era Vuca Peringkat Kebangsaan
- Kursus Kepimpinan Peringkat Kebangsaan

# --- Footer ---
st.markdown("---")
