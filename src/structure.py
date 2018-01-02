# !/usr/bin/env python
# coding: utf-8

import os

class Structure:
	def __init__(self):
		self.schema = []


	def load(self, data="data", data_file="schema.txt"):
		"""Find path structure.txt, open structure.txt, clean line break and append characters in list"""
		directory = os.path.dirname(os.path.dirname(__file__))
		path_to_file = os.path.join(directory, data, data_file)

		with open(path_to_file) as f:
			for line in f :
				clean_line = line.strip()
				liste = list(clean_line)
				self.schema.append(liste)
		return self.schema

	# Fonction determinant si une position est un passage ou un mur
	def checking_values(self):
		for liste in self.schema:
			for character in liste:
				if character == '_':
					driveway = True
				else:
					driveway = False
		return driveway
					
	
	def show(self):
		"""Show each list in self.structure"""
		for liste in self.schema:
			print(liste)

				
#if __name__ == "__main__":
maze = Structure()
maze.load()
maze.checking_values()
maze.show()