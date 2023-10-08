def usa_today_home_links_sport_base(content):
    links = []
    main_content = content.find_all('a', class_=['gnt_m_flm_a',  'gnt_m_he', 'gnt_m_tl'])
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def usa_today_home_links_politics_base(content):
    links = []
    main_content = content.find_all('a', class_=['gnt_m_flm_a',  'gnt_m_he', 'gnt_m_tl'])
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def usa_today_home_links_climate_base(content):
    links = []
    main_content = content.find_all('a', class_=['gnt_m_flm_a',  'gnt_m_he', 'gnt_m_tl'])
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def usa_today_home_links_global_affairs_base(content):
    links = []
    main_content = content.find_all('a', class_=['gnt_m_flm_a',  'gnt_m_he', 'gnt_m_tl'])
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links


def usa_today_home_links_economics_base(content):
    links = []
    main_content = content.find_all('a', class_=['gnt_m_flm_a',  'gnt_m_he', 'gnt_m_tl'])
    for tag in main_content:
        links.append(tag.get('href'))
    links = list(set(links))
    return links