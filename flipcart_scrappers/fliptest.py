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

driver.get('https://www.flipkart.com/mobiles?otracker=nmenu_sub_Electronics_0_Mobiles')

