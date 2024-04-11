import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def initiate():
  conn = st.connection('gsheets', type=GSheetsConnection)
  
  df = conn.read(ttl = 0)
  spreadsheet = conn.client._open_spreadsheet()  
  worksheets = spreadsheet.worksheets()
  st.write(worksheets)
  return df
