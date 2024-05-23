#simple script demonstrating selenium 
#importing files
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setting up the webdriver
service= Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

#here we are opening the google
driver.get("https://google.com")
#waiting for the search textbox in google and search 'manish karki github'
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"gLFyf")))
input_element=driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("manish karki github"+Keys.ENTER)

#waiting for the search result and click on the first result "Manish karki Manishkarki1"
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Manish karki Manishkarki1")))
link= driver.find_element(By.PARTIAL_LINK_TEXT,"Manish karki Manishkarki1")
link.click()
#taking screenshot
driver.save_screenshot("manishgithub.png")
#using custom javascript code to scrolldown
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

time.sleep(10)
driver.quit()
