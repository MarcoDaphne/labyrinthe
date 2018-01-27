# !/usr/bin/env python3
# coding: utf-8

import os

import constant as c

class Maze:
	def __init__(self):
		self.structure = []
		self.free_position = []
		self.macgyver_location = ()
		self.end_location = []

	def load(self, data="data", data_file="schema.txt"):
		"""Loads a maze from a text file and retrieves useful positions""" 
		directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		path_to_file = os.path.join(directory, data, data_file)
		with open(path_to_file) as f:
			for i, line in enumerate(f):
				clean_line = line.strip()
				liste = list(clean_line)
				self.structure.append(liste)
				for j, element in enumerate(liste):
					if element == c.FREE:
						self.free_position.append((i, j))
					elif element == c.MACGYVER:
						self.macgyver_location = i, j
					elif element == c.GATEKEEPER:
						self.end_location.append((i-1, j, i+1, j, i, j-1, i, j+1))
		return self.structure, self.free_position, self.macgyver_location, self.end_location

	def get(self, i, j):
		"""Gets a position in the maze"""
		return self.structure[i][j]

	def set(self, i, j, element):
		"""Install an element on a maze position"""
		self.structure[i][j] = element

	def show(self):
		"""Displays the maze"""
		for line in self.structure:
			print(line)


if __name__ == "__main__":
	maze = Maze()
	maze.load()
	maze.show()