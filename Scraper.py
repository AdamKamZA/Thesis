import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
from Outlets.BBC import bbc_home_links_sport_base, bbc_home_links_politics_base

"""
I need to create a map function that will work for whatever news site title i put in
This title will route to its own unique cleanup function
The general request, and post to db will remain the same, as well as clean up, it will all be formatted accordingly
"""

"""
Define an object that maps a topic and outlet to their base source, makes things easier to manage
"""

OUTLETS = {
    'BBC': {
        'sport': 'https://www.bbc.com/sport',
        'politics': 'https://www.bbc.com/news/politics',
        'climate': 'https://www.bbc.com/news/science-environment-56837908',
        'global affairs': 'https://www.bbc.com/news/world',
        'economics': 'https://www.bbc.com/news/business/economy'
    }
}

BBC_SPORT = [
    "football",
    "golf",
    "cricket",
    "disability-sport",
    "rugby-union",
    "american-football",
    "formula1",
    "tennis",
    "athletics",
    "cycling"
]

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/88.0.4324.150 Safari/537.36"}
class Scraper:
    def __init__(self, outlet, topic):
        self.outlet = outlet
        self.topic = topic
        self.headers = HEADER

    def scrape(self):
        # Must first scrape the page and use the cleaned result in the action, where the data is extracted
        soup_content = self.scrape_page()

        # Parse content to be cleaned and investigated per outlet
        outlet_instance = WebsiteMapper(self.outlet, self.topic, soup_content)
        outlet_instance.execute()

    def scrape_page(self) -> str:
        try:
            assert OUTLETS[self.outlet][self.topic] is not None
            response = requests.get(OUTLETS[self.outlet][self.topic], headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                return soup
            else:
                print("Request failed with status code", response.status_code)
        except AssertionError:
            raise AssertionError("OUTLETS[self.outlet][self.topic] should not be None")


class ActionDispatcher(type):
    def __new__(cls, name, bases, attrs):
        actions = {}
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and hasattr(attr_value, "action_name"):
                action_name = getattr(attr_value, "action_name")
                actions[action_name] = attr_value
        attrs["actions"] = actions
        return super().__new__(cls, name, bases, attrs)


class WebsiteMapper(metaclass=ActionDispatcher):
    def __init__(self, action, topic, soup_content):
        self.action = action
        self.topic = topic
        self.content = soup_content

    def execute(self):
        action_function = self.actions.get(self.action)
        if action_function:
            action_function(self)
        else:
            print(f"Unsupported action: {self.action}")

    @staticmethod
    def action_handler(action_name):
        def decorator(func):
            setattr(func, "action_name", action_name)
            return func
        return decorator

    @action_handler("BBC")
    def perform_action1(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = bbc_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = bbc_home_links_politics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            if self.topic == 'sport':
                article_obj = self.bbc_sport(url, article_content)
                if article_obj is not None:
                    if isinstance(article_obj, list):
                        articles = articles + article_obj
                    else:
                        articles.append(article_obj)
            elif self.topic == 'politics':
                article_obj = self.bbc_politics(url, article_content)
                if article_obj is not None:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    @action_handler("action2")
    def perform_action2(self):
        print("Performing action 2")

    @action_handler("action3")
    def perform_action3(self):
        print("Performing action 3")

    def make_request(self, link, base_url=None):
        # Update link grabbing for sport
        if base_url is not None:
            url = urllib.parse.urljoin(base_url, link)
        else:
            url = link

        response = requests.get(url, headers=HEADER)
        article_content = None
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            article_content = soup
        else:
            print("Request failed with status code", response.status_code)

        return article_content, url

    def bbc_sport(self, url, article_content, nested=False):

        article_obj = {}
        # Single recursive layer to check other sport home pages
        if not nested:
            article_rec_array=[]
            # get last route value to see if its a base page
            final_route = url.split('/')[-1]
            if final_route in BBC_SPORT:
                # Make request using full url, provided from parent make_request call
                nested_content, nested_url_base = self.make_request(url)
                nested_links = bbc_home_links_sport_base(self.content, nested_content)
                for nested_link in nested_links:
                    article_content, nested_url = self.make_request(nested_link, url)
                    article_obj = self.bbc_sport(nested_url, article_content, True)
                    if article_obj is not None:
                        article_rec_array.append(article_obj)
                return article_rec_array

        try:
            tag_article = article_content.find('article')
            title = tag_article.find('h1').get_text()
            author = tag_article.find(class_="qa-contributor-name gel-long-primer")
            if author is None:
                author = "BBC - No Explicit Author - " + self.topic
            else:
                author = author.get_text()

            # get text for every child element in article tag
            article_text = []
            # get first div which contains all content
            tag_article_content = tag_article.find('div', recursive=False)
            for child in tag_article_content.children:
                if child.name:
                    article_text.append(child.get_text())
            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None
        return article_obj

    def bbc_politics(self, url, article_content, nested=False):
        article_obj = {}
        try:
            tag_article = article_content.find('article')
            article_text = []
            # get article content and clean
            content = tag_article.find_all(attrs={"data-component": "text-block"})
            for text_block in content:
                text_content = text_block.find('p').get_text()
                article_text.append(text_content)

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

            title = article_content.find('h1').get_text()
            author_container = tag_article.find(attrs={"data-component": "byline-block"})
            author = ""
            if author_container is None:
                print("No author, default BBC politics")
                author = "BBC - No Explicit Author - " + self.topic
            else:
                author = author_container.find(class_="ssrcss-68pt20-Text-TextContributorName e8mq1e96").get_text()

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None
        return article_obj

# Example usage:
# if __name__ == "__main__":
#     my_instance = WebsiteMapper('BBC')  # Replace with the desired action
#     my_instance.execute()
