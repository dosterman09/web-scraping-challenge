#!/usr/bin/env python
# coding: utf-8

# Scraping Mars!

# In[1]:


import pandas as pd
import datetime as dt
from flask import Flask
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():

#create empty dictionary 
mars_info_dict = {}

# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Mars News

# In[3]:


#Nasa Mars News Site
url = "https://redplanetscience.com/"
browser.visit(url)


# In[4]:


#Scrape using BeautifulSoup
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')


# In[5]:


#Retrieve Title and News Paragraph

article = news_soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text
print(news_title)
print(news_p)
#add to dict
mars_info_dict['news_title'] = news_title


# Mars Space Image

# In[6]:


mars_image_url = 'https://spaceimages-mars.com/'
browser.visit(mars_image_url)


# In[7]:


#Scrape using BeautifulSoup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')


# In[8]:


image_soup = image_soup.find('img', class_='headerimage')['src']
mars_image_url = f'https://spaceimages-mars.com/{mars_image_url}'
mars_image_url
print(mars_image_url)
#add dict
mars_info_dict['mars_image_url'] = mars_image_url


# Mars Facts

# In[9]:


mars_facts = 'https://galaxyfacts-mars.com/'
#pandas to read html
tables = pd.read_html(mars_facts)
#Find Mars Facts DataFrame
df = tables[1]
#Assign the columns
df.columns = ['Description', 'Value']
html_table = df.to_html(table_id="html_tbl_css",justify='left',index=False)
#add parameter
data = df.to_dict(orient='records')
df


# In[10]:


facts_url = "https://galaxyfacts-mars.com/"
browser.visit(facts_url)
mars_data = pd.read_html(facts_url)
mars_data = pd.DataFrame(mars_data[0])
mars_facts = mars_data.to_html(header = False, index = False)
print(mars_facts)
#add dict
mars_info_dict['mars_facts'] = mars_facts


# In[11]:


url_hemisphere = "https://marshemispheres.com/"
browser.visit(url_hemisphere)

html_hemisphere = browser.html
soup = BeautifulSoup(html_hemisphere, "html.parser")



# In[12]:


# Scrape all items that contain mars hemispheres information
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_info = []

# main url for loop
hemispheres_url = "https://marshemispheres.com/"

# Loop through the list of all hemispheres information
for i in hemispheres:
    title = i.find("h3").text
    hemispheres_img = i.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains image 
    browser.visit(hemispheres_url + hemispheres_img)
    
    # HTML Object
    image_html = browser.html
    web_info = BeautifulSoup(image_html, "html.parser")
    
    # Create full image url
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    
    hemispheres_info.append({"title" : title, "img_url" : img_url})


# Display titles and images ulr 
    print("")
    print(title)
    print(img_url)
    print("-----------------------------------------")

    #add dict
mars_info_dict['hemisphere_url'] = hemisphere_img


# In[ ]:




