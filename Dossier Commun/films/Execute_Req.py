import mysql.connector as MC
import datetime
import sys
import os
import random

def AllUsersConnection(): 
    try: 
        return MC.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'g5gqwagr' )
    except:
        try: 
            return MC.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'python4life' )
        except:
            return MC.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'isaac' )




filmsOptions = ["Afficher", "Modifier", "Ajouter", "Supprimer", "Recherche"]
filmHeader = [ "Tout sélectionner", "ID", "TITRE DU FILM", "GENRE DU FILM", "AUTEUR(S) DU FILM", "DATE DE SORTIE", "NOMBRE D'ENTREE AU BOX OFFICE", "PAYS"]
filmHeaderToPrint = [1, 2, 3, 4, 5, 6, 7]
sqlFilm = {1:"IdFilm", 2:"titre", 3:"genrefilm.nom", 4:"realisateur", 5:"datesortie", 6:"boxoffice", 7:"pays"}
defaultHeaderList = [1, 2, 3, 4, 5, 6, 7]

filmHeader2 = ["TITRE DU FILM", "REALISATEUR(TRICE) DU FILM", "PAYS", "NOMBRE D'ENTREE AU BOX OFFICE", "DATE DE SORTIE" ]



def FilmMenuSentence(_filmHeaderToPrint):
    _fimMenuSentence = "Bienvenu cHEZ EqlaFlix/FILMS. \n Veuillez choisir les différentes options d'affichage : "
    for name in filmHeader: 
        if filmHeader.index(name) in _filmHeaderToPrint:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name + "       ( X )"
        else:
            _fimMenuSentence += "\n" + str(filmHeader.index(name)) + " - " + name
    _fimMenuSentence += "\n \"OK\" -   pour Afiicher les films \n \"Q\" -	Pour quitter le menu de Films \n Entrez votre choix n° " + str(len(_filmHeaderToPrint) + 1) + " : "
    return _fimMenuSentence


# Cette fonction retourne la liste des options de Films à afficher;
def FilmHeaderToPrint(): 
    _filmHeaderToPrint = []
    _fimMenuSentence = FilmMenuSentence(_filmHeaderToPrint)
    _userChoice = input(_fimMenuSentence).lower()
    os.system('cls')
    while _userChoice != "ok" and _userChoice != "q" and _userChoice != "":
        try: 
            _userChoice = int(_userChoice)
            if _userChoice == 0 : 
                return defaultHeaderList
            elif 1<= _userChoice < len(filmHeader) :
                if _userChoice in _filmHeaderToPrint: 
                    print(f"\n {_userChoice} - {filmHeader[_userChoice]} a déjà été sélectionné. ")
                else:
                    _filmHeaderToPrint.append(_userChoice)
            else: 
                _fimMenuSentence = FilmMenuSentence(_filmHeaderToPrint)
                _userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _fimMenuSentence ).lower()
                os.system('cls')
            print(f"\n 0{len(_filmHeaderToPrint)} sélection(s) éffectuée(s). ")
            _fimMenuSentence = FilmMenuSentence(_filmHeaderToPrint)
            _userChoice = input( "\n " + _fimMenuSentence).lower()
            os.system("cls")
        except:
            _fimMenuSentence = FilmMenuSentence(_filmHeaderToPrint)
            _userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _fimMenuSentence).lower()
            os.system('cls')
        _fimMenuSentence = FilmMenuSentence(_filmHeaderToPrint)
    else: 
        if _userChoice == "q": 
            # return -1
            sys.exit()
        elif (_userChoice == "ok" and len(_filmHeaderToPrint) != 0) or (_userChoice == "" and len(_filmHeaderToPrint) != 0): 
            return _filmHeaderToPrint
        elif (_userChoice == "ok" and len(_filmHeaderToPrint) == 0) or (_userChoice == "" and len(_filmHeaderToPrint) == 0):
            return defaultHeaderList


# cette function vérifie si un input entré est une date valide ou pas 
def IsValidDate(_date): 
    _isValidDate = True
    try:
        year, month, day = _date.split('/')
    except :
        _isValidDate = False
    try:
        datetime.datetime(int(year), int(month), int(day))
    except:
        _isValidDate = False
    return _isValidDate


# cette fonction vérifie si un input est un entier naturel 
def IsPositiveNumber(_val): 
    if _val.isdigit() and int(_val) >=0 : 
        return True
    return False


# cette fonction prend un input, vérifie s'il est un nombre positif et renvoit sa valeur, en proposant le "q" ou "entrer" pour quitter
def TakePositifNumber(_input):
    while not (IsPositiveNumber(_input) or len(_input) == 0 or _input.lower()=="q") :    
        _input = input("Veuillez entrer un entier positif  (pressez \"Q\" ou \"entrée\"  pour quitter ) : ")
    else: 
        if IsPositiveNumber(_input) : 
            return int(_input)
        else:
            sys.exit()


# cette fonction prend un input, vérifie s'il s'agit d'une date valide et renvoit sa valeur, en proposant le "q" ou "" pour quitter
def TakeDate(_input):
    while not (IsValidDate(_input) or len(_input) == 0 or _input.lower()=="q") :    
        _input = input("Veuillez entrer une date valide au format \"aaaa/mm/jj\" (pressez \"Q\" ou \"entrée\" pour quitter ) : ")
    else: 
        if IsValidDate(_input) : 
            return _input
        else:
            sys.exit()
        

