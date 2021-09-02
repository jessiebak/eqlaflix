import os
import mysql.connector
from Execute_Req import *

os.system("cls")

# utile pour la sychronisation de la requête d'enregistrement 
# filmHeader2 = ["TITRE(VF)", "TITRE(VO)", "DESCRIPTION", "ACTEUR PRINCIPAL" , "DATE DE SORTIE", "NOMBRE D'EPISODE", "NOMBRE DE SAISONS" ]


def SaveFilmReq(_filmToSave): 
    req = """INSERT INTO Videogames (Videogames_Titre, Videogames_Développeur, Videogames_Editeur,  Videogames_Categorie, Videogames_DateSortie) VALUES (%s, %s, %s, %s, %s)"""
    data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4])
    Execute_ReqInsert(req, data)









# IDVieogames      Videogames_Titre      Videogames_DateSortie     Videogames_Développeur     Videogames_Editeur     Videogames_Categorie