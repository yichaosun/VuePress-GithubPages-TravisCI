#!/usr/bin/env python3

import json

class Response:
	code = int
	msg = str
	data ={}
	
	def __init__(self,code,msg = "success",data={}):
		self.code = code
		self.msg = msg
		self.data = data
	
	def toJson(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
				sort_keys=True)
	
if __name__ == "__main__":
	res = Response(2,"success",{'list':['a','v']})
	res.data["d"] = "a"
	res.data["list"].append("c")
	print(res.toJson())
	