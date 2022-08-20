#!/usr/bin/env python3
import sys
import requests,json

sys.path.append('../')

from contentProvider.provider import Provider

class HolidayProvider(Provider):
	
	url = 'https://www.mxnzp.com/api/holiday/recent/list?app_id=gqhuoqrfotppshlf&app_secret=d1VTL3pPcjBPNDRncS9IMkNCb2M2Zz09'
	
	def __init__(self):
		self.biz = "holiday"
		
	def support(self,biz):
		return self.biz == biz
	
	def provide(self):
		publish = []
		data = self.getUrl(self.url)
		if isinstance(data, list):
			for item in data:
				self.assembleSingleItem(publish,item)
		return publish;
	
	
	def assemble(self,params):
		pass
		
	def assembleSingleItem(self,publish,item):
		if(item["residueDays"]>0):
			column = {
				'index':'publish',
				'publishContent':"还有 {}天 是{}({})".format(item["residueDays"],item["holidayName"],item["date"]),
			}
			publish.append(column)
		
		
	def getUrl(self,url):
		headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0'}
		response = requests.get(url=url,headers=headers)
		data = json.loads(response.text)["data"]
		return data
	
if __name__ == "__main__":
	prov = HolidayProvider()
	if prov.support('holiday'):
		print(prov.provide())
		