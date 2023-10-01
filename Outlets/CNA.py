def cna_home_links_sport_base(content):
    links = []
    main_content = content.find_all('div', class_='list-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def cna_home_links_politics_base(content):
    links = []
    main_content = content.find_all('div', class_='media-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def cna_home_links_climate_base(content):
    links = []
    main_content = content.find_all('div', class_='list-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def cna_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all('div', class_='list-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def cna_home_links_economics_base(content):
    links = []
    main_content = content.find_all('div', class_='list-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links