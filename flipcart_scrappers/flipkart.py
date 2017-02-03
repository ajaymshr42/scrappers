import json
from firebase import firebase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time
firebase=firebase.FirebaseApplication('https://firstdatasample.firebaseio.com/')
driver=webdriver.Chrome()
driver.maximize_window()

def scrapper(driver,link,branch):
	driver.get(link)
	try:
		driver.find_element_by_xpath('//*[@id="registerPopupBox"]/div[2]/a/img').click()
	except:
		pass

	for i in range(100):
		try:
			driver.find_element_by_xpath('//*[@id="registerPopupBox"]/div[2]/a/img').click()
		except:
			pass
		try:
			driver.find_element_by_xpath('//*[@id="loading_view_more"]').click()
		except:
			pass
		try:
			driver.execute_script("window.scrollTo(0,{});".format(i*100))
		except:
			pass
		try:
			driver.find_element_by_xpath('//*[@id="loading_view_more"]').click()
		except:
			pass
		
	data={}

	items=driver.find_elements_by_xpath('//*[contains(@id,"p_")]/div')
	for item in items:
		try:
			data['name']=item.find_element_by_xpath('.//div[2]/div[1]/a').text
			data['image']=item.find_element_by_xpath('.//div[1]/a/div/img').get_attribute('src')
			data['offerPrice']=item.find_element_by_xpath('.//div[2]/div[2]/div[2]/p[2]').text
			data['retailPrice']=item.find_element_by_xpath('.//div[2]/div[2]/div[1]/p[2]/span').text
			data['discount']=item.find_element_by_xpath('.//div[2]/div[2]/div[3]/p[2]/span').text
			data['savings']=item.find_element_by_xpath('.//div[2]/div[2]/div[3]/p[2]').text
		except:
			try:
				data['name']=item.find_element_by_xpath('.//a/div/div[1]').text
				data['image']=item.find_element_by_xpath('.//div/div[1]/a/img').get_attribute('src')
				data['offerPrice']=item.find_element_by_xpath('.//a/div/div[2]/div[2]/p[2]').text
				data['retailPrice']=item.find_element_by_xpath('.//a/div/div[2]/div[1]/p[2]/span').text
				data['discount']=item.find_element_by_xpath('.//a/div/div[2]/div[3]/p[2]/span').text
				data['savings']=item.find_element_by_xpath('.//a/div/div[2]/div[3]/p[2]/text()').text4
			except:
				pass
		try:
			firebase.post("/pepperfry{}".format(branch),data)
		except:
			pass
	time.sleep(5)
urls={
	'electronics':{
		'mobiles':'https://www.flipkart.com/mobiles?otracker=nmenu_sub_Electronics_0_Mobiles'
	}
}

# for cat in urls:
# 	for sub_cat in urls[cat]:
# 		print cat,sub_cat,type(urls[cat][sub_cat])


if type(urls) is dict:
	for cat in urls:
		if(type(urls[cat]) is dict):
			# print cat,"\n"
			for sub_cat in urls[cat]:
				if(type(urls[cat][sub_cat]) is dict):
					# print "\t",sub_cat,"\n"
					for sub_sub_cat in urls[cat][sub_cat]:
						if(type(urls[cat][sub_cat][sub_sub_cat]) is dict):
							# print "\t","\t",sub_sub_cat,"\n"
							for sub_sub_sub_cat in urls[cat][sub_cat][sub_sub_cat]:
								if(type(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat]) is dict):
									# print "\t","\t","\t",sub_sub_sub_cat,"\n"
									for sub_sub_sub_sub_cat in urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat]:
										if(type(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat]) is dict):
											# print "\t","\t","\t","\t",sub_sub_sub_sub_cat,"\n"
											for sub5_cat in urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat]:
												# print "\t","\t","\t","\t","\t",sub5_cat,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat]
												if(type(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat]) is dict):
													# print "\t","\t","\t","\t",sub_sub_sub_sub_cat,"\n"
													for sub6_cat in urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat]:
														# print "\t","\t","\t","\t","\t",sub5_cat,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat]
														scrapper(driver,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat][sub6_cat],"/{}/{}/{}/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat,sub_sub_sub_sub_cat,sub5_cat,sub6_cat))
												else:
													scrapper(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat],"/{}/{}/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat,sub_sub_sub_sub_cat,sub5_cat))
										else:
											# print "\t","\t","\t","\t",sub_sub_sub_sub_cat,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat]
											scrapper(driver,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat],"/{}/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat,sub_sub_sub_sub_cat))
								else:
									# print "\t","\t","\t",sub_sub_sub_cat,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat]
									scrapper(driver,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat],"/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat))
						else:
							# print "\t","\t",sub_sub_cat,cat,sub_cat,sub_sub_cat,urls[cat][sub_cat][sub_sub_cat]
							scrapper(driver,urls[cat][sub_cat][sub_sub_cat],"/{}/{}/{}".format(cat,sub_cat,sub_sub_cat))
				else:
					# print "\t",sub_cat,urls[cat][sub_cat],"\n"
					scrapper(driver,urls[cat][sub_cat],"/{}/{}".format(cat,sub_cat))
		else:
			# print cat,urls[cat],"\n"
			scrapper(driver,urls[cat],"/{}".format(cat))
else:
	print "not suitable"

driver.quit()