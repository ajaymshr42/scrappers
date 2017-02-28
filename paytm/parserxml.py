import xml.etree.ElementTree as ET
import re
cats={}
tree = ET.parse('sitemap.xml')
root = tree.getroot()
for child in root:
	for spc in child:
		arr=spc.text.split('/')
		if(arr[3]=='shop' and len(arr)>5 and not 'paytm' in arr[5] and not 'deals' in arr[5] and not 'coupons' in arr[5]):
			cats[arr[5]]={}
print cats