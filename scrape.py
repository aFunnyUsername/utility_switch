from bs4 import BeautifulSoup
from splinter import Browser
import re


def get_browser():
    exe_path = {'executable_path': 'chromedriver.exe'}
    #NOTE change headless to True for production
    browser = Browser('chrome', **exe_path, headless=False)
    return browser


def scrape_pluginillinois():
    browser = get_browser() 
    browser.visit("https://www.pluginillinois.org/OffersBegin.aspx")
    results = browser.html
    soup = BeautifulSoup(results, 'html.parser')

    """
    options = [i.findAll('option') for i in soup.findAll(
        'select', 
        attrs={'name':'ctl00$ctl00$ctl00$ctl00$MasterContent$MasterContent$RightColumn$RightColumn$UtilityServiceTerritoryList'})]
   """ 
     
    dropdown = soup.find('select', attrs={'name':'ctl00$ctl00$ctl00$ctl00$MasterContent$MasterContent$RightColumn$RightColumn$UtilityServiceTerritoryList'})
    options_full = dropdown.findAll('option') 
    
    options = []
    for option in options_full:
        options.append(option.get_text())

    all_suppliers = [] 
    for i in range(len(options)):
        element = browser.find_by_id('MasterContent_MasterContent_RightColumn_RightColumn_UtilityServiceTerritoryList').first
        element.select(i+1)
        button = browser.find_by_xpath('//*[@id="MasterContent_MasterContent_RightColumn_RightColumn_SubmitButton"]')
        button.click()
        results = browser.html
        browser.back()

        soup = BeautifulSoup(results, 'html.parser')
        #NOTE, this is Zohaibs code, need to understand more of what is going on here
        results_raw = soup.find('table', class_='DataTable').find_all('img')
        suppliers1 = re.findall(r'src=\"/images/(.*?).jpg\"', str(results_raw))
        results2_raw = soup.find('table', class_='DataTable').find_all('img')
        suppliers2 = re.findall(r'alt=\"(.*?)\"', str(results2_raw))

        suppliers = suppliers1 + suppliers2

        all_suppliers.append(suppliers)

    browser.quit()

    suppliers_by_region = {}
    for i in range(len(options)):
        suppliers_by_region[options[i]] = all_suppliers[i]

    return suppliers_by_region 






