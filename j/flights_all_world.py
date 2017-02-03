from selenium import webdriver
import time
import re
from firebase import firebase
firebase=firebase.FirebaseApplication('https://firstdatasample.firebaseio.com/')
letter_maker=re.compile('[^a-zA-Z]')
branch='/data/flights/all'
driver=webdriver.PhantomJS()
driver.get('http://airport-authority.com/browse')
base_url=driver.current_url.split('/')[0]+"//"+driver.current_url.split('/')[2]+"/"
links=[]
main_page_elem=driver.find_elements_by_xpath('//*[@id="browse-list"]/table/tbody/tr/td/ul/li/a')
for i in main_page_elem:
	links.append({'name':i.text,'link':str(i.get_attribute('href'))})
	



for i in links:
	name=letter_maker.sub('',i['name'])
	driver.get(str(i['link']))
	locations=driver.find_elements_by_xpath('//*[@id="search-results"]/tbody/tr/td[1]')
	names=driver.find_elements_by_xpath('//*[@id="search-results"]/tbody/tr/td[2]/a')
	for index in range(2,len(locations)):
		data={
			'city':locations[index].text,
			'name':names[index].text
		}
		firebase.post("{}/{}".format(branch,name.replace(' ','')),data)