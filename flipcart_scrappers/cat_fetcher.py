from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

main_cats=[]
sub_cats=[]


browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.flipkart.com/")
time.sleep(2)

# ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="container"]/div/header/div[2]/div/ul/li[1]/a/span')).perform()

browser.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div[2]/div/div/div[2]/form/div/div[1]/div/input').send_keys('mobile')
browser.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div[2]/div/div/div[2]/form/div/div[2]/button').click()



print browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[1]/a/div[2]/div[1]/div[1]').text

# columns_main_count=len(browser.find_elements_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td/div[1]/h2'))
# for col in range(1,columns_main_count+1):
# 	row_at_col=len(browser.find_elements_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[{}]/div/h2'.format(col)))	
# 	for row in range(1,row_at_col+1):
# 		print col,row
# 		print browser.find_element_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[{}]/div[{}]/h2'.format(col,row)).text
# 		elems_at_col_row=browser.find_elements_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[{}]/div[{}]/ul/li/a'.format(col,row))
# 		for elem in elems_at_col_row:
# 			print "\t",elem.text