#written in selenium python for fetching the data using xpath same can be done using any language

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

main_cats=[]
sub_cats=[]


browser=webdriver.Chrome()
browser.maximize_window()
browser.get("http://www.amazon.in/gp/site-directory/ref=nav_shopall_fullstore")
time.sleep(2)

columns_main_count=len(browser.find_elements_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td/div[1]/h2'))
for col in range(1,columns_main_count+1):
	row_at_col=len(browser.find_elements_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[{}]/div/h2'.format(col)))	
	for row in range(1,row_at_col+1):
		print col,row
		print browser.find_element_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[{}]/div[{}]/h2'.format(col,row)).text
		elems_at_col_row=browser.find_elements_by_xpath('//*[@id="shopAllLinks"]/tbody/tr/td[{}]/div[{}]/ul/li/a'.format(col,row))
		for elem in elems_at_col_row:
			print "\t",elem.text
