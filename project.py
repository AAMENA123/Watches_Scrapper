from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
import os



driver = webdriver.Chrome()
query = "Watches"
file = 0
for i in range(1):
    driver.get(f"https://www.amazon.in/s?k={query}+for+Men+under+2000rs&page={i}&xpid=RfpR251T-laoh&crid=EG9BL7L3Y9J1&qid=1756646547&sprefix=watches+for+men+under+2000rs%2Caps%2C276&ref=sr_pg_2")
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    for elem in elems:
        d =  elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w",encoding ="utf-8" ) as f:
            f.write(d)
        with open(f"data/{query}_{file}.txt","w",encoding ="utf-8" ) as f:
            f.write(d)
            file+=1
print(f"The number of items:{len(elems)}")
time.sleep(2)
driver.close()  

