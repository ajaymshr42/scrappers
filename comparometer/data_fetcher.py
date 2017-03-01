from selenium import webdriver

driver=webdriver.PhantomJS()


driver.maximize_window()
driver.get('http://m.comparometer.in/')

data=[]

for item in driver.find_elements_by_xpath('//*[@id="mm-0"]/div[5]/div/a'):
	data.append({'name':str(item.text),'link':str(item.get_attribute('href'))})

print data



