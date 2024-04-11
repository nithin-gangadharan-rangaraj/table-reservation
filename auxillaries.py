import streamlit as st
import streamlit_gsheets
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def initiate():
  st.write(st-gsheets-connection.__version__)
  conn = st.connection('gsheets', type=GSheetsConnection)
  return conn

def worksheet_names(conn):
  try:
    spreadsheet = conn.client._open_spreadsheet()  
    worksheets = [wsheet.title for wsheet in spreadsheet.worksheets()]
  except AttributeError:
    worksheets = [wsheet.title for wsheet in conn.worksheets()]
  return worksheets

def create_worksheet(conn, name, df):
  conn.create(
            worksheet=name,
            data=df,
            )

def update_worksheet(conn, wsheet, df):
  conn.update(
            worksheet=wsheet,
            data=df,
        )

def read_worksheet(conn, wsheet):
  df = conn.read(
                worksheet = wsheet,
                ttl = 0
        )
  return df


