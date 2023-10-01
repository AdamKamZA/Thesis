def yahoo_home_links_sport_base(content):
    links = []
    featured_content = content.select("#LeadLeft-0-SportsNTK-Proxy > div > div")[0].find_all('a')
    extra_content = content.find(id="Aside").find_all('a')
    main_content = featured_content+extra_content
    for anchor in main_content:
        links.append(anchor.get('href'))
    links = list(set(links))
    return links