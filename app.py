from pathlib import Path 
import streamlit as st
from PIL import Image

#------- PATH SETTINGS---------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir  /"styles"/"main.css"
resume_file = current_dir / "assets" / "Rakesh_Chaudhary_Resume_L10_7016.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rakesh Chaudhary"
PAGE_ICON = "🌏"
NAME = "Rakesh Chaudhary"
DESCRIPTION = """
**Senior Analyst - Data Engineering and Analytics**
"""
EMAIL = "arcsle09plus@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rakesh-chaudhary-7a4355159/",
    "HackerRank": "https://www.hackerrank.com/arcsle09?hr_r=1",
    "Project Euler":"https://projecteuler.net/profile/arcsle09.png",
    "SAFe® 6 SCM":"https://www.credly.com/badges/2fdebb68-df7f-47a9-bb2e-d801bb685d9a"
}

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
✔️ Technology professional having 5 + Years of experience in all phases of agile software development lifecycle. \n
✔️ 5 Years of strong hands on experience building,deploying and maintaining the data extraction,transformation,validation and ingestion pipelines for large datasets using **Python, SQL and Pyspark**.\n
✔️ 3 + Years of hands on experience developing & deploying small/mid/large web scraping solutions using **Scrapy, Requests ,Selenium, Beautifulsoup and APIs**. \n
✔️ 2 + Years of working experience on performing EDA and building classification models for in house data science problems. \n
✔️ 1 + Years of experience developing data vizualizations using PowerBI and Plotly \n
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
    🗄️ Databases: **Oracle | Snowflake | MySQL** \n
    🕸️ REST API Frameworks: **Django | Flask** \n
    📚 Machine Learning: **Tree Based Classifiers | StackEnsamble Classifier | Azure ML** \n
    🚀 DevOps Tools: **Git | Bitbucket | Docker**\n
    🌩️ Cloud Services: **Databricks | Blob | ADF | S3 | BigQuery** \n
    📅 Project Tracking/Docs Tools: **Jira | Confluence** \n

    """
    )

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Professional Work History")
st.write("---")
url = 'https://nielseniq.com/global/en/'
st.write("🧑‍💼", "**Senior Analyst | [NielsenIQ](%s)**" % url)
st.write("11/2018 - Present")

st.write(
    """🚧 **Store Level Sales Data Classification**
- ► Lead Development efforts to implement classifier for highly imbalanced binary classification problem.\n 
- ► Wrote analytical SQL to extract long timeseries data from oracle DB for training the models.\n
- ► Performed EDA and visualizations for each country dataset to understand the distributions and feature importance.\n
- ► Explored various feature selection techniques to find the most impactful features.\n
- ► performed basic hyper-parameter tuning techniques to find the best model parameters.\n
- ► Used Azure ML service to perform machine learning steps for large datasets.\n
Tools: **Tree based classifiers(imblearn),Azure ML,polars,python,git,azure-blob**
""")

st.write(
    """🚧 **Ecommerce Web Data Acquisition**
- ► Developing and Deploying Small/Mid/Large Scale in-house Web Scrapers for E-commerce Data Acquisition Ops.\n
- ► Developed the web-scrapers for south korea based websites in order to scrape products(Avg 2 million) info (categories,price,sales,name) and ingested cleaned data to postgres DB.\n
- ► Integrated Selenium and Scrapy libraries to scrape the javascript enabled contents of the websites.\n
- ► Developed the Web Crawler for UK based Retailer Sites to scrape the Nutrition and Ingredients Details of thousands of products.\n
- ► Developed and deployed various webscrapers for Italy based retailer websites in order to download the promotional flyers(Avg 1000 flyers per week).\n
- ► Prepared the documentations and guidelines to troubleshoot webscrapers. \n
- ► Trained and mentored junior developers for future maintenance,enhancements and developments. \n
Tools: **PostgresDB, SQL, Python, Selenium, Scrapy, Pandas, Docker, shell, Azure-Blob,git**
""")

st.write(
    """🚧 **Optical Web Crawler**
