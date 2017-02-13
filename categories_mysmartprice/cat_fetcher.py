from selenium import webdriver

driver=webdriver.PhantomJS()
driver.get('http://www.mysmartprice.com/')

cats={}
for i in driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div/a'):
	cat=i.find_element_by_xpath('./span[2]').text
	cats[str(cat).replace(' ','_')]={
		'name':str(cat),
		'link':str(i.get_attribute('href'))
	}


for i in cats:
	driver.get(cats[i]['link'])
	cats[i]['categories']={}
	for j in driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/a'):
		cat=j.text
		cats[i]['categories'][str(cat).replace(' ','_')]={
			'name':str(j.text),
			'link':str(j.get_attribute('href'))
		}


print cats