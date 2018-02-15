#! /usr/bin/env python3
# Coding : utf-8

import maze as mz
import syringe as sy
import constants as c

class Macgyver:
	def __init__(self, mz, sy):
		self.mz = mz
		self.sy = sy
		self.bag = []

	def move_and_locate(self, i, j):
		"""Move then locate MacGyver sur le labyrinthe"""
		self.mz.set(i, j, c.MACGYVER)
		self.mz.locate_macgyver(i, j)

	def pick_up_or_move(self, i, j):
		"""Retrieves objects if existing or moves"""
		if self.mz.get(i, j) == c.NEEDLE:
			self.bag.append(c.NEEDLE)
			self.move_and_locate(i, j)
		elif self.mz.get(i, j) == c.TUBE:
			self.bag.append(c.TUBE)
			self.move_and_locate(i, j)
		elif self.mz.get(i, j) == c.ETHER:
			self.bag.append(c.ETHER)
			self.move_and_locate(i, j)
		elif len(self.bag) == len(self.sy.items) and (i, j) in self.mz.end_locations[0]:
			self.move_and_locate(i, j)
			self.mz.show()
			print("==> Bravo!!! Vous avez vaincu de Murdoc!!!")
			return True
		elif (i, j) in self.mz.end_locations[0]:
			self.move_and_locate(i, j)
			self.mz.show()
			print("==> Vous avez perdu...")
			return True		
		else:	
			self.move_and_locate(i, j)

	def step_up(self):
		"""Move Macgyver one position up"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i - 1, j) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 < i < len(structure):
			self.mz.set(i, j, c.FREE)
			return self.pick_up_or_move(i - 1, j)
	
	def step_right(self):
		"""Move Macgyver one position to the right"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i, j + 1) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 < j < len(structure):
			self.mz.set(i, j, c.FREE)
			return self.pick_up_or_move(i, j + 1)

	def step_down(self):
		"""Move Macgyver one position down"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i + 1, j) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 <= i < len(structure):
			self.mz.set(i, j, c.FREE)
			return self.pick_up_or_move(i + 1, j)

	def step_left(self):
		"""Move Macgyver one position to the left"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i, j - 1) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 < j < len(structure):
			self.mz.set(i, j, c.FREE)
			return self.pick_up_or_move(i, j - 1)


if __name__ == "__main__":
	maze = mz.Maze()
	maze.load()
	syringe = sy.Syringe(maze)
	syringe.place_items()
	macgyver = Macgyver(maze, syringe)
	macgyver.step_up()
	macgyver.step_right()
	macgyver.step_down()
	macgyver.step_left()