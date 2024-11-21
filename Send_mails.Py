from smtplib import SMTP
import time

receiveremail='other_people_mail@gmail.com'
email='my_mail@gmail.com'
apppasswords='contra'

with SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(email,apppasswords)
    smtp.sendmail(email,receiveremail,f"Subject: estes es el titulo\n\nhola como estas")


# while, time.sleep()