import os
import datetime
import mysql.connector
from series.Execute_Req import *

sortHeader = [ "Tri par défaut", "mots clés ", "Series sorties en : ", "Series sortis avant : " , "Series sorties après : ", "ayant aumoins ... Saisons"]



os.system("cls")


def SortMenuSentence(_sortList):
    _fimMenuSentence = "Bienvenu cHEZ EqlaFlix/SERIES. \n Veuillez choisir les différentes options d'affichage : "
    for name in filmHeader: 
        if filmHeader.index(name) in _sortList:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name + "       ( X )"
        else:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name
    _fimMenuSentence += "\n \"OK\" -   pour Afiicher les Series \n \"Q\" -	Pour quitter le menu de Series \n Entrez votre choix n° " + str(len(_sortList) + 1) + " : "
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
    while not(1 <= userChoice <= 6):
        userChoice = TakePositifNumber(input("Votre choix: "))
    else:
        if userChoice == 1:
            _req += " order by Serie_TitreVF asc;" 
            return _req
        elif userChoice == 2: 
            value = "%" + input("terme à rechercher : ") + "%"
            _req += " where (Serie_TitreVF like '" + value + "' or Serie_TitreVO like '" + value + "' or Serie_Description like '" + value + "' or Serie_ActeurPrincipal like '" + value + "' ) order by Serie_TitreVO asc;"
            return _req
        elif userChoice == 3 : 
            value = "%" + str(TakePositifNumber(input("année recherchée : "))) + "%"
            _req += " where Serie_DateSortie like '" + value + "' order by Serie_TitreVF asc;" 
            return _req
        elif userChoice == 4 : 
            value = TakeDate(input("entrez une date au format \"aaaa/mm/jj\" : "))
            _req += " where Serie_DateSortie <= '" + value + "' order by Serie_DateSortie desc;"
            return _req
        elif userChoice == 5 : 
            value = TakeDate(input("entrez une date au format \"aaaa/mm/jj\" : "))
            _req += " where Serie_DateSortie >= '" + str(value) + "' order by Serie_DateSortie asc;"
            return _req
        elif userChoice == 6 : 
            value = TakePositifNumber(input("entrez une valeur : "))
            _req += " where Serie_Saisons >= " + str(value) + " order by Serie_Saisons asc;"
            return _req


    

# IDSerie  Serie_TitreVF         Serie_TitreVO        Serie_DateSortie      Series_Episode      Serie_Saisons    Serie_Description    Serie_ActeurPrincipal
