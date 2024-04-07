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

def all_time_slots():
    # Define the start and end times
    start_time = datetime.strptime('11:00', '%H:%M')
    end_time = datetime.strptime('22:00', '%H:%M')
    
    # Initialize the list to store time slots as datetime objects
    time_slots = []
    
    # Generate time slots every half hour
    current_time = start_time
    while current_time <= end_time:
        time_slots.append(current_time)
        current_time += timedelta(minutes=30)
    return time_slots

def get_valid_time_slots(time_slots):
    current_time = datetime.now()
    valid_slots = [f"{t.hour}:{t.minute:02d}" for t in time_slots if t > current_time]
    st.write(valid_slots)
    return valid_slots

def get_valid_dates():
    today = datetime.now().date()
    seventh_day = today + timedelta(days=6)
    return today, seventh_day

def get_info():
  with st.form("reservation", border=False):
    group_size = st.number_input("🤵‍♂️Size of the Group", min_value = 1, max_value = 12)

    today, seventh_day = get_valid_dates()
    book_date = st.date_input("📅 Reservation Date", min_value=today, max_value=seventh_day, format="DD/MM/YYYY", help = "Can be reserved for the next 6 days.")

      
    book_time = st.selectbox("🕛 Pick a Time Slot", options = get_valid_time_slots(all_time_slots()))
    
    reserve_button = st.form_submit_button("Reserve", type = "primary")
    if reserve_button:
        st.write("This functionality is not working yet. :(")

if __name__ == "__main__":
  get_info()
