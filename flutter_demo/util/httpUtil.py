#!/usr/bin/env python3

import requests,json

def getUrl(url):
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0'}
	response = requests.get(url=url,headers=headers)
	data = json.loads(response.text)["data"]
	return data

if __name__ == "__main__":
	print(getUrl('https://api.vvhan.com/api/60s?type=json'))
	
	