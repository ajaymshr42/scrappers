from selenium import webdriver


driver=webdriver.PhantomJS()
driver.get('https://www.snapdeal.com/page/sitemap')


for i in driver.find_elements_by_xpath('//*[@id="SMWrapr"]/div[2]/ul/li/a/span[2]'):
	print i.text.replace('\n',' ')