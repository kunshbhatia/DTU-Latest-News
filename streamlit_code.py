import streamlit as st
from backend_code import main_code
import pandas as pd
from urllib.parse import quote
import random

logo_png = "https://we-recycle.org/wp-content/uploads/2014/03/dtu-logo.png"
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

search_bar = st.text_input("Search A Notice")

input = st.selectbox(label="Select The News You Have Interest" ,options=['Latest News',"Notices","Jobs","Tenders","Forthcoming Events","1st Year Notices"],index=1)

facts = [
    "🏫 Delhi Technological University (DTU), originally founded as Delhi College of Engineering in 1941, is one of India's oldest engineering colleges. 🎓 Over the decades, it has transformed into a hub of innovation, research, and technical excellence.",    
    "📜 In 2009, DCE was officially upgraded to DTU, giving it university status. 🌟 This autonomy allowed DTU to expand its academic programs, research scope, and international collaborations.",
    "🌳 The DTU campus is spread across 164 acres in Rohini, Delhi. 🏞️ With tree-lined roads, eco-friendly infrastructure, and vibrant student life, it offers a perfect balance of academics and campus culture.",
    "⚙️ DTU has more than 15 academic departments, covering engineering, management, design, and applied sciences. 📚 This diversity helps students pursue interdisciplinary learning and cutting-edge research.",
    "🎭 The university boasts over 100 active student societies and clubs, ranging from robotics and coding to dramatics and literature. 🤝 These clubs form the heartbeat of DTU's dynamic student culture.",
    "🎶 Engifest, DTU's annual cultural fest, is one of the largest student festivals in North India. 🌟 With concerts, competitions, and celebrity performances, it attracts thousands of students from across the country.",
    "💼 DTU maintains an excellent placement record, with top recruiters like Google, Microsoft, Amazon, and consulting giants visiting the campus. 💰 Many students secure packages in double-digit lakhs annually.",
    "🔬 Research and innovation are at the core of DTU's mission, with projects funded by organizations like DRDO, ISRO, and AICTE. 🚀 Students frequently publish papers and file patents in diverse fields.",
    "🌟 DTU has produced legendary alumni such as Vinod Dham, known as the Father of the Pentium chip, and Rajat Gupta, former Managing Director of McKinsey. 🧑‍🎓 Its alumni network spans the globe.",
    "💡 Entrepreneurship is strongly encouraged at DTU, with dedicated incubation centers and startup support. 🚀 Many student-led startups have grown into successful companies, shaping India's startup ecosystem."
]

      
with st.spinner(f'Loading . Do your know {random.choice(facts)}'):
    headings,links = main_code(input=input)

df= pd.DataFrame({"Title" : headings,
                  "Links" : links})

df.drop_duplicates()

if search_bar:
    search_bar_set = []
    search_bar_set.append(search_bar.split())
    text = set(search_bar_set[0])
    req = []
    for i in df['Title'].str.split():
        if text.issubset(set(i)) == True:
            i = " ".join(i)
            try:
                req.append(headings.index(i))
            except:
                pass 

    df = df.iloc[req]

df["Links"] = df["Links"].apply(lambda x: f"[Open Link]({quote(x, safe=':/')})" if x[0:4] == "http" else "Not Uploded")
st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)

st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 0;">
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        © 2025 Kunsh Bhatia | Built with ❤️ and ☕
    </div>
""", unsafe_allow_html=True)