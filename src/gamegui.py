#! /usr/bin/env python3
# Coding: utf-8

import os
import pygame
import time

import maze as mz
import syringe as sy
import macgyver as mg
import constants as c


class GameGui:
	def __init__(self, mz, sy, mg):
		self.mz = mz 
		self.sy = sy # (L'initialisation ne fonctionne pas et si ca fonctionne, self.maze.load() sera charger à chaque fois que self.graph_maze() sera chargé)
		self.mg = mg
		self.surface = ' ' # (Comment initialiser self.surface ? C'est la solution que j'ai trouvé pour ne pas dégradé l'image)

	def seek(self, picture):
		"""Seek and return a picture"""
		directory = os.path.dirname(os.path.dirname(os.path.abspath((__file__))))
		path_to_file = os.path.join(directory, "pictures", picture)
		return path_to_file

	def presentation(self):
		"""Customize the icon and title of the window"""
		pict_icon = pygame.image.load(self.seek(c.ICON_IMG))
		pygame.display.set_icon(pict_icon)
		pygame.display.set_caption(c.TITLE)

	def graph_maze(self):
		"""Displays the maze in graphical mode"""
		pygame.init()
		self.surface = pygame.display.set_mode((480, 480))
		self.presentation()
		pict_wall = pygame.image.load(self.seek(c.WALL_IMG)).convert_alpha()
		pict_floor = pygame.image.load(self.seek(c.FLOOR_IMG)).convert_alpha()
		pict_macgyver = pygame.image.load(self.seek(c.MACGYVER_IMG)).convert_alpha()
		pict_gatekeeper = pygame.image.load(self.seek(c.MURDOC_IMG)).convert_alpha()
		pict_needle = pygame.image.load(self.seek(c.NEEDLE_IMG)).convert_alpha()
		pict_tube = pygame.image.load(self.seek(c.TUBE_IMG)).convert_alpha()
		pict_ether = pygame.image.load(self.seek(c.ETHER_IMG)).convert_alpha()
				
		i = 0
		for line in self.mz.structure:
			j = 0
			for element in line:
				if element == c.FREE:
					self.surface.blit(pict_floor, (j, i))
				elif element == c.MACGYVER:
					self.surface.blit(pict_macgyver, (j, i))
				elif element == c.GATEKEEPER:
					self.surface.blit(pict_gatekeeper, (j, i))
				elif element == c.NEEDLE:
					self.surface.blit(pict_needle, (j, i))
				elif element == c.TUBE:
					self.surface.blit(pict_tube, (j, i))
				elif element == c.ETHER:
					self.surface.blit(pict_ether, (j, i))
				else:
					self.surface.blit(pict_wall, (j, i))
				j += 32
			i += 32

	def play(self):
		"""Launch the game"""
		self.graph_maze()
		pict_win = pygame.image.load(self.seek(c.WIN_IMG)).convert()
		pict_loose = pygame.image.load(self.seek(c.LOOSE_IMG)).convert()
		end = False
		while not end:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						end = self.mg.step_up()
					elif event.key == pygame.K_DOWN:
						end = self.mg.step_down()
					elif event.key == pygame.K_LEFT:
						end = self.mg.step_left()
					elif event.key == pygame.K_RIGHT:
						end = self.mg.step_right()
					self.graph_maze()
					if end == c.WIN:
						self.surface.blit(pict_win, (0, 0))
					elif end == c.LOOSE:
						self.surface.blit(pict_loose, (0, 0))
				elif event.type == pygame.QUIT:
					end = True # (Est ce que je peux mettre exit() à cause du timer ?)
			pygame.display.flip()
		time.sleep(5)
		pygame.quit()


if __name__ == "__main__":
	maze = mz.Maze()
	syringe = sy.Syringe(maze)
	macgyver = mg.Macgyver(maze, syringe)
	gamegui = GameGui(maze, syringe, macgyver)
	maze.load()
	syringe.place_items()
	gamegui.play()