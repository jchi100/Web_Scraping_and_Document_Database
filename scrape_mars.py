

from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter.browser import Browser
import time


def scrape():
# Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    result = soup.find('div',class_='content_title')
    news_title= result.find('a').text
    result_p = soup.find('div',class_='image_and_description_container')
    news_p = result_p.find('div',class_='rollover_description_inner').text

    url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    result = soup.find_all('div',class_='js-tweet-text-container')[0]

    mars_weather = result.find('p').contents[0]


    url = "https://space-facts.com/mars/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
# Use Pandas to scrape the table containing facts about the planet including Diameter, Mass
    table = soup.find_all('table')
    df = pd.read_html(str(table))[0]

    df = df.rename(columns={0:'',1:'value'})
    df.set_index('', inplace=True)
    mars_fact_html = df.to_html()

# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres
    
    executable_path = {'executable_path':'/Users/jingc/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
  #  browser = Browser('chrome', headless=True)
  
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)
    hemisphere_image_urls = []

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    results = soup.find_all('div', class_='item')

    for result in results:
        hemisphere = {}
        newurl = 'https://astrogeology.usgs.gov'+ result.find('a')['href']
        browser.visit(newurl)
        new_html = browser.html
        soup = BeautifulSoup(new_html,'html.parser')
        sample = soup.find('div', class_='downloads')
        hemisphere['img_url'] = sample.find('a')['href']
        title = soup.find('h2',class_="title").text
        hemisphere['title'] = title.replace(' Enhanced','')
        hemisphere_image_urls.append(hemisphere)
      
        time.sleep(1)

#Use splinter to navigate the site and find the image url for the current Featured Mars Image 


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
   
    browser.visit(url)
    search_bar_xpath ='//*[@id="full_image"]'
    search_button = browser.find_by_xpath(search_bar_xpath)[0]
    search_button.click()

    time.sleep(2)
    moreinfo_button = browser.find_link_by_partial_text('more info')
    moreinfo_button.click()
    time.sleep(2)
    response = browser.html
    featuredimg_soup = BeautifulSoup(response, 'html.parser')
    featured_img_url = 'https://www.jpl.nasa.gov'+featuredimg_soup.find('figure', class_='lede').a['href']

    browser.quit()

    mars_dict = {'news_title':news_title,
             'news_paragraph': news_p,
             'current_weather':mars_weather,
             'featured_img':featured_img_url,
             'mars_fact':mars_fact_html,
             'hemisphere_images':hemisphere_image_urls
            }
    return mars_dict

