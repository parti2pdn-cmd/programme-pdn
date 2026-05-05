import streamlit as st

st.set_page_config(
    page_title="البرنامج الانتخابي — PDN",
    page_icon="☂",
    layout="wide"
)

# Remove Streamlit default padding
st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }
    .stApp { margin: 0; padding: 0; }
</style>
""", unsafe_allow_html=True)

with open("programme_PDN_site.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=18000, scrolling=False)
