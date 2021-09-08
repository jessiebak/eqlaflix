import sys
import os
# from films.EqlaFlixFilms import *
from films import EqlaFlixFilms as Films
from series import EqlaFlixFilms as Series
from jeux import EqlaFlixFilms as Jeux

os.system('cls')

# cette fonction gére le menu principal de  EQLAFLIX
def EQLAFLIX(): 
    _menuSentence = "\n EQLA-FLIX \n 1- JEUX \n 2- FILMS \n 3- SERIES \n \"Q\"-	Pour quitter  \n Votre choix : "
    _userChoice = input(_menuSentence).lower()
    os.system('cls')
    while _userChoice != "q":
        try: 
            _userChoice = int(_userChoice)
            if _userChoice == 1 :
                Jeux.DisplayFilmsMenu()
            elif _userChoice == 2 : 
                Films.DisplayFilmsMenu()
            elif _userChoice == 3: 
                Series.DisplayFilmsMenu()
            else: 
                _userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _menuSentence ).lower()
                os.system('cls')
            _userChoice = input(_menuSentence).lower()
            os.system('cls')
        except:
            _userChoice = input( _menuSentence).lower()
            os.system('cls')
        print("\n")
    else: 
        sys.exit()


EQLAFLIX()









