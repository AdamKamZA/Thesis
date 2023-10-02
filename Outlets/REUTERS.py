def reuters_home_links_sport_base(content):
    links = []
    main_content = content.find(id="main-content").find_all('ul')
    anchors = []
    for ul in main_content:
        anchors = anchors + ul.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))

    links = list(set(links))
    return links

# politics can select several pages for the link, so the request in this function can be for the base page
# then the next 75 to get 750
# TODO: The politics, which requires a different approach


def reuters_home_links_climate_base(content):
    links = []
    main_content = content.find_all('div', attrs={"data-testid": "0"})
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def reuters_home_links_global_affairs_base(content):
    links = []
    main_content = content.find(id="main-content").find_all('ul')
    anchors = []
    for ul in main_content:
        anchors = anchors + ul.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))

    links = list(set(links))
    return links


def reuters_home_links_economics_base(content):
    links = []
    main_content = content.find_all('div', attrs={"data-testid": "0"})
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links

