#! /usr/bin/env/ python3
# Coding : utf-8

import maze as mz

import random


class Syringe:
	def __init__(self, mz):
		self.mz = mz
		self.needle = 'N'
		self.tube = 'T'
		self.ether = 'E'

	def find_random_position(self):
		"""Method returning a random free position"""
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
		"""Method placing objects randomly in the labyrinth"""
		syringe = [self.needle, self.tube, self.ether]
		schema = self.mz.structure
		for element in syringe:
			x, y = self.find_random_position()
			schema[x][y] = element


if __name__ == "__main__":
	syringe = Syringe(mz)
	syringe.find_random_position()
	syringe.place_items()
