from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import re
from firebase import firebase
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.amazon.in/Smartphones/b/ref=sd_allcat_sa_menu_mobile_smartphone?ie=UTF8&node=1805560031')

branch='/products'
firebase = firebase.FirebaseApplication('https://project-a440d.firebaseio.com/', None)

for i in range(1,50):
	items=driver.find_elements_by_xpath('//*[starts-with(@id,"result")]')
	for item in items:
		parent_link=driver.current_url
		name=item.find_element_by_xpath('./div/div[3]/div[1]/a/h2').text
		link=item.find_element_by_xpath('./div/div[3]/div[1]/a').get_attribute('href')
		key=firebase.post(branch,{})

		try:
			driver2=webdriver.Chrome()
			driver2.get(link)

			features=[]
			for feature in driver2.find_elements_by_xpath('//*[@id="feature-bullets"]/ul/li/span'):
				features.append(feature.text)
			prodDetails={
				'os':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[1]/td[2]').text,
				'ram':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[2]/td[2]').text,
				'weight':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[3]/td[2]').text,
				'dimensions':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[4]/td[2]').text,
				'modelNumber':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[5]/td[2]').text,
				'wirelessCommunicationTechnology':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[6]/td[2]').text,
				'connectivity':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[7]/td[2]').text,
				'specialFeatures':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[8]/td[2]').text,
				'otherCameraFeatures':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[9]/td[2]').text,
				'formFactor':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[10]/td[2]').text,
				'color':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[12]/td[2]').text,
				'battery':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[13]/td[2]').text,
				'inBox':driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[14]/td[2]').text,
				'features':features
			}

			data={
					'name':name,
					'key':str(key['name']),
					'link':link,
					'category':'Mobiles & Accessories',
					'subCategory':'mobiles',
					'type':'smartphone',
					'details':prodDetails,
					'price':driver2.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text,
					'retailPrice':re.sub("\D", "", driver2.find_element_by_xpath('//*[@id="regularprice_savings"]/td[2]').text.split('(')[0]),
					'discount':re.sub("\D", "", driver2.find_element_by_xpath('//*[@id="regularprice_savings"]/td[2]').text.split('(')[1])
				}
			try:
				data['shippingType']=	driver2.find_element_by_xpath('//*[@id="price-shipping-message"]/b').text
			except:
				pass



			# print driver2.find_element_by_xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr[2]/td[2]').text
			# print driver2.find_element_by_xpath('')
			firebase.put(branch,'{}'.format(str(key['name'])),{'name':name,'amazon':data})
			firebase.put('/amazon',str(key['name']),data)
			firebase.put('/productCategory/mobile&Accessories/mobiles/smartphones','{}'.format(str(key['name'])),{'name':name,'amazon':data})
			firebase.put('/keys',str(key['name']),{'name':name,'links':{'amazon':link}})
			driver2.quit()
		except:
			driver2.quit()

	driver.find_element_by_xpath('//*[@id="pagnNextLink"]/span[2]').click()


driver.quit()