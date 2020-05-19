from  selenium import webdriver
# Now we are importing Keys as 
# It uses to take control on Key while testing 
from selenium.webdriver.common.keys import Keys
import time
# import these for exception handling conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\web_driver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")


# Here we are just finding the name using that function
# right now this is a searchbox and we are finding it by name
# you can find it in inspect window and check it name 
search = driver.find_element_by_name("s")
# sending what to type in search box
search.send_keys("test")

# Now to enter the search result
# here Keys is that we import and 
# after writing we just hit enter 
search.send_keys(Keys.RETURN)


# You can also get the whole page source
# remove the comment and run
# print(driver.page_source)

# Now  that we get the page result of Hello world
# let's check for the  all search results
# the below line simple help us to 
# wait for 10 second to load the site 
# that is it is waiting for a particular thing to exist in page
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    #print(main.text)
    articles = driver.find_elements_by_tag_name("article")
    for article in articles:
        summary = driver.find_element_by_class_name("entry-summary")
        print(summary.text)
except:
    driver.quit()




# It is used to delay the code 
# by 5 seconds 
# use it by import time module 
time.sleep(5)


# Closing the chrome window
driver.quit()
