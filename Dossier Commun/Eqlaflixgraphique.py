


import mysql.connector as MC 
import tkinter as tk
from tkinter.constants import *

import tkinter.ttk as ttk

from mysql.connector import connection
from mysql.connector.errors import ProgrammingError 
from films.Execute_Req import AllUsersConnection
def ShowAllseries():
	   
	TreeviewSeries(ResultGrid)
	searchEntry.delete(0,END)
	updaterecord(1)
	DisplayButtons()
	
	
def ShowAllFilms():
	TreeviewFilms(ResultGrid)
	searchEntry.delete(0,END)
	updaterecord(2)
	DisplayButtons()
		
def ShowAllGames():
	TreeviewGames(ResultGrid)
	searchEntry.delete(0,END)
	updaterecord(3)
	DisplayButtons()

def DisplayButtons():
	if resultbox.winfo_ismapped()== False: 
		resultbox.pack(side= TOP, anchor = CENTER, fill= BOTH, expand= True)
	if sortinglist.winfo_ismapped() == False:
		sortinglist.pack(side= LEFT)
	if updatebutton.winfo_ismapped() == False:
		updatebutton.pack(side=LEFT)
	if ShowAllButton.winfo_ismapped() == False: 
		ShowAllButton.pack(side = LEFT,fill= Y)
	if searchEntry.winfo_ismapped() == False: 
		searchEntry.pack(fill=Y)

def TreeviewSeries(ResultGrid):

	ResultGrid["columns"]= ("Titre", "DateSortie", "Episodes", "Saisons", "Description")
	ResultGrid.column("#0", width=0, stretch = NO)
	ResultGrid.column("Titre", width=255, anchor = W)
	ResultGrid.column("DateSortie", width=80, anchor = CENTER)
	ResultGrid.column("Episodes", width=80, anchor = CENTER)
	ResultGrid.column("Saisons", width=80, anchor = CENTER)
	ResultGrid.column("Description", width=2000, anchor = W)

	ResultGrid.heading("#0", text="")
	ResultGrid.heading("Titre", text= "Titre", anchor = CENTER)
	ResultGrid.heading("DateSortie", text= "Date de sortie", anchor = CENTER)
	ResultGrid.heading("Episodes",text= "épisodes", anchor = CENTER)
	ResultGrid.heading("Saisons", text = "Saisons", anchor = CENTER)
	ResultGrid.heading("Description", text= "Description", anchor = CENTER)

	#linking Scrollbar to Treeview
		
	scrollingX = tk.Scrollbar(resultbox, orient= HORIZONTAL)
	scrollingY = tk.Scrollbar(resultbox, orient= VERTICAL)
	scrollingX.pack(side=BOTTOM, fill= X)
	scrollingY.pack(side=RIGHT, fill= Y)
	ResultGrid.configure(xscrollcommand=scrollingX.set, yscrollcommand=scrollingY.set)
	scrollingX.config(command=ResultGrid.xview)
	scrollingY.config(command=ResultGrid.yview)
	
	ResultGrid.pack(fill= BOTH, expand= True)

	#adding Style 
	style = ttk.Style()
	style.theme_use("default")
	style.configure("Treeview",background= "steelblue2", foreground= "white", fieldbackground="#1F1F1F", rowheight=35, color="white", font=("Helvetica",10))
	style.map("Treeview", background=[("selected", appBG2)])

def TreeviewFilms(ResultGrid):
	ResultGrid["columns"]= ("Titre", "DateSortie", "Genre", "Réalisateur", "BoxOffice")
	ResultGrid.column("#0", width=0, stretch = NO)
	ResultGrid.column("Titre", width=350, anchor = W)
	ResultGrid.column("DateSortie", width=80, anchor = CENTER)
	ResultGrid.column("Genre", width=150, anchor = CENTER)
	ResultGrid.column("Réalisateur", width=255, anchor = CENTER)
	ResultGrid.column("BoxOffice", width=2000, anchor = W)

	ResultGrid.heading("#0", text="")
	ResultGrid.heading("Titre", text= "Titre", anchor = CENTER)
	ResultGrid.heading("DateSortie", text= "Date de sortie", anchor = CENTER)
	ResultGrid.heading("Genre",text= "Genre", anchor = CENTER)
	ResultGrid.heading("Réalisateur", text = "Réalisateur", anchor = CENTER)
	ResultGrid.heading("BoxOffice", text= "Box Office", anchor = W)

	#linking Scrollbar to Treeview

	scrollingX = tk.Scrollbar(resultbox, orient= HORIZONTAL)
	scrollingY = tk.Scrollbar(resultbox, orient= VERTICAL)
	scrollingX.pack(side=BOTTOM, fill= X)
	scrollingY.pack(side=RIGHT, fill= Y)
	ResultGrid.configure(xscrollcommand=scrollingX.set, yscrollcommand=scrollingY.set)
	scrollingX.config(command=ResultGrid.xview)
	scrollingY.config(command=ResultGrid.yview)

	ResultGrid.pack(fill= BOTH, expand= True)

	#adding Style 
	style = ttk.Style()
	style.theme_use("default")
	style.configure("Treeview",background= "light goldenrod yellow", foreground= "white", fieldbackground="#1F1F1F", rowheight=35, color="white", font=("Helvetica",10))
	style.map("Treeview", background=[("selected", appBG2)])
	
