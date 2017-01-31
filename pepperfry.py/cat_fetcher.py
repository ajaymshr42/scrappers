from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.action_chains import ActionChains
import time


browser=webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.pepperfry.com/')

browser.find_element_by_xpath('//*[@id="registerPopupBox"]/div[2]/a/img').click()
main_cats=browser.find_elements_by_xpath('//*[@id="menu_wrapper"]/ul/li/a')
main_cats_num=len(browser.find_elements_by_xpath('//*[@id="menu_wrapper"]/ul/li/a'))
for i in range(1,main_cats_num+1):
	ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="menu_wrapper"]/ul/li[{}]/a'.format(i))).perform()
	try:
		print browser.find_element_by_xpath('//*[@id="nav_furniture"]/div[1]/div[1]/div[1]/div[1]/ul/li[1]/a').text
	except:
		pass
	time.sleep(3)