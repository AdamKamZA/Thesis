import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
from Outlets.BBC import bbc_home_links_sport_base, bbc_home_links_politics_base, bbc_home_links_climate_base, \
    bbc_home_links_global_affairs_base, bbc_home_links_economics_base
from Outlets.NEWS24 import news24_home_links_sport_base, news24_home_links_politics_base, news24_content, \
    news24_home_links_climate_base, news24_home_links_global_affairs_base, news24_home_links_economics_base
from Outlets.AL_JAZEERA import al_jazeera_home_links_sport_base, al_jazeera_home_links_politics_base, \
    al_jazeera_home_links_climate_base, al_jazeera_home_links_global_affairs_base, al_jazeera_home_links_economics_base
from Outlets.HINDUSTANTIMES import hindu_times_home_links_sport_base, hindu_times_home_links_politics_base, \
    hindu_times_home_links_climate_base, hindu_times_home_links_global_affairs_base, \
    hindu_times_home_links_economics_base
from Outlets.TIMESOFINDIA import times_of_india_home_links_sport_base, times_of_india_home_links_politics_base, \
    times_of_india_home_links_climate_base, times_of_india_home_links_global_affairs_base, \
    times_of_india_home_links_economics_base
from Outlets.CNA import cna_home_links_sport_base, cna_home_links_politics_base, cna_home_links_climate_base, \
    cna_home_links_global_affairs_base, cna_home_links_economics_base
from Outlets.CNN import cnn_home_links_sport_base, cnn_home_links_politics_base, cnn_home_links_climate_base, \
    cnn_home_links_global_affairs_base, cnn_home_links_economics_base
from Outlets.YAHOO import yahoo_home_links_sport_base, yahoo_home_links_politics_base, yahoo_home_links_climate_base, \
    yahoo_home_links_global_affairs_base, yahoo_home_links_economics_base

