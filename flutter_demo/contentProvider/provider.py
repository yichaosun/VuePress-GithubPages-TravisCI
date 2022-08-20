#!/usr/bin/env python3

import abc

class Provider(abc.ABC):
	@abc.abstractmethod
	def support(self,biz):
		pass
	
	@abc.abstractmethod
	def provide(self):
		pass
		
	@abc.abstractmethod
	def assemble(self,params):
		pass

