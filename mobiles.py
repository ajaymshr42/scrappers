from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import re
from firebase import firebase
driver=webdriver.Chrome()
driver.maximize_window()
firebase = firebase.FirebaseApplication('https://project-a440d.firebaseio.com/', None)

driver.get('http://www.amazon.in/s/ref=lp_1389432031_nr_n_0?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805559031&bbn=1389432031&ie=UTF8&qid=1488215717&rnid=1389432031')
num_next=int(driver.find_element_by_xpath('//*[@id="pagn"]/span[6]').text)
for index in range(num_next):
	i=0
	items=driver.find_elements_by_xpath('//*[starts-with(@id,"result")]')
	for item in items:
		key=firebase.post('/amazon',{})
		data={}
		ddat=item.find_element_by_xpath('./div').text
		print ddat.split('\n')
		data['name']=str(ddat.split('\n')[2])
		data['price']=ddat.split('\n')[4].split(' ')[1]
		data['save']=ddat.split('\n')[5].split(' ')[2]
		data['discount']=ddat.split('\n')[5].split(' ')[2].rstrip(')').rstrip('%').lstrip('(')
		firebase.put('/amazon','{}'.format(str(key['name'])),data)
		i+=1
		if(i==24):
			break
	try:
		next_url=driver.find_element_by_xpath('//*[@id="pagnNextLink"]').get_attribute('href')
		driver.get(next_url)
		time.sleep(3)
	except:
		pass
print 'completetd'
driver.quit()
