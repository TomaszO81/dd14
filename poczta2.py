import smtplib
import secrets
from email.mime.text import MIMEText

odbiorca = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

temat = 'Hello znowu z Pythona Tomek'
tresc = 'To jest wiadomość z polskimi znakami żźćąśęó'

wiadomosc = MIMEText(tresc, _charset='utf-8')
wiadomosc['Subject'] = temat
wiadomosc['From'] = nadawca
wiadomosc['To'] = odbiorca

mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(nadawca,haslo)
mailer.sendmail(nadawca,odbiorca,wiadomosc.as_string())

print('Wiadomosc wysłana')
mailer.close()
