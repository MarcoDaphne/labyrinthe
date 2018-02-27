#! /usr/bin/env python3
# Coding : utf-8

"""This module is responsible for launching the game"""

import maze as mz
import syringe as sy
import macgyver as mg
import constants as c


class Game:
    """Formatting the game with the methods of the other class and his own"""
    def __init__(self, mz, sy, mg):
        """Constructor

        Params:
            mz: Instance of class Maze
            sy: Instance of class Syringe
            mg: Instance of class Macgyver

        """
        self.mz = mz
        self.sy = sy
        self.mg = mg
        self.want_play = None
        self.get_direction = None

    def get_answer(self):
        """Asks the user if he wants to play

        Return:
            str : a letter

        """
        self.want_play = input("Souhaitez-vous jouer ?('o' / 'n')\n")
        return self.want_play

    def choose_direction(self):
        """Asks the user in which direction he wants to move MacGyver

        Return:
            str : a letter

        """
        self.get_direction = input("""
Utiliser les touches ou sur 'l' pour quitter:
'z': Haut    'q': Gauche    'd': Droite    's': Bas
""")
        return self.get_direction

    def move(self):
        """Move MacGyver according to the user's choice

        If the method get_direction() return a 'z' or 's' or 'q' or 'd',
        MacGyver wiil go up or down or left or right.
        This method wiil determine whether the user has won or not,
        if the conditions are met or not in the method pick_up_or_move()
        in the class Macgyver.
        If the method get_direction() return a 'l' the user leaves the game.

        """
        if self.get_direction == c.UP:
            return self.mg.step_up()
        elif self.get_direction == c.DOWN:
            return self.mg.step_down()
        elif self.get_direction == c.LEFT:
            return self.mg.step_left()
        elif self.get_direction == c.RIGHT:
            return self.mg.step_right()
        elif self.get_direction == c.LEAVE:
            exit()

    def show_pickup(self):
        """Notifies each object picked up

        Displays the comparison between the number of elements in the bag,
        and the number of elements composing the syringe.
        Then displays in more detail the name of each item picked up,
        when it is picked up.

        """
        print("""
Vous avez {}/{} objets.
        """.format(len(self.mg.bag), len(self.sy.items)))
        for item in self.mg.bag:
            if item == c.NEEDLE:
                print("- Aiguille", end=" ")
            elif item == c.TUBE:
                print("- Tube", end=" ")
            elif item == c.ETHER:
                print("- Fiole d'Ether", end=" ")
        print()

    def start(self):
        """Launch the game

        Proceedings:
        Load the maze, then display the maze
        Ask the user if he wants to play
        If yes, place the objects on the maze, if not leave the game
        Enter in the game loop
        Display the maze with placed objects
        Show the object counter
        Ask the user which way the user wants to move Macgyver
        Move Macgyver
        Check the end of game conditions
        if won, display congratulation
        if lost, display you lost

        """
        loading = self.mz.load()
        display = self.mz.show()
        play = self.get_answer()
        end = False
        if play == c.YES:
            set_items = self.sy.place_items()
            while not end:
                display = self.mz.show()
                notify_pickup = self.show_pickup()
                choice = self.choose_direction()
                end = self.move()
            if end == c.WIN:
                display = self.mz.show()
                print("\nBravo!!! \nVous avez endormi Murdoc.")
            elif end == c.LOOSE:
                display = self.mz.show()
                print("\nMurdoc a tué MacGyver!!!")


if __name__ == '__main__':
    maze = mz.Maze()
    syringe = sy.Syringe(maze)
    macgyver = mg.Macgyver(maze, syringe)
    game = Game(maze, syringe, macgyver)
    game.start()
