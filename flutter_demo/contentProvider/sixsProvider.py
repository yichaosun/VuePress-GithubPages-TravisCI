#!/usr/bin/env python3

import sys
import os
import pathlib
import requests,json


sys.path.append('../')

from contentProvider.provider import Provider

class SixsProvider(Provider):

	url = 'https://api.vvhan.com/api/60s?type=json'
	
	def __init__(self,biz):
		self.biz = biz
	
	def support(self,biz):
		return self.biz == biz
	
	def getUrl(self,url):
		headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0'}
		response = requests.get(url=url,headers=headers)
		print(response.text)
		data = json.loads(response.text)["data"]
		return data
	
	def provide(self):
		publish = []
		data = self.getUrl(self.url)
		if isinstance(data, list):
			for i in data:
				publish.extend(self.assembleSingleItem(i))
		return publish
		
		
	def assembleSingleItem(self,item):
		itemList = []
		messages=item.split(";");
		idx = 0;
		for message in messages:
			if 0 == idx:
				itemList.append(self.handleSinglePublish(message))
			else:
				itemList.append(self.handleSingleEvent(message))
				
			idx = idx+1
			
		return itemList
	
	
	def handleSinglePublish(self,message):
		publish = {
			"index":"publish",
		}
		meta = message.split("：")
		
		if len(meta)>1 and len(meta[0])<=10:
			publish["from"] = meta[0]
			publish["publishContent"]=meta[1]
		else :
			publish["publishContent"] = message
		return publish
	
	def handleSingleEvent(self,message):
		event = {
			"index":"event",
		}
		meta = message.split("：")
		
		if len(meta)>1 and len(meta[0])<=10:
			event["who"] = meta[0]
			event["what"]=meta[1]
		else :
			event["what"] = message
		return event
	


if __name__ == "__main__":
	sixp = SixsProvider("60s")
	if sixp.support('60s'):
		print(sixp.provide())
	
