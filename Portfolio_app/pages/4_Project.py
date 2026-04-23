import streamlit as st

st.set_page_config(page_title="Projects | My Portfolio", page_icon="🎓", layout="wide")
# --- Header ---
st.markdown("""
<h1 style='font-family:Syne,sans-serif;font-weight:800;font-size:48px;margin-bottom:8px;'>Projects</h1>
<div style='width:60px;height:4px;background:linear-gradient(90deg,#7c6af7,#e85d8a);border-radius:2px;margin-bottom:12px;'></div>
<p style='color:#7a7a96;font-size:16px;margin-bottom:32px;'>A collection of things built for school requirements and group work.</p>
""", unsafe_allow_html=True)

# --- Project Data ---
projects = [
    {
        "title": "Library Management System",
        "category": "Backend",
        "tags": ["Python", "MySQL",],
        "desc": "A simple library system for managing books, borrowers, and due dates. Supports search, borrow/return tracking, and admin controls.",
        "emoji": "📚",
        "status": "Done",
        "year": "2026",
        "demo": None,
        "highlight": True,
    },
    {
        "title": "Interactive Form App",
        "category": "Data & ML",
        "tags": ["Python", "Streamlit", "Pandas"],
        "desc": "A mini Streamlit app with dynamic input forms, real-time data display, and simple visualizations. Built for quick demos and class presentations.",
        "emoji": "📊",
        "status": "Done",
        "year": "2026",
        "demo": None,
        "highlight": True,
    },
    {
        "title": "Health Sync Record",
        "category": "Web App",
        "tags": ["Streamlit", "MySQL", "JavaScript", "PHP"],
        "desc": "A web-based health record system to replaced manual paper-based recording in Tagpu,Man,Mas for managing patient data, medical history, and health syncing across users. Built as a group capstone requirement.",
        "emoji": "🏥",
        "status": "In Process",
        "year": "2026",
        "demo": None,
        "highlight": True,
    },
    {
        "title": "Health Sync Record",
        "category": "Web App",
        "tags": ["Streamlit", "MySQL", "JavaScript", "Python"],
        "desc": "A web-based platform for syncing and storing health records, with dashboards for patient history, appointments, and health metrics tracking.",
        "emoji": "🏥",
        "status": "In Process",
        "year": "2026",
        "demo": None,
        "highlight": False,
    },
]

# --- Filter Row ---
all_cats = ["All"] + list(dict.fromkeys([p["category"] for p in projects]))
fcol1, fcol2 = st.columns([3, 1])
with fcol1:
    selected_cat = st.radio("Filter:", all_cats, horizontal=True, label_visibility="collapsed")
with fcol2:
    search = st.text_input("Search", placeholder="Search projects...", label_visibility="collapsed")

# --- Filter Logic ---
filtered = projects
if selected_cat != "All":
    filtered = [p for p in filtered if p["category"] == selected_cat]
if search:
    s = search.lower()
    filtered = [p for p in filtered if s in p["title"].lower() or s in p["desc"].lower() or any(s in t.lower() for t in p["tags"])]

st.markdown(f"<p style='color:#7a7a96;font-size:13px;margin-bottom:20px;", unsafe_allow_html=True)

# --- Project Grid ---
for i in range(0, len(filtered), 2):
    row_projects = filtered[i:i+2]
    cols = st.columns(len(row_projects))
    for col, proj in zip(cols, row_projects):
        with col:
            status_color = {
                "Done": "#3ecfb2",
                "In Progress": "#f5c542",
                "Archived": "#7a7a96"
            }.get(proj["status"], "#7a7a96")

            tags_html = "".join([
                f"<span style='background:#1e1e2e;border-radius:6px;padding:3px 10px;"
                f"font-size:11px;font-weight:600;color:#7c6af7;margin-right:4px;'>{t}</span>"
                for t in proj["tags"]
            ])
            demo_btn = (
                f"<a href='{proj['demo']}' target='_blank' "
                f"style='flex:1;text-align:center;padding:8px;"
                f"background:linear-gradient(135deg,#7c6af7,#e85d8a);border-radius:8px;color:#fff;"
                f"text-decoration:none;font-family:Syne,sans-serif;font-weight:700;font-size:13px;'></a>"
                if proj["demo"] else ""
            )

            featured_badge = (
                "<div style='position:absolute;top:16px;right:16px;background:linear-gradient(135deg,#7c6af7,#e85d8a);"
                "color:#fff;font-size:10px;font-family:Syne,sans-serif;font-weight:700;"
                "padding:3px 10px;border-radius:20px;letter-spacing:1px;'></div>"
                if proj["highlight"] else ""
            )

            border_color = "#7c6af7" if proj["highlight"] else "#1e1e2e"
            box_shadow = "box-shadow:0 0 30px rgba(124,106,247,0.15);" if proj["highlight"] else ""

            parts = [
                f"<div style='background:#13131e;border:1px solid {border_color};"
                f"border-radius:18px;padding:24px;margin-bottom:16px;position:relative;{box_shadow}'>",
                featured_badge,
                f"<div style='font-size:36px;margin-bottom:12px;'>{proj['emoji']}</div>",
                f"<div style='display:flex;align-items:center;gap:8px;margin-bottom:8px;'>",
                f"<h3 style='font-family:Syne,sans-serif;font-weight:800;font-size:18px;margin:0;color:#e8e8f0;'>{proj['title']}</h3>",
                f"<span style='background:{status_color}22;color:{status_color};font-size:11px;"
                f"font-weight:700;padding:2px 8px;border-radius:20px;'>{proj['status']}</span>",
                "</div>",
                f"<div style='color:#7c6af7;font-size:12px;font-weight:600;margin-bottom:10px;"
                f"text-transform:uppercase;letter-spacing:1px;'>{proj['category']} · {proj['year']}</div>",
                f"<p style='color:#a8a8c0;font-size:13px;line-height:1.7;margin-bottom:14px;'>{proj['desc']}</p>",
                f"<div style='margin-bottom:16px;'>{tags_html}</div>",                "</div>",
            ]
            st.markdown("".join(parts), unsafe_allow_html=True)

st.markdown("<hr style='border-color:#1e1e2e;margin:40px 0;'>", unsafe_allow_html=True)