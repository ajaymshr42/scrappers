from selenium import webdriver
import time
import re
from firebase import firebase

firebase=firebase.FirebaseApplication('https://project-a440d.firebaseio.com/',None)

driver=webdriver.Chrome()

driver.maximize_window()

links={
  "Laptops": "https://www.compareraja.in/laptops.html",
  "Refrigerators": "https://www.compareraja.in/refrigerators.html",
  "TVs": "https://www.compareraja.in/televisions.html",
  "ACs": "https://www.compareraja.in/air-conditioners.html",
  "Washing Machines": "https://www.compareraja.in/washing-machines.html",
  "Mobiles": "https://www.compareraja.in/mobiles.html"
}
items={}

def findKey(key):
	if(key=='ACs'):
		return '/electronics/airConditioners'
	elif(key=='Refrigerators'):
		return '/electronics/refrigerators'
	elif(key == 'TVs'):
		return 'televisions'
	elif(key == '/electronics/Washing Machines'):
		return 'washingMachines'
	elif(key=='Laptops'):
		return '/electronics/laptops'
	else:
		return '/electronics/mobiles'

def disbalePop():
	try:
		driver.find_element_by_xpath('//*[@id="spopup"]/a').click()
	except:
		pass

for key in links:
	driver.get(links[key])
	items[key]={}

	elems=0
	total_text=driver.find_element_by_xpath('//*[@id="Total_Count"]').text
	one_page_count=int(total_text.split('-')[1].split(' ')[1])
	total_count=int(total_text.split('Of')[1].split(' ')[1])
	num_loads=total_count/one_page_count+1
	for index in range(num_loads):
		try:
			driver.find_element_by_xpath('//*[@id="spopup"]/a').click()
		except:
			pass
		scoll_amt=int(driver.find_element_by_xpath('//*[@id="dv_loadMore"]').location['y'])
		driver.execute_script('LoadMoreData()')
	products=driver.find_elements_by_xpath('//*[starts-with(@id,"form1")]/ul/li/article')
	for item in products:
		data={}
		try:
			data['name']=str(item.find_element_by_xpath('./div[1]/a[2]').text)
			llindex=1
		except:
			llindex=2

		data['name']=str(item.find_element_by_xpath('./div[starts-with(@class,"prodcut-detail")]/a[2]'.format(llindex)).text)
		
		data['category']='electronics'
		data['subCategory']=key
		data['price']=int(re.sub("[^0-9]", "",item.find_element_by_xpath('./div[starts-with(@class,"prodcut-detail")]/b').text))
		data['link']=str(item.find_element_by_xpath('./div[starts-with(@class,"prodcut-detail")]/a[2]'.format(llindex)).get_attribute('href'))
		data['image']=str(item.find_element_by_xpath('./div[starts-with(@class,"prodcut-detail")]/a[1]/img'.format(llindex)).get_attribute('src'))
		data['description']={}
		for descs in item.find_element_by_xpath('./div[starts-with(@class,"prodcut-summry")]/ul[starts-with(@class,"sumery")]'.format(llindex)).text.split('\n'):
			data['description'][str(descs.split(':')[0])]=str(descs.split(':')[1])
		data_key=findKey(key)
		data['path']=data_key
		data['specKey']=data_key.split('/')[2]
		firekey=firebase.post(data_key,{})['name']
		data['firekey']=firekey
		# firebase.put("/data/{}".format(data_firekey),firekey,data)
		firebase.put('/products',firekey,data)
	print "{} is done".format(key)		
driver.quit()