def TreeviewGames(ResultGrid):
	ResultGrid["columns"]= ("Titre", "DateSortie", "Développeur", "Editeur", "Catégorie")
	ResultGrid.column("#0", width=0, stretch = NO)
	ResultGrid.column("Titre", width=350, anchor = W)
	ResultGrid.column("DateSortie", width=80, anchor = CENTER)
	ResultGrid.column("Développeur", width=200, anchor = CENTER)
	ResultGrid.column("Editeur", width=255, anchor = CENTER)
	ResultGrid.column("Catégorie", width=2000, anchor = W)

	ResultGrid.heading("#0", text="")
	ResultGrid.heading("Titre", text= "Titre", anchor = CENTER)
	ResultGrid.heading("DateSortie", text= "Date de sortie", anchor = CENTER)
	ResultGrid.heading("Développeur",text= "Développeur", anchor = CENTER)
	ResultGrid.heading("Editeur", text = "Editeur", anchor = CENTER)
	ResultGrid.heading("Catégorie", text= "Catégorie", anchor = CENTER)

	#linking Scrollbar to Treeview
	
	scrollingX = tk.Scrollbar(resultbox, orient= HORIZONTAL)
	scrollingY = tk.Scrollbar(resultbox, orient= VERTICAL)
	scrollingX.pack(side=BOTTOM, fill= X)
	scrollingY.pack(side=RIGHT, fill= Y)
	ResultGrid.configure(xscrollcommand=scrollingX.set, yscrollcommand=scrollingY.set)
	scrollingX.config(command=ResultGrid.xview)
	scrollingY.config(command=ResultGrid.yview)

	
	ResultGrid.pack(fill= BOTH, expand= True)
	
	#adding Style 
	style = ttk.Style()
	style.theme_use("default")
	style.configure("Treeview",background= "orchid2", foreground= "white", fieldbackground="#1F1F1F", rowheight=35, color="white", font=("Helvetica",10))
	style.map("Treeview", background=[("selected", appBG2)])
	
def Seriesmode():
	global ResultGrid, options
	for item in ResultGrid.get_children():
		ResultGrid.delete(item)
	
	ShowAllButton.config(text="VOIR TOUTES LES SERIES", command= ShowAllseries)
	options = optionlistconfig("series")
	option_value.set(options[0])
	sortinglist['menu'].delete(0,END)
	for choice in options:
		sortinglist["menu"].add_command(label=choice, command=tk._setit(option_value, choice))
	updatebutton.config(bg="sky blue2", fg= 'black')
	ShowAllseries()
def FilmsMode():
	
	global ResultGrid, options
	for item in ResultGrid.get_children():
		ResultGrid.delete(item)
	
	
	ShowAllButton.config(text= "VOIR TOUS LES FILMS", command= ShowAllFilms)
	options = optionlistconfig("films")
	option_value.set(options[0])
	sortinglist['menu'].delete(0,END)
	for choice in options:
		sortinglist["menu"].add_command(label=choice, command=tk._setit(option_value, choice))
	updatebutton.config(bg="lightgoldenrod", fg= 'black')
	ShowAllFilms()

def GamesMode():
	global ResultGrid, options
	for item in ResultGrid.get_children():
		ResultGrid.delete(item)
	
	ShowAllButton.config(text= "VOIR TOUS LES JEUX", command= ShowAllGames)
	options = optionlistconfig("games")
	option_value.set(options[0])
	sortinglist['menu'].delete(0,END)
	for choice in options:
		sortinglist["menu"].add_command(label=choice, command=tk._setit(option_value, choice))
	updatebutton.config(bg="hot pink", fg= 'black')
	ShowAllGames()
