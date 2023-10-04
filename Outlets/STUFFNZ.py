def stuff_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_="display-asset")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def stuff_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_="display-asset main_article display-thumb reorder-disabled")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def stuff_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_="display-asset main_article display-thumb reorder-disabled")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def stuff_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_="display-asset")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links


def stuff_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_="display-asset main_article display-thumb reorder-disabled")
    for article in main_content:
        links.append(article.find('a').get('href'))
    links = list(set(links))
    return links

