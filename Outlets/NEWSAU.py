def news_au_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_='mosaic_mx_column')
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def news_au_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_='l1-s_list')
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def news_au_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_='l1-s_list')
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def news_au_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_='mosaic_mx_column')
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def news_au_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_='mosaic_mx_column')
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links

