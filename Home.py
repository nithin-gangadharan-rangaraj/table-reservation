import streamlit as st
from datetime import datetime, timedelta
import pytz
from auxillaries import *

style = '''
    <style>
        header {visibility: hidden;}
        MainMenu {visibility: hidden;}
        .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                }
        
        
        /* Targeting the background color of the calendar */
        div[data-baseweb="calendar"] div[role="grid"] {
          background-color: white;
        }
    </style>
'''
st.markdown(style, unsafe_allow_html=True)
australian_timezone = pytz.timezone('Australia/Sydney')

def all_time_slots():
    # Define the start and end times
    start_time = datetime.now(australian_timezone).replace(hour = 11, minute = 0)
    end_time = datetime.now(australian_timezone).replace(hour = 22, minute = 0)
    
    # Initialize the list to store time slots as datetime objects
    time_slots = []
    
    # Generate time slots every half hour
    current_time = start_time
    while current_time <= end_time:
        time_slots.append(current_time)
        current_time += timedelta(minutes=30)
    return time_slots

def get_valid_time_slots(time_slots, book_date):
    current_time = datetime.now(australian_timezone)
    if book_date > current_time.date():
        valid_slots = [f"{t.hour}:{t.minute:02d}" for t in time_slots]
    else:
        valid_slots = [f"{t.hour}:{t.minute:02d}" for t in time_slots if t > current_time]
    return valid_slots

def get_start_end_dates():
    today = datetime.now(australian_timezone).date()
    seventh_day = today + timedelta(days=6)
    return today, seventh_day

def get_valid_dates():
    today = datetime.now(australian_timezone).date()
    date_list = [date.strftime('%d/%m/%Y') for date in [today + timedelta(days=i) for i in range(7)]]
    return date_list

def verify_contact(num):
    return len(str(num)) == 10 and num.isnumeric()

def get_info():
  with st.container(border=False):
    book_name = st.text_input("❓Name")
    book_number = st.text_input("📞 Contact number")
    group_size = st.number_input("🤵‍♂️Size of the Group", min_value = 1, max_value = 12)

    today, seventh_day = get_start_end_dates()
    book_date = st.date_input("📅 Reservation Date", min_value=today, max_value=seventh_day, format="DD/MM/YYYY", help = "Can be reserved for the next 6 days.")

      
    book_time = st.selectbox("🕛 Pick a Time Slot", options = get_valid_time_slots(all_time_slots(), book_date))
    if verify_contact(book_number):
        if st.button("Reserve", type = "primary", use_container_width = True):
            st.write("This functionality is not working yet. :(")
    else:
        st.write('Contact number should have 10 digits.')

def create_new_df():
    columns = ['Name', 'Group size', 'Number'] + [slot.strftime('%H:%M') for slot in all_time_slots()]
    df = pd.DataFrame(columns=columns)
    return df

def check_sheets(conn):
    date_list = get_valid_dates()
    existing_worksheets = worksheet_names(conn)
    to_be_created = list(set(date_list) - set(existing_worksheets))
    if len(to_be_created) > 0:
        empty_df = create_new_df()
        for date in to_be_created:
            create_worksheet(conn, date, empty_df)
    

if __name__ == "__main__":
  conn = initiate()
  check_sheets(conn)
  get_info()
