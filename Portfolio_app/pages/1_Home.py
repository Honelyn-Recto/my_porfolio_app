import streamlit as st

st.set_page_config(page_title="Home | Honelyn Recto", page_icon="🏠", layout="wide")
# Hero
st.markdown("""
<div style='padding:60px 0 40px;'>
    <div style='font-family:Syne,sans-serif;font-size:12px;font-weight:700;letter-spacing:3px;
        text-transform:uppercase;color:#7c6af7;margin-bottom:14px;'>👋 Hello, I'm</div>
        Honelyn Recto
    </h1>
    <div style='font-size:20px;color:#7a7a96;margin-bottom:24px;font-weight:300;'>
        Currently Computer Science Student <span style='color:#e85d8a;font-weight:500;'>Masbate, PH 🇵🇭</span>
    </div>
    <p style='font-size:16px;color:#a8a8c0;max-width:600px;line-height:1.8;margin-bottom:32px;'>
        I am a Computer Science student learning how to code. I enjoy building basic apps for my school projects and focus on writing clear, organized code.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border-color:#1e1e2e;margin:40px 0;'>", unsafe_allow_html=True)

# What I do
st.markdown("<h2 style='font-family:Syne,sans-serif;font-weight:800;margin-bottom:24px;'>What I Do</h2>", unsafe_allow_html=True)

services = [
    ("🖥️", "App Development", "I build simple apps for my school projects. I am learning how to connect the front part of an app that users see with the back part that handles data"),
    ("📊", "Python Coding", "I use Python to solve coding problems for my classes. I have finished two Python courses and I'm practicing how to write better code every day."),
    ("🤖", "Mobile Apps", "I am learning how to create apps for Android phones. I focus on making them easy to use for my school assignments."),
]

cols = st.columns(4)
for col, (icon, title, desc) in zip(cols, services):
    with col:
        st.markdown(f"""
        <div style='background:#1313;border:1px solid #23a;border-radius:16px;padding:24px;height:200px;'>
            <div style='font-size:28px;margin-bottom:12px;'>{icon}</div>
            <div style='font-family:Syne,sans-serif;font-weight:700;font-size:15px;margin-bottom:8px;'>{title}</div>
            <div style='color:#7a7a96;font-size:9px;line-height:1.2;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr style='border-color:#1e1e2e;margin:40px 0;'>", unsafe_allow_html=True)

# Timeline
st.markdown("<h2 style='font-family:Syne,sans-serif;font-weight:800;margin-bottom:24px;'>My Journey</h2>", unsafe_allow_html=True)

timeline = [
    ("2022– 2023", "BS Computer Science", "DEBESMSCAT UNIVERSITY")
]
for year, role, org, in timeline:
    st.markdown(f"""
    <div style='display:flex;gap:20px;margin-bottom:20px;'>
        <div style='min-width:150px;text-align:right;'>
            <div style='font-family:Syne,sans-serif;font-weight:700;font-size:12px;color:#7c6af7;padding-top:4px;'>{year}</div>
        </div>
        <div style='width:2px;background:linear-gradient(180deg,#7c6af7,#e85d8a);border-radius:2px;flex-shrink:0;'></div>
        <div style='background:#1313;border:1px solid #23a;border-radius:12px;padding:16px 20px;flex:1;'>
            <div style='font-family:Syne,sans-serif;font-weight:700;font-size:15px;'>{role}</div>
            <div style='color:#1313;font-size:13px;margin-bottom:8px;font-weight:500;'>{org}</div>
            <div style='color:#7a7a96;font-size:13px;line-height:1.6;'>{desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

