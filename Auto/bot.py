import time
import pickle
import sys
from selenium import webdriver, common

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
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
        time.sleep(1)

        buy_btn = driver.find_element_by_class_name('buyTicketsBtn').click()
        print('Clicked')
        time.sleep(0.5)
        driver.find_element_by_class_name('buyTicketsBtn').click()
        time.sleep(2)
        ticket = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div[2]/div/select/option[3]').click()
        area = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div[3]/div/div[1]/form/p/map/area[2]').click()
    except:
        break
# time.sleep(0.5)
# real_buy = driver.find_element_by_xpath('//*[@id="bookNowBtn"]').click()
