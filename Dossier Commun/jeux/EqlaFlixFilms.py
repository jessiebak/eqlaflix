import sys
import os
import time
from jeux import EF_filmsDisplay as EFD
from jeux import EF_AddFilm as EFA
from jeux import EF_Delete as EFDel
from jeux import EF_Search as EFS
from jeux import EF_modify as EFM
from jeux import EF_sort as EFSo

os.system('cls')


# cette fonction gére le menu principal des jeux 
def DisplayFilmsMenu(): 
    _menuSentence = "\n EqleFlix/Games \n 1- Afficher \n 2- Modifier \n 3- Ajouter \n 4- Supprimer \n 5- Rechercher \n 6- Affichage Aléatoire \n 7- Tri \n  \"Q\"-	Pour quitter  \n Votre choix : "
    _userChoice = input(_menuSentence).lower()
    os.system('cls')
    while _userChoice != "q":
        try: 
            _userChoice = int(_userChoice)
            if _userChoice == 1 :
                _filmHeadertoPrint = EFD.FilmHeaderToPrint()
                EFD.Execute_Req(EFD.DisplayOptionsReq(_filmHeadertoPrint), EFD.filmHeader, _filmHeadertoPrint)
            elif _userChoice == 2 : 
                filmHeadertoPrint = EFD.FilmHeaderToPrint()
                id = EFM.ChooseFilmInTable(EFD.Execute_Req(EFD.DisplayOptionsReq(filmHeadertoPrint), EFD.filmHeader, filmHeadertoPrint), EFD.filmHeader, filmHeadertoPrint)
                EFM.UpdateFilmReq(id, EFM.AddFilm())
            elif _userChoice == 3: 
                EFA.SaveFilmReq(EFA.AddFilm())
            elif _userChoice == 4: 
                _filmHeadertoPrint = EFD.FilmHeaderToPrint()
                EFDel.ChooseInTable(EFD.Execute_Req(EFD.DisplayOptionsReq(_filmHeadertoPrint), EFD.filmHeader, _filmHeadertoPrint))
            elif _userChoice == 5: 
                _filmHeadertoPrint = EFD.FilmHeaderToPrint()
                EFD.Execute_Req( EFS.SortMainMenu(EFD.DisplaySearchReq(_filmHeadertoPrint)), EFD.filmHeader, _filmHeadertoPrint)
            elif _userChoice == 6: 
                _filmHeadertoPrint = EFD.FilmHeaderToPrint()
                EFD.Execute_ReqRandom(EFD.DisplayOptionsReq(_filmHeadertoPrint), EFD.filmHeader, _filmHeadertoPrint)
            elif _userChoice == 7: 
                EFSo.DisplaySortingMenu()
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











