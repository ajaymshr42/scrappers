from selenium import webdriver

driver=webdriver.PhantomJS()

driver.get('http://www.paytm.com')

for i in driver.find_elements_by_xpath('//*[@id="app"]/div/div[3]/div/div[5]/div[2]/div/div/div[2]/div/div/div/a'):
	print i.text