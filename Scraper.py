import requests
from bs4 import BeautifulSoup
import urllib.parse

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
            response = requests.get(OUTLETS[self.outlet][self.topic],headers=self.headers)
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
        main_content = self.content.find('main')
        main_children = main_content.find_all('div', recursive=False)
        article_containers = main_children[3:]
        article_ul = []
        for container in article_containers:
            article_ul.append(container.find('ul'))
        links = []
        for story in article_ul:
            link_list = story.find_all("a")
            if link_list != 0 or link_list is not None:
                links = links + link_list
            else:
                print("None value, skipping")

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        writers = []
        for link in links:
            url = urllib.parse.urljoin(base_url, link.get('href'))
            response = requests.get(url, headers=HEADER)
            article_content = None
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                article_content = soup
            else:
                print("Request failed with status code", response.status_code)

            try:
                tag_article = article_content.find('article')
                header = tag_article.find('header')
                container = header.find('div')
                writer = container.find(class_='qa-contributor-name gel-long-primer')
                writer_content = writer.contents[0][3:]
                writers.append(writer_content)
            except AttributeError:
                print("AttributeError:\nInvalid article structure\nSkipping url: " + url)

        print(writers)

    @action_handler("action2")
    def perform_action2(self):
        print("Performing action 2")

    @action_handler("action3")
    def perform_action3(self):
        print("Performing action 3")


# Example usage:
# if __name__ == "__main__":
#     my_instance = WebsiteMapper('BBC')  # Replace with the desired action
#     my_instance.execute()
