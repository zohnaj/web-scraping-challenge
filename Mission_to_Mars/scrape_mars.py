from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time 

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser=init_browser()

    #NASA Mars News 
    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    news_title=soup.find('div', class_='content_title').text
    news_para=soup.find('div', class_='article_teaser_body')


    #JPL Mars Space Images-Featured Image 
    url_image= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    button_fi=browser.find_by_id('full_image')
    button_fi.click()

    browser.is_element_present_by_text('more info', wait_time=1)
    image_url=browser.find_link_by_partial_text('more info')
    image_url.click()


    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    image_url=soup.select_one('figure.lede a img').get('src')
    image_url

    featured_image_url='https://www.jpl.nasa.gov/'+image_url


    #Mars Weather 
    url_weather='https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)

    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    mars_weather=soup.find('div', 'tweet', class_= 'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')

    #Mars Facts 
    url_facts='https://space-facts.com/mars/'
    tables=pd.read_html(url_facts)
    facts_df=tables[0]

    facts_html_table = facts_df.to_html()
    facts_html_table.replace('\n', '')


    #Mars Hemispheres
    url_hemisphere_cerberus= 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_hemisphere_cerberus)

    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    cerberus_hemisphere_url=soup.find('div', class_= 'downloads')
    cerberus_link=cerberus_hemisphere_url.find('a')
    cerberus_final_link=cerberus_link['href']


    url_hemisphere_schiaparelli= 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_hemisphere_schiaparelli)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    schiaparelli_hemisphere_url=soup.find('div', class_= 'downloads')
    schiaparelli_link=schiaparelli_hemisphere_url.find('a')
    schiaparelli_final_link=schiaparelli_link['href']


    url_hemisphere_syrtis= 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_hemisphere_syrtis)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    syrtis_hemisphere_url=soup.find('div', class_= 'downloads')
    syrtis_link=syrtis_hemisphere_url.find('a')
    syrtis_final_link=syrtis_link['href']


    url_hemisphere_valles= 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_hemisphere_valles)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    valles_hemisphere_url=soup.find('div', class_= 'downloads')
    valles_link=valles_hemisphere_url.find('a')
    valles_final_link=valles_link['href']


    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": cerberus_final_link},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_final_link},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": syrtis_final_link},
        {"title": "Valles Marineris Hemisphere", "img_url": valles_final_link},
    ]


    mars_results={
        "news_title": news_title,
        "news_paragraph": news_para,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": facts_html_table,
        "hemisphere_images": hemisphere_image_urls
        }

    browser.quit()

    return mars_results