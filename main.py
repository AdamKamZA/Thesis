from Thesis.Data.DBHandler import Handler
from Scraper import Scraper

def main():
    # Retrieve from database so that we can investigate and train using the saved model
    # handler = Handler()
    # handler.count_author()
    # handler.close()
    scraper = Scraper('NPR', 'economics')
    scraper.scrape()


if __name__ == '__main__':
    main()
