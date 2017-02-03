from selenium import webdriver
import time
import re
from firebase import firebase
firebase=firebase.FirebaseApplication('https://firstdatasample.firebaseio.com/')
letter_maker=re.compile('[^a-zA-Z]')
branch='/data/flights/domestic'
driver=webdriver.PhantomJS()
driver.get('http://airport-authority.com/browse-IN')
driver.get(str(i['link']))
locations=driver.find_elements_by_xpath('//*[@id="search-results"]/tbody/tr/td[1]')
names=driver.find_elements_by_xpath('//*[@id="search-results"]/tbody/tr/td[2]/a')
shorts=driver.find_elements_by_xpath('//*[@id="search-results"]/tbody/tr/td[2]')
for index in range(2,len(locations)):
	data={
		'city':locations[index].text,
		'name':names[index].text,
		'code':shorts[index].text
	}
	firebase.post("{}/{}".format(branch,name.replace(' ','')),data)
