import os
import datetime
import mysql.connector
from films.Execute_Req import *

os.system("cls")


# cette fonction affiche la liste des différents films et permet de choisir un filme à modifier et renvoit son id
# attention _filmToModify fait reférence à toute la partie Display
def ChooseFilmInTable(_filmToModify, _header, _headerToPrint): 
    print("sélectionnez l'élément à modifier  dans cette liste. ")
    _userInput = input("\n votre choix : ")
   
    while not (IsPositiveNumber(_userInput) and int(_userInput) <= len(_filmToModify) ) : 
        print("Veuillez entrer un nombre valide ")
        _userInput =  input("Entrer le N° de l'item à supprimer ") 
    else:
        print("Voilà le film à modifier : ")
        Execute_Req( """ SELECT * FROM FILMS WHERE idfilm = %s """ % ( _filmToModify[int(_userInput)] ), _header, _headerToPrint)
    return _filmToModify[int(_userInput)] 


# cette fonction va modifier le film choisit 
def UpdateFilmReq(_id, _filmToSave): 
    req = """UPDATE films SET Titre = %s, realisateur= %s, pays= %s, boxoffice= %s, DateSortie= %s, Genre= %s WHERE idfilm = %s"""
    data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _filmToSave[5], _id)
    Execute_ReqInsert(req, data)






# id = ChooseInTable(DisplayFilms, _header, _headerToPrint)
# filmToSave = ChooseInTable(AddFilm())
# UpdateFilmReq(_id, _filmToSave)


# filmHeadertoPrint = [1, 2, 3, 4, 5, 6, 7]

# filmlist = {1: 63, 2: 8, 3: 37, 4: 7, 5: 6, 6: 10, 7: 2, 8: 17, 9: 50, 10: 38, 11: 31, 12: 34, 13: 5, 14: 3, 15: 35, 16: 40, 17: 14, 18: 4, 19: 27, 20: 39, 21: 42, 22: 18, 23: 49, 24: 33, 25: 28, 26: 43, 27: 36, 28: 16, 29: 32, 30: 13, 31: 12, 32: 24, 33: 25, 34: 20, 35: 23, 36: 44, 37: 48, 38: 9, 39: 26, 40: 11, 41: 45, 42: 15, 43: 30, 44: 19, 45: 52, 46: 21, 47: 1, 48: 22, 49: 51, 50: 29, 51: 47, 52: 41}

# id = ChooseFilmInTable(filmlist, filmHeader, filmHeadertoPrint)
# print(id)
# filmToSave = ChooseInTable(AddFilm())
# print(filmToSave)
# UpdateFilmReq(id, filmToSave)

# print(ChooseInTable([]))
