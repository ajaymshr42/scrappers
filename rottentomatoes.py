from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.rottentomatoes.com/m/the_incredible_hulk')
print driver.find_element_by_xpath('//*[@id="reviews"]/div[1]/div[1]/div/div[2]/p').text