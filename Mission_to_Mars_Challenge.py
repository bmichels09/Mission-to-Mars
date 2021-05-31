# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemi_soup = soup(html, 'html.parser')

# Get each description div from the page and loop over them
descriptions = hemi_soup.find_all('div', class_='description')
for description in descriptions:
    # Get the title
    title = description.a.h3.get_text()
    
    # Get the URL of the image's page
    image_host = description.a['href']
    image_host = url + image_host
    
    # Go to that URL
    browser.visit(image_host)
    html = browser.html
    host_soup = soup(html, 'html.parser')
    
    # Get the title
    title = host_soup.find('div', class_='cover').h2.get_text()
    
    # Get the URL for the full image
    image_path = host_soup.find('a', text='Sample').get('href')
    image_url = url + image_path
    
    # Add the title and image URL to the dictionary
    hemisphere_image_urls.append({'url': image_url, 'title': title})

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()