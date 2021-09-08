import mysql.connector as MC
from Execute_Req import AllUsersConnection
from jeux.EqlaFlixFilms import *

def SortFilms(header):
	conn= AllUsersConnection()
	cursor= conn.cursor()
	cursor.execute("SELECT * from Series ORDER BY ?",header)
	print(cursor.fetchall())

def DisplaySortingMenu():
	_menuSentence = "\n EqleFlix/Séries \n Trier par: \n 1- Titre (VF) \n 2- Titre (VO) \n 3- Date de sortie \n 4- Nombre d'épisodes \n 5- Nombre de saison \n  \"Q\"-	Pour quitter  \n Votre choix : "
	_userChoice = input(_menuSentence).lower()
	while _userChoice!="q":
		try:
			_userChoice= int(_userChoice)
			if _userChoice==1:
				header= "TitreVF"
				SortFilms(header)
			elif _userChoice==2:
				header= "TitreVO"
				SortFilms(header)
			elif _userChoice==3:
				header= "DateSortie"
				SortFilms(header)
			elif _userChoice==4:
				header= "Episode"
				SortFilms(header)
			elif _userChoice==5:
				header= "Saisons"
				SortFilms(header)
			else: 
				_userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _menuSentence ).lower()
			_userChoice = input(_menuSentence).lower()
		except:
			_userChoice = input( _menuSentence).lower()
	else:
		DisplayFilmsMenu

DisplayFilmsMenu()