# cette fonction execute la requette finale 
def Execute_Req( _req, _header = 0, _headerToPrint = 0):
    _matchIdToNumber = {}
    try: 
        connection = AllUsersConnection()
        Cursor = connection.cursor() 
        Cursor.execute(_req)
        filmlist = Cursor.fetchall()
        if _header != 0 and _headerToPrint != 0 : 
            header = "N°   |  "
            for i in _headerToPrint: 
                header += _header[i] + "    |   "
            print(header)
        lineNum = 1
        for elt in filmlist:   
            _matchIdToNumber[lineNum] = elt[0]
            printLine = str(lineNum) + "    |   "   
            for j in range(1, len(elt)):    
                printLine += str(elt[j]) + "    |   "  
            if _header != 0 and _headerToPrint != 0 :  
                print(printLine)   
            lineNum += 1
    except  :
        print("une erreur s'est produite dans le script  de la fonction Execute_Req du fichier execute_Req")
    finally: 
        if(connection.is_connected()):
            connection.close()
            connection.close()
        return _matchIdToNumber


# cette fonction execute la requette finale pour l'affichage aléatoire 
def Execute_ReqRandom( _req, _header = 0, _headerToPrint = 0):
    _matchIdToNumber = {}
    randNum = TakePositifNumber(input("Combien de films aléatoires souhaitez vous générer ? "))
    connect = AllUsersConnection()
    Cursor = connect.cursor() 
    req = "select count(*) from films;"
    Cursor.execute(req)
    maxNum = int(Cursor.fetchone()[0])
    try: 
        connection = AllUsersConnection()
        Cursor = connection.cursor() 
        Cursor.execute(_req)
        filmlist = Cursor.fetchall()
        if 0 < randNum <= maxNum : 
            randlist = random.sample(filmlist, randNum)
        elif randNum == 0 : 
            print("Vous avez choisi de ne pas afficher de film. ")
            return
        else: 
            print(f"Nous ne disposons que de {maxNum} films dans notre base de données.")
            randlist = random.sample(filmlist, maxNum)
        if _header != 0 and _headerToPrint != 0 : 
            header = "N°   |  "
            for i in _headerToPrint: 
                header += _header[i] + "    |   "
            print(header)
        lineNum = 1
        for elt in randlist:   
            _matchIdToNumber[lineNum] = elt[0]
            printLine = str(lineNum) + "    |   "   
            for j in range(1, len(elt)):    
                printLine += str(elt[j]) + "    |   "  
            if _header != 0 and _headerToPrint != 0 :  
                print(printLine)   
            lineNum += 1
    except  :
        print("une erreur s'est produite dans le script  Execute_ReqRandom du fichier execute_Req")
    finally: 
        if(connection.is_connected()):
            connection.close()
            connection.close()
        return _matchIdToNumber


# cette fonction execute la requette finale d'insersion de données 
def Execute_ReqInsert( _req, _data):
    try: 
        connection = AllUsersConnection()
        Cursor = connection.cursor() 
        Cursor.execute(_req, _data )
        connection.commit()
    except  :
        print("une erreur s'est produite dans le script d'ajout de données")
    finally: 
        if(connection.is_connected()):
            connection.close()
            connection.close()


# cette fonction propose des champs de film à renseigner et renvois un tableau contenant les différentes valeurs remplies
def AddFilm():
    _filmToSave = []
    print("Veuillez entrer : ")
    for elt in filmHeader2: 
        if filmHeader2.index(elt) <= 2 : 
            _filmToSave.append(input(f"{elt} : "))
        elif filmHeader2.index(elt) == 3 :
            _userInput =  input(f"{elt} : ")
            while not IsPositiveNumber(_userInput): 
                print("Veuillez entrer un entier positif")
                _userInput =  input(f"{elt} : ")
            else:
                _filmToSave.append(int(_userInput))
        elif filmHeader2.index(elt) == 4 :
            _userInput =  input(f"{elt} au format 'aaaa/mm/jj' : ")
            while not IsValidDate(_userInput): 
                print("Veuillez entrer une date valide au format 'aaaa/mm/jj'. ")
                _userInput =  input(f"{elt} : ")
            else:
                _filmToSave.append(_userInput)
    return _filmToSave


# cette fonction donne l'a possibilité de choisir un genre existant dans la table genre et d'y ajouter si le genre n'existe pas 
def ChooseInTable(_filmToSave): 
     
    _header = ["Tout Sélectionner", "Id", "Genre", "description"]
    _headerToPrint = [2]
    _req = "select idgenre, nom from genrefilm order by nom asc;"
    print("sélectionnez un élément dans cette liste; taper 0 si vous désirez ajouter un nouveau genre \n ")
    _idxToId = Execute_Req( _req, _header, _headerToPrint)
    _userInput = input("\n votre choix : ")
    connexion = AllUsersConnection()
    cursor = connexion.cursor()
    while not (IsPositiveNumber(_userInput) and int(_userInput) <= len(_idxToId) ) : 
        print("Veuillez entrer un nombre valide ")
        _userInput =  input("Genre de Film : ")
    else:
        if int(_userInput) == 0: 
            print("Ajout de Genre de Film : ")
            nom = input("Genre : ") 
            description = input("ajouter une description : ") 
            cursor.execute("""INSERT INTO genrefilm (nom, description) VALUES ("%s", "%s")""" % (nom, description))
            _filmToSave.append(int(cursor.lastrowid))
            connexion.commit()
        else:
            _filmToSave.append(_idxToId[int(_userInput)])
    if(connexion.is_connected()):
        connexion.close()
        connexion.close()
    return _filmToSave

