from selenium import webdriver
import time
from firebase import firebase
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.amazon.in/s/ref=lp_1389432031_nr_n_0?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805559031&bbn=1389432031&ie=UTF8&qid=1488047795&rnid=1389432031')


mobiles=[]
firebase = firebase.FirebaseApplication('https://firstdatasample.firebaseio.com/', None)
branch='/categories/electronics/mobiles/featurePhones'

num_scrolls=int(driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text)
for i in range(0,num_scrolls):
	items=driver.find_elements_by_xpath('//*[starts-with(@id, "result")]')
	for i in items:
		try:
			name=i.find_element_by_xpath('div/div[3]/div[1]').text
			mobiles.append(name)
			firebase.post(branch,{'name':name})
		except:
			try:
				name=i.find_element_by_xpath('div/div[3]/div[1]/a').get_attribute('title')
				mobiles.append(name)
				firebase.post(branch,{'name':name})
			except:
				pass
		print name

	driver.find_element_by_xpath('//*[@id="pagnNextString"]').click()
	print len(mobiles)
	time.sleep(3)
