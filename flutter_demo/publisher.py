#!/usr/bin/env python3

from contentProvider.sixsProvider import *
from contentProvider.holidayProvider import *

class Publisher:
	providers = []
	
	def __init__(self):
		
		sixp = SixsProvider()
		holiday = HolidayProvider()
		self.providers.append(sixp)
		self.providers.append(holiday)
	
	
	def provide(self,biz):
		for p in self.providers:
			if p.support(biz):
				return p.provide()
			
if __name__ == "__main__":
	publisher = Publisher()
	print(publisher.provide('60s'))
	print(publisher.provide('holiday'))
		