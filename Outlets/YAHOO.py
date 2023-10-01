def yahoo_home_links_sport_base(content):
    links = []
    featured_content = content.select("#LeadLeft-0-SportsNTK-Proxy > div > div")[0].find_all('a')
    extra_content = content.find(id="Aside").find_all('a')
    main_content = featured_content+extra_content
    for anchor in main_content:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def yahoo_home_links_politics_base(content):
    links = []
    main_content = content.find_all('ul', attrs={"data-test-locator": "stream-items"})[0]
    anchors = main_content.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def yahoo_home_links_climate_base(content):
    links = []
    main_content = content.find(id="stream-wrapper").find_all('ul', recursive=False)
    anchors = []
    for list_item in main_content:
        anchors = anchors + list_item.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def yahoo_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all('ul', attrs={"data-test-locator": "stream-items"})[0]
    anchors = main_content.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def yahoo_home_links_economics_base(content):
    links = []
    main_content = content.find_all('li', class_="js-stream-content")
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')

    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links