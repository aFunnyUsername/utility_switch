import scrape
import mongo_manager


def scrape_page(page):
    if page == 'pluginillinois': 
        data_by_region = scrape.scrape_pluginillinois()
    return data_by_region 

def insert_scraped_data(data):
    mongo_manager.to_mongo(data)


#insert_scraped_data(scrape_page('pluginillinois'))

insert_scraped_data(scrape_page('pluginillinois'))



