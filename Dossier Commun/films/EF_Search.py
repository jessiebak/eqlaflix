import os
import datetime
import mysql.connector
from films.Execute_Req import *

sortHeader = [ "Tri par défaut", "mots clés ", "films sortis en : ", "film sortis avant : " , "film sortis après : ", "ayant aumoins ... entrées au B.O"]



os.system("cls")


def SortMenuSentence(_sortList):
    _fimMenuSentence = "Bienvenu cHEZ EqlaFlix/FILMS. \n Veuillez choisir les différentes options d'affichage : "
    for name in filmHeader: 
        if filmHeader.index(name) in _sortList:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name + "       ( X )"
        else:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name
    _fimMenuSentence += "\n \"OK\" -   pour Afiicher les films \n \"Q\" -	Pour quitter le menu de Films \n Entrez votre choix n° " + str(len(_sortList) + 1) + " : "
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
            _req += " order by titre asc;" 
            return _req
        elif userChoice == 2: 
            value = "%" + input("terme à rechercher : ") + "%"
            _req += " and (titre like '" + value + "' or realisateur like '" + value + "' or pays like '" + value + "' or datesortie like '" + value + "' ) order by titre asc;"
            return _req
        elif userChoice == 3 : 
            value = "%" + str(TakePositifNumber(input("année recherchée : "))) + "%"
            _req += " and datesortie like '" + value + "' order by titre asc;" 
            return _req
        elif userChoice == 4 : 
            value = TakeDate(input("entrez une date au format \"aaaa/mm/jj\" : "))
            _req += " and datesortie <= '" + value + "' order by datesortie desc;"
            return _req
        elif userChoice == 5 : 
            value = TakeDate(input("entrez une date au format \"aaaa/mm/jj\" : "))
            _req += " and datesortie >= '" + str(value) + "' order by datesortie asc;"
            return _req
        elif userChoice == 6 : 
            value = TakePositifNumber(input("entrez une valeur : "))
            _req += " and BoxOffice >= " + str(value) + " order by BoxOffice asc;"
            return _req



def RandomSearch(): 
    randNum = TakePositifNumber(input("Combien de films aléatoires souhaitez vous générer ? "))
    connection = AllUsersConnection()
    Cursor = connection.cursor() 
    req = "select count(*) from films;"
    Cursor.execute(req)
    maxNum = Cursor.fetchone()
    


# print(SortMainMenu(""))
# print(SortMenu2())


# RandomSearch()