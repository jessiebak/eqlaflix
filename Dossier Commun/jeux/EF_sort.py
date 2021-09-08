import mysql.connector as MC
from Execute_Req import AllUsersConnection
#from EqlaFlixFilms import *

def SortFilms(header):
	conn= AllUsersConnection()
	cursor= conn.cursor()
	cursor.execute("select * from videogames order by %s" % (header))
	display = cursor.fetchall()
	for games in display:
		print(f"ID Jeu : {games[0]} | Nom : {games[1]} | Date de sortie : {games[2]} | Dévveloppeur  : {games[3]} | Editeur {games[4]} | Catégorie : {games[5]} ")

def DisplaySortingMenu():
	_menuSentence = "\n EqleFlix/Films \n Trier par: \n 1- Titre \n 2- Date de Sortie \n 3- Développeur \n 4- Editeur \n 5- Catégorie \n \"Q\"-	Pour quitter \n Votre choix : "
	_userChoice = input(_menuSentence).lower()
	while _userChoice!="q":
		try:
			_userChoice= int(_userChoice)
			if _userChoice==1:
				header= "Videogames_Titre"
				SortFilms(header)
			elif _userChoice==2:
				header= "Videogames_DateSortie"
				SortFilms(header)
			elif _userChoice==3:
				header= "Videogames_Développeur"
				SortFilms(header)
			elif _userChoice==4:
				header= "Videogames_Editeur"
				SortFilms(header)
			elif _userChoice==5:
				header= "Videogames_Categorie"
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

