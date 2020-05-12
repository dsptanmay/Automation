from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
repName = sys.argv[1]
emailAddress = sys.argv[2]
passwd = sys.argv[3]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/login")
driver.implicitly_wait(3)

emailButton = driver.find_element_by_xpath('//*[@id="login_field"]')
emailButton.send_keys(emailAddress)

passwordButton = driver.find_element_by_xpath('//*[@id="password"]')
passwordButton.send_keys(passwd)

driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
time.sleep(4)
driver.get('https://github.com/new')
repo = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo.send_keys(repName)
time.sleep(1)
submitButton = driver.find_element_by_xpath(
    '//*[@id="new_repository"]/div[3]/button')
submitButton.click()
time.sleep(3)
driver.close()
print("\n")
print("https://github.com/dsptanmay/{}.git".format(repName))
