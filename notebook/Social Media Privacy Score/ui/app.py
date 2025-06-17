# ui/app.py
"""
Streamlit front-end for Social Media Privacy Risk Scorer.
Displays color-coded risk meter and actionable safety tips.
"""
import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL", "https://<your-space>.hf.space")

# Page configuration
st.set_page_config(
    page_title="Privacy Risk Scorer",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 Social Media Privacy Risk Scorer")
st.write(
    "Enter your post below to calculate its privacy risk score, "
    "visualize the level, and get tailored safety tips."
)

# User input
text = st.text_area("Your Post", height=150)

# Action: Check Risk
if st.button("Check Risk") and text.strip():
    with st.spinner("Scoring your post..."):
        try:
            resp = requests.post(f"{API_URL}/score", json={"text": text})
            resp.raise_for_status()
            risk = resp.json().get("risk_score", 0)
        except Exception as e:
            st.error(f"Error fetching score: {e}")
            st.stop()

    # Display metric
    st.metric(label="Privacy Risk (%)", value=f"{risk:.2f}")

    # Color-coded progress bar
    st.progress(int(risk))

    # Actionable safety tips
    if risk < 30:
        st.success("**Low Risk**: ✅ This post is unlikely to expose sensitive PII.")
    elif risk < 70:
        st.warning(
            "**Moderate Risk**: ⚠️ Consider removing or anonymizing personal details."
        )
    else:
        st.error(
            "**High Risk**: 🚫 This post contains significant PII. Avoid sharing!"
        )

    # Offer improvement
    if st.button("Improve Post"):
        with st.spinner("Rewriting for privacy..."):
            try:
                rep = requests.post(f"{API_URL}/rewrite", json={"text": text})
                rep.raise_for_status()
                improved = rep.json().get("rewritten", "")
            except Exception as e:
                st.error(f"Error rewriting post: {e}")
                improved = None

        if improved:
            st.subheader("🔄 Improved Post")
            st.write(improved)
