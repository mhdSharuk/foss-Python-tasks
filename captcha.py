import requests ; from bs4 import BeautifulSoup
import sys

s=input("enter search word :")
base="http://www.google.co.in"
url="http://www.google.co.in/search?q="+ s


response=requests.get(url)

bs=BeautifulSoup(response.text,"lxml")

for item in bs.select(".r a"):
	print(item.text)


for nextPage in bs.select(".fl"):
		res=requests.get(base + nextPage.get('href'))
		bs= BeautifulSoup(res.text,"lxml")
		for item in bs.select(".r a"):
				print(item.text)
