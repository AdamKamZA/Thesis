def sky_news_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_="sdc-site-tiles__item sdc-site-tile glints-box glints-box-hover glints-box"
                                           "--mobile-edge sdc-site-tile--has-link")
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def sky_news_sport_sub_links(content):
    links = []
    main_content_1 = content.find(class_="news-top-story block")
    main_content_2 = content.find(class_="grid news-list-featured block")
    main_content_3 = content.find(class_="news-list block")
    main_content = [main_content_1, main_content_2, main_content_3]
    if main_content_1 is None and main_content_2 is None and main_content_3 is None:
        main_content = content.find_all(class_="sdc-site-tiles__item sdc-site-tile glints-box glints-box-hover "
                                               "glints-box--mobile-edge sdc-site-tile--has-link")
    anchors = []
    for container in main_content:
        anchors = anchors + container.find_all('a')
    for anchor in anchors:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links


def sky_news_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_="sdc-site-tiles__item sdc-site-tile glints-box glints-box-hover glints-box"
                                           "--mobile-edge sdc-site-tile--has-link")
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def sky_news_home_links_climate_base(content):
    links = []
    main_content = content.find_all(class_="sdc-site-tiles__item sdc-site-tile glints-box glints-box-hover glints-box"
                                           "--mobile-edge sdc-site-tile--has-link")
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def sky_news_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_="sdc-site-tiles__item sdc-site-tile glints-box glints-box-hover glints-box"
                                           "--mobile-edge sdc-site-tile--has-link")
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links


def sky_news_home_links_economics_base(content):
    links = []
    main_content = content.find_all(class_="sdc-site-tiles__item sdc-site-tile glints-box glints-box-hover glints-box"
                                           "--mobile-edge sdc-site-tile--has-link")
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    links = list(set(links))
    return links