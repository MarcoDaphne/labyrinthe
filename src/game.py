#! /usr/bin/env python3
# Coding : utf-8

"""-tc- Ajouter une docstring de fichier"""

import maze as mz
import syringe as sy
import macgyver as mg
import constants as c


class Game:
    """-tc- Ajouter une docstring de classe"""

    def __init__(self, mz, sy, mg):
        """-tc- Ajouter une docstring pour chaque fichier"""
        self.mz = mz
        self.sy = sy
        self.mg = mg
        self.want_play = c.EMPTY
        self.get_direction = c.EMPTY

    def get_answer(self):
        """Asks the user if he wants to play"""
        self.want_play = input("Souhaitez-vous jouer ?('o' / 'n')\n")
        return self.want_play

    def choose_direction(self):
        """Asks the user in which direction he wants to move MacGyver"""
        self.get_direction = input("""
Utiliser les touches ou sur 'l' pour quitter:
'z': Haut    'q': Gauche    'd': Droite    's': Bas
""")
        return self.get_direction

    def move(self):
        """Move MacGyver according to the user's choice"""
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
        """Notifies each object picked up"""
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
        """Launch the game"""
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


def main():
    maze = mz.Maze()
    syringe = sy.Syringe(maze)
    macgyver = mg.Macgyver(maze, syringe)
    game = Game(maze, syringe, macgyver)
    game.start()

if __name__ == '__main__':
    main()
