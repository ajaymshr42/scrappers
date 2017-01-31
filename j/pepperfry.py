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
		firebase.post("/pepperfry{}".format(branch),data)
	time.sleep(5)
urls={
	'furniture':{
		'livingRoom':{
			'seating':{
				'sofas':{
					'threeSeater':'https://www.pepperfry.com/furniture-sofas-sofas-couches-three-seater.html?v=all',
					'twoSeater':'https://www.pepperfry.com/furniture-sofas-two-seater-sofas.html?v=all',
					'oneSeater':'https://www.pepperfry.com/furniture-sofas-one-seater-sofas.html?v=all',
					'sofaSets':'https://www.pepperfry.com/furniture-sofas-sofa-sets.html?v=all',
					'sectionalSofas':'https://www.pepperfry.com/furniture-sofa-sectionals.html?v=all'
				},
				'recliners':{
					'threeSeater':'https://www.pepperfry.com/furniture-sofa-recliners-three-seater.html?v=all',
					'twoSeater':'https://www.pepperfry.com/furniture-sofa-recliners-two-seater.html?v=all',
					'oneSeater':'https://www.pepperfry.com/furniture-sofa-recliners-one-seater.html?v=all',
					'reclinerSets':'https://www.pepperfry.com/furniture-sofa-recliners-sets.html?v=all'
				},
				'sofaCumBeds':{
					'engineeredWood':'https://www.pepperfry.com/furniture-sofa-cum-beds-engineered-wood.html?v=all',
					'fabric':'https://www.pepperfry.com/furniture-sofa-cum-beds-fabric.html?v=all',
					'metal':'https://www.pepperfry.com/furniture-sofa-cum-beds-metal.html?v=all',
					'leatherette':'https://www.pepperfry.com/furniture-sofa-cum-beds-leatherette.html?v=all'
				},
				'settees':'https://www.pepperfry.com/furniture-settees.html',
				'benches':'https://www.pepperfry.com/furniture-benches.html',
				'stools':'https://www.pepperfry.com/furniture-stools.html',
				'pouffes':'https://www.pepperfry.com/furniture-poufee-stools.html',
				'beanBags':{
					'cover':'https://www.pepperfry.com/furniture-bean-bags-bean-bag-cover.html?v=all',
					'beans':'https://www.pepperfry.com/furniture-bean-bags-bean-bags-with-beans.html?v=all'
				},
				'foutons':'https://www.pepperfry.com/furniture-futons.html'
			},
			'storage':{
				'cabinetsAndSideboards':{
					'contemporary':'https://www.pepperfry.com/furniture-cabinets-and-sideboards-contemporary.html?v=all',
					'modern':'https://www.pepperfry.com/furniture-cabinets-and-sideboards-modern.html?v=all',
					'colonial':'https://www.pepperfry.com/furniture-cabinets-and-sideboards-modern.html?v=all',
					'electric':'https://www.pepperfry.com/furniture-cabinets-sideboards-eclectic.html?v=all',
					'indianEthnic':'https://www.pepperfry.com/furniture-cabinets-and-sideboards-indian-ethnic.html?v=all'
				},
				'hutch':'https://www.pepperfry.com/furniture-hutch-cabinets.html',
				'entertainmentUnit':{
					'modern':'https://www.pepperfry.com/furniture-entertainment-units-modern.html?v=all',
					'contemporary':'https://www.pepperfry.com/furniture-entertainment-units-contemporary.html?v=all',
					'colonial':'https://www.pepperfry.com/furniture-entertainment-units-colonial.html?v=all',
					'eclectic':'https://www.pepperfry.com/furniture-entertainment-units-eclectic.html?v=all',
					'indianEthnic':'https://www.pepperfry.com/furniture-entertainment-units-indian-ethnic.html?v=all'
				},
				'showRack':{
					'engineeredWood':'https://www.pepperfry.com/furniture-shoe-racks-engineered-wood.html?v=all',
					'solidWood':'https://www.pepperfry.com/furniture-shoe-racks-solid-wood.html?v=all',
					'metal':'https://www.pepperfry.com/furniture-shoe-racks-metal.html?v=all',
					'mouldedPlastic':'https://www.pepperfry.com/furniture-shoe-racks-moulded-plastic.html?v=all'
				},
				'magzineRack':'https://www.pepperfry.com/furniture-magazine-racks.html',
				'trunksAndBoxes':'https://www.pepperfry.com/furniture-trunks-boxes.html'
			},
			'chairs':{
				'armChairs':'https://www.pepperfry.com/furniture-arm-chairs.html?v=all',
				'foldingChairs':'https://www.pepperfry.com/furniture-folding-chairs.html?v=all',
				'metalChairs':'https://www.pepperfry.com/furniture-metal-chairs.html?v=all',
				'stackingChairs':'https://www.pepperfry.com/furniture-chairs-stacking-chairs.html?v=all',
				'ergonomicChairs':'https://www.pepperfry.com/furniture-office-furniture-office-chairs-ergonomic-chairs.html?v=all',
				'executiveChairs':'https://www.pepperfry.com/furniture-office-furniture-office-chairs-executive-chairs.html?v=all'
			},
			'tables':{
				'coffeeTable':{
					'rectangle':'https://www.pepperfry.com/furniture-rectangle-coffee-tables.html?v=all',
					'square':'https://www.pepperfry.com/furniture-square-coffee-tables.html?v=all',
					'round':'https://www.pepperfry.com/furniture-round-coffee-tables.html?v=all',
					'oval':'https://www.pepperfry.com/furniture-oval-coffee-tables.html?v=all',
					'abstract':'https://www.pepperfry.com/furniture-abstract-coffee-tables.html?v=all'
				},
				'coffeeTableSets':{
					'rectangle':'https://www.pepperfry.com/furniture-rectangle-coffee-table-sets.html?v=all',
					'square':'https://www.pepperfry.com/furniture-square-coffee-table-sets.html?v=all',
					'round':'https://www.pepperfry.com/furniture-round-coffee-table-sets.html?v=all'
				},
				'endTable':{
					'contemporary':'https://www.pepperfry.com/furniture-end-tables-contemporary.html?v=all',
					'modern':'https://www.pepperfry.com/furniture-end-tables-modern.html?v=all',
					'colonial':'https://www.pepperfry.com/furniture-end-tables-colonial.html?v=all',
					'indianEthnic':'https://www.pepperfry.com/furniture-end-tables-indian-ethnic.html?v=all',
					'eclectic':'https://www.pepperfry.com/furniture-end-tables-eclectic.html?v=all'
				},
				'consoleTables':{
					'contemporary':'https://www.pepperfry.com/furniture-console-tables-contemporary.html?v=all',
					'colonial':'https://www.pepperfry.com/furniture-console-tables-colonial.html?v=all',
					'modern':'https://www.pepperfry.com/furniture-console-tables-modern.html?v=all',
					'eclectic':'https://www.pepperfry.com/furniture-console-tables-eclectic.html?v=all',
					'indianEthnic':'https://www.pepperfry.com/furniture-console-tables-indian-ethnic.html?v=all'
				},
				'setsOfTable':{
					'contemporary':'https://www.pepperfry.com/furniture-sets-of-tables-contemporary.html?v=all',
					'colonial':'https://www.pepperfry.com/furniture-sets-of-tables-colonial.html?v=all',
					'eclectic':'https://www.pepperfry.com/furniture-sets-of-tables-eclectic.html?v=all',
					'modern':'https://www.pepperfry.com/furniture-sets-of-tables-modern.html?v=all',
					'indianEthnic':'https://www.pepperfry.com/furniture-sets-of-tables-indian-ethnic.html?v=all'
				}
			}
		},
		'bedroom':{
			'beds':{
				'queenSizedBeds':'https://www.pepperfry.com/furniture-beds-queen-sized-beds.html?v=all',
				'kingSizedBeds':'https://www.pepperfry.com/furniture-beds-king-sized-beds.html?v=all',
				'singleBeds':'https://www.pepperfry.com/furniture-beds-single.html?v=all',
				'posterBeds':'https://www.pepperfry.com/furniture-beds-poster.html?v=all'
			},
			'wardrobes':{
				'doubleDoorWardrobes':'https://www.pepperfry.com/furniture-double-door-wardrobes.html?v=all',
				'tripleDoorsWardrobes':'https://www.pepperfry.com/furniture-three-door-wardrobes.html?v=all',
				'fourDoorWardrobes':'https://www.pepperfry.com/furniture-four-door-wardrobes.html?v=all',
				'fourplusDoorWardrobes':'https://www.pepperfry.com/furniture-four-plus-door-wardrobes.html?v=all',
				'oneDoorWardrobes':'https://www.pepperfry.com/furniture-single-door-wardrobes.html?v=all',
				'slidingDoorWardrobes':'https://www.pepperfry.com/furniture-sliding-door-wardrobes.html?v=all'
			},
			'bedSidetables':{
				'modern':'https://www.pepperfry.com/furniture-bed-side-tables-modern.html?v=all',
				'contemporary':'https://www.pepperfry.com/furniture-bed-side-tables-contemporary.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-bed-side-tables-colonial.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-bed-side-tables-eclectic.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-bed-side-tables-indian-ethnic.html?v=all'
			},
			'chestOfDrawer':{
				'contemporary':'https://www.pepperfry.com/furniture-chest-of-drawers-contemporary.html?v=all',
				'modern':'https://www.pepperfry.com/furniture-chest-of-drawers-modern.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-chest-of-drawers-colonial.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-chest-of-drawers-eclectic.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-chest-of-drawers-indian-ethnic.html?v=all'
			},
			'dressingTables':'https://www.pepperfry.com/furniture-dressing-tables.html',
			'bedRoomSets':'https://www.pepperfry.com/furniture-bed-room-sets.html',
			'mattresses':{
				'queenBeds':'https://www.pepperfry.com/furniture-mattresses-queen-beds.html?v=all',
				'kingBeds':'https://www.pepperfry.com/furniture-mattresses-king-beds.html?v=all',
				'singleBeds':'https://www.pepperfry.com/furniture-mattresses-single-beds.html?v=all',
				'mattressProtector':'https://www.pepperfry.com/furniture-mattresses-mattress-protectors.html?v=all'
			},
			'linenTrunks':'https://www.pepperfry.com/furniture-linen-trunk-boxes.html'
		},
		'studyRoom':{
			'bookCases':{
				'modern':'https://www.pepperfry.com/furniture-book-cases-modern.html?v=all',
				'contemporary':'https://www.pepperfry.com/furniture-book-cases-contemporary.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-book-cases-colonial.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-book-cases-eclectic.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-book-cases-indian-ethnic.html?v=all'
			},
			'fileCabinet':'https://www.pepperfry.com/furniture-office-furniture-office-storage-file-cabinets.html',
			'bookShelves':{
				'modern':'https://www.pepperfry.com/furniture-book-shelves-modern.html?v=all',
				'contemporary':'https://www.pepperfry.com/furniture-book-shelves-contemporary.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-book-shelves-eclectic.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-book-shelves-colonial.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-book-shelves-indian-ethnic.html?v=all'
			},
			'studyAndLaptopnTable':{
				'contemporary':'https://www.pepperfry.com/furniture-study-laptop-tables-contemporary.html?v=all',
				'modern':'https://www.pepperfry.com/furniture-study-laptop-tables-modern.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-study-laptop-tables-colonial.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-study-laptop-tables-eclectic.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-study-laptop-tables-indian-ethnic.html?v=all'
			}
		},
		'diningRoom':{
			'diningChairs':{
				'contemporary':'https://www.pepperfry.com/furniture-dining-chairs-contemporary.html?v=all',
				'modern':'https://www.pepperfry.com/furniture-dining-chairs-modern.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-dining-chairs-colonial.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-dining-chairs-eclectic.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-dining-chairs-indian-ethnic.html?v=all'
			},
			'diningSets':{
				'sixSeater':'https://www.pepperfry.com/furniture-dining-sets-six-seater.html?v=all',
				'fourSeater':'https://www.pepperfry.com/furniture-dining-sets-four-seater.html?v=all',
				'twoSeater':'https://www.pepperfry.com/furniture-dining-sets-two-seater.html?v=all',
				'eightSeater':'https://www.pepperfry.com/furniture-dining-sets-eight-seater.html?v=all'
			},
			'diningTable':{
				'sixSeater':'https://www.pepperfry.com/furniture-six-seater-dining-tables.html?v=all',
				'fourSeater':'https://www.pepperfry.com/furniture-four-seater-dining-tables.html?v=all',
				'twoSeater':'https://www.pepperfry.com/furniture-two-seater-dining-tables.html?v=all',
				'eightSeater':'https://www.pepperfry.com/furniture-eight-seater-dining-tables.html?v=all'
			},
			'hutchCabinets':'https://www.pepperfry.com/furniture-hutch-cabinets.html'
		},
		'barFurniture':{
			'barCabinets':{
				'contemporary':'https://www.pepperfry.com/furniture-contemporary-bar-cabinets.html?v=all',
				'modern':'https://www.pepperfry.com/furniture-modern-bar-cabinets.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-eclectic-bar-cabinets.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-colonial-bar-cabinets.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-indian-ethnic-bar-cabinets.html?v=all'
			},
			'barUnits':'https://www.pepperfry.com/furniture-bar-units.html?v=all',
			'barTrollys':'https://www.pepperfry.com/furniture-bar-trolleys.html?v=all',
			'barSets':'https://www.pepperfry.com/bar-furniture-bar-sets.html?v=all',
			'barChairs':{
				'contemporary':'https://www.pepperfry.com/furniture-contemporary-bar-chairs.html?v=all',
				'modern':'https://www.pepperfry.com/furniture-modern-bar-chairs.html?v=all',
				'eclectic':'https://www.pepperfry.com/furniture-bar-eclectic-bar-chairs.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-colonial-bar-chairs.html?v=all'
			},
			'wineRacks':'https://www.pepperfry.com/furniture-wine-racks.html?v=all',
			'barStools':{
				'eclectic':'https://www.pepperfry.com/furniture-eclectic-bar-stools.html?v=all',
				'contemporary':'https://www.pepperfry.com/furniture-contemporary-bar-stools.html?v=all',
				'modern':'https://www.pepperfry.com/furniture-modern-bar-stools.html?v=all',
				'colonial':'https://www.pepperfry.com/furniture-colonial-bar-stools.html?v=all',
				'indianEthnic':'https://www.pepperfry.com/furniture-indian-ethnic-bar-stools.html?v=all'
			}
		},
		'gardenFurniture':{
			'patioSets':'https://www.pepperfry.com/furniture-outdoor-patio-sets.html?v=all',
			'balconySets':'https://www.pepperfry.com/furniture-outdoor-balcony-sets.html?v=all',
			'diningSets':'https://www.pepperfry.com/garden-outdoor-furniture-dining-sets.html?v=all',
			'swings':'https://www.pepperfry.com/furniture-outdoor-furniture-swings.html?v=all',
			'loungersAndDaybeds':'https://www.pepperfry.com/furniture-outdoor-furniture-loungers.html?v=all',
			'tables':'https://www.pepperfry.com/furniture-outdoor-and-garden-furniture-tables.html?v=all',
			'chairs':'https://www.pepperfry.com/furniture-outdoor-and-garden-furniture-seating.html?v=all',
			'seeteesAndBenches':'https://www.pepperfry.com/furniture-outdoor-furniture-outdoor-settees-benches.html?v=all',
			'canopiesAndUmbrella':'https://www.pepperfry.com/garden-outdoor-furniture-canopies-umbrellas.html?v=all',
			'firepits':'https://www.pepperfry.com/garden-outdoor-furniture-firepits.html?v=all'
		},
		'kids':{
			'beds':{
				'bunk':'https://www.pepperfry.com/furniture-kids-furniture-beds-bunk-beds.html?v=all',
				'single':'https://www.pepperfry.com/furniture-kids-furniture-beds-single-beds.html?v=all',
				'double':'https://www.pepperfry.com/furniture-kids-furniture-beds-double-beds.html?v=all'
			},
			'storage':{
				'wardrobes':'https://www.pepperfry.com/furniture-kids-furniture-wardrobes.html?v=all',
				'storageCabinets':'https://www.pepperfry.com/furniture-children-storage.html?v=all',
				'chestOfDrawers':'https://www.pepperfry.com/furniture-kids-furniture-chest-of-drawers.html?v=all',
				'storageBoxes':'https://www.pepperfry.com/kids-kids-furniture-storage-storage-boxes.html?v=all'
			},
			'study':{
				'studyTables':'https://www.pepperfry.com/furniture-kids-study-tables.html?v=all',
				'drawingDesks':'https://www.pepperfry.com/furniture-kids-furniture-tables-drawing-desks.html?v=all',
				'bookShelvesAndCases':'https://www.pepperfry.com/furniture-kids-furniture-book-shelves-and-cases.html?v=all',
				'chairs':'https://www.pepperfry.com/furniture-children-chairs.html?v=all',
				'tableAndChairSets':'https://www.pepperfry.com/furniture-children-tables.html?v=all'
			},
			'bedsideTables':'https://www.pepperfry.com/furniture-kids-furniture-bed-side-tables.html?v=all',
			'cradles':'https://www.pepperfry.com/furniture-children-cradles.html?v=all',
			'beanBags':{
				'cover':'https://www.pepperfry.com/furniture-kids-furniture-seating-bean-bags.html?v=all',
				'beans':'https://www.pepperfry.com/kids-bean-bags-with-beans.html?v=all'
			},
			'sofas':'https://www.pepperfry.com/furniture-kids-furniture-sofas.html?v=all',
			'babyHoghChairs':'https://www.pepperfry.com/kids-kids-furniture-baby-high-chairs.html?v=all',
			'chairs':'https://www.pepperfry.com/furniture-children-chairs.html?v=all'
		}
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
														scrapper(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat][sub6_cat],"/{}/{}/{}/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat,sub_sub_sub_sub_cat,sub5_cat,sub6_cat))
												else:
													scrapper(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat][sub5_cat],"/{}/{}/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat,sub_sub_sub_sub_cat,sub5_cat))
										else:
											# print "\t","\t","\t","\t",sub_sub_sub_sub_cat,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat]
											scrapper(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat][sub_sub_sub_sub_cat],"/{}/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat,sub_sub_sub_sub_cat))
								else:
									# print "\t","\t","\t",sub_sub_sub_cat,urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat]
									scrapper(urls[cat][sub_cat][sub_sub_cat][sub_sub_sub_cat],"/{}/{}/{}/{}".format(cat,sub_cat,sub_sub_cat,sub_sub_sub_cat))
						else:
							# print "\t","\t",sub_sub_cat,cat,sub_cat,sub_sub_cat,urls[cat][sub_cat][sub_sub_cat]
							scrapper(urls[cat][sub_cat][sub_sub_cat],"/{}/{}/{}".format(cat,sub_cat,sub_sub_cat))
				else:
					# print "\t",sub_cat,urls[cat][sub_cat],"\n"
					scrapper(urls[cat][sub_cat],"/{}/{}".format(cat,sub_cat))
		else:
			# print cat,urls[cat],"\n"
			scrapper(urls[cat],"/{}".format(cat))
else:
	print "not suitable"

driver.quit()