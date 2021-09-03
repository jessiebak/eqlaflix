import os
import datetime
from jeux.Execute_Req import *



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
        cursor.execute("""DELETE FROM Videogames where IDVieogames = %s """ % ( _filmToDelete[int(_userInput)] ))
        connexion.commit()        
    if(connexion.is_connected()):
        connexion.close()







# IDVieogames      Videogames_Titre      Videogames_DateSortie     Videogames_Développeur     Videogames_Editeur     Videogames_Categorie
