#! /usr/bin/env python3
# coding: utf-8

"""
Module attend to load a text file(containing a maze drawing).
Scan each line of the file to retrieve key informations,
for attributes and methods in the class.
Displays a maze
"""

import os

import constants as c


class Maze:
    """Create a labyrinth from a text file"""
    def __init__(self):
        """Constructor"""
        self.structure = []
        """Empty list: Will contain the lists forming the maze"""
        self.free_pos = []
        """Empty list: Will contain the free positions"""
        self.macgyver_location = ()
        """Empty tuple: Will contain Macgyver position"""
        self.endl = []
        """Empty list: Will contain the positions determining
        the end of the game
        """

    def load(self, data="data", data_file="schema.txt"):
        """Load a maze from a text file
        Scan each line of the text file and incrementing i,
        Append each line in list,
        Append the lists in list (self.structure).
        Scan each character in lists and incrementing j,
        Append each free charater "space" in list (self.free_pos).
        Get "M" position (i, j) back in a tuple (self.macgyver_location).
        Append all positions around "G" in list (self.endl)

        Args:
            data: Directory containing the text file
            data_file: file containing the maze drawing

        returns:
            list: List of lists in the .txt file
            list: List of free positions
            tuple: Macgyver position
            list: List of end game positions

        """
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
                    elif element == c.MURDOC:
                        self.endl.append(
                            ((i-1, j), (i+1, j), (i, j-1), (i, j+1)))
        return self.structure, self.free_pos, self.macgyver_location, self.endl

    def get(self, i, j):
        """Get a position in self.structure

        Args:
            i (int): integer representing one of the self.structure lists
            j (int): integer representing the index of a list

        returns:
            A (i, j) position in self.structure

        """
        return self.structure[i][j]

    def set(self, i, j, element):
        """Install an element on a maze position

        Args:
            i (int): integer representing one of the self.structure lists
            j (int): integer representing the index of a list
            element (str): Change a character of the (i, j) position

        """
        self.structure[i][j] = element

    def locate_macgyver(self, i, j):
        """locate MacGyver after each move

        Args:
            i (int): integer representing one of the self.structure lists
            j (int): integer representing the index of a list

        """
        self.macgyver_location = i, j

    def show(self):
        """Cleanly displays the maze"""
        for line in self.structure:
            print(line)


if __name__ == "__main__":
    maze = Maze()
    maze.load()
    maze.show()
