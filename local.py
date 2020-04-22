from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
repName = sys.argv[1]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/login")
driver.implicitly_wait(3)

emailButton = driver.find_element_by_xpath('//*[@id="login_field"]')
emailButton.send_keys("dsp.tanmay@gmail.com")

passwordButton = driver.find_element_by_xpath('//*[@id="password"]')
passwordButton.send_keys("tanmay03bookworm#")

driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
time.sleep(4)
driver.get('https://github.com/new')
repo = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo.send_keys(repName)
time.sleep(2)
submitButton = driver.find_element_by_xpath(
    '//*[@id="new_repository"]/div[3]/button')
submitButton.click()
time.sleep(3)
driver.close()
print("https://github.com/dsptanmay/{}.git".format(repName))
