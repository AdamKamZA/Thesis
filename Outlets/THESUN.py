def the_sun_home_links_sport_base(content):
    links = []
    main_content = content.find('main')
    main_containers = main_content.find_all(class_='sun-grid-container')

    anchors = []
    for container in main_containers:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    links_filtered = [item for item in links if '/betting' not in item]
    links = links_filtered
    return links

# use page/number to advantage to get more
def the_sun_home_links_politics_base(content):
    links = []
    main_content = content.find('main')
    main_containers = main_content.find_all(class_='sun-row')

    anchors = []
    for container in main_containers:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def the_sun_home_links_climate_base(content):
    links = []
    main_content = content.find('main')
    main_containers = main_content.find(class_='grids-container')

    anchors = []
    for container in main_containers:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def the_sun_home_links_global_affairs_base(content):
    links = []
    main_content = content.find('main')
    main_containers = main_content.find_all(class_='sun-row')

    anchors = []
    for container in main_containers:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def the_sun_home_links_economics_base(content):
    links = []
    main_content = content.find('main')
    main_containers = main_content.find_all(class_='sun-row')

    anchors = []
    for container in main_containers:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links