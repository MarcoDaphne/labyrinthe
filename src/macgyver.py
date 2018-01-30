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
		"""Vérifie et ramasse les objets quand Mac Gyver passe sur leurs positions"""
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

	def step_up(self):
		"""Déplace MacGyver d'un position vers le haut"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i - 1, j) != c.WALL and (i, j) not in self.mz.end_location[0] and 0 < i < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i - 1, j)
			if (i - 1, j) in self.mz.end_location[0]:
				if len(self.bag) == len(self.sy.items):
					print("Super!!! Vous avez assomé le Gardien")
					return True
				else:
					exit("Le gardien a assomé MacGyver...")
	
	def step_right(self):
		"""Déplace MacGyver d'un position vers la droite"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i, j + 1) != c.WALL and (i, j) not in self.mz.end_location[0] and 0 < j < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i, j + 1)
			if (i, j + 1) in self.mz.end_location[0]:
				if len(self.bag) == len(self.sy.items):
					print("Super!!! Vous avez assomé le Gardien")
					return True
				else:
					exit("Le gardien a assomé MacGyver...")

	def step_down(self):
		"""Déplace MacGyver d'un position vers le bas"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i + 1, j) != c.WALL and (i, j) not in self.mz.end_location[0] and 0 <= i < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i + 1, j)
			if (i + 1, j) in self.mz.end_location[0]:
				if len(self.bag) == len(self.sy.items):
					print("Super!!! Vous avez assomé le Gardien")
					return True
				else:
					exit("Le gardien a assomé MacGyver...")

	def step_left(self):
		"""Déplace MacGyver d'un position vers la gauche"""
		structure = self.mz.structure
		i, j = self.mz.macgyver_location
		if self.mz.get(i, j - 1) != c.WALL and (i, j) not in self.mz.end_location[0] and 0 < j < len(structure):
			self.mz.set(i, j, c.FREE)
			self.pick_up_or_move(i, j - 1)
			if (i, j - 1) in self.mz.end_location[0]:
				if len(self.bag) == len(self.sy.items):
					print("Super!!! Vous avez assomé le Gardien")
					return True
				else:
					exit("Le gardien a assomé MacGyver...")


if __name__ == "__main__":
	hero = Macgyver(mz, sy)
	hero.step_up()
	hero.step_right()
	hero.step_down()
	hero.step_left()