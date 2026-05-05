import streamlit as st

st.set_page_config(
    page_title="البرنامج الانتخابي — PDN",
    page_icon="☂️",
    layout="wide"
)

with open("programme_PDN_site.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=6000, scrolling=True)