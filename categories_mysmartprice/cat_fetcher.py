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


for cat in cats:
	driver.get(cats[cat]['link'])
	cats[cat]['categories']={}
	sub_cats=driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[1]')
	for index_cat in range(3,3+len(sub_cats)-1):
		sub_cat_name=sub_cats[index_cat-3].text
		cats[cat]['categories'][str(sub_cat_name).replace(" ","_")]={}
		cats[cat]['categories'][str(sub_cat_name).replace(" ","_")]['name']=str(sub_cat_name)
		cats[cat]['categories'][str(sub_cat_name).replace(" ","_")]['categories']={}
		items=driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div[{}]/div[2]/div/div/a'.format(index_cat))
		for item in items:
			cat_name=item.text
			cats[cat]['categories'][str(sub_cat_name).replace(" ","_")]['categories'][str(cat_name).replace(" ","_")]={
				'name':str(cat_name),
				'link':str(item.get_attribute('href'))
			}
with open("categoriesfile.txt","w") as file:
	file.write("{}".format(cats))