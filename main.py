import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Spatia - AI Room Understanding",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #F7F8FC;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #263238;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #6B7280;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: 650;
    color: #263238;
    margin-top: 25px;
    margin-bottom: 15px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 15px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
}

.object-card {
    background: #EEF7F4;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #D8EEE7;
}

.object-name {
    font-size: 18px;
    font-weight: 600;
    color: #263238;
}

.object-count {
    font-size: 14px;
    color: #6B7280;
}

.tip {
    background: #FFF8E7;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #F4C95D;
    margin-bottom: 15px;
}

.layout-box {
    background: white;
    border-radius: 18px;
    padding: 20px;
    border: 1px solid #E5E7EB;
}

.room {
    position: relative;
    height: 500px;
    background: #F2EDE4;
    border: 5px solid #8D6E63;
    border-radius: 12px;
    overflow: hidden;
}

.bed {
    position: absolute;
    background: #78909C;
    color: white;
    border-radius: 10px;
    padding: 18px;
    text-align: center;
    font-weight: 600;
}

.old-bed {
    left: 5%;
    top: 10%;
    width: 30%;
    height: 22%;
}

.modern-bed {
    right: 5%;
    top: 30%;
    width: 45%;
    height: 30%;
}

.table {
    position: absolute;
    left: 35%;
    bottom: 18%;
    width: 28%;
    height: 14%;
    background: #795548;
    color: white;
    border-radius: 8px;
    padding: 15px;
    text-align: center;
}

.laptop {
    position: absolute;
    left: 43%;
    bottom: 23%;
    width: 12%;
    height: 7%;
    background: #263238;
    color: white;
    border-radius: 5px;
    text-align: center;
    padding-top: 8px;
    font-size: 12px;
}

.door {
    position: absolute;
    right: 0;
    bottom: 5%;
    width: 8%;
    height: 22%;
    background: #A1887F;
    color: white;
    writing-mode: vertical-rl;
    text-align: center;
    padding: 10px 5px;
}

.cupboard {
    position: absolute;
    left: 5%;
    bottom: 5%;
    width: 20%;
    height: 15%;
    background: #5D4037;
    color: white;
    border-radius: 6px;
    text-align: center;
    padding-top: 18px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">✨ Spatia</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered room understanding & interior planning</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# ROOM TYPE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🏠 Your Room</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
    <h2>Bedroom</h2>
    <p>
    Spatia analyzed your room and identified furniture,
    electronics, access points and workspace areas.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ROOM IMAGE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📷 Room Snapshot</div>',
    unsafe_allow_html=True
)

image_path = Path("bedroom_frames/frame_0.jpg")

if image_path.exists():
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.image(
            str(image_path),
            caption="Room view analyzed by Spatia",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="card">
            <h3>AI Understanding</h3>
            <p>✓ Modern bed</p>
            <p>✓ Older iron bed</p>
            <p>✓ Low floor table</p>
            <p>✓ Laptop</p>
            <p>✓ Chair</p>
            <p>✓ Cupboard</p>
            <p>✓ Washroom entrance</p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.warning("Room image not found.")


# --------------------------------------------------
# OBJECT INVENTORY
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🔎 Detected Objects</div>',
    unsafe_allow_html=True
)

objects = [
    ("🛏️", "Modern Bed", "Main sleeping area"),
    ("🛏️", "Iron Bed", "Secondary bed"),
    ("💻", "Laptop", "Workspace"),
    ("🪑", "Chair", "Seating"),
    ("🪵", "Floor Table", "Current workspace"),
    ("🚪", "Cupboard", "Storage"),
]

cols = st.columns(3)

for i, (icon, name, description) in enumerate(objects):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="object-card">
            <div style="font-size:35px">{icon}</div>
            <div class="object-name">{name}</div>
            <div class="object-count">{description}</div>
        </div>
        """, unsafe_allow_html=True)


# --------------------------------------------------
# VISUAL ROOM LAYOUT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🗺️ Visual Room Layout</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="layout-box">

<h3>Spatia Layout Concept</h3>

<div class="room">

    <div class="bed old-bed">
        Older Bed
    </div>

    <div class="bed modern-bed">
        Modern Bed
    </div>

    <div class="cupboard">
        Cupboard
    </div>

    <div class="table">
        Floor Table
    </div>

    <div class="laptop">
        💻
    </div>

    <div class="door">
        Washroom
    </div>

</div>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">💡 Spatia Design Recommendations</div>',
    unsafe_allow_html=True
)

recommendations = [
    (
        "🖥️",
        "Workspace",
        "Consider replacing the low floor table with a compact desk against a wall to create a more comfortable study area."
    ),
    (
        "🛏️",
        "Bed Arrangement",
        "Maintain a clear walking path around the beds and avoid blocking the main movement area."
    ),
    (
        "🗄️",
        "Storage",
        "Keep sufficient clearance in front of the cupboard so its doors can open comfortably."
    ),
    (
        "🚪",
        "Washroom Access",
        "Keep the area around the washroom entrance free from large furniture."
    ),
    (
        "📚",
        "Organization",
        "Create a dedicated study zone for the laptop, charging cable and study materials."
    )
]

for icon, title, description in recommendations:

    st.markdown(f"""
    <div class="tip">
        <h3>{icon} {title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    "<center>✨ Spatia • AI-powered space understanding</center>",
    unsafe_allow_html=True
)