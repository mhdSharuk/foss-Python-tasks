import requests; 
from bs4 import BeautifulSoup
import sys

input_name = raw_input("input a word: ")
url= "http://www.google.co.in/search?q=" + str(input_name)


response=requests.get(url)

bs=BeautifulSoup(response.text,'lxml')

for item in bs.select(".r a"):
	print(item.text)
