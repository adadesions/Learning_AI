import sys
import time
import pickle
import requests
from selenium import webdriver
import cv2

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


# driver = webdriver.Chrome(executable_path='./chromedriver')
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.set_window_size(1024, 768)
driver.get('https://www.allticket.com/findex.html?d=1517665139545')
driver.find_element_by_id('loginBtn').click()

time.sleep(0.5)

email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')
# captcha_ele = driver.find_element_by_xpath('//*[@id="atk-modal-login"]/div/div/div/form/div[4]/div[1]/img[1]')
# captcha_location = captcha_ele.location
# captcha_size = captcha_ele.size
# driver.save_screenshot('wholescreen.png')

# screen = Image.open('wholescreen.png')
# left = captcha_location['x']
# top = captcha_location['y']
# right = captcha_location['x'] + captcha_size['width']
# bottom = captcha_location['y'] + captcha_size['height']

# screen = screen.crop((left, top, right, bottom))
# screen.save('captcha.png')

time.sleep(0.3)
# im = Image.open('./captcha.png')
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('mod_captcha.png')
# text = pytesseract.image_to_string(Image.open('./captcha.png'), config='tessedit_char_whitelist=0123456789')
# print(text)

email.send_keys(sys.argv[1])
password.send_keys(sys.argv[2])
time.sleep(10)
print('Time up')
pickle.dump(driver.get_cookies(), open("AllticketCookies.pkl", "wb"))
print('Done logged in')
