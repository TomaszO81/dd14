import smtplib
import secrets

adresat = 'bullet81@gmail.com'

nadawca = secrets.login
haslo = secrets.haslo

mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(nadawca,haslo)


temat = 'Subject: Hello from Arek in Python\n'
wiadomosc = 'To wiadomosc z pythona'

tresc_wiadomosci = temat + wiadomosc

mailer.sendmail(nadawca,adresat,tresc_wiadomosci)
print('Wyslano maila')
mailer.quit()