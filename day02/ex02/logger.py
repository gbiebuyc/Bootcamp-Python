#!/usr/bin/env python3
import time
from random import randint
import os

f = open('machine.log', 'w')

def log(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		ret = func(*args, **kwargs)
		delta = time.time() - start
		if delta < 1.0:
			delta *= 1000
			delta_str = '%.3f ms' % delta
		else:
			delta_str = '%.3f s ' % delta
		print('(%s)Running: %-20s[ exec-time = %s ]' % (
			os.environ['USER'],
			func.__name__.replace('_', ' ').title(),
			delta_str),
			file=f
		)
		return ret
	return wrapper

class CoffeeMachine():
	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
	
	@log
	def boil_water(self):
		return "boiling..."
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)

