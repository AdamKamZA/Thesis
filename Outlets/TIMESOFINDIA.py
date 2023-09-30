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
    return links


def times_of_india_home_links_politics_base(content):
    links = []
    main_content = content.find(class_='top-newslist').find_all('li')
    for tag in main_content:
        links = links + [tag.find('a').get('href')]
    return links

