#! /usr/bin/env python3
# Coding: utf-8

"""This module is responsible for launching the game in graphical mode"""

import os
import pygame
import time

import maze
import syringe as syrg
import macgyver as macg
import constants as c


class GameGui:
    """Formatting the game with the methods of the other class and his own"""
    def __init__(self, maze, syrg, macg):
        """Constructor

        Params:
            maze: Instance of class Maze
            syrg: Instance of class Syringe
            macg: Instance of class Macgyver

        """
        self.maze = maze.Maze()
        self.maze.load()
        self.syrg = syrg.Syringe(self.maze)
        self.macg = macg.Macgyver(self.maze, self.syrg)
        self.surface = None

    def seek(self, picture):
        """Seek and return a path to the image

        Params:
            picture(str): Name of the image

        Return:
            A path to the image

        """
        dos = os.path.dirname(os.path.dirname(os.path.abspath((__file__))))
        path_to_file = os.path.join(dos, "pictures", picture)
        return path_to_file

    def presentation(self):
        """Customize the window

        Add an icon to the window
        Add a title to the window

        """
        pict_icon = pygame.image.load(self.seek(c.ICON_IMG))
        pygame.display.set_icon(pict_icon)
        pygame.display.set_caption(c.TITLE)

    def graph_maze(self):
        """Displays the maze in graphical mode

        Pygame initialization
        Create a Pygame window (480x480)
        Execute the method self.presentation()
        Upload all images
        Scan each line of the maze then each character
        Increment all positions by 32 (Picture format)
        Display each image on the window according to the scanned character,
        and its location. 'M'> Macgyver image, '#'> wall image etc...
        """
        pygame.init()
        self.surface = pygame.display.set_mode(c.WINDOW_SIZE)
        self.presentation()
        img_wall = pygame.image.load(self.seek(c.WALL_IMG)).convert_alpha()
        img_floor = pygame.image.load(self.seek(c.FLOOR_IMG)).convert_alpha()
        img_macg = pygame.image.load(self.seek(c.MACGYVER_IMG)).convert_alpha()
        img_murdoc = pygame.image.load(self.seek(c.MURDOC_IMG)).convert_alpha()
        img_needle = pygame.image.load(self.seek(c.NEEDLE_IMG)).convert_alpha()
        img_tube = pygame.image.load(self.seek(c.TUBE_IMG)).convert_alpha()
        img_ether = pygame.image.load(self.seek(c.ETHER_IMG)).convert_alpha()
        for i, line in enumerate(self.maze.structure):
            for j, element in enumerate(line):
                position = j * c.SPRITE_SIZE, i * c.SPRITE_SIZE
                if element == c.FLOOR:
                    self.surface.blit(img_floor, position)
                elif element == c.MACGYVER:
                    self.surface.blit(img_macg, position)
                elif element == c.MURDOC:
                    self.surface.blit(img_murdoc, position)
                elif element == c.NEEDLE:
                    self.surface.blit(img_needle, position)
                elif element == c.TUBE:
                    self.surface.blit(img_tube, position)
                elif element == c.ETHER:
                    self.surface.blit(img_ether, position)
                else:
                    self.surface.blit(img_wall, position)

    def show(self, size, written, color, location):
        """Show informations with pygame method font

        Params:
            size (int): Font size
            written (str): What we want to write
            color (tuple): R, G, B
            location (tuple): Abscissa, Ordinate

        Return:
            A customizable pygame text with a transparent background

        """
        font = pygame.font.Font(None, size)
        text = written
        ren = font.render(text, 1, color)
        return self.surface.blit(ren, location)

    def counter(self):
        """Show objects counter

        Use the self.show() method with the written parameter create,
        to take the length of the attributes self.macg.bag and self.syrg.items

        Return:
            A pygame text representing an object counter

        """
        items = len(self.syrg.items)
        bag = len(self.macg.bag)
        written = "Picked Objects : {} / {}".format(bag, items)
        return self.show(c.COUNT_SIZ, written, c.COUNT_COL, c.COUNT_LOC)

    def play(self):
        """Launch the game

        Proceedings:
        Place the objects
        Show the maze with pygame
        Show the object counter
        Declare 'end' and assign him False, to handle the end of the game
        Enter in the game loop, then in the pygame events loop
        Move Macgyver up, or down, or left, or right according to the user
        presses directional key up, or key down, or key left, or key right
        Display the maze with pygame
        Display the object counter
        Check the length self.macg.bag
        If it has the same length as self.syrg.items
        Display a pygame text (Made Syringe)
        Check the end conditions
        If won, display a pygame text (You win)
        If lost, display a pygame text (Game Over)
        Refresh window pygame

        """
        self.syrg.place_items()
        self.graph_maze()
        self.counter()
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        end = self.macg.step_up()
                    elif event.key == pygame.K_DOWN:
                        end = self.macg.step_down()
                    elif event.key == pygame.K_LEFT:
                        end = self.macg.step_left()
                    elif event.key == pygame.K_RIGHT:
                        end = self.macg.step_right()
                    self.graph_maze()
                    self.counter()
                    if len(self.macg.bag) == len(self.syrg.items):
                        self.show(c.SY_SIZ, c.SY_WRI, c.SY_COL, c.SY_LOC)
                    if end == c.WIN:
                        self.show(c.WIN_SIZ, c.WIN_WRI, c.WIN_COL, c.WIN_LOC)
                    elif end == c.LOOSE:
                        self.show(c.LOS_SIZ, c.LOS_WRI, c.LOS_COL, c.LOS_LOC)
                elif event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()
        time.sleep(3)
        pygame.quit()


def main():
    """Creating the GameGui object and launching the game"""
    gamegui = GameGui(maze, syrg, macg)
    gamegui.play()

if __name__ == "__main__":
    main()
