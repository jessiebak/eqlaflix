import os
import mysql.connector
from series.Execute_Req import *

os.system("cls")

# utile pour la sychronisation de la requête d'enregistrement 
# filmHeader2 = ["TITRE(VF)", "TITRE(VO)", "DESCRIPTION", "ACTEUR PRINCIPAL" , "DATE DE SORTIE", "NOMBRE D'EPISODE", "NOMBRE DE SAISONS" ]


def SaveFilmReq(_filmToSave): 
    req = """INSERT INTO series (Serie_TitreVF, Serie_TitreVO, Serie_Description,  Serie_ActeurPrincipal, Serie_DateSortie, Series_Episode, Serie_Saisons) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _filmToSave[5], _filmToSave[6])
    Execute_ReqInsert(req, data)









# IDSerie  Serie_TitreVF         Serie_TitreVO        Serie_DateSortie      Series_Episode      Serie_Saisons    Serie_Description    Serie_ActeurPrincipal