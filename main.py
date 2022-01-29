# All dependencies in requirements.txt

from bs4 import BeautifulSoup
from links import FORM_LINK, BROKER_WEBSITE_LINK, CHROME_DRIVER_PATH, HOME_PAGE
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ----------------------------XPATH and SELECTORS for Google Forms-----------------------------#

SUBMIT_BUTTON_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
NEW_RESPONSE_XPATH = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
INPUT_CLASS = "quantumWizTextinputPaperinputInput"
TEXT_AREA_CLASS = "quantumWizTextinputPapertextareaInput"
PROPERTY_ADDR_SELECTOR = 'article div.overflow-hidden.overflow-ellipsis.whitespace-nowrap.max-w-70.text-gray-light' \
                         '.leading-4 '
PROPERTY_PRICE_SELECTOR = 'article div#minDeposit.flex div.flex'
PROPERTY_LINK_SELECTOR = 'article a[itemprop~=url]'


# ----------------------------Beautiful Soup and ChromeDriver Setup ---------------------------#

# Using Request to get markup
response = requests.get(url=BROKER_WEBSITE_LINK)
website = response.text
# print(website)

# Making Soup
soup = BeautifulSoup(website, "lxml")
# print(soup.title)

# Setting up Chrome Driver and Service Object
chrome_service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)

# ----------------------- WEB SCRAPING to get Places to rent in Bangalore -------------------#

# Links of properties
property_links = list()
for anchor_tag in soup.select(PROPERTY_LINK_SELECTOR):
    property_links.append(f"{HOME_PAGE}{anchor_tag.get('href')}")

# Price of properties
property_price = list()
for div in soup.select(PROPERTY_PRICE_SELECTOR):
    # removing junk characters
    property_price.append(div.getText().replace('â¹', ''))
property_price = property_price[::2]

# Address of Property
property_addr = list()
for div in soup.select(PROPERTY_ADDR_SELECTOR):
    property_addr.append(div.getText())

# Zipping Up for Each Property
properties = zip(property_addr, property_price, property_links)

# --------------------------------AUTOMATE GOOGLE FORMS ----------------------------------------#

driver.get(FORM_LINK)
time.sleep(1)
# Iterate through each data
for rent_property in properties:
    # Initialize count is zero
    count = 0
    # contain input boxes
    inputs = driver.find_elements(By.CLASS_NAME, INPUT_CLASS)
    # contain text areas
    text_area = driver.find_elements(By.CLASS_NAME, TEXT_AREA_CLASS)
    # Iterate through all input boxes
    for value in inputs:
        # enter value
        value.send_keys(rent_property[count])
        # increment count value
        count += 1

    # Iterate through all text areas
    for value in text_area:
        # enter value
        value.send_keys(rent_property[count])
        # increment count value
        count += 1

    # click on submit button
    submit = driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH)
    submit.click()

    # fill another response
    another_response = driver.find_element(By.XPATH, NEW_RESPONSE_XPATH)
    another_response.click()

# close the window
driver.close()
