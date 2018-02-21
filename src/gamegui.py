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
        # (self.maze = mz.Maze) non fonctionnel)
        self.sy = sy
        self.mg = mg
        self.surface = ' '
        # (Comment initialiser self.surface ?)

    def seek(self, picture):
        """Seek and return a picture"""
        dos = os.path.dirname(os.path.dirname(os.path.abspath((__file__))))
        path_to_file = os.path.join(dos, "pictures", picture)
        return path_to_file

    def presentation(self):
        """Customize the icon and title of the window"""
        pict_icon = pygame.image.load(self.seek(c.ICON_IMG))
        pygame.display.set_icon(pict_icon)
        pygame.display.set_caption(c.TITLE)

    def graph_maze(self):
        """Displays the maze in graphical mode"""
        pygame.init()
        self.surface = pygame.display.set_mode(c.WINDOW_SIZE)
        self.presentation()
        img_wall = pygame.image.load(self.seek(c.WALL_IMG)).convert_alpha()
        img_floor = pygame.image.load(self.seek(c.FLOOR_IMG)).convert_alpha()
        img_macg = pygame.image.load(self.seek(c.MACGYVER_IMG)).convert_alpha()
        img_murdoc = pygame.image.load(self.seek(c.GATEKEEPER_IMG)).convert_alpha()
        img_needle = pygame.image.load(self.seek(c.NEEDLE_IMG)).convert_alpha()
        img_tube = pygame.image.load(self.seek(c.TUBE_IMG)).convert_alpha()
        img_ether = pygame.image.load(self.seek(c.ETHER_IMG)).convert_alpha()
        for i, line in enumerate(self.mz.structure):
            for j, element in enumerate(line):
                position = j * c.SPRITE_SIZE, i * c.SPRITE_SIZE
                if element == c.FLOOR:
                    self.surface.blit(img_floor, position)
                elif element == c.MACGYVER:
                    self.surface.blit(img_macg, position)
                elif element == c.GATEKEEPER:
                    self.surface.blit(img_murdoc, position)
                elif element == c.NEEDLE:
                    self.surface.blit(img_needle, position)
                elif element == c.TUBE:
                    self.surface.blit(img_tube, position)
                elif element == c.ETHER:
                    self.surface.blit(img_ether, position)
                else:
                    self.surface.blit(img_wall, position)

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
                    end = True
                    # (Est ce que je peux mettre exit() à cause du timer ?)
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
