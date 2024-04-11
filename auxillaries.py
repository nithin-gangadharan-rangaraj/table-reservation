import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def initiate():
  conn = st.connection('gsheets', type=GSheetsConnection)
  
  df = conn.read(ttl = 0)
  worksheets = conn.worksheets()
  st.write(worksheets)
  return df
