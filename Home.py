import streamlit as st

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

def get_info():
  with st.form("reservation"):
    group_size = st.number_input("🤵‍♂️:white[Size of the Group]")
    book_date = st.date_input("📅 Reservation Date")
    book_time = st.selectbox("🕛 Pick a Time Slot", options = ['12:00', '12:30'])
    
    reserve_button = st.form_submit_button("Reserve", type = "primary")
    if reserve_button:
      st.write("This functionality is not working yet. :(")

if __name__ == "__main__":
  get_info()
