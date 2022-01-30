# data-entry-job-automation


### What does this project do ?
This project uses [Selenium](https://selenium-python.readthedocs.io/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to automate data-entry jobs for research . 
This project uses the case of automating data-entry for different places available for rent in a city.
  + Web Scrape to get places of rent from a broker website Using bs4
  + Automate Data Entry into Google Form Using selenium


### How to install all dependencies/libraries with the correct version ?
To install all dependencies for the project from `requirements.txt` , follow these steps -

1. Navigate to the project folder
```
2. pip install -r requirements.txt
```

### What is there in `links.py` ?


`links.py` contains global path variables unique to my computer which are as follows - 


| Constants | Description |
| ------ | ----------- |
|   FORM_LINK | Google form link used to fill data. Form contains 3 inputs, address, price, and link to property. |
| BROWSER_WEBSITE_LINK | Link of the wesite to scrape data from. Navigate to any brokery website and apply filters such as place, number of rooms, budget etc. Copy the url. |
|  CHROME_DRIVER_PATH   | Absolute Path of the chrome driver in Local Storage. |
|  HOME_PAGE | Home page link of the broker website. Used to convert relative links. |


### How to get the Chrome Driver ?
Even after installing all dependencies a suitable version of `CHROMEDRIVER` needs to be installed. 
Choose appropriate Chrome driver based on OS and Google Chrome version uou will use. [Click Here](https://chromedriver.chromium.org/downloads) to get it.

Other browser drivers can also be used. Selenium is compatible with many popular drivers (requirements.txt need not be changed).


### Web Scraping Issues you can run into 


  + The classes used to scrape data from the broker website are specific to the website I have used. You need to choose appropriate selectors for yours.
  + The selectors / classes that need to be changed are mentioned in the section XPATH and SELECTORS for Google Forms in `main.py`
  + Google form selectors remains the same. Google form should have three short answer fields - Address, Price, Link to property







