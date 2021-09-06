import mysql.connector as MC
from Execute_Req import AllUsersConnection
from jeux.EqlaFlixFilms import *

def SortFilms(header):
	conn= AllUsersConnection()
	cursor= conn.cursor()
	cursor.execute("SELECT * from Videogames ORDER BY ?",header)
	print(cursor.fetchall())

def DisplaySortingMenu():
	_menuSentence = "\n EqleFlix/Jeux \n Trier par: \n 1- Titre \n 2- Date de sortie \n 3- Développeur \n 4- Editeur \n 5- Catégorie \n  \"Q\"-	Pour quitter  \n Votre choix : "
	_userChoice = input(_menuSentence).lower()
	while _userChoice!="q":
		try:
			_userChoice= int(_userChoice)
			if _userChoice==1:
				header= "Titre"
				SortFilms(header)
			elif _userChoice==2:
				header= "DateSortie"
				SortFilms(header)
			elif _userChoice==3:
				header= "Développeur"
				SortFilms(header)
			elif _userChoice==4:
				header= "Editeur"
				SortFilms(header)
			elif _userChoice==5:
				header= "Categorie"
				SortFilms(header)
			else: 
				_userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _menuSentence ).lower()
			_userChoice = input(_menuSentence).lower()
		except:
			_userChoice = input( _menuSentence).lower()
	else:
		DisplayFilmsMenu

DisplayFilmsMenu()
