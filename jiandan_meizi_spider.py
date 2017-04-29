import requests
from bs4 import BeautifulSoup
import os
import time
headers = {
    'Host': 'jandan.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/42.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': 'http://jandan.net/ooxx/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
#save image
def imgdownload(imgurl):
		html=requests.get(imgurl)
		with open("{}".format(os.path.basename(imgurl)),"wb") as fb:
			fb.write(html.content)
#get singpage all image url and call save function
def get_img_url(page_url):
	html=requests.get(page_url,headers=headers).text
	soup=BeautifulSoup(html,"lxml")
	for url in soup.find_all("a",class_="view_img_link"):
		all_img_url=url.get("href")
		temp="http:"+all_img_url
		imgdownload(temp)
		print (temp)
#url join default 1-23
s=time.clock()
for number in range(1,24):
	get_img_url("http://jandan.net/ooxx/page-"+str(number)+"#comments")
	time.sleep(10)
e=time.clock()
print ("{}".format(str(e-s)),"secound!")