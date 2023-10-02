# contains page query system, can be used to loop and query multiple pages to get a lot more content

def guardian_home_links_sport_base(content):
    links = []
    main_content = content.find('main')
    main_ul = main_content.find_all('ul')

    anchors = []
    for ul in main_ul:
        anchors = anchors + ul.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def guardian_home_links_politics_base(content):
    links = []
    main_content = content.find('main')
    main_ul = main_content.find_all('ul')

    anchors = []
    for ul in main_ul:
        anchors = anchors + ul.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def guardian_home_links_climate_base(content):
    links = []
    main_content = content.find('main')
    main_ul = main_content.find_all('ul')

    anchors = []
    for ul in main_ul:
        anchors = anchors + ul.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def guardian_home_links_global_affairs_base(content):
    links = []
    main_content = content.find(class_='fc-container__inner')
    main_ul = main_content.find_all('ul')

    anchors = []
    for ul in main_ul:
        anchors = anchors + ul.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def guardian_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_='fc-item__container')

    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links

