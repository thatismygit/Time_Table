# 📅 ERP Timetable Scraper

This project is a **web scraping tool** that automatically fetches and organizes timetable data from an ERP system. Instead of manually logging in and checking schedules, this scraper retrieves the timetable and presents it in a structured, interactive format for easy access and use.

## ✨ Features

* 🔐 **Automated login** – securely logs into the ERP portal using stored credentials
* 📋 **Timetable extraction** – scrapes class/lecture schedule data from ERP
* 🗂 **Data structuring** – organizes timetable into a clean and readable format
* 📑 **Export options** – save timetable as CSV/JSON or view in an interactive table
* 🌐 **Streamlit UI** – simple web interface to view timetable directly in the browser
* ⚡ **Fast & efficient** – reduces time spent navigating the ERP manually

## 🛠 Tech Stack

* **Python**

  * `os` – environment variable handling
  * `requests` – HTTP requests for ERP login & data fetching
  * `BeautifulSoup` – parsing and scraping timetable HTML
  * `datetime` – handling date/time formatting
  * `dotenv` – securely loading ERP credentials
  * `streamlit` – interactive web interface for displaying timetable
  * `pandas` – structuring and presenting timetable data

---