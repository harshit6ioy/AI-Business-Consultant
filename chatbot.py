import streamlit as st, os, json
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import date

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="SWOT Tool", page_icon="📊")
st.title("📊 Business SWOT Analyzer")

if "msgs" not in st.session_state: st.session_state.msgs = []
if "done" not in st.session_state: st.session_state.done = False

with st.sidebar:
    st.subheader("Business Info")
    name = st.text_input("Name", key="n")
    industry = st.text_input("Industry", key="i")
    loc = st.text_input("Location", "", key="l")
    d = st.date_input("Date", date.today(), key="d")
    st.subheader("Options")
    fin = st.checkbox("Financials", True, key="f")
    comp = st.checkbox("Competitors", True, key="c")
    rec = st.checkbox("Recommendations", True, key="r")

def get_context(n,i):
    return {
        "finance": {"trend": "up" if len(n)%2==0 else "flat", "note": f"Status for {n}"},
        "industry": {"growth": "5-8%", "trend": "hot" if len(i)%3==0 else "stable"},
        "position": {"rank": "leader" if len(n)>8 else "challenger", "plus": ["Brand", "Innovation"]}
    }

def make_swot(n,i,l=""):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        ctx = get_context(n,i)
        prompt = f"""SWOT for:
- {n} in {i}
- Location: {l if l else 'Global'}
- Date: {d}

Context: {json.dumps(ctx)}

Include:
1. Focus on {n}
2. Concise points
3. {"Financial data" if fin else "No money talk"}
4. {"Competitive view" if comp else "No rivals"}
5. {"Action steps" if rec else "No advice"}

Format:
# Strengths
- Point
# Weaknesses
- Point
# Opportunities
- Point
# Threats
- Point
{"# Recommendations" if rec else ""}"""
        return model.generate_content(prompt).text
    except Exception as e: return f"Error: {str(e)}"

if st.sidebar.button("Generate"):
    if not name or not industry: st.warning("Need name and industry")
    else:
        with st.spinner("Working..."):
            q = f"SWOT for {name} in {industry}"
            if not st.session_state.done: st.session_state.msgs.append({"r": "user", "c": q})
            res = make_swot(name, industry, loc)
            st.session_state.msgs[-1 if st.session_state.done else -1] = {"r": "ai", "c": res}
            st.session_state.done = True
            st.rerun()

for msg in st.session_state.msgs:
    with st.chat_message(msg["r"]): st.markdown(msg["c"])

if st.sidebar.button("Clear"): 
    st.session_state.msgs = []
    st.session_state.done = False
    st.rerun()