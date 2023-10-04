def abc_net_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_='Featured_containerCard__RBQLn')
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links

