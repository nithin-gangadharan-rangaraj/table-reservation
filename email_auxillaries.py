import streamlit as st
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os



def send_information(name, number, size, time, date):
    # try:
        multipart = MIMEMultipart()
        try:
            email = st.secrets['email']
            password = st.secrets['password']
        except KeyError:
            email = os.environ.get("email")
            password = os.environ.get("password")
            
        multipart["From"] = f"Reservation <{email}>"
        multipart["To"] = email
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
        server.login(email, password)
        server.sendmail(email, email, multipart.as_string())
        server.quit()
    # except:
    #     st.error("Sorry! There is some technical error, please call the restaurant for confirmation.")
