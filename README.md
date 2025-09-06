# 📰 DTU Latest News

This project is a simple **web scraping app** that collects the **latest news and notices** from the official website of **Delhi Technological University (DTU)** and shows them in a clean table with clickable links using **Streamlit**.

---

## 📌 Introduction

Instead of manually checking the DTU website every day, this app automatically scrapes the notices and displays them in one place.  
It is built with:
- **Python**  
- **BeautifulSoup** (for HTML parsing)  
- **Requests** (for fetching the website)  
- **Pandas** (for handling data)  
- **Streamlit** (for the web interface)  

---

## 📂 Project Structure

```
DTU-Latest-News/
├── streamlit_code.py   # Main Streamlit application
├── backend_code.py     # Handles fetching data from the website
├── data.txt            # Stores raw HTML/data fetched
├── requirements.txt    # List of dependencies
└── README.md           # Project description
```

---

## ⚙️ Requirements

Install the dependencies before running:
pip install -r requirements.txt

---

## 🛠 How It Works

- The scraper fetches the Latest News / Notices section from DTU’s website.
- It extracts: Notice title , Notice link (PDF / webpage) and All links are cleaned (spaces fixed) and made clickable in the Streamlit table.

---

## 👨‍💻 Author

- Made with ❤️ by Kunsh Bhatia
- Feel free to fork, improve, and share!



