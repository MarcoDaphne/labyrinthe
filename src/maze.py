# !/usr/bin/env python3
# coding: utf-8

import os

class Maze:
	def __init__(self):
		self.structure = []
		self.free_position = []


	def load(self, data="data", data_file="schema.txt"):
		"""Find path schema.txt, open schema.txt, clean line break and append line in list then character in other list"""
		directory = os.path.dirname(os.path.dirname(__file__))
		path_to_file = os.path.join(directory, data, data_file)

		with open(path_to_file) as f:
			for i, line in enumerate(f):
				clean_line = line.strip()
				liste = list(clean_line)
				self.structure.append(liste)
				for j, element in enumerate(liste):
					if element == '_':
						self.free_position.append((i, j))
		return self.structure, self.free_position
					
	def show(self):
		"""Show each list in self.structure"""
		for liste in self.structure:
			print(liste)


if __name__ == "__main__":
	maze = Maze()
	maze.load()
	maze.show()