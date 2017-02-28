from selenium import webdriver

driver=webdriver.PhantomJS()
driver.get('http://www.mysmartprice.com/mobile/pricelist/mobile-price-list-in-india.html#subcategory=mobile')

names=[]
try:
	elems=driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div[2]/a')
	for elem in elems:
		names.append(elem.text)
	print driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/div[3]/div[2]/div[1]/div[49]/a[4]').text
	print driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/div[3]/div[2]/div[1]/div[49]/a[7]').text
except:
	pass
print len(names)