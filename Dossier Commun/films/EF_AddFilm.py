import os
import mysql.connector
from films.Execute_Req import *



os.system("cls")


def SaveFilmReq(_filmToSave): 
    req = """INSERT INTO films (titre, realisateur, pays, boxoffice, DateSortie, Genre) VALUES (%s, %s, %s, %s, %s, %s)"""
    data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _filmToSave[5])
    Execute_ReqInsert(req, data)



# SaveFilmReq(ChooseInTable(AddFilm()))

# print(ChooseInTable([]))








