import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    news_soup = bs(html, 'html.parser')

    slide_elem = news_soup.select_one('ul.item_list li.slide')

    news_title = slide_elem.find('div', class_='content_title').text

    news_p = slide_elem.find('div', class_='article_teaser_body').text

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    more_info_element = browser.links.find_by_partial_text('more info')
    more_info_element.click()

    html = browser.html
    img_soup = bs(html, 'html.parser')

    img_url_rel = img_soup.select_one('figure.lede a img').get('src')

    featured_image_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
