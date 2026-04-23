import streamlit as st

st.set_page_config(page_title="Skills | Honelyn Recto", page_icon="⚡", layout="wide")
st.markdown("""
<h1 style='font-family:Syne,sans-serif;font-weight:800;font-size:48px;margin-bottom:8px;'>Skills</h1>
<div style='width:60px;height:4px;background:linear-gradient(90deg,#7c6af7,#e85d8a);border-radius:2px;margin-bottom:12px;'></div>
<p style='color:#7a7a96;font-size:16px;margin-bottom:32px;'>A snapshot of my technical toolkit and proficiency levels.</p>
""", unsafe_allow_html=True)

# Category filter
category = st.selectbox("Filter by category:", ["All", "Frontend", "Backend", "Data & ML", "DevOps & Tools"])

all_skills = {
    "Frontend": [
        ("JavaScript ", 75), ("HTML & CSS", 90),
    ],
    "Backend": [
        ("Python", 80), 
    ],
    "Data & ML": [
        ("Pandas / NumPy", 50), ("Streamlit", 85),
        ("Matplotlib / Plotly", 50), ("SQL", 50),
    ],
    "DevOps & Tools": [
        ("Git / GitHub", 92), ("AI", 100),("Streamlit",90)
    ],
}

if category == "All":
    display_skills = {k: v for k, v in all_skills.items()}
else:
    display_skills = {category: all_skills[category]}

# Skill bars
for cat, skills in display_skills.items():
    st.markdown(f"""
    <h3 style='font-family:Syne,sans-serif;font-weight:700;font-size:18px;
        color:#1e1e2e;margin:24px 0 16px;letter-spacing:1px;
        text-transform:uppercase;'>{cat}</h3>
    """, unsafe_allow_html=True)
    
    scols = st.columns(2)
    for i, (skill, level) in enumerate(skills):
        with scols[i % 2]:
            color = "#1313" if level >= 85 else "#e85d8a" if level >= 70 else "#3ecfb2"
            st.markdown(f"""
            <div style='background:#1313;border:1px solid #23a;border-radius:12px;
                padding:16px 20px;margin-bottom:10px;'>
                <div style='display:flex;justify-content:space-between;margin-bottom:8px;'>
                    <span style='font-weight:600;font-size:14px;'>{skill}</span>
                    <span style='font-family:Syne,sans-serif;font-weight:700;font-size:14px;
                        color:{color};'>{level}%</span>
                </div>
                <div style='background:#1e1e2e;border-radius:6px;height:8px;overflow:hidden;'>
                    <div style='height:100%;width:{level}%;border-radius:6px;
                        background:linear-gradient(90deg,{color},{color}aa);
                        transition:width 0.5s ease;'></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<hr style='border-color:#1e1e2e;margin:40px 0;'>", unsafe_allow_html=True)

# Certifications
st.markdown("<h2 style='font-family:Syne,sans-serif;font-weight:800;margin-bottom:20px;'>Certifications</h2>", unsafe_allow_html=True)

# List of your certificates
# Note: Replace 'path_to_image.jpg' with your actual file names (e.g., 'python_cert.png')
certs = [
    ("Python Essential 1", "Pages/Python Essential 1.png"),
    ("Introduction to IoT", "Pages/Intoduction to IoT.png"),
    ("Android App Development For Beginner", "Pages/Andriod App development for beginner.png"),
    ("Python for Beginner", "Pages/Python for Beginner.png"),
]

ccols = st.columns(4)

for col, (name, img_url) in zip(ccols, certs):
    with col:
        # Display the image of the certificate
        st.image(img_url, use_container_width=True)
        
        # Display the name below the image in a styled div
        st.markdown(f"""
        <div style='background:#1313;border:1px solid #23a;border-radius:0 0 14px 14px;
            padding:15px;text-align:center;margin-top:-5px;'>
            <div style='font-family:Syne,sans-serif;font-weight:700;font-size:13px;
                line-height:1.4;'>{name}</div>
        </div>
        """, unsafe_allow_html=True)