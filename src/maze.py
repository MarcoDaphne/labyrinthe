#! /usr/bin/env python3
# coding: utf-8

import os

import constants as c


class Maze:
    def __init__(self):
        self.structure = []
        self.free_pos = []
        self.macgyver_location = ()
        self.endl = []

    def load(self, data="data", data_file="schema.txt"):
        """Loads a maze from a text file and retrieves useful positions"""
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_file = os.path.join(directory, data, data_file)
        with open(path_to_file) as f:
            for i, line in enumerate(f):
                clean_line = line.strip()
                liste = list(clean_line)
                self.structure.append(liste)
                for j, element in enumerate(liste):
                    if element == c.FLOOR:
                        self.free_pos.append((i, j))
                    elif element == c.MACGYVER:
                        self.macgyver_location = i, j
                    elif element == c.GATEKEEPER:
                        self.endl.append(
                            ((i-1, j), (i+1, j), (i, j-1), (i, j+1)))
        return self.structure, self.free_pos, self.macgyver_location, self.endl

    def get(self, i, j):
        """Gets a position in the maze"""
        return self.structure[i][j]

    def set(self, i, j, element):
        """Install an element on a maze position"""
        self.structure[i][j] = element

    def locate_macgyver(self, i, j):
        """locate MacGyver after each move"""
        self.macgyver_location = i, j

    def show(self):
        """Displays the maze"""
        for line in self.structure:
            print(line)


if __name__ == "__main__":
    maze = Maze()
    maze.load()
    maze.show()
