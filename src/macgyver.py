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

	def check_pick_up(self, pos_x, pos_y):
		"""Vérifie et ramasse les objets quand Mac Gyver passe sur leurs positions"""
		if self.mz.get(pos_x, pos_y) == c.NEEDLE:
			self.bag.append(c.NEEDLE)
			self.mz.set(pos_x, pos_y, c.MACGYVER)
			self.mz.macgyver_location = pos_x, pos_y
		elif self.mz.get(pos_x, pos_y) == c.TUBE:
			self.bag.append(c.TUBE)
			self.mz.set(pos_x, pos_y, c.MACGYVER)
			self.mz.macgyver_location = pos_x, pos_y
		elif self.mz.get(pos_x, pos_y) == c.ETHER:
			self.bag.append(c.ETHER)
			self.mz.set(pos_x, pos_y, c.MACGYVER)
			self.mz.macgyver_location = pos_x, pos_y
		else:
			self.maze.set(pos_x, pos_y, c.MACGYVER)
			self.maze.macgyver_location = pos_x, pos_y

	def step_up(self):
		"""Déplace MacGyver d'un position vers le haut"""
		structure = self.mz.structure
		x, y = self.mz.macgyver_location
		self.mz.set(x, y , c.FREE)
		if self.mz.get(x - 1, y) == c.WALL:
			self.mz.set(x, y, c.MACGYVER)
		elif x - 1 not in range(0, len(structure)):
			self.mz.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x - 1, y)

	def step_right(self):
		"""Déplace MacGyver d'un position vers la droite"""
		structure = self.mz.structure
		x, y = self.mz.macgyver_location
		self.mz.set(x, y , c.FREE)
		if self.mz.get(x, y + 1) == c.WALL:
			self.mz.set(x, y, c.MACGYVER)
		elif y + 1 not in range(0, len(structure[0])):
			self.mz.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x, y + 1)

	def step_down(self):
		"""Déplace MacGyver d'un position vers le bas"""
		structure = self.mz.structure
		x, y = self.mz.macgyver_location
		self.mz.set(x, y , c.FREE)
		if self.mz.get(x + 1, y) == c.WALL:
			self.mz.set(x, y, c.MACGYVER)
		elif self.mz.get(x + 1, y) == c.GATEKEEPER:
			if len(self.bag) == len(self.sy.items): #A Vérifier
				self.mz.set(x + 1, y, c.MACGYVER)
				return True
				#Sortir de la boucle partie
			else:
				self.mz.set(x, y, c.MACGYVER)
				print("Vous avez {}/{}".format(len(self.bag), len(self.sy.items)))

		elif x + 1 not in range(0, len(structure)):
			self.mz.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x + 1, y)
		return False

	def step_left(self):
		"""Déplace MacGyver d'un position vers la gauche"""
		structure = self.mz.structure
		x, y = self.mz.macgyver_location
		self.mz.set(x, y , c.FREE)
		if self.mz.get(x, y - 1) == c.WALL:
			self.mz.set(x, y, c.MACGYVER)
		elif y - 1 not in range(0, len(structure[0])):
			self.mz.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x, y - 1)


if __name__ == "__main__":
	hero = Macgyver()
	hero.step_up()
	hero.step_right()
	hero.step_down()
	hero.step_left()