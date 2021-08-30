import os
import datetime
import mysql.connector
from Execute_Req import *



os.system("cls")


# tab = {1: 62, 2: 63, 3: 8, 4: 37, 5: 7, 6: 6, 7: 10, 8: 2, 9: 17, 10: 50, 11: 38, 12: 31, 13: 34, 14: 5, 15: 3, 16: 35, 17: 40, 18: 14, 19: 4, 20: 27, 21: 39, 22: 42, 23: 18, 24: 49, 25: 33, 26: 28, 27: 43, 28: 36, 29: 16, 30: 32, 31: 13, 32: 12, 33: 24, 34: 25, 35: 20, 36: 23, 37: 44, 38: 48, 39: 9, 40: 26, 41: 11, 42: 64, 43: 45, 44: 15, 45: 46, 46: 30, 47: 19, 48: 52, 49: 21, 50: 1, 51: 22, 52: 51, 53: 29, 54: 47, 55: 41}

def ChooseInTable(_filmToDelete): 
     
    print("sélectionnez l'élémen à supprimer  dans cette liste. ")
    _userInput = input("\n votre choix : ")
    connexion = mysql.connector.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'isaac' )
    cursor = connexion.cursor()
    while not (IsPositiveNumber(_userInput) and int(_userInput) <= len(_filmToDelete) ) : 
        print("Veuillez entrer un nombre valide ")
        _userInput =  input("Entrer le N° de l'item à supprimer ") 
    else:
        cursor.execute("""UPDATE films SET deleted = 1 where idfilm = %s """ % ( _filmToDelete[int(_userInput)] ))
        connexion.commit()        
    if(connexion.is_connected()):
        connexion.close()



# ChooseInTable(tab)