# DOCS - https://python-googlesearch.readthedocs.io/en/latest/
# Got it from here - https://www.geeksforgeeks.org/performing-google-search-using-python-code/

import xlrd
import time
import urllib.error

# imports module for google searching 
try: 
	from googlesearch import search
except ImportError: 
	print("No module named 'google' found") 

#to read input workbook
book = xlrd.open_workbook('/Users/tavasyaagarwal/desktop/growthhacking.xlsx')
sheet = book.sheet_by_name('Outlets')

inputdata = []
outputdata = []

for i in range(sheet.nrows):
	inputdata.append(sheet.cell_value(i, 1))

#removing the first two cell values -- they aren't URLs
inputdata.remove('')
inputdata.remove('Outlets we published on')
#print(data)

#print (len(data))

# # to search 
# try:
for j in range(275, len(inputdata)):
	query = "protein in site:" + inputdata[j]
		#time.sleep(5)


	for k in search(query, tld="com", num=10, stop=10, pause=2):
		print(k)

# except urllib.error.HTTPError:
# 	result = *urllib.error.HTTPError.reason
# 	print(result)

#print(results)
	




# query = "Geeksforgeeks"

# for j in search(query, tld="co.in", num=10, stop=3, pause=2): 
# 	print(j) 
