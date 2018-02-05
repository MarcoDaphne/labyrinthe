#! /usr/bin/env python3
# Coding: utf-8

import random

import maze as mz
import constant as c

class Syringe:
	def __init__(self, mz):
		self.mz = mz
		self.items = [c.NEEDLE, c.TUBE, c.ETHER]
		self.chosen_positions = []

	def find_random_position(self):
		"""Return a random position"""
		structure = self.mz.structure
		passage = self.mz.free_positions
		end_positions = self.mz.end_locations[0]
		i = -1
		j = -1
		while (i, j) not in passage:
			i = random.randint(0, len(structure) - 1)
			j = random.randint(0, len(structure[0]) - 1)
		else:
			return i, j

	def place_items(self):
		"""Place three objects randomly on the maze"""
		for element in self.items:
			i, j = self.find_random_position()
			self.mz.set(i, j, element)


if __name__ == "__main__":
	maze = mz.Maze()
	syringe = Syringe(maze)
	maze.load()
	syringe.place_items()
	maze.show()