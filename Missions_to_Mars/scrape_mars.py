import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    # Opening the browser
    browser = init_browser()

    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(10)
    html = browser.html
    news_soup = bs(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')
    news_title = slide_elem.find('div', class_='content_title').text
    news_p = slide_elem.find('div', class_='article_teaser_body').text

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(15)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    more_info_element = browser.links.find_by_partial_text('more info')
    more_info_element.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel = img_soup.select_one('figure.lede a img').get('src')
    featured_image_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(10)
    mars_pic1 = browser.links.find_by_partial_text('Cerberus')
    mars_pic1.click()
    mars_pic1o = browser.links.find_by_partial_text('Open')
    mars_pic1o.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    img1_title = img_soup.find("h2", class_="title").text
    img1_url = img_soup.find("li").a['href']

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(10)
    mars_pic2 = browser.links.find_by_partial_text('Schiaparelli')
    mars_pic2.click()
    mars_pic2o = browser.links.find_by_partial_text('Open')
    mars_pic2o.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    img2_title = img_soup.find("h2", class_="title").text
    img2_url = img_soup.find("li").a['href']
    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(10)
    mars_pic3 = browser.links.find_by_partial_text('Syrtis')
    mars_pic3.click()
    mars_pic3o = browser.links.find_by_partial_text('Open')
    mars_pic3o.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    img3_title = img_soup.find("h2", class_="title").text
    img3_url = img_soup.find("li").a['href']

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(10)
    mars_pic4 = browser.links.find_by_partial_text('Valles')
    mars_pic4.click()
    mars_pic4o = browser.links.find_by_partial_text('Open')
    mars_pic4o.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    img4_title = img_soup.find("h2", class_="title").text
    img4_url = img_soup.find("li").a['href']

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(10)
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Planet Profile:', 'Mars (The Red Planet)']
    df.set_index('Planet Profile:', inplace=True)
    html_table_n = df.to_html()
    html_table = html_table_n.replace('\n', '')

    # Storing data in my dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "img1_title": img1_title,
        "img1_url": img1_url,
        "img2_title": img2_title,
        "img2_url": img2_url,
        "img3_title":img3_title,
        "img3_url": img3_url,
        "img4_title": img4_title,
        "img4_url": img4_url,
        "html_table": html_table,
    }

    # Closing the browser after scraping
    browser.quit()

    # Return results
    return mars_data
