def msn_home_links_sport_base(content):
    links = []
    print(content)
    main_content = content.find_all('msft-article-card')
    # anchors = []
    # for tag in main_content:
    #     anchors = anchors + tag.find_all('a')
    # for anchor in anchors:
    #     links.append(anchor.get('href'))
    #
    # links = list(set(links))
    # links = [link for link in links if "/authors" not in link]
    print(main_content)
    return []


def msn_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_="article-list__list")
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))

    links = list(set(links))
    links = [link for link in links if "/authors" not in link]
    return links


def msn_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_="article-list__list")
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))

    links = list(set(links))
    links = [link for link in links if "/authors" not in link]
    return links


def msn_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_="article-list__list")
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))

    links = list(set(links))
    links = [link for link in links if "/authors" not in link]
    return links


def msn_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_="article-list__list")
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))

    links = list(set(links))
    links = [link for link in links if "/authors" not in link]
    return links