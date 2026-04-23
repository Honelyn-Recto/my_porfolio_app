import streamlit as st
import re
import time

st.set_page_config(page_title="Contact | Honelyn Recto", page_icon="📬", layout="wide")

st.markdown("""
<h1 style='font-family:Syne,sans-serif;font-weight:800;font-size:48px;margin-bottom:8px;'>Get In Touch</h1>
<div style='width:60px;height:4px;background:linear-gradient(90deg,#7c6af7,#e85d8a);border-radius:2px;margin-bottom:12px;'></div>
<p style='color:#7a7a96;font-size:16px;margin-bottom:40px;'> If you have inquires or whatever I'd love to hear that from you</p>
""", unsafe_allow_html=True)

col_form, col_info = st.columns([3, 2], gap="large")

with col_form:
    st.markdown("<h2 style='font-family:Syne,sans-serif;font-weight:700;font-size:22px;margin-bottom:20px;'>Send a Message</h2>", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=False):
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            name = st.text_input("Your Name *", placeholder="Honelyn Recto")
        with fcol2:
            email = st.text_input("Your Email *", placeholder="honelynrecto20@gmail.com")

        subject = st.selectbox("Subject *", [
            " School Project Collaboration",
            "Group Study / Group Work",
            "Feedback on My Project ",
            "Just Saying Hi",
            "Other"
        ])

        message = st.text_area("Message *", placeholder="Tell me about your project or question...", height=150)

        terms = st.checkbox("I agree that this message is just a portfolio demo and won't actually be sent 😄")
        submitted = st.form_submit_button("🚀 Send Message")

    if submitted:
        errors = []
        if not name.strip():
            errors.append("Name is required.")
        if not email.strip() or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("A valid email is required.")
        if not message.strip() or len(message.strip()) < 20:
            errors.append("Message must be at least 20 characters.")
        if not terms:
            errors.append("Please accept the terms to continue.")

        if errors:
            for e in errors:
                st.error(e)
        else:
            with st.spinner("Sending your message..."):
                time.sleep(1.5)
            st.success("✅ Message sent! I'll get back to you within 24 hours.")
            st.markdown(f"""
            <div style='background:#13131e;border:1px solid #1e1e2e;border-radius:12px;
                padding:20px;margin-top:12px;'>
                <div style='color:#7a7a96;font-size:12px;margin-bottom:10px;
                    font-family:Syne,sans-serif;font-weight:700;letter-spacing:1px;
                    text-transform:uppercase;'>Message Summary</div>
                <div style='font-size:14px;line-height:1.8;'>
                    <b>From:</b> {name} ({email})<br>
                    <b>Subject:</b> {subject}<br>
                    <b>Message:</b> {message[:80]}{'...' if len(message) > 80 else ''}
                </div>
            </div>
            """, unsafe_allow_html=True)

with col_info:
    st.markdown("<h2 style='font-family:Syne,sans-serif;font-weight:700;font-size:22px;margin-bottom:20px;'>Contact Info</h2>", unsafe_allow_html=True)

    contacts = [
        ("📧", "Email", "honelynrecto20@gmail.com", "mailto:honelynrecto20@gmail.com"),
        ("💼", "LinkedIn", "linkedin.com/in/Honelyn Recto", "www.linkedin.com/in/honelyn-recto-b13018404"),
        ("🐙", "GitHub", "github.com/Honelyn-Recto", "https://github.com/"),
        ("📍", "Location", "Masbate, Philippines", None),
    ]

    for icon, label, val, link in contacts:
        content = f"<a href='{link}' target='_blank' style='color:#7c6af7;text-decoration:none;font-size:14px;font-weight:500;'>{val}</a>" if link else f"<span style='font-size:14px;'>{val}</span>"
        st.markdown(f"""
        <div style='display:flex;align-items:center;gap:16px;padding:14px 18px;
            background:#1313;border:1px solid #1e1e2e;border-radius:12px;margin-bottom:10px;'>
            <div style='font-size:22px;width:32px;text-align:center;'>{icon}</div>
            <div>
                <div style='color:#7a7a96;font-size:11px;font-weight:700;letter-spacing:1px;
                    text-transform:uppercase;margin-bottom:2px;'>{label}</div>
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color:#1e1e2e;margin:48px 0 32px;'>", unsafe_allow_html=True)
