def cna_home_links_sport_base(content):
    links = []
    main_content = content.find_all('div', class_='list-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    return links


def cna_home_links_politics_base(content):
    links = []
    main_content = content.find_all('div', class_='list-object')
    for tag in main_content:
        links.append(tag.find('a').get('href'))
    return links

