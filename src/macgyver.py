#! /usr/bin/env python3
# Coding : utf-8

import maze as mz
import syringe as sy
import constant as c

class Macgyver:
	def __init__(self, mz, sy):
		self.mz = mz
		self.sy = sy
		self.bag = []

	def pick_up_or_move(self, i, j):
		"""Retrieves objects if existing or moves"""
		if self.mz.get(i, j) == c.NEEDLE:
			self.bag.append(c.NEEDLE)
			self.mz.set(i, j, c.MACGYVER)
			self.mz.locate_macgyver(i, j)
		elif self.mz.get(i, j) == c.TUBE:
			self.bag.append(c.TUBE)
			self.mz.set(i, j, c.MACGYVER)
			self.mz.locate_macgyver(i, j)
		elif self.mz.get(i, j) == c.ETHER:
			self.bag.append(c.ETHER)
			self.mz.set(i, j, c.MACGYVER)
			self.mz.locate_macgyver(i, j)
		else:
			self.mz.set(i, j, c.MACGYVER)
			self.mz.locate_macgyver(i, j)

	def win_or_die(self, i, j):
		"""Determines whether MacGyver out of maze or not"""
		if len(self.bag) == len(self.sy.items) and (i, j) in self.mz.end_locations[0]:
			print("Bravo!!! Vous avez assomé le gardien et trouvé la sortie.")
			return True
		elif (i, j) in self.mz.end_locations[0]:
			print("Oh non!!! Le gardien a tué MacGyver.")
			return True

	def step_up(self):
		"""Move Macgyver one position up"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i - 1, j) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 < i < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i - 1, j)
			return self.win_or_die(i - 1, j)
	
	def step_right(self):
		"""Move Macgyver one position to the right"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i, j + 1) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 < j < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i, j + 1)
			return self.win_or_die(i, j + 1)

	def step_down(self):
		"""Move Macgyver one position down"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i + 1, j) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 <= i < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i + 1, j)
			return self.win_or_die(i + 1, j)

	def step_left(self):
		"""Move Macgyver one position to the left"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i, j - 1) != c.WALL and (i, j) not in self.mz.end_locations[0] and 0 < j < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i, j - 1)
			return self.win_or_die(i, j - 1)


if __name__ == "__main__":
	maze = mz.Maze()
	syringe = sy.Syringe(maze)
	macgyver = Macgyver(maze, syringe)
	macgyver.step_up()
	macgyver.step_right()
	macgyver.step_down()
	macgyver.step_left()