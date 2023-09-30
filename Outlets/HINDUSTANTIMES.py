def hindu_times_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_='cartHolder')
    for tag in main_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    links = list(set(links))
    return links


def hindu_times_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_='cartHolder')
    for tag in main_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    links = list(set(links))
    return links


def hindu_times_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_='cartHolder')
    for tag in main_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    links = list(set(links))
    return links


def hindu_times_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_='cartHolder')
    for tag in main_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    links = list(set(links))
    return links


def hindu_times_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_='cartHolder')
    for tag in main_content:
        links = links + [a.get('href') for a in tag.find_all('a')]
    links = list(set(links))
    return links

