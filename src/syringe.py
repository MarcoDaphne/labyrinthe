#! /usr/bin/env/ python3
# Coding : utf-8

import random

import maze as mz
import constant as c

class Syringe:
	def __init__(self, mz):
		self.mz = mz
		self.items = [c.NEEDLE, c.TUBE, c.ETHER]

	def find_random_position(self):
		"""Return a random position"""
		structure = self.mz.structure
		passage = self.mz.free_position
		i = -1
		j = -1
		while (i, j) not in passage:
			i = random.randint(0, len(structure))
			j = random.randint(0, len(structure[0]))
			if (i, j) in passage:
				return i, j

	def place_items(self):
		"""Place three objects randomly on the maze""" 
		for element in self.items:
			i, j = self.find_random_position()
			self.mz.set(i, j, element)


if __name__ == "__main__":
	fragment = Syringe(mz)
	fragment.place_items()