- ► Designed and Developed the in-house Web Crawler for Nielsen Global Client to refresh the data for antibacterial and disinfectant products in databases.
- ► Deploy the web crawler in remote Linux VMs to capture the product images for 32 countries for the given list of products(Avg 50k for each country).
- ► designed and developed the postgres Database to store the data for 32 countries.
- ► The Bot crawls through images to get the best image, extracts the text from the images(OCR) and ingest the cleaned data into postgres DB.
- ► Implemented python multiprocess Method on OCR algorithm to boost the OCR process.\n
- ► wrote unit test cases for OCR and webcrawling modules. \n
Tools: **PostgresDB, SQL, Python, Selenium, pandas, EasyOCR, git, Docker, shell**
""")

st.write(
    """🚧 **Retailer Data Health Dashboard**
- ► Developed,deployed & schedule rule-based data extraction & transformation pipelines using
Pyspark.\n 
- ► stored the output of the pyspark pipelines using parquet format in azure blob storage.
- ► Used 2 different data sources(oracle database and remote storage) to read the input data in PowerBI.\n
- ► Build KPIs and Visualizations in PowerBI for store-level and retailer-level input data.\n
- ► wrote analytical SQL queries to fetch timeseries data. \n
Tools: **PowerBI,oracle SQL,pyspark,git,azure-blob**
""")

st.write(
    """🚧 **Global Item Xcode App**
- ► Wrote the data extraction and transformation pipelines to build country level product info vocab.\n
- ► Developed and schedule the data pipelines using pyspark in databricks platform.\n
- ► stored the output of data pipelines in azure blob in parquet format.\n
- ► Led the Django UI App development for end user inputs and product coding activities.\n
- ► Used celery workers to handle background product search tasks and offload the UI.\n 
- ► Deployed the the Django application in remote linux on-prem machine.\n
- ► Developed the string match module using polars(multi-threaded dataframe library) to optimize the search for the best 4 match.\n
Tools: **Databricks, Pyspark, polars, Azure-Blob, PostgresDB, Python, shell, git**
""")

st.write(
    """🚧 **Ecommerce Data Validation**
- ► Implemented various validation checks for large web-scraped data designed by Data Science Team\n
- ► Developed flask UI for in-house data operations team to operate these checks before the data ingested to production databases.\n
- ► developed data validation pipelines using python-polars dataframe library.\n
- ► wrote unit test cases for validation modules using pytest. \n
Tools: **Python, Polars, Docker, shell, Azure-Blob,git**
""")

st.write(
    """🚧 **Charlink Multi Classification**
- ► An integral part of R&D POD Team for ML exercise on existing Global Item Repositories and other Nielsen’s Consumer Insight Platforms. \n
- ► Regular communication with the senior leadership, Data Scientists, Statisticians, and project stake holders to gather technical requirements. \n
- ► Understood the Cloud RDBMS schema and built various Analytical SQL queries to build data pipelines to be consumed by Research Scientists. \n
- ► Develop the matrix comparison method to compare the accuracy for multiple ML POCs. \n
- ► Prepare the documentation for end-users to run data pipelines.\n
Tools: **Python, SQL, pandas**
""")

st.write(
    """🚧 **Retailer POS Sales Data Validation, Automation and Client Data Inquiry**
- ► A key member of a Sales Data Ingestions and Validations Team for Nielsen Canada. \n
- ► Analyze and validate the input/retailer data and provide the solutions to Nielsen's Premium clients. \n
- ►	Learnt various DWH facts and business rules to solve client's database queries. \n
- ► Communicate with the Major Retailers to resolve the critical IT and POS data transmission incidents. \n
- ► Developed Stored Procedures and Triggers using PL/SQL to apply data validation Rules and Generate DML Logs. \n
- ► Built Analytical SQL queries using Oracle SQL Developer Tool for generating the insightful reports. \n
- ► Prepared KPI Reports for New ETL Platform and presented them to Senior Leadership Team. \n
- ► Trained and mentor a team of 4 people on ETL operations.\n
Tools: **Oracle SQL Developer, Python, PL/SQL, git, bitbucket**
"""
)





