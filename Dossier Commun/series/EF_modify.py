import os
import datetime
import mysql.connector
from Execute_Req import *

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
        print("Voilà le film à modifier : ")
        Execute_Req( """ SELECT * FROM series WHERE IDSerie = %s """ % ( _filmToModify[int(_userInput)] ), _header, _headerToPrint)
    return _filmToModify[int(_userInput)] 


# cette fonction va modifier la serie choisi
def UpdateFilmReq(_id, _filmToSave): 
    req = """UPDATE series SET Serie_TitreVF = %s, Serie_TitreVO= %s, Serie_Description= %s, Serie_ActeurPrincipal = %s , Serie_DateSortie= %s, Series_Episode= %s, Serie_Saisons= %s WHERE IDSerie = %s"""
    data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _filmToSave[5], _filmToSave[6], _id)
    Execute_ReqInsert(req, data)




# IDSerie  Serie_TitreVF         Serie_TitreVO        Serie_DateSortie      Series_Episode      Serie_Saisons    Serie_Description    Serie_ActeurPrincipal
