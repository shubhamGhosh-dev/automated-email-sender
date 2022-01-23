
# Project Title

This is an Automated Email Sending system using python.
It reads the Name, Email ID and Interest of recipients and get
all latest news from https://newsapi.org based on recipient's interest, 
and sends these news to each recipient.



## Run Locally

1. Clone the project

```bash
  git clone https://github.com/shubhamGhosh-dev/automated-email-sender.git
```

2. Go to the project directory

```bash
  cd automated-email-sender
```

3. Create a ```.env``` file and add these Environment Variables

```bash
API_KEY=<your_api_key>
EMAIL_ID=<your_email_id>
PASSWORD=<password>
```
4. Edit the ```people.xlsx``` file according to Your recipients list.
5. Install dependencies

```bash
  pip install -r requirements.txt
```

6. Run the App

```bash
  python main.py
```


## Note
If you are using a Gmail Account as sender's email account, then you 
have to turn on "Less secure app access" by going -> manage google account -> Security