import os
import datetime
import mysql.connector
from jeux.Execute_Req import *

os.system("cls")

# filmHeader2 = ["TITRE(VF)", "TITRE(VO)", "DESCRIPTION", "ACTEUR PRINCIPAL" , "DATE DE SORTIE", "NOMBRE D'EPISODE", "NOMBRE DE SAISONS" ]

# cette fonction affiche la liste des différents films et permet de choisir une serie à modifier et renvoit son id
# attention _filmToModify fait reférence à toute la partie Display
def ChooseFilmInTable(_filmToModify, _header, _headerToPrint): 
    print("sélectionnez l'élément à modifier  dans cette liste. ")
    _userInput = input("\n votre choix : ")
   
    while not (IsPositiveNumber(_userInput) and int(_userInput) <= len(_filmToModify) ) : 
        print("Veuillez entrer un nombre valide ")
        _userInput =  input("Entrer le N° de l'item à supprimer ") 
    else:
        print("Voilà le jeu à modifier : ")
        Execute_Req( """ SELECT * FROM Videogames WHERE IDVieogames = %s """ % ( _filmToModify[int(_userInput)] ), _header, _headerToPrint)
    return _filmToModify[int(_userInput)] 


# cette fonction va modifier le jeu choisi
def UpdateFilmReq(_id, _filmToSave): 
    req = """UPDATE Videogames SET Videogames_Titre = %s, Videogames_Développeur= %s, Videogames_Editeur= %s, Videogames_Categorie = %s , Videogames_DateSortie= %s WHERE IDVieogames = %s"""
    data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _id)
    Execute_ReqInsert(req, data)




# IDVieogames      Videogames_Titre      Videogames_DateSortie     Videogames_Développeur     Videogames_Editeur     Videogames_Categorie
