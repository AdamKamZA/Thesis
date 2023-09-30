def news24_content(content):
    return content.find(class_="article__body NewsArticle").find_all(['strong', 'p'])

def news24_home_links_sport_base(content):
    main_content = content.find('encapsulate')
    links = [a.get('href') for a in main_content.find_all('a')]
    return links

def news24_home_links_politics_base(content):
    main_content = content.find(class_='tf-lhs-col')
    links = [a.get('href') for a in main_content.find_all('a')]
    return links

def news24_home_links_climate_base(content):
    main_content = content.find(class_='tf-lhs-col')
    links = [a.get('href') for a in main_content.find_all('a')]
    return links

def news24_home_links_global_affairs_base(content):
    main_content = content.find(class_='tf-lhs-col')
    links = [a.get('href') for a in main_content.find_all('a')]
    return links

def news24_home_links_economics_base(content):
    main_content = content.find(class_='tf-lhs-col')
    links = [a.get('href') for a in main_content.find_all('a')]
    return links

