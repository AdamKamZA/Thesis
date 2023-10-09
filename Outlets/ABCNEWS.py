def abc_news_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_='ContentRoll__Item')

    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def abc_news_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_='ContentRoll__Item')

    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def abc_news_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_='ContentRoll__Item')

    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def abc_news_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_=['LatestHeadlines__item','ContentRoll__Item'])

    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def abc_news_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_='ContentRoll__Item')

    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links