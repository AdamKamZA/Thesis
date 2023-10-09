def cbs_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_=['article-list-content-block', 'article-list-marquee-item',
                                            'article-list-stack-item'])
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def cbs_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_='item__anchor')
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def cbs_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_='item__anchor')
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def cbs_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_='item__anchor')
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def cbs_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_='item__anchor')
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links

