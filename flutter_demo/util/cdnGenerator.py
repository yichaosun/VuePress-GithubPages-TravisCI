#!/usr/bin/env python3

import base64
import time
import string

class CDNFileGenerator:
	oneZFDay = 8985600 # 104*24*60*60
	oneDay = 86400 # 60*60*24
	oneHour = 3600 # 60*60
	fiveMin = 300 # 60*5

	asciiDic = dict({0: 'H', 1: 'O', 2: 'c', 3: 't', 4: 'u', 5: 'R', 6: 'z', 7: 'y', 8: 'd', 9: 'e', 10: 'q', 11: 'k', 12: 'X', 13: 'p', 14: 's', 15: 'E', 16: 'P', 17: 'W', 18: 'j', 19: 'U', 20: 'g', 21: 'G', 22: 'w', 23: 'V', 24: 'b', 25: 'F', 26: 'L', 27: 'a', 28: 'N', 29: 'Y', 30: 'C', 31: 'T', 32: 'x', 33: 'S', 34: 'I', 35: 'o', 36: 'Z', 37: 'h', 38: 'r', 39: 'Q', 40: 'D', 41: 'm', 42: 'l', 43: 'A', 44: 'i', 45: 'B', 46: 'n', 47: 'f', 48: 'K', 49: 'M', 50: 'J', 51: 'v'})

	def index(self):
			duration = int(time.time())%self.oneZFDay
			d = duration//self.oneDay
			dr = duration%self.oneDay
			h = dr//self.oneHour
			hr = dr%self.oneHour
			v = hr//self.fiveMin
	
			if d > 51:
				return "{}{}{}{}==".format(self.asciiDic[d-51],"7",self.asciiDic[(d+h)%51],self.asciiDic[(d+h+v+9)%48])
			else:
				return "{}{}{}{}==".format("1",self.asciiDic[d],self.asciiDic[(d+h+4)%52],self.asciiDic[(d+h+v+9)%47])


if __name__ == "__main__":
	cd = CDNFileGenerator()
	print(cd.index())