OUTLETS = {
    'BBC': {
        'sport': 'https://www.bbc.com/sport',
        'politics': 'https://www.bbc.com/news/politics',
        'climate': 'https://www.bbc.com/news/science-environment-56837908',
        'global affairs': 'https://www.bbc.com/news/world',
        'economics': 'https://www.bbc.com/news/business/economy'
    },
    'NEWS24': {
        'sport': 'https://www.news24.com/sport',
        'politics': 'https://www.news24.com/news24/politics',
        'climate': 'https://www.news24.com/fin24/climate_future',
        'global affairs': 'https://www.news24.com/news24/world',
        'economics': 'https://www.news24.com/fin24/economy'
    },
    'ALJAZEERA': {
        'sport': 'https://www.aljazeera.com/sports/',
        'politics': 'https://www.aljazeera.com/tag/politics/',
        'climate': 'https://www.aljazeera.com/climate-crisis/',
        'global affairs': 'https://www.aljazeera.com/news/',
        'economics': 'https://www.aljazeera.com/economy/'
    },
    'HINDUSTANTIMES': {
        'sport': 'https://www.hindustantimes.com/sports',
        'politics': 'https://www.hindustantimes.com/topic/politics/news',
        'climate': 'https://www.hindustantimes.com/topic/climate-change/news',
        'global affairs': 'https://www.hindustantimes.com/world-news',
        'economics': 'https://www.hindustantimes.com/topic/economy/news'
    },
    "TIMESOFINDIA": {
        'sport': 'https://timesofindia.indiatimes.com/sports',
        'politics': 'https://timesofindia.indiatimes.com/politics/news',
        'climate': 'https://timesofindia.indiatimes.com/topic/climate-change/news',
        'global affairs': 'https://timesofindia.indiatimes.com/topic/world-affairs/news',
        'economics': 'https://timesofindia.indiatimes.com/business/economy'
    },
    "CNA": {
        'sport': 'https://www.channelnewsasia.com/sport',
        'politics': 'https://www.channelnewsasia.com/topic/politics',
        'climate': 'https://www.channelnewsasia.com/sustainability',
        'global affairs': 'https://www.channelnewsasia.com/world',
        'economics': 'https://www.channelnewsasia.com/business'
    },
    "CNN": {
        'sport': 'https://edition.cnn.com/sport',
        'politics': 'https://edition.cnn.com/politics',
        'climate': 'https://edition.cnn.com/world/cnn-climate',
        'global affairs': 'https://edition.cnn.com/world',
        'economics': 'https://edition.cnn.com/business'
    },
    "YAHOO": {
        'sport': 'https://sports.yahoo.com/',
        'politics': 'https://news.yahoo.com/politics/',
        'climate': 'https://www.yahoo.com/tagged/climate-change',
        'global affairs': 'https://news.yahoo.com/world/',
        'economics': 'https://finance.yahoo.com/news/'
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

    def scrape_page(self) -> BeautifulSoup:
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

    @action_handler("actionNameHere")
    def perform_actionNumberHere(self):
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

    # region Yahoo

    @action_handler("YAHOO")
    def perform_action8(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = yahoo_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = yahoo_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = yahoo_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = yahoo_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = yahoo_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.yahoo_sport(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def yahoo_sport(self, url, article_content):
        article_obj = {}
        try:
            article_tag = article_content.find('article')
            title = article_tag.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            author = article_tag.find(class_='caas-author-byline-collapse')
            if author is None:
                author = "CNN - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())
            # Getting first simple date and its last child - this is the better date format
            time = article_tag.find('time').get_text()
            time = re.sub(r'\s+', ' ', time.strip())

            content_container = article_tag.find(class_="caas-body")
            article_text = []
            for child in content_container.children:
                if child.name == 'p' or child.name == 'h2':
                    article_text.append(child.get_text())

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text.strip())

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion


    # region The Washington Post
    @action_handler("CNN")
    def peform_action7(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = cnn_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = cnn_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = cnn_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = cnn_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = cnn_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.cnn_all(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def cnn_all(self, url, article_content):
        article_obj = {}
        try:
            title = article_content.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            author = article_content.find(class_='byline__names')
            if author is None:
                author = "CNN - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())
            # Getting first simple date and its last child - this is the better date format
            time = article_content.find(class_='timestamp').get_text()
            time = re.sub(r'\s+', ' ', time.strip())

            content = article_content.find_all(class_="paragraph inline-placeholder")
            article_text = []
            for tag in content:
                article_text.append(tag.get_text())

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text.strip())

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion

    # region Channel News Asia

    @action_handler("CNA")
    def perform_action6(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = cna_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = cna_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = cna_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = cna_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = cna_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.cna_all(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def cna_all(self, url, article_content):
        article_obj = {}
        try:
            title = article_content.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            author = article_content.find(class_='h6 h6--author-name')
            if author is None:
                author = "CNA - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())
            # Getting first simple date and its last child - this is the better date format
            time = article_content.select_one('.article-publish.article-publish--').get_text()
            time = re.sub(r'\s+', ' ', time.strip())

            content = article_content.find_all(class_="text")
            text_blocks = []
            for tag in content:
                text_blocks = text_blocks + tag.find_all('p')

            article_text = []
            for block in text_blocks:
                article_text.append(block.get_text())

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text.strip())

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion

    # region Times of India

    @action_handler("TIMESOFINDIA")
    def perform_action5(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = times_of_india_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = times_of_india_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = times_of_india_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = times_of_india_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = times_of_india_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.times_india_all(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def times_india_all(self, url, article_content):
        article_obj = {}
        try:
            title = article_content.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            header_content = article_content.find(class_="xf8Pm byline")
            author = header_content.find('a')
            if author is None:
                author = "TIMESOFINDIA - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())
            # Getting first simple date and its last child - this is the better date format
            time = header_content.find('span').get_text()

            article_with_extras = article_content.find('div', attrs={'data-articlebody': '1'}). \
                find_all('div', recursive=False)[-1]
            divs_to_remove = article_with_extras.find_all('div')

            # Loop through the divs and extract each one
            for div in divs_to_remove:
                div.extract()
            article_text = article_with_extras.get_text()
            article_text = re.sub(r'\s+', ' ', article_text)

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion

    # region Hindustan Times

    @action_handler("HINDUSTANTIMES")
    def perform_action4(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = hindu_times_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = hindu_times_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = hindu_times_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = hindu_times_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = hindu_times_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.hindu_times_all(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def hindu_times_all(self, url, article_content):
        article_obj = {}
        try:
            title = article_content.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            author = article_content.find(class_="storyBy")
            if author is None:
                author = "HINDUSTANTIMES - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())

            # Getting first simple date and its last child - this is the better date format
            time = article_content.find(class_="dateTime secTime storyPage").get_text()

            contents = article_content.find(class_='detail').find_all('p')

            article_text = []
            for tag in contents:
                text = tag.get_text()
                article_text.append(text)

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion

    # region Al Jazeera

    @action_handler("ALJAZEERA")
    def perform_action3(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = al_jazeera_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = al_jazeera_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = al_jazeera_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = al_jazeera_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = al_jazeera_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.al_jazeera_all(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def al_jazeera_all(self, url, article_content):
        article_obj = {}
        try:
            title = article_content.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            author = article_content.find(class_="article-author-name-item")
            if author is None:
                author = "ALJAZEERA - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())

            # Getting first simple date and its last child - this is the better date format
            time = article_content.find(class_="date-simple").find_all('span')[-1].get_text()

            # getting article div in cleaner method, last is always the sources and then the p containers of text
            contents = article_content.find('main').find_all('div', recursive=False)[-2].find_all('p', recursive=False)
            if not contents:
                contents = article_content.find('main').find_all('div', recursive=False)[-2].find_all('p')

            # print("TITLE -- ", title)
            # print(contents)
            article_text = []
            for tag in contents:
                text = tag.get_text()
                article_text.append(text)

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion

    # region NEWS24

    @action_handler("NEWS24")
    def perform_action2(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = news24_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = news24_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = news24_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = news24_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = news24_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            article_obj = self.news24_all(url, article_content)
            if article_obj is not None and len(article_obj['content']) > 0:
                if isinstance(article_obj, list):
                    articles = articles + article_obj
                else:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def news24_all(self, url, article_content):
        article_obj = {}
        try:
            is_locked = True if article_content.find(class_="article__prime") is not None else False
            if is_locked:
                print("Premium article, skipping: ", url)
                return None

            title = article_content.find('h1').get_text()
            title = re.sub(r'\s+', ' ', title.strip())
            author = article_content.find(class_="article__author")
            if author is None:
                author = "NEWS24 - No Explicit Author - " + self.topic
            else:
                author = author.get_text()
                author = re.sub(r'\s+', ' ', author.strip())

            # TODO Convert time to date function
            time = article_content.find(class_="article__date").get_text()

            contents = news24_content(article_content)
            # print(content)
            article_text = []
            for tag in contents:
                text = tag.get_text()
                article_text.append(text)

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    # endregion

    # region BBC

    @action_handler("BBC")
    def perform_action1(self):
        articles = []
        links = []
        if self.topic == 'sport':
            links = bbc_home_links_sport_base(self.content)
        if self.topic == 'politics':
            links = bbc_home_links_politics_base(self.content)
        if self.topic == 'climate':
            links = bbc_home_links_climate_base(self.content)
        if self.topic == 'global affairs':
            links = bbc_home_links_global_affairs_base(self.content)
        if self.topic == 'economics':
            links = bbc_home_links_economics_base(self.content)

        # make request to each link and scrape and save content
        base_url = OUTLETS[self.action][self.topic]
        for link in links:
            article_content, url = self.make_request(link, base_url)
            if self.topic == 'sport':
                article_obj = self.bbc_sport(url, article_content)
                if article_obj is not None and len(article_obj['content']) > 0:
                    if isinstance(article_obj, list):
                        articles = articles + article_obj
                    else:
                        articles.append(article_obj)
            elif self.topic in ['politics', 'climate', 'global affairs', 'economics']:
                article_obj = self.bbc_politics_climate_affairs(url, article_content)
                if article_obj is not None and len(article_obj['content']) > 0:
                    articles.append(article_obj)

        print(articles[0:10])
        print(len(articles))

    def bbc_sport(self, url, article_content, nested=False):
        article_obj = {}
        # Single recursive layer to check other sport home pages
        if not nested:
            article_rec_array = []
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
            time = article_content.find('time').get('datetime')
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
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None

        return article_obj

    def bbc_politics_climate_affairs(self, url, article_content):
        article_obj = {}
        try:
            tag_article = article_content.find('article')

            title = article_content.find('h1').get_text()
            author_container = tag_article.find(attrs={"data-component": "byline-block"})
            author = ""
            if author_container is None:
                print(f"No author, default BBC {self.topic}")
                author = "BBC - No Explicit Author - " + self.topic
            else:
                author = author_container.find(class_="ssrcss-68pt20-Text-TextContributorName e8mq1e96").get_text()

            time = article_content.find('time').get('datetime')

            article_text = []
            # get article content and clean
            content = tag_article.find_all(attrs={"data-component": "text-block"})
            for text_block in content:
                text_content = text_block.find('p').get_text()
                article_text.append(text_content)

            article_text = " ".join(article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

            article_obj = {
                'title': title,
                'writer': author,
                'content': article_text,
                'publish_time': time,
                'link': url
            }

        except AttributeError:
            print("AttributeError:\nInvalid article structure\nSkipping url: " + url)
            return None
        except IndexError:
            print("IndexError: Most likely invalid article structure\nSkipping url: " + url)
            return None
        return article_obj

    # endregion
