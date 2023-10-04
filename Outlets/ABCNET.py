def abc_net_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_='CardLayout_content__bev76')
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def abc_net_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_='CardLayout_content__bev76')
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def abc_net_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_='CardLayout_content__bev76')
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def abc_net_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_='CardLayout_content__bev76')
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def abc_net_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_='CardLayout_content__bev76')
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links