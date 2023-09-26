from pathlib import Path 
import streamlit as st
from PIL import Image

#------- PATH SETTINGS---------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir  /"styles"/"main.css"
resume_file = current_dir / "assets" / "Rakesh_Chaudhary_Resume_0976.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rakesh Chaudhary"
PAGE_ICON = ":wave:"
NAME = "Rakesh Chaudhary"
DESCRIPTION = """
Senior Data Analyst/Engineer | Python Developer
"""
EMAIL = "arcsle09plus@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rakesh-chaudhary-7a4355159/",
    "HackerRank": "https://www.hackerrank.com/arcsle09?hr_r=1",
    "Certified Scrum Master":"https://www.credly.com/badges/2fdebb68-df7f-47a9-bb2e-d801bb685d9a"
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }

st.set_page_config(page_icon=PAGE_ICON,page_title=PAGE_TITLE)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Short Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience Summary")
st.write(
    """
✔️ Technology professional having 5+ Years of experience in all phases of agile software development lifecycle. \n
✔️ 5 Years of strong hands on experience building & deploying data extraction,transformation,validation and ingestion pipelines for large datasets using **Python, SQL and Pyspark**.\n
✔️ 3 + Years of hands on experience developing & deploying small/mid/large web scraping solutions using **Scrapy, Requests ,Selenium, Beautifulsoup and APIs**. \n
✔️ 1 + Years of experience developing data vizualizations using PowerBI and Plotly \n
✔️ 1 + Years of working experience on performing EDA and building classification models. \n
✔️ Good experience working with different file formats (JSON,CSV,parquet,xlsx).\n
✔️ Have good knowledge of FMCG and Finance Domains.\n
✔️ Self-motivated, Adaptive, Good Communicator and Problem Solver.\n
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
    👩‍💻 Programming: **Python | SQL** \n
    🗃️ Data Transformation APIs: **Pyspark | Pandas | Polars** \n
    📊 Data Visulization: **PowerBI | Plotly** \n
    🗄️ Databases: **Oracle | Snowflake** \n
    📚 Modeling: **Tree Based Classifiers | StackEnsamble Classifier** \n
    🚀 DevOps Tools: **Git | Bitbucket | Docker | Jenkins**\n
    🌩️ Cloud Services: **Databricks | Blob | ADF | S3 | BigQuery** \n
    📅 Project Tracking/Docs Tools: **Jira | Confluence**

"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Professional Work History")
st.write("---")







