import sys
import time
import pickle
import requests
from selenium import webdriver

# driver = webdriver.Chrome(executable_path='./chromedriver')
driver = webdriver.Firefox(executable_path='../drivers/geckodriver')
driver.set_window_size(1024, 768)
driver.get('https://www.allticket.com/findex.html?d=1517665139545')
driver.find_element_by_id('loginBtn').click()

time.sleep(0.5)

email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')

time.sleep(0.3)

email.send_keys(sys.argv[1])
password.send_keys(sys.argv[2])
time.sleep(10)
print('Time up')
pickle.dump(driver.get_cookies(), open("AllticketCookies.pkl", "wb"))
print('Done logged in')
