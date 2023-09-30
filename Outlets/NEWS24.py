def news24_home_links_sport_base(content):
    main_content = content.find('encapsulate')
    links = [a.get('href') for a in main_content.find_all('a')]
    return links