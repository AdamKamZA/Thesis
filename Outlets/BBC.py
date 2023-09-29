def bbc_home_links_sport_base(content, page_content=None):
    main_content = None
    if page_content is None:
        main_content = content.select_one("#main-content > div:nth-child(4) > div > div > ul")
    else:
        main_content = page_content.select_one("#main-content > div:nth-child(4) > div > div > ul")
        # For different structures of sport pages
        if main_content is None:
            main_content = page_content.find('div', class_="sp-c-cluster")
    links = [a.get('href') for a in main_content.find_all("a")]
    return links

def bbc_home_links_politics_base(content):
    # could be different for sport and economics etc. as this uses sport page for testing
    main_content = content.select_one('#topos-component > div.no-mpu > div > div:nth-child(2) > div')
    links = [a.get('href') for a in main_content.find_all("a")]
    return links

def bbc_home_links_climate_base(content):
    main_content = content.find(id="index-page")
    links = [a.get('href') for a in main_content.find_all("a")]
    return links

def bbc_home_links_global_affairs_base(content):
    main_content = content.select_one("#topos-component > div.no-mpu")
    links = [a.get('href') for a in main_content.find_all("a")]
    return links

def bbc_home_links_economics_base(content):
    main_content = content.select_one("#topos-component > div.no-mpu > div > div:nth-child(2)")
    links = [a.get('href') for a in main_content.find_all("a")]
    return links
