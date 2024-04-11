import streamlit as st
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def send_information(name, number, size, time, date):
    try:
        multipart = MIMEMultipart()
        multipart["From"] = f"Reservation <{st.secrets['email']}>"
        multipart["To"] = st.secrets['email']
        multipart["Subject"] = f'Reservation for {name.upper()}'  
    
        message = f"""\
        <p>Greetings,</p>
        <p>A reservation has been made. Here are the details:</p><br>
        <p><strong>Name: {name}</strong></p>
        <p><strong>Contact: {number}</strong></p>
        <p><strong>Date: {date}</strong></p>
        <p><strong>Group size: {size}</strong></p>
        <p><strong>Time slot: {time}</strong></p>

        <p>Cheers.</p>
        """

        multipart.attach(MIMEText(message, "html"))
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(st.secrets['email'], st.secrets['password'])
        server.sendmail(st.secrets['email'], st.secrets['email'], multipart.as_string())
        server.quit()
    except:
        st.error("Sorry! There is some technical error, please call the restaurant for confirmation.")
