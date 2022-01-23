import time
import yagmail
import pandas
from news import NewsFeed
import datetime
from dotenv import dotenv_values

config = dotenv_values()

df = pandas.read_excel('people.xlsx')


def send_emails():
    news = NewsFeed(interest=row['interest'],
                    from_date=yesterday,
                    to_date=today)
    email.send(to=f"{row['email']}",
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\nSee what's on {row['interest']} today.\n{news.get()}")


while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 17:
        print('Run')
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        email = yagmail.SMTP(user=config['EMAIL_ID'], password=config['PASSWORD'])
        for index, row in df.iterrows():
            send_emails()
        time.sleep(86000)

