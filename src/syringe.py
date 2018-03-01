#! /usr/bin/env python3
# Coding: utf-8

"""This Module is responsible for placing random objects in the maze."""

import random

import maze
import constants as c


class Syringe:
    """This class represents a decomposed syringe.

    Each piece is randomly placed in the maze.

    """
    def __init__(self, maze):
        """Constructor

        Params:
            maze: Instance of class Maze

        """
        self.maze = maze
        self.items = [c.NEEDLE, c.TUBE, c.ETHER]

    def find_random_positions(self):
        """Find random positions

        Transform lists into sets
        Extract free positions in freeway
        Choose positions (from the number of objects in self.items) in freeway

        return:
            list: A list of tuples

        """
        passage = set(self.maze.free_pos)
        end_positions = set(self.maze.endl[0])
        freeway = passage - end_positions
        chosen_positions = random.sample(freeway, len(self.items))
        return chosen_positions

    def place_items(self):
        """Place objects randomly on the maze

        Get the list of tuples in find_random_positions()
        According to the number of objects in items
        Get a position in list of tuples
        Place the object accordind to this position

        """
        position = self.find_random_positions()
        for n, item in enumerate(self.items):
            i, j = position[n]
            self.maze.set(i, j, item)


if __name__ == "__main__":
    maze = maze.Maze()
    syringe = Syringe(maze)
    maze.load()
    syringe.place_items()
    maze.show()
