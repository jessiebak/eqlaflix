import os
import datetime
import mysql.connector
from Execute_Req import *

sortHeader = [ "Tri par défaut", "mots clés ", "Jeux sorties en : ", "Jeux sortis avant : " , "Jeux sorties après : "]



os.system("cls")


def SortMenuSentence(_sortList):
    _fimMenuSentence = "Bienvenu cHEZ EqlaFlix/Games. \n Veuillez choisir les différentes options d'affichage : "
    for name in filmHeader: 
        if filmHeader.index(name) in _sortList:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name + "       ( X )"
        else:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name
    _fimMenuSentence += "\n \"OK\" -   pour Afiicher les jeux \n \"Q\" -	Pour quitter le menu de jeux \n Entrez votre choix n° " + str(len(_sortList) + 1) + " : "
    return _fimMenuSentence


# Cette fonction retourne la liste des options de Films à afficher;
def SortMenu2(): 
    _sortList = []
    _fimMenuSentence = FilmMenuSentence(_sortList)
    _userChoice = input(_fimMenuSentence).lower()
    os.system('cls')
    while _userChoice != "ok" and _userChoice != "q" and _userChoice != "":
        try: 
            _userChoice = int(_userChoice)
            if _userChoice == 0 : 
                return defaultHeaderList
            elif 1<= _userChoice < len(filmHeader) :
                if _userChoice in _sortList: 
                    print(f"\n {_userChoice} - {filmHeader[_userChoice]} a déjà été sélectionné. ")
                else:
                    _sortList.append(_userChoice)
            else: 
                _fimMenuSentence = FilmMenuSentence(_sortList)
                _userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _fimMenuSentence ).lower()
                os.system('cls')
            print(f"\n 0{len(_sortList)} sélection(s) éffectuée(s). ")
            _fimMenuSentence = FilmMenuSentence(_sortList)
            _userChoice = input( "\n " + _fimMenuSentence).lower()
            os.system("cls")
        except:
            _fimMenuSentence = FilmMenuSentence(_sortList)
            _userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _fimMenuSentence).lower()
            os.system('cls')
        _fimMenuSentence = FilmMenuSentence(_sortList)
    else: 
        if _userChoice == "q": 
            # return -1
            sys.exit()
        elif (_userChoice == "ok" and len(_sortList) != 0) or (_userChoice == "" and len(_sortList) != 0): 
            return _sortList
        elif (_userChoice == "ok" and len(_sortList) == 0) or (_userChoice == "" and len(_sortList) == 0):
            return defaultHeaderList



def SortMainMenu(_req): 
    print("MENU DE TRI : ")
    for i in sortHeader:
        print(str(sortHeader.index(i) + 1 ), " - " , i )
    userChoice = TakePositifNumber(input("Votre choix: "))
    while not(1 <= userChoice <= 5):
        userChoice = TakePositifNumber(input("Votre choix: "))
    else:
        if userChoice == 1:
            _req += " order by Videogames_Titre asc;" 
            return _req
        elif userChoice == 2: 
            value = "%" + input("terme à rechercher : ") + "%"
            _req += " where (Videogames_Titre like '" + value + "' or Videogames_Développeur like '" + value + "' or Videogames_Editeur like '" + value + "' or Videogames_Categorie like '" + value + "' ) order by Videogames_Titre asc;"
            return _req
        elif userChoice == 3 : 
            value = "%" + str(TakePositifNumber(input("année recherchée : "))) + "%"
            _req += " where Videogames_DateSortie like '" + value + "' order by Videogames_Titre asc;" 
            return _req
        elif userChoice == 4 : 
            value = TakeDate(input("entrez une date au format \"aaaa/mm/jj\" : "))
            _req += " where Videogames_DateSortie <= '" + value + "' order by Videogames_DateSortie desc;"
            return _req
        elif userChoice == 5 : 
            value = TakeDate(input("entrez une date au format \"aaaa/mm/jj\" : "))
            _req += " where Videogames_DateSortie >= '" + str(value) + "' order by Videogames_DateSortie asc;"
            return _req
        


    

# IDVieogames      Videogames_Titre      Videogames_DateSortie     Videogames_Développeur     Videogames_Editeur     Videogames_Categorie
