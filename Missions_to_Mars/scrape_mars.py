from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import html
import json
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

#***********************************************************************
def NASA_Mars_News():
    browser = init_browser()

    # Visit: mars.nasa.gov
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(3)

    # Extract HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Latest new title:
    news_title = soup.find_all(class_ = "content_title")
    news_title = news_title[1].text

    # Latest new paragraph:
    news_p = soup.find_all(class_ = "article_teaser_body")
    news_p = news_p[0].text

    # Store data in a dictionary
    Latest_New = {
        'news_title': news_title,
        'news_p': news_p
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return Latest_New

#***********************************************************************
def featured_image():
    browser = init_browser()

    # Visit: www.jpl.nasa.gov
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(3)

    # Extract HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Latest Space Image:
    image = soup.find(class_ = 'button fancybox').get_attribute_list('data-fancybox-href')
    image = image[0]

    # Lastest space image URL: 
    base_url = 'https://www.jpl.nasa.gov'
    featured_image_url = base_url + image

    # Store data in a dictionary
    featured_image = {
        'image': featured_image_url
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return featured_image

#***********************************************************************
def mars_weather():
    browser = init_browser()

    # Visit: twitter.com
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(5)

    # Extract HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Latest Weather:
    weather = soup.find_all(class_ = "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    weather = weather[27].text
    weather = weather.replace('\n', ' ')
    weather = weather.replace('InSight ', '')

    # Store data in a dictionary
    mars_weather = {
        'weather': weather
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_weather

#***********************************************************************
def mars_facts():
    browser = init_browser()

    # Visit: space-facts.com
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    time.sleep(3)

    # Extract HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Facts:
    facts = soup.find_all(class_ ="tablepress tablepress-id-p-mars")
    description = []
    value = []

    for fact in facts[0].tbody.find_all("tr"):
        description.append(fact.find_all("td")[0].text)
        value.append(fact.find_all("td")[1].text)

    # Results:
    # Data Frame
    Facts_DF = pd.DataFrame({ "Description": description, "Value": value })
    
    # Facts to HTML:
    Facts_HTML = Facts_DF.to_html(index = False)

    # Store data in a dictionary
    mars_facts = {
        'facts': Facts_HTML
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_facts

#***********************************************************************
def mars_hemispheres():
    browser = init_browser()

    # Visit: strogeology.usgs.gov
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    time.sleep(3)

    # Extract HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Hemispheres:
    hemispheres = soup.find(class_ = "collapsible results")
    List = []
    for hemisphere in hemispheres:
        List.append(hemisphere.find("a"))

    # Extract href's:
    urls = []
    for element in List[1:5]:
        urls.append(element.get_attribute_list('href')[0])

    # Extract image 1 from 4
    # Activate Browser
    url1 = 'https://astrogeology.usgs.gov'
    url = url1 + urls[0]
    browser.visit(url)
    time.sleep(3)
    # Extract elements from HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hem_title_1 = soup.find(class_ = "title").text
    hem_img_1 = soup.find(target = "_blank").get_attribute_list('href')

    # Extract image 2 from 4
    # Activate Browser
    url1 = 'https://astrogeology.usgs.gov'
    url = url1 + urls[1]
    browser.visit(url)
    time.sleep(3)
    # Extract elements from HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hem_title_2 = soup.find(class_ = "title").text
    hem_img_2 = soup.find(target = "_blank").get_attribute_list('href')

    # Extract image 3 from 4
    # Activate Browser
    url1 = 'https://astrogeology.usgs.gov'
    url = url1 + urls[2]
    browser.visit(url)
    time.sleep(3)
    # Extract elements from HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hem_title_3 = soup.find(class_ = "title").text
    hem_img_3 = soup.find(target = "_blank").get_attribute_list('href')

    # Extract image 4 from 4
    # Activate Browser
    url1 = 'https://astrogeology.usgs.gov'
    url = url1 + urls[3]
    browser.visit(url)
    time.sleep(3)
    # Extract elements from HTML
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hem_title_4 = soup.find(class_ = "title").text
    hem_img_4 = soup.find(target = "_blank").get_attribute_list('href')

    # Store data in a dictionary

    #mars_hemispheres = [
    #    {"title": hem_title_1, "img_url": hem_img_1[0]},
    #    {"title": hem_title_2, "img_url": hem_img_2[0]},
    #    {"title": hem_title_3, "img_url": hem_img_3[0]},
    #    {"title": hem_title_4, "img_url": hem_img_4[0]}
    #    ]
    mars_hemispheres = {
        'title_1': hem_title_1,
        'url_1': hem_img_1[0],
        'title_2': hem_title_2,
        'url_2': hem_img_2[0],
        'title_3': hem_title_3,
        'url_3': hem_img_3[0],
        'title_4': hem_title_4,
        'url_4': hem_img_4[0],
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_hemispheres

#