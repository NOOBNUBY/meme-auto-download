from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

word = "짤"

driver = webdriver.Chrome()

driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

elem = driver.find_element(By.CLASS_NAME,'gLFyf')
elem.send_keys(word)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CLASS_NAME,'mye4qd').click()
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CLASS_NAME,'rg_i')
count = 1
for images in images:
    try:
        images.click() 
        time.sleep(1)
        imgUrl = driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
        urllib.request.urlretrieve(imgUrl, f"./download/{count}짤.jpg")
        count = count + 1 
    except:
        pass
