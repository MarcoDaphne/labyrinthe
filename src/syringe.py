#! /usr/bin/env python3
# Coding: utf-8

import random

import maze as mz
import constants as c


class Syringe:
    def __init__(self, mz):
        self.mz = mz
        self.items = [c.NEEDLE, c.TUBE, c.ETHER]

    def find_random_positions(self):
        """Return a random position"""
        passage = set(self.mz.free_pos)
        end_positions = set(self.mz.endl[0])
        freeway = passage - end_positions
        chosen_positions = random.sample(freeway, len(self.items))
        return chosen_positions

    def place_items(self):
        """Place three objects randomly on the maze"""
        position = self.find_random_positions()
        for n, item in enumerate(self.items):
            i, j = position[n]
            self.mz.set(i, j, item)


if __name__ == "__main__":
    maze = mz.Maze()
    syringe = Syringe(maze)
    maze.load()
    syringe.place_items()
    maze.show()
