# -*- coding: utf-8 -*-
# @Author: grlyk
# @Date:   2019-07-17 08:17:58
# @Last Modified by:   grlyk
# @Last Modified time: 2019-10-21 14:10:09
#!/usr/bin/python
import requests
from requests.adapters import HTTPAdapter
import time
import os

url = " https://s0.xinger.ink/acgimg/acgurl.php"
headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" }

#超时重新访问
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries = 3))
s.mount('https://', HTTPAdapter(max_retries = 3))

Set = set()

#检查是否存在img文件夹
if os.path.exists(".//img") == False:
	os.mkdir(".//img")

# 爬取200次
# n = int(input())
n = 200
cnt = 1
while cnt <= n:
	print(cnt)
	
	a = s.get(url, timeout = (5, 10))
	Hash = hash(a.content) 	
	
	if Hash in Set :
		print("repeat")
		continue

	else :
		Set.add(Hash)
		file = open(".\\img\\" + str(cnt) + ".jpg", "wb")
		file.write(a.content)
		file.close()
		cnt += 1
	
	time.sleep(1)
