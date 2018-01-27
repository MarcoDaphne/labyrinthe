#! /usr/bin/env/python3
# Coding : utf-8

import maze as mz
import syringe as sy
import macgyver as mg

class Game:
	def __init__(self, mz, sy, character):
		self.mz = mz
		self.sy = sy
		self.character = character
		self.want_play = c.EMPTY
		self.get_direction = c.EMPTY

	def get_answer(self):
		"""Ask the user if he wants to play"""
		self.want_play = input("==> Souhaitez-vous jouer au labyrinthe ? ('o' / 'n')\n")
		return self.want_play

	def choose_direction(self):
		"""Ask the user which way he wants to move Mac Gyver""" 
		self.get_direction = input("""\n==> Utiliser les touches ci-dessous pour vous déplacer ou sur 'l' pour quitter:
		'z': Haut 
'q': Gauche			'd': Droite
		's': Bas	
""")
		return self.get_direction

	def move(self):
		"""Move MacGyver"""
		if self.get_direction == c.UP:
			self.character.step_up()
		elif self.get_direction == c.DOWN:
			self.character.step_down()
		elif self.get_direction == c.LEFT:
			self.character.step_left()
		elif self.get_direction == c.RIGHT:
			self.character.step_right()
		elif self.get_direction == c.LEAVE:
			exit()

	def show_pickup(self):
		"""Notify each item picked up"""
		print("==> Objets ramassés: ", end=" ")
		for item in self.character.bag:
			if item == c.NEEDLE:
				print("- Aiguille", end=" ")
			elif item == c.TUBE:
				print("- Tube", end=" ")
			elif item == c.ETHER:
				print("- Fiole d'Ether", end=" ")

	def start(self):
		"""Launch the Game"""
		display = self.mz.show()
		play = self.get_answer()
		end = False
		while not end and play == c.YES:
			set_items = self.sy.place_items()
			while not end:
				display = self.mz.show()
				choice = self.choose_direction()
				end = self.move()
				notify_pickup = self.show_pickup()


def main():
	maze = Maze()
	maze.load()
	syringe = Syringe(maze)
	macgyver = Character(maze, syringe)
	game = Game(maze, syringe, macgyver)
	game.start()

if __name__ == '__main__':
	main()
