import streamlit as st

def get_info():
  with st.form("reservation"):
    group_size = st.number_input("🤵‍♂️Size of the Group")
    book_date = st.date_input("📅 Reservation Date")
    book_time = st.selectbox("🕛 Pick a Time Slot", options = ['12:00', '12:30'])
    
    reserve_button = st.form_submit_button("Reserve", type = "primary")
    if reserve_button:
      st.write("This functionality is not working yet. :(")

if __name__ == "__main__":
  get_info()
