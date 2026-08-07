import streamlit as st
import os
from crew import create_crew
import time
import traceback


st.set_page_config(
    page_title="Multi-Agent Football Intelligence Platform",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

/* Background */

.stApp{
    background:
        radial-gradient(circle at top left,#1db95422,transparent 30%),
        radial-gradient(circle at bottom right,#0d6efd22,transparent 35%),
        #0b1220;
}

/* Hide Streamlit */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:#121b2f;
    border-right:1px solid rgba(255,255,255,.06);

}

/* Hero */

.hero{

    padding:45px;

    border-radius:22px;

    background:linear-gradient(
    135deg,
    #16a34a,
    #0f766e,
    #1d4ed8);

    color:white;

    margin-bottom:35px;

    box-shadow:0 15px 45px rgba(0,0,0,.35);

    animation:fadeUp .8s ease;

}

.hero h1{

    font-size:52px;

    font-weight:800;

    margin-bottom:10px;

}

.hero p{

    font-size:18px;

    opacity:.95;

}

/* Cards */

.metric-card{

    background:#172033;

    border:1px solid rgba(255,255,255,.08);

    border-radius:18px;

    padding:25px;

    text-align:center;

    transition:.35s;

    box-shadow:0 10px 30px rgba(0,0,0,.25);

}

.metric-card:hover{

    transform:translateY(-8px);

    border-color:#22c55e;

}

.metric-title{

    color:#94a3b8;

    font-size:15px;

}

.metric-value{

    color:white;

    font-size:34px;

    font-weight:800;

}

/* Titles */

h1,h2,h3{

    color:white;

}

/* TextArea */

textarea{

    background:#172033 !important;

    color:white !important;

    border-radius:16px !important;

    border:1px solid rgba(255,255,255,.08) !important;

    font-size:16px !important;

}

/* Button */

.stButton>button{

    width:100%;

    height:58px;

    border:none;

    border-radius:15px;

    background:linear-gradient(
    135deg,
    #22c55e,
    #15803d);

    color:white;

    font-size:18px;

    font-weight:700;

    transition:.3s;

    box-shadow:0 8px 25px rgba(34,197,94,.35);

}

.stButton>button:hover{

    transform:translateY(-3px);

    box-shadow:0 12px 30px rgba(34,197,94,.55);

}

/* Containers */

.block-container{

    padding-top:2rem;

    max-width:1400px;

}

/* Animation */

@keyframes fadeUp{

    from{

        opacity:0;

        transform:translateY(30px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

.fade{

    animation:fadeUp .7s ease;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("# ⚽ Multi-Agent Football Intelligence Platform")

    st.caption("Advanced AI-Powered Football Analysis and Reporting")

    st.divider()

    st.markdown("### 🤖 Agents")

    st.success("✅ Request Agent")

    st.info("🌍 Scout Agent")

    st.info("🔎 Scraping Agent")

    st.warning("🧠 Recommendation Agent")

    st.error("📄 Report Agent")

    st.divider()

    st.markdown("### 🛠 Tech Stack")

    st.markdown("""
- CrewAI
- Gemini 
- Tavily
- ScrapeGraph AI
- Streamlit
""")

    st.divider()

    st.success("🟢 System Online")

# ==========================================================
# Hero
# ==========================================================

st.markdown("""

<div class="hero">

<h1>⚽ Multi-Agent Football Intelligence Platform</h1>

<p>

Advanced AI-Powered Football Analysis and Reporting

Search • Scout • Analyze • Compare • Summarize • Generate Reports

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# Dashboard
# ==========================================================

c1,c2,c3,c4=st.columns(4)

with c1:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">AI Agents</div>

<div class="metric-value">5</div>

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">Search Engine</div>

<div class="metric-value">Tavily</div>

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">Extraction</div>

<div class="metric-value">AI</div>

</div>

""",unsafe_allow_html=True)

with c4:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">Reports</div>

<div class="metric-value">HTML</div>

</div>

""",unsafe_allow_html=True)

st.write("")

# ==========================================================
# User Request
# ==========================================================

st.markdown("## 🎯 Football Intelligence Request")

user_request=st.text_area(

"",
height=220,

placeholder="""
Examples

• Compare Rodri and Declan Rice

• Latest Rodri transfer news

"""
)

generate=st.button("🚀 Generate AI Scout Report")

# ==========================================================
# Run CrewAI
# ==========================================================

import json
import streamlit.components.v1 as components

if generate:

    if not user_request.strip():

        st.warning("Please enter a football request.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    workflow = st.empty()

    report_placeholder = st.empty()

    try:

        workflow.markdown("""
### 🤖 Agent Execution

🟢 **Request Agent** → Understanding your request...

🌍 **Scout Agent** → Searching football sources...

🔎 **Scraping Agent** → Extracting structured information...

🧠 **Recommendation Agent** → Reasoning over football intelligence...

📄 **Report Agent** → Building professional report...
""")

        progress.progress(10)
        status.info("🚀 Initializing Football Intelligence Platform...")
        time.sleep(.5)

        progress.progress(25)
        status.info("🌍 Searching reliable football sources...")

        crew = create_crew(user_request)

        result = crew.kickoff(
            inputs={
                "request": user_request
            }
        )

        progress.progress(70)
        status.info("🧠 Building football intelligence...")

        final_report = str(result)

        st.session_state["report"] = final_report

        progress.progress(100)

        status.success("✅ Report Generated Successfully!")


    except Exception:
        st.error(traceback.format_exc())

# ==========================================================
# REPORT
# ==========================================================

if st.session_state.get("report"):

    report = st.session_state["report"]

    report = (
        report
        .replace("```html","")
        .replace("```HTML","")
        .replace("```","")
        .strip()
    )

    st.markdown("## 📄 Football Intelligence Report")

    components.html(
        report,
        height=900,
        scrolling=True,
    )

    col1,col2,col3=st.columns([1,1,6])

    with col1:

        st.download_button(

            "⬇️ HTML",

            data=report,

            file_name="football_scout_report.html",

            mime="text/html",
        )

    with col2:

        st.download_button(

            "📄 TXT",

            data=report,

            file_name="football_scout_report.txt",

            mime="text/plain",
        )

# ==========================================================
# RAW OUTPUT
# ==========================================================

with st.expander("🧠 Raw AI Output", expanded=False):

    st.code(st.session_state.get("report",""), language="html")

# ==========================================================
# Footer
# ==========================================================

st.markdown("""

<br><br>

<hr style="border:1px solid #2b364d;">

<div style="text-align:center;padding:20px">

<h3 style="color:white;margin-bottom:5px;">

⚽ Multi-Agent Football Intelligence Platform

</h3>

<p style="color:#9aa6b2">

Multi-Agent Football Intelligence Platform

</p>

<p style="color:#6b7280;font-size:13px">

Powered by CrewAI • Tavily • ScrapeGraph • LLMs and Agents • Streamlit

</p>

</div>

""",unsafe_allow_html=True)