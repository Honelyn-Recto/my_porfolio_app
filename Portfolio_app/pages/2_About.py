import streamlit as st

st.set_page_config(page_title="About | Honelyn Recto", layout="wide")

st.markdown("""
<h1 style='font-family:Syne,sans-serif;font-weight:800;font-size:48px;margin-bottom:8px;'>About Me</h1>
<div style='width:60px;height:4px;background:linear-gradient(90deg,#7c6a,#e85d8a);border-radius:2px;margin-bottom:32px;'></div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2])


with col_left:
    st.markdown("""
    <p style='font-size:16px;line-height:1.9;color:#13131e;margin-bottom:20px;'>
        Hi! I'm <strong style='color:#e8e;'>Honelyn Recto</strong>, a passionate Student who's willing to learn new things and been curiuos about lot of things
        from Masbate, Philippines. I'm currently studying and taking bachelor of science in computer science eager to learn how to code somehow even though it's not my prefered course i am so lucky be part of this course because it helps me to understand the advanatge and disadvantage of using social media in daily life.
                 
    </p>
    <p style='font-size:16px;line-height:1.9;color:#13131e;margin-bottom:20px;'>
       I'm 3rd year now and slowly learning and willing to learn or explore new things within this field.
                
    </p>
    <p style='font-size:16px;line-height:1.9;color:#13131e;'>
        When I'm not coding, you'll see me lying or sleeping HAHA,
        or making projects related to the other subjects. I believe that great software is as much about
        empathy and design thinking as it is about technical skill.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <h3 style='font-family:Syne,sans-serif;font-weight:700;margin-bottom:16px;'>Personal Info</h3>
    """, unsafe_allow_html=True)

    info_items = [
        ("📍", "Location", "Masbate, Philippines"),
        ("🎓", "Bachelor", "BS Computer Science, DEBESMSCAT"),
        ("💼", "Status", "Open to opportunities"),
        ("🌐", "Languages", "English, Filipino"),
        ("🎂", "Age", "21 years old"),
        ("📧", "Email", "honelynrecto20@gmail.com"),
    ]
    cols = st.columns(2)
    for i, (icon, label, val) in enumerate(info_items):
        with cols[i % 2]:
            st.markdown(f"""
            <div style='background:#1313;border:1px solid #23a;border-radius:10px;
                padding:12px 16px;margin-bottom:10px;display:flex;align-items:center;gap:12px;'>
                <span style='font-size:18px;'>{icon}</span>
                <div>
                    <div style='color:#7a7a96;font-size:11px;font-weight:600;letter-spacing:1px;
                        text-transform:uppercase;'>{label}</div>
                    <div style='font-size:14px;font-weight:500;'>{val}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


import base64

with open("Pages/20260310_140458.jpg", "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()
with col_right:
    st.markdown("""
    <div style='background:linear-gradient(135deg,#7c6af7 0%,#e85d8a 100%);
        border-radius:24px;aspect-ratio:1;display:flex;align-items:center;justify-content:center;
        max-width:320px;margin:0 auto;padding:8px;'>
        <img src='data:image/jpeg;base64,{img_base64}' 
             style='width:100%;height:100%;object-fit:cover;border-radius:18px;'/>
    </div>
    """.format(img_base64=img_base64), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Fun facts
    facts = [
        ("☕", "Not coffee lover", "100%"),
        ("💻", "Interested to learn how to code", "100%"),
        ("🌙", "Late-night sessions", "Too many"),
    ]
    for icon, label, val in facts:
        st.markdown(f"""
        <div style='display:flex;justify-content:space-between;align-items:center;
            padding:12px 16px;border-bottom:1px solid #1313;'>
            <span style='color:#a8a8c0;font-size:14px;'>{icon} {label}</span>
            <span style='font-family:Syne,sans-serif;font-weight:700;font-size:14px;
                color:#1313;'>{val}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr style='border-color:#1e1e2e;margin:40px 0;'>", unsafe_allow_html=True)

# Values
st.markdown("""
<h2 style='font-family:Syne,sans-serif;font-weight:800;margin-bottom:24px;'>My Values</h2>
""", unsafe_allow_html=True)

values = [
    ("🔍", "Curiosity", "I never stop learning. Every project is a chance to explore new ideas, tools, and perspectives."),
    ("🌱", "Growth Mindset", "Failure is feedback. I embrace challenges as opportunities to evolve and improve."),
]

vcols = st.columns(4)
for col, (icon, title, desc) in zip(vcols, values):
    with col:
        st.markdown(f"""
        <div style='background:#1313;border:1px solid #23a;border-radius:16px;
            padding:24px;text-align:center;height:200px;'>
            <div style='font-size:32px;margin-bottom:12px;'>{icon}</div>
            <div style='font-family:Syne,sans-serif;font-weight:700;font-size:15px;margin-bottom:8px;'>{title}</div>
            <div style='color:#7a7a96;font-size:12px;line-height:1.6;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr style='border-color:#23a;margin:40px 0;'>", unsafe_allow_html=True)

# Interests / hobbies
st.markdown("""
<h2 style='font-family:Syne,sans-serif;font-weight:800;margin-bottom:16px;'>Outside of Code</h2>
""", unsafe_allow_html=True)
hobbies = ["📸 Photography", "📚 Reading","🎵 Music", "🍳 Cooking", "🌿 Plants"]
hobby_html = "".join([f"<span style='background:#1313;border-radius:20px;padding:8px 16px;font-size:14px;display:inline-block;margin:4px;'>{h}</span>" for h in hobbies])
st.markdown(f"<div style='display:flex;flex-wrap:wrap;gap:4px;'>{hobby_html}</div>", unsafe_allow_html=True)
