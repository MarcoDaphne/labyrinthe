#! /usr/bin/env python3
# Coding: utf-8

import os
import pygame

import maze as mz
import syringe as sy
import macgyver as mg
import game as g
import constants as c


class GameGui:
	def __init__(self, mz, sy, mg, g):
		self.mz = mz
		self.sy = sy
		self.mg = mg
		self.g = g

	def seek(self, picture):
		"""Seek and return a picture"""
		directory = os.path.dirname(os.path.dirname(os.path.abspath((__file__))))
		path_to_file = os.path.join(directory, "pictures", picture)
		return path_to_file

	def graph_maze(self):
		"""Displays the maze in graphical mode"""
		pygame.init()
		surface = pygame.display.set_mode((480, 640))
		p_wall = pygame.image.load(self.seek("wall.png")).convert_alpha()
		p_floor = pygame.image.load(self.seek("grass.png")).convert()
		p_macgyver = pygame.image.load(self.seek("macgyver.png")).convert_alpha()
		p_gatekeeper = pygame.image.load(self.seek("murdoc.png")).convert_alpha()
				
		i = 160
		for line in self.mz.structure:
			j = 0
			for element in line:
				if element == ' ':
					surface.blit(p_floor, (j, i))
				elif element == 'M':
					surface.blit(p_macgyver, (j, i))
				elif element == 'G':
					surface.blit(p_gatekeeper, (j, i))
				else:
					surface.blit(p_wall, (j, i))
				j += 32
			i += 32

		end = False
		while not end:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					end = True
			pygame.display.flip()
		pygame.quit()

if __name__ == "__main__":
	maze = mz.Maze()
	maze.load()
	syringe = sy.Syringe(maze)
	macgyver = mg.Macgyver(maze, syringe)
	game = g.Game(maze, syringe, macgyver)
	gamegui = GameGui(maze, syringe, macgyver, game)
	gamegui.graph_maze()