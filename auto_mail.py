import config
import smtplib
from email.message import EmailMessage
from get_cost import get_cost,URL

EMAIL_ID = config.EMAIL_ID
EMAIL_PASS = config.EMAIL_PASS
EMAIL_SEND = config.EMAIL_SEND
cost = get_cost()

mesg = EmailMessage()
mesg['Subject'] = "Amazon Price of Chords"
mesg['To'] = ', '.join(EMAIL_SEND)
mesg['From'] = EMAIL_ID
mesg.set_content(f'The price for the Chords is: {cost}\n The URL is: {URL}')

with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
	s.login(EMAIL_ID,EMAIL_PASS)
	s.send_message(mesg)
