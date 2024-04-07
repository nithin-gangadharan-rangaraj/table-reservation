import streamlit as st
from datetime import datetime, timedelta

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
        MainMenu {visibility: hidden;}
        .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                }
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

def get_valid_dates():

    today = datetime.now().date()
    seventh_day = today + timedelta(days=6)
    return today, seventh_day

def get_info():
  with st.form("reservation", border=False):
    group_size = st.number_input("🤵‍♂️Size of the Group", min_value = 1, max_value = 12)

    today, seventh_day = get_valid_dates()
    book_date = st.date_input("📅 Reservation Date", min_value=today, max_value=seventh_day, format="DD/MM/YYYY")

      
    book_time = st.selectbox("🕛 Pick a Time Slot", options = ['12:00', '12:30'])
    
    reserve_button = st.form_submit_button("Reserve", type = "primary")
    if reserve_button:
      st.write("This functionality is not working yet. :(")

if __name__ == "__main__":
  get_info()
