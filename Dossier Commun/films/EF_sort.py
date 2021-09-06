import mysql.connector as MC
from Execute_Req import AllUsersConnection
from EqlaFlixFilms import *

def SortFilms(header):
	conn= AllUsersConnection()
	cursor= conn.cursor()
	cursor.execute("SELECT * from Films ORDER BY ?",header)
	print(cursor.fetchall())

def DisplaySortingMenu():
	_menuSentence = "\n EqleFlix/Films \n Trier par: \n 1- Titre \n 2- Genre \n 3- Réalisateur \n 4- Date de sortie \n 5- Box office \n 6- Pays \n  \"Q\"-	Pour quitter  \n Votre choix : "
	_userChoice = input(_menuSentence).lower()
	while _userChoice!="q":
		try:
			_userChoice= int(_userChoice)
			if _userChoice==1:
				header= "Titre"
				SortFilms(header)
			elif _userChoice==2:
				header= "Genre"
				SortFilms(header)
			elif _userChoice==3:
				header= "Realisateur"
				SortFilms(header)
			elif _userChoice==4:
				header= "DateSortie"
				SortFilms(header)
			elif _userChoice==5:
				header= "BoxOffice"
				SortFilms(header)
			elif _userChoice==6:
				header= "Pays"
				SortFilms(header)
			else: 
				_userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _menuSentence ).lower()
			_userChoice = input(_menuSentence).lower()
		except:
			_userChoice = input( _menuSentence).lower()
	else:
		DisplayFilmsMenu

DisplayFilmsMenu()
