import time
import pickle
import sys
from selenium import webdriver, common

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.set_window_size(1024, 768) # optional
driver.get(sys.argv[1])
# driver.get('https://www.allticket.com/findex.html?d=1517665139545')
while True:
    try:
        for cookie in pickle.load(open("AllticketCookies.pkl", "rb")):
            driver.add_cookie(cookie)
        # driver.refresh()
        # time.sleep(1)

        exo = driver.find_element_by_xpath('//*[@id="hot-card"]/div[1]/div/a/div').click()
        # winter = driver.find_element_by_xpath('//*[@id="recommend-card"]/div[3]/div/a/div').click()
        time.sleep(0.5)

        buy_btn = driver.find_element_by_class_name('buyTicketsBtn').click()
        print('Clicked')
        time.sleep(0.5)
        driver.find_element_by_class_name('buyTicketsBtn').click()
        driver.refresh()
    except:
        # area = driver.find_element_by_tag_name('area').click()
        break
# time.sleep(0.5)
# ticket = driver.find_element_by_xpath('//*[@id="ticketValue"]/option[5]').click()
# real_buy = driver.find_element_by_xpath('//*[@id="bookNowBtn"]').click()