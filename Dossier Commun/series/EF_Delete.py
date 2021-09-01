import os
import datetime
from Execute_Req import *



os.system("cls")



def ChooseInTable(_filmToDelete): 
     
    print("sélectionnez l'élémen à supprimer  dans cette liste. ")
    _userInput = input("\n votre choix : ")
    connexion = AllUsersConnection()
    cursor = connexion.cursor()
    while not (IsPositiveNumber(_userInput) and int(_userInput) <= len(_filmToDelete) ) : 
        print("Veuillez entrer un nombre valide ")
        _userInput =  input("Entrer le N° de l'item à supprimer ") 
    else:
        cursor.execute("""DELETE FROM series where IDSerie = %s """ % ( _filmToDelete[int(_userInput)] ))
        connexion.commit()        
    if(connexion.is_connected()):
        connexion.close()







# IDSerie  Serie_TitreVF         Serie_TitreVO        Serie_DateSortie      Series_Episode      Serie_Saisons    Serie_Description    Serie_ActeurPrincipal
