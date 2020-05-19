# getting webdriver from selenium
# you can download web driver from : https://chromedriver.chromium.org/downloads
from  selenium import webdriver

# after downloading web driver as per your chrome 
# save it in any location and add its path here
PATH = "C:\web_driver\chromedriver.exe"

# The first thing is to activate driver using webdriver 
driver = webdriver.Chrome(PATH)

# adding the website to visit
driver.get("http://www.youtube.com")

# printing the title of the website
print(driver.title)

# Using close() , it  automatically closes after open the page 
driver.close()
