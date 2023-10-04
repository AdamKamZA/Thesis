def nine_news_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_="story-block story-block--has-media")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    links = [link for link in links if "/pictures-of-the-week" not in link and "//wwos.nine.au" not in link]
    return links


def nine_news_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_="story-block story-block--has-media")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def nine_news_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_="story-block story-block--has-media")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def nine_news_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_="story-block story-block--has-media")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def nine_news_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_="story-block story-block--has-media")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links