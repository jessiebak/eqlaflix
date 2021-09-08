import mysql.connector as MC
from Execute_Req import AllUsersConnection
#from EqlaFlixFilms import *

def SortFilms(header):
	conn= AllUsersConnection()
	cursor= conn.cursor()
	cursor.execute("select * from series order by %s" % (header))
	display = cursor.fetchall()
	for film in display:
		print(f"ID Serie : {film[0]} | Titre : {film[1]} | Date de sortie : {film[3]} | Episodes : {film[4]} | Saisons: {film[5]} | Description : {film[6]} ")

def DisplaySortingMenu():
	_menuSentence = "\n EqleFlix/Films \n Trier par: \n 1- Titre \n 2- Date de Sortie \n 3- Nombre d'épisodes \n 4- Nombre de saisons \n \"Q\"-	Pour quitter  \n Votre choix : "
	_userChoice = input(_menuSentence).lower()
	while _userChoice!="q":
		try:
			_userChoice= int(_userChoice)
			if _userChoice==1:
				header= "Serie_TitreVF"
				SortFilms(header)
			elif _userChoice==2:
				header= "Serie_DateSortie"
				SortFilms(header)
			elif _userChoice==3:
				header= "Series_Episode"
				SortFilms(header)
			elif _userChoice==4:
				header= "Serie_Saisons"
				SortFilms(header)
			else: 
				_userChoice = input("\n Votre choix est incorrect; Veuillez entrer un choix valide. \n" + _menuSentence ).lower()
			_userChoice = input(_menuSentence).lower()
		except:
			_userChoice = input( _menuSentence).lower()
	#else:
		#DisplayFilmsMenu
1

DisplaySortingMenu()

# SortFilms("titre")

