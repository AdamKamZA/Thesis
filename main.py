from Thesis.Data.DBHandler import Handler
from Scraper import Scraper

def main():
    # Retrieve from database so that we can investigate and train using the saved model
    # handler = Handler()
    # handler.count_author()
    # handler.close()
    scraper = Scraper('GUARDIAN', 'economics')
    scraper.scrape()


# I think in the nested part, I am still just making a normal request to the same home page and not going into each link
if __name__ == '__main__':
    main()
