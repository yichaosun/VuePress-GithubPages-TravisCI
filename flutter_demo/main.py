#!/usr/bin/env python3

from publisher import *
from response import *
from util.cdnGenerator import *

if __name__ == "__main__":
	publisher = Publisher()
	pubCard2 = publisher.provide('holiday')
	response = Response(0)
	response.data['list']=[
		{
			'id':1,
			'content':pubCard2
		}
	]
	print(response.toJson())
	path = 'pub'
	cd = CDNFileGenerator()
	idx = cd.index()
	
	f = open("flutter_demo/{}/{}.json".format(path,idx),'w')
	f.write(response.toJson())
	f.close()