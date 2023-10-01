def cnn_home_links_sport_base(content):
    links = []
    main_content = content.find_all(class_="stack")
    anchors = []
    for stack in main_content:
        anchors = anchors + stack.find_all('a')

    for tag in anchors:
        links.append(tag.get('href'))

    links = list(set(links))
    return links


def cnn_home_links_politics_base(content):
    links = []
    main_content = content.find_all(class_="stack")
    anchors = []
    for stack in main_content:
        anchors = anchors + stack.find_all('a')

    for tag in anchors:
        links.append(tag.get('href'))

    links = list(set(links))
    return links


def cnn_home_links_climate_base(content):
    links = []
    featured_content = content.find(class_="container__field-links container_lead-plus-headlines-with-images__field-links").\
        find_all('div', recursive=False)
    second_content = content.find_all(class_="stack")
    main_content = featured_content + second_content
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')

    for tag in anchors:
        links.append(tag.get('href'))

    links = list(set(links))
    return links


def cnn_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all(class_="stack")
    anchors = []
    for stack in main_content:
        anchors = anchors + stack.find_all('a')

    for tag in anchors:
        links.append(tag.get('href'))

    links = list(set(links))
    return links


def cnn_home_links_economics_base(content):
    links = []
    featured_content = content.find(
        class_="container__field-links container_lead-plus-headlines-with-images__field-links"). \
        find_all('div', recursive=False)
    second_content = content.find_all(class_="stack")
    main_content = featured_content + second_content
    anchors = []
    for tag in main_content:
        anchors = anchors + tag.find_all('a')

    for tag in anchors:
        links.append(tag.get('href'))

    links = list(set(links))
    return links

