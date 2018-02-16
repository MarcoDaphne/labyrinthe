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

	def title(self, surface):
		pygame.draw.rect(surface, (255, 153, 102), (0, 0, 480, 60))
		# Possible Ecriture colorée sur fond noir

	def graph_maze(self):
		"""Displays the maze in graphical mode"""
		pygame.init()
		surface = pygame.display.set_mode((480, 640))
		self.title(surface)
		p_wall = pygame.image.load(self.seek("wall.png")).convert_alpha()
		p_floor = pygame.image.load(self.seek("grass.png")).convert_alpha()
		p_macgyver = pygame.image.load(self.seek("macgyver.png")).convert_alpha()
		p_gatekeeper = pygame.image.load(self.seek("murdoc.png")).convert_alpha()
		p_needle = pygame.image.load(self.seek("needle.png")).convert_alpha()
		p_tube = pygame.image.load(self.seek("tube.png")).convert_alpha()
		p_ether = pygame.image.load(self.seek("ether.png")).convert_alpha()
				
		i = 60
		for line in self.mz.structure:
			j = 0
			for element in line:
				if element == ' ':
					surface.blit(p_floor, (j, i))
				elif element == 'M':
					surface.blit(p_macgyver, (j, i))
				elif element == 'G':
					surface.blit(p_gatekeeper, (j, i))
				elif element == 'N':
					surface.blit(p_needle, (j, i))
				elif element == 'T':
					surface.blit(p_tube, (j, i))
				elif element == 'E':
					surface.blit(p_ether, (j, i))
				else:
					surface.blit(p_wall, (j, i))
				j += 32
			i += 32

	def want_play(self):
		self.graph_maze()
		end = False
		while not end:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_o:
						self.sy.place_items()
						self.graph_maze()
				elif event.type == pygame.QUIT:
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
	#syringe.place_items()
	gamegui.want_play()