def updaterecord(tableNumber):
	global searchEntry, ResultGrid
	searching= tk.StringVar()
	searching = searchEntry.get() 

	curseur = connexion.cursor()
	
	for record in ResultGrid.get_children(): 
		ResultGrid.delete(record)
	
	if tableNumber == 1: 
		_order = CheckOrder("series")
		
		req = "select * from series where Serie_TitreVF like %s" + _order
		data = "%" + searching +'%',

		curseur.execute(req, data)
		response = curseur.fetchall()
		updatebutton.configure(command = lambda : updaterecord(1))
		searchEntry.bind_all("<Enter>", lambda : updaterecord(1))

		for i, n in enumerate(response):
			ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[3], n[4], n[5],n[6]), tags=n[1])
	
	elif tableNumber == 2:
		_order = CheckOrder("films")
		req = "select films.IdFilm, films.Titre, genrefilm.nom, films.realisateur, films.datesortie, films.boxoffice from films inner join genrefilm on films.genre = genrefilm.idgenre where films.Titre like %s" + _order
		data = "%" + searching +'%',
		curseur.execute(req, data)
		response = curseur.fetchall()
		updatebutton.config(command = lambda : updaterecord(2))
		searchEntry.bind("<Enter>", lambda : updaterecord(2))
		for i, n in enumerate(response):
			ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[4], n[2], n[3],n[5]), tags=n[1])
	
	elif tableNumber == 3:	

		_order = CheckOrder("games")
		req = "select * from videogames where videogames_Titre like %s " + _order 
		data = "%" + searching + '%', 
		curseur.execute(req, data)
		response = curseur.fetchall()
		updatebutton.config(command = lambda : updaterecord(3))
		searchEntry.bind("<Enter>", lambda : updaterecord(3))
	
		for i, n in enumerate(response):
			ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[2], n[3], n[4],n[5]), tags=n[1])
				
def optionlistconfig(_mode): 

	if _mode == "series": 
		_optionlist = ["Trier par Titre", "Trier par Date de sortie (plus récent)","Trier par Date de sortie (plus ancien)" , "Trier par Episode (Le plus)", "Trier par Episodes (Le moins)", 'Trier par Saisons (Le plus)', "Trier par Saison (Le moins)"]
		return _optionlist
	elif _mode == "films": 
		_optionlist = ["Trier par Titre", "Trier par Date de sortie (Le plus récent)", "Trier par Date de sortie (Le plus ancien)", "Trier par genre", "Tier par Box Office", "Trier par Réalisateur"]		
		return _optionlist
	elif _mode == "games":	
		_optionlist = ["Trier par Titre","Trier par Date de sortie (plus récent)", "Trier par Date de sortie (plus ancien)", "Trier par Développeur", "Trier par Editeur", "Trier par Catégorie"] 
		return _optionlist	


def CheckOrder(_categorie): 

	if _categorie == "series": 
		if option_value.get() == options[0]:
			return "order by Serie_TitreVF"
		elif option_value.get() == options[1]: 
			return "order by Serie_DateSortie DESC"
		elif option_value.get() == options[2]: 
			return "order by Serie_DateSortie"
		elif option_value.get() == options[3]: 
			return "order by Series_Episode DESC"
		elif option_value.get() == options[4]: 
			return "order by Series_Episode "
		elif option_value.get() == options [5]: 
			return "order by Serie_Saisons DESC"
		elif option_value.get() == options [6]: 
			return "order by Serie_Saisons"
	elif _categorie == "films":
		if option_value.get() == options[0]:
			return "order by films.Titre"
		elif option_value.get() == options[1]: 
			return "order by films.DateSortie DESC"
		elif option_value.get() == options[2]: 
			return "order by films.DateSortie"
		elif option_value.get() == options[3]: 
			return "order by films.Genre"
		elif option_value.get() == options [4]: 
			return "order by films.BoxOffice"
		elif option_value.get() == options [5]: 
			return "order by films.Realisateur"
	elif _categorie == "games":
		if option_value.get() == options[0]:
			return "order by Videogames_Titre"
		elif option_value.get() == options[1]: 
			return "order by Videogames_DateSortie DESC"
		elif option_value.get() == options[2]: 
			return "order by Videogames_DateSortie"
		elif option_value.get() == options[3]: 
			return "order by Videogames_Développeur"
		elif option_value.get() == options[4]: 
			return "order by Videogames_Editeur"
		elif option_value.get() == options[5]: 
			return "order by Videogames_Categorie"
	
global connexion 
connexion = AllUsersConnection()

#creating Window
root = tk.Tk()
root.title("Eqlaflix - Votre plafeforme d'information Films, jeux et séries")
root.geometry("1920x1020")
appBG, appBG2, policeBG ="black", "red", "white"
appFont = ("Helvetica", 25)
root.config(bg= appBG)
RatioMainbox, RatioMainboxHeight = 4/6, 1/10
padding = 20
appfont =("Helvetica",26)
Bdheight = "5px"

WindowFrame= tk.Frame(root, width= 1280, height= 720, bg= appBG)
FrameH1= tk.Frame(WindowFrame, width= WindowFrame.winfo_width()*RatioMainbox, height= WindowFrame.winfo_height()*RatioMainboxHeight, bg= appBG2, pady= padding, borderwidth=Bdheight)
TitleH1 =tk.Label(FrameH1, text= "EQLAFLIX", font= appFont, bg= appBG2, fg=policeBG, padx=padding, borderwidth=Bdheight)
TitleH2 =tk.Label(FrameH1, text= "Votre plateforme d'information sur les films, séries et jeux vidéos", font= appFont, bg= appBG2, fg=policeBG, padx=padding, borderwidth=Bdheight)


MenuFrame = tk.Frame(WindowFrame, width= root.winfo_screenwidth(), bg="black")
ShowAllButton= tk.Button(MenuFrame, text= "VOIR TOUTES LES SERIES", command= lambda : [f()for f in [ShowAllseries]] , font = ("Helvetica", 15))
sideBar=tk.Frame(root, bg=appBG, width= int(WindowFrame.winfo_width()/6), height= int(WindowFrame.winfo_height()))
sideBar2=tk.Frame(root, bg=appBG, width= int(WindowFrame.winfo_width()/6), height= int(WindowFrame.winfo_height()))
resultbox = tk.Frame(root, width=(WindowFrame.winfo_width()- sideBar.winfo_width()), height= root.winfo_screenheight() -WindowFrame.winfo_height()- MenuFrame. winfo_width(), borderwidth=Bdheight, bg= "black")



SeriesPanelButton = tk.Button(sideBar,text="Séries", font= appfont, fg= policeBG, bg= appBG, height=int(sideBar.winfo_height()/3), command= Seriesmode )

#Right buttons panel

sideBar.pack(fill = Y, side=LEFT, expand= True)

sideBar2.pack(fill = Y, side=RIGHT, expand= True)
SeriesPanelButton.pack(expand= True, side=TOP, fill= BOTH)
FilmPanelButton = tk.Button(sideBar,text="Film", font= appfont, fg= policeBG, bg= appBG, height=int(sideBar.winfo_height()/3), command= FilmsMode )
FilmPanelButton.pack(expand= True, fill= BOTH)
GamePanelButton = tk.Button(sideBar,text="Jeux Vidéo", font= appfont, fg= policeBG, bg= appBG, height=int(sideBar.winfo_height()/3), command= GamesMode )
GamePanelButton.pack(expand= True,side = BOTTOM,fill= BOTH)


global searchEntry
searchEntry= tk.Entry(MenuFrame, font=appFont)





global sortinglist, option_value, options

choice = tk.StringVar()


SortFrame = tk.Frame(WindowFrame)
options = optionlistconfig("series")
option_value = tk.StringVar()
sortinglist = tk.OptionMenu(SortFrame, option_value, *options) 
option_value.set(options[0])



WindowFrame.pack(side = TOP, fill = BOTH)
FrameH1.pack(side=TOP, fill= Y)
MenuFrame.pack(fill= Y)
SortFrame.pack(side=LEFT)

TitleH1.pack()
TitleH2.pack()

global updatebutton
updatebutton = tk.Button(WindowFrame, text = "Actualiser", font = ("Helvetica", 12), bg="skyBlue2")


#Creating Treeview
global ResultGrid 
ResultGrid = ttk.Treeview(resultbox, height= root.winfo_screenheight())
ResultGrid.pack(fill= BOTH, expand= True)
	

#End of app method, close window and SQL server

root.mainloop()