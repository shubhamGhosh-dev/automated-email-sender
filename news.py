import requests
from dotenv import dotenv_values

config = dotenv_values()


class NewsFeed:
    """
        Representing multiple news titles as a single string
    """
    base_url = "https://newsapi.org/v2/everything"
    API_KEY = config['API_KEY']

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._get_url()

        articles = self._get_article(url)

        email_body = ""
        for article in articles:
            email_body = email_body + '\n\n' + article['title'] + '\n' + article['url']

        return email_body

    def _get_article(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _get_url(self):
        url = f"{self.base_url}?" \
              f"q={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"sortBy=popularity&" \
              f"language={self.language}&" \
              f"apiKey={self.API_KEY}"
        return url
