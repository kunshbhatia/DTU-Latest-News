import streamlit as st
from backend_code import main_code
import pandas as pd
from urllib.parse import quote

logo_png = "https://we-recycle.org/wp-content/uploads/2014/03/dtu-logo.png"
headings,links = main_code()
st.set_page_config(layout="wide",page_title="DTU Latest NEWS",page_icon=logo_png)

st.markdown(
    """
    <style>
    [alt="Logo"] {
        height: 50px
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.logo(logo_png,icon_image=logo_png)
st.header("DTU Latest NEWS")

headings_table = pd.DataFrame(headings)
links_table = pd.DataFrame(links)

df = pd.concat((headings_table,links_table),axis=1)
df.drop_duplicates()
df.columns = ['Title','Links']

df["Links"] = df["Links"].apply(lambda x: f"[Open Link]({quote(x, safe=':/')})" if x[0:4] == "http" else "Not Uploded")
st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)

st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 0;">
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        © 2025 Kunsh Bhatia | Built with ❤️ and ☕
    </div>
""", unsafe_allow_html=True)