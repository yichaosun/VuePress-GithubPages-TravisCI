#!/usr/bin/env python3

from publisher import *
from response import *

if __name__ == "__main__":
	publisher = Publisher()
	pubCard = publisher.provide('60s')
	card = {
		'id':1,
		'content':pubCard
	}
	response = Response(0)
	response.data['list']=[
		card
	]
	print(response.toJson())