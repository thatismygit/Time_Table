import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

# ERP login and timetable URLs


def fetch_timetable(username: str, password: str, TIMETABLE_URL: str, LOGIN_URL: str):
    """Logs into ERP and fetches timetable data as a list of lists."""
    session = requests.Session()
    
    # Authenticate
    credentials = {"username": username, "password": password}
    response = session.post(LOGIN_URL, data=credentials)
    if response.status_code != 200:
        raise Exception("Login failed, check credentials or connection.")

    # Fetch timetable page
    tt_response = session.get(TIMETABLE_URL)
    soup = BeautifulSoup(tt_response.text, "html.parser")

    # Extract timetable data
    table_div = soup.find("div", class_="table-responsive")
    if not table_div:
        raise Exception("Timetable not found in response.")

    h5_tags = table_div.find_all("h5")

    time_table = []
    for h5 in h5_tags:
        # Extract text, clean spaces and brackets
        values = [text.strip("[] ").strip() for text in h5.stripped_strings]
        time_table.append(values)

    return time_table[8:]  # skip initial headers or unwanted rows

def get_today_schedule(time_table):
    """Returns today's schedule based on weekday."""
    day_num = date.today().weekday() + 1  # Monday = 1, Sunday = 7
    start_index = 8 * (day_num - 1)
    end_index = 8 * day_num
    return time_table[start_index:end_index]

if __name__ == "__main__":
    load_dotenv(override=True)
    LOGIN_URL = os.getenv("LOGIN_URL")
    TT_URL = os.getenv("TIMETABLE_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    timetable = fetch_timetable(USERNAME, PASSWORD, TT_URL, LOGIN_URL)
    today_schedule = get_today_schedule(timetable)
    # print(today_schedule)

    if today_schedule:
        df = pd.DataFrame(today_schedule, columns=["Faculty", "Subject/Room", "Batch"])
        df.index = df.index + 1
        st.subheader(f"Today's Schedule ({date.today().strftime('%A, %d %B %Y')})")
        st.table(df)  # or st.dataframe(df) for interactive scroll
    else:
        st.warning("No schedule available for today.")