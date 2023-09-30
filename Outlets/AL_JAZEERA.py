def al_jazeera_home_links_sport_base(content):
    links = []
    featured_content = content.find(class_='featured-articles-list')
    other_content = content.find(id="news-feed-container")
    all_content = [featured_content, other_content]
    for tag in all_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    return links


def al_jazeera_home_links_politics_base(content):
    links = []
    featured_content = content.find(class_='featured-articles-list')
    other_content = content.find(id="news-feed-container")
    all_content = [featured_content, other_content]
    for tag in all_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    return links


# Could be changed to get access to the read more to get more links, as only half loads in requests get
def al_jazeera_home_links_climate_base(content):
    links = []
    featured_content = content.find(class_='featured-articles-list')
    other_content = content.find(id="news-feed-container")
    all_content = [featured_content, other_content]
    for tag in all_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    return links


def al_jazeera_home_links_global_affairs_base(content):
    links = []
    featured_content = content.find(class_='featured-articles-list')
    other_content = content.find(id="news-feed-container")
    all_content = [featured_content, other_content]
    for tag in all_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    return links


def al_jazeera_home_links_economics_base(content):
    links = []
    featured_content = content.find(class_='featured-articles-list')
    other_content = content.find(id="news-feed-container")
    all_content = [featured_content, other_content]
    for tag in all_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    return links


