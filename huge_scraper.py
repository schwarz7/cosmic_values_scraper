'''
Once upon a time....
There was a game called Pet Simulator X...
and this website list the price (value for trading and value for sell in gems[in-game currency]) of all sort of pets...
Then here I'm scraping for the price of an especific type of pet, also known as HUGE pets

'''
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

url = 'https://petsimulatorvalues.com/huges'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'} )
webpage = urlopen(req).read()
with requests.Session() as c:
	soup = BeautifulSoup(webpage, 'html5lib')
	huge_infos = soup.find_all('p', attrs={'class': 'sqsrte-small'})

# Print the list on screen	

		
	for i in range(0, len(huge_infos)):
		huge_infos[i] = huge_infos[i].string
		#print in a nice way
		print(huge_infos[i])
	#Print the whole list
	#print(huge_infos)

# Tool to mannualy Search for values

search = input('Type the name of Huge to search:')
pos = huge_infos.index(search)
value = huge_infos[pos+1]
gems = huge_infos[pos+2]
print(f'{search}: {value}  /  {gems}')


#Save process into a .txt file

#Based on website layout, every 5 entrys are related to the same huge pet
counter = 0
with open('/home/schwarz/python/scraper/value_list.txt', "w") as fp:
	for i in range(0, len(huge_infos)):
		counter = counter + 1
		huge_infos[i] = huge_infos[i].string
		if counter % 5 == 0:
			fp.write("%s\n" % huge_infos[i])
		else:
			fp.write("%s / " % huge_infos[i])

	print('Done')
	
