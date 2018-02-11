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

	def find_random_positions(self):
		"""Return a random position"""
		passage = set(self.mz.free_positions)
		end_positions = set(self.mz.end_locations[0])
		freeway = passage - end_positions
		chosen_positions = random.sample(freeway, len(self.items))
		for position in chosen_positions:
			return position

	def place_items(self):
		"""Place three objects randomly on the maze"""
		for item in self.items:
			i, j = self.find_random_positions()
			self.mz.set(i, j, item)


if __name__ == "__main__":
	maze = mz.Maze()
	syringe = Syringe(maze)
	maze.load()
	syringe.place_items()
	maze.show()