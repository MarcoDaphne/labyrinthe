#! /usr/bin/env python3
# Coding : utf-8

import maze as mz
import syringe as sy
import constants as c


class Macgyver:
    def __init__(self, mz, sy):
        self.mz = mz
        self.sy = sy
        self.bag = []

    def move_and_locate(self, i, j):
        """Move then locate MacGyver sur le labyrinthe"""
        self.mz.set(i, j, c.MACGYVER)
        self.mz.locate_macgyver(i, j)

    def pick_up_or_move(self, i, j):
        """Retrieves objects if existing or moves"""
        if self.mz.get(i, j) == c.NEEDLE:
            self.bag.append(c.NEEDLE)
            self.move_and_locate(i, j)
        elif self.mz.get(i, j) == c.TUBE:
            self.bag.append(c.TUBE)
            self.move_and_locate(i, j)
        elif self.mz.get(i, j) == c.ETHER:
            self.bag.append(c.ETHER)
            self.move_and_locate(i, j)
        elif len(self.bag) == len(self.sy.items) and (i, j) in self.mz.endl[0]:
            self.move_and_locate(i, j)
            return c.WIN
        elif (i, j) in self.mz.endl[0]:
            self.move_and_locate(i, j)
            return c.LOOSE
        else:
            self.move_and_locate(i, j)

    def step_up(self):
        """Move Macgyver one position up"""
        i, j = self.mz.macgyver_location
        strt = self.mz.structure
        get = self.mz.get(i - 1, j)
        if get != c.WALL and 0 < i < len(strt):
            self.mz.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i - 1, j)

    def step_right(self):
        """Move Macgyver one position to the right"""
        i, j = self.mz.macgyver_location
        strt = self.mz.structure
        get = self.mz.get(i, j + 1)
        if get != c.WALL and 0 < j < len(strt):
            self.mz.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i, j + 1)

    def step_down(self):
        """Move Macgyver one position down"""
        i, j = self.mz.macgyver_location
        strt = self.mz.structure
        get = self.mz.get(i + 1, j)
        if get != c.WALL and 0 <= i < len(strt):
            self.mz.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i + 1, j)

    def step_left(self):
        """Move Macgyver one position to the left"""
        i, j = self.mz.macgyver_location
        strt = self.mz.structure
        get = self.mz.get(i, j - 1)
        if get != c.WALL and 0 < j < len(strt):
            self.mz.set(i, j, c.FLOOR)
            return self.pick_up_or_move(i, j - 1)


if __name__ == "__main__":
    maze = mz.Maze()
    maze.load()
    syringe = sy.Syringe(maze)
    syringe.place_items()
    macgyver = Macgyver(maze, syringe)
    macgyver.step_up()
    macgyver.step_right()
    macgyver.step_down()
    macgyver.step_left()
