#Written by Jerom Mariya Antony

import smtplib
import datetime as dt
from tkinter.font import names

import pandas
import random
MY_EMAIL="jeromdhoni77@gmail.com"

SERVER="smtp.gmail.com"

DOB=dt.datetime(year=2026,month=7,day=28)
curr_date=dt.datetime.now()


PWD = "lisj uhrt axcq fepy"

birthdaynames=pandas.read_csv("birthdays.csv")

dicbirthname=birthdaynames.to_dict(orient="records")
# print(dicbirthname)
for i in dicbirthname:
    # print(i)
    names=i["name"]
    year=i["year"]
    month=i["month"]
    day=i["day"]
    if month==curr_date.month and day==curr_date.day:
        replaced_name=names

# print(replaced_name)
randomin=random.randint(1,3)
letterrandom=f"letter_{randomin}.txt"
with open(f"letter_templates/{letterrandom}","r") as letter1:
    firstletter=letter1.read()
    final_letter= firstletter.replace("[NAME]",replaced_name)

    with smtplib.SMTP(SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PWD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="1331jero@gmail.com",
                            msg=f"Subject:Happy Birthday\n\n {final_letter}")



