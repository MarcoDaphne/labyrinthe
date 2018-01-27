#! /usr/bin/env python3
# Coding : utf-8

class Character:
	def __init__(self, maze, syringe):
		self.maze = maze
		self.syringe = syringe
		self.bag = []

	def check_pick_up(self, pos_x, pos_y):
		"""Vérifie et ramasse les objets quand Mac Gyver passe sur leurs positions"""
		if self.maze.get(pos_x, pos_y) == c.NEEDLE:
			self.bag.append(c.NEEDLE)
			self.maze.set(pos_x, pos_y, c.MACGYVER)
			self.maze.macgyver_location = pos_x, pos_y
		elif self.maze.get(pos_x, pos_y) == c.TUBE:
			self.bag.append(c.TUBE)
			self.maze.set(pos_x, pos_y, c.MACGYVER)
			self.maze.macgyver_location = pos_x, pos_y
		elif self.maze.get(pos_x, pos_y) == c.ETHER:
			self.bag.append(c.ETHER)
			self.maze.set(pos_x, pos_y, c.MACGYVER)
			self.maze.macgyver_location = pos_x, pos_y
		else:
			self.maze.set(pos_x, pos_y, c.MACGYVER)
			self.maze.macgyver_location = pos_x, pos_y

	def step_up(self):
		"""Déplace MacGyver d'un position vers le haut"""
		structure = self.maze.structure
		x, y = self.maze.macgyver_location
		self.maze.set(x, y , c.FREE)
		if self.maze.get(x - 1, y) == c.WALL:
			self.maze.set(x, y, c.MACGYVER)
		elif x - 1 not in range(0, len(structure)):
			self.maze.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x - 1, y)

	def step_right(self):
		"""Déplace MacGyver d'un position vers la droite"""
		structure = self.maze.structure
		x, y = self.maze.macgyver_location
		self.maze.set(x, y , c.FREE)
		if self.maze.get(x, y + 1) == c.WALL:
			self.maze.set(x, y, c.MACGYVER)
		elif y + 1 not in range(0, len(structure[0])):
			self.maze.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x, y + 1)

	def step_down(self):
		"""Déplace MacGyver d'un position vers le bas"""
		structure = self.maze.structure
		x, y = self.maze.macgyver_location
		self.maze.set(x, y , c.FREE)
		if self.maze.get(x + 1, y) == c.WALL:
			self.maze.set(x, y, c.MACGYVER)
		elif self.maze.get(x + 1, y) == c.GATEKEEPER:
			if len(self.bag) == len(self.syringe.items): #A Vérifier
				self.maze.set(x + 1, y, c.MACGYVER)
				return True
				#Sortir de la boucle partie
			else:
				self.maze.set(x, y, c.MACGYVER)
				print("Vous avez {}/{}".format(len(self.bag), len(self.syringe.items)))

		elif x + 1 not in range(0, len(structure)):
			self.maze.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x + 1, y)
		return False

	def step_left(self):
		"""Déplace MacGyver d'un position vers la gauche"""
		structure = self.maze.structure
		x, y = self.maze.macgyver_location
		self.maze.set(x, y , c.FREE)
		if self.maze.get(x, y - 1) == c.WALL:
			self.maze.set(x, y, c.MACGYVER)
		elif y - 1 not in range(0, len(structure[0])):
			self.maze.set(x, y, c.MACGYVER)
		else:
			self.check_pick_up(x, y - 1)