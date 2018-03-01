#! /usr/bin/env python3
# Coding : utf-8

import maze
import syringe as syrg
import constants as c

"""This module is responsible for determining the possibilities of MacGyver"""


class Macgyver:
    """This class creates MacGyver's movements

    Go up, down, left, right, pick up, lose or win.

    """
    def __init__(self, maze, syrg):
        """Constructor

        params:
            maze: Instance of class Maze
            syrg: Instance of class syringe

        """
        self.maze = maze
        self.syrg = syrg
        self.bag = []

    def move_and_locate(self, i, j):
        """Move then locate MacGyver sur le labyrinthe

        Params:
            i (int): Ordinate of maze
            j (int): Abscissa of maze

        """
        self.maze.set(i, j, c.MACGYVER)
        self.maze.locate_macgyver(i, j)

    def pick_up_or_move(self, i, j):
        """Retrieves objects if existing or moves

        According to the movement,
        Check if there is an object,
        Pick it up if yes,
        Otherwise continue
        Check if all items in the bag and if MacGyver is in front of Murdoc,
        Won if so,
        if not Lose.

        Params:
            i (int): Ordinate of maze
            j (int): Ordinate of maze

        Return:
            str: If you win
            str: If you lose

        """
        sprite = self.maze.get(i, j)
        end = self.maze.endl[0]
        if sprite in self.syrg.items:
            self.bag.append(sprite)
            self.move_and_locate(i, j)
        elif len(self.bag) == len(self.syrg.items) and (i, j) in end:
            self.move_and_locate(i, j)
            return c.WIN
        elif (i, j) in end:
            self.move_and_locate(i, j)
            return c.LOOSE
        else:
            self.move_and_locate(i, j)

    def step_up(self):
        """Move Macgyver one position up

        Check if the position above MacGyver's location is not a wall,
        or out of the maze. If this is not the case replace the MacGyver's
        location with a blank space and return self.pick_up_or_move() with
        the position above as the parameter.

        Return:
            str: Return value of the (self.pick_up_or_move()) method

        """
        i, j = self.maze.macgyver_location
        strt = self.maze.structure
        get = self.maze.get(i - 1, j)
        if get != c.WALL and 0 < i < len(strt):
            self.maze.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i - 1, j)

    def step_right(self):
        """Move Macgyver one position to the right

        Check if the position to the right MacGyver's location is not a wall,
        or out of the maze. If this is not the case replace the MacGyver's
        location with a blank space and return self.pick_up_or_move() with
        the position to the right as the parameter.

        Return:
            str: Return value of the (self.pick_up_or_move()) method

        """
        i, j = self.maze.macgyver_location
        strt = self.maze.structure
        get = self.maze.get(i, j + 1)
        if get != c.WALL and 0 < j < len(strt):
            self.maze.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i, j + 1)

    def step_down(self):
        """Move Macgyver one position down

        Check if the position below MacGyver's location is not a wall,
        or out of the maze. If this is not the case replace the MacGyver's
        location with a blank space and return self.pick_up_or_move() with
        the position below as the parameter.

        Return:
            str: Return value of the (self.pick_up_or_move()) method

        """
        i, j = self.maze.macgyver_location
        strt = self.maze.structure
        get = self.maze.get(i + 1, j)
        if get != c.WALL and 0 <= i < len(strt):
            self.maze.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i + 1, j)

    def step_left(self):
        """Move Macgyver one position to the left

        Check if the position to the right MacGyver's location is not a wall,
        or out of the maze. If this is not the case replace the MacGyver's
        location with a blank space and return self.pick_up_or_move() with
        the position to the right as the parameter.

        Return:
            str: Return value of the (self.pick_up_or_move()) method

        """
        i, j = self.maze.macgyver_location
        strt = self.maze.structure
        get = self.maze.get(i, j - 1)
        if get != c.WALL and 0 < j < len(strt):
            self.maze.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i, j - 1)


if __name__ == "__main__":
    maze = maze.Maze()
    maze.load()
    syringe = syrg.Syringe(maze)
    syringe.place_items()
    macgyver = Macgyver(maze, syringe)
    macgyver.step_up()
    macgyver.step_right()
    macgyver.step_down()
    macgyver.step_left()
