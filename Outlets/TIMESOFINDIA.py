def times_of_india_home_links_sport_base(content):
    links = []
    # main_content = content.find_all('div', attrs={'data-type':'in_view'})
    main_content = content.find_all(class_='iN5CR')
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')
    href = []
    for anchor in anchors:
        href.append(anchor.get('href'))

    # ignore the links that contain photostory, videoshow
    links_filtered = [item for item in href if 'photostory' not in item and 'videoshow' not in item]
    links = links_filtered
    links = list(set(links))
    return links


def times_of_india_home_links_politics_base(content):
    links = []
    main_content = content.find(class_='top-newslist').find_all('li')
    for tag in main_content:
        links = links + [tag.find('a').get('href')]
    links = list(set(links))
    return links


def times_of_india_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_='uwU81')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def times_of_india_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_='uwU81')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def times_of_india_home_links_economics_base(content):
    links = []
    main_content_top = content.find(class_='top-newslist').find_all('li')
    main_content_extra = content.find(class_='list5 clearfix').find_all('li')
    main_content = main_content_top + main_content_extra
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links