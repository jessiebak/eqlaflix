
from io import StringIO
from re import search
import mysql.connector as MC 
import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk

from mysql.connector import connection
from mysql.connector.errors import ProgrammingError 

#SQL Connection
# connexion = MC.connect(host= 'localhost', database= 'Eqlaflix', user = 'root', password = 'python4life')
# curseur = connexion.cursor()

def ShowAllseries():
	   
	TreeviewSeries(ResultGrid)
	
	curseur = connexion.cursor()
	req = "select * from series"
	curseur.execute(req)
	response = curseur.fetchall()
	
	for i, n in enumerate(response):
		ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[3], n[4], n[5],n[6]), tags=n[1])
	
	# updaterecord()

		
	
def ShowAllFilms():
	TreeviewFilms(ResultGrid)
	curseur = connexion.cursor()
	req = "select films.IdFilm, films.Titre, genrefilm.nom, films.realisateur, films.datesortie, films.boxoffice from films inner join genrefilm on films.genre = genrefilm.idgenre "
	curseur.execute(req)
	response = curseur.fetchall()
	
	for i, n in enumerate(response):
		ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[4], n[2], n[3],n[5]), tags=n[1])
	
	

		
def ShowAllGames():
	TreeviewGames(ResultGrid)
	
	curseur = connexion.cursor()
	req = "select * from videogames"
	curseur.execute(req)
	response = curseur.fetchall()
	
	for i, n in enumerate(response):
			ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[2], n[3], n[4],n[5]), tags=n[1])

	



def classsify():
	pass
	
	

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
	pass

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
	for item in ResultGrid.get_children():
		ResultGrid.delete(item)
	ShowAllButton.config(text="VOIR TOUTES LES SERIES", command= ShowAllseries)
	

	
	
def FilmsMode():
	for item in ResultGrid.get_children():
		ResultGrid.delete(item)
	ShowAllButton.config(text= "VOIR TOUS LES FILMS", command= ShowAllFilms)
def GamesMode():
	for item in ResultGrid.get_children():
		ResultGrid.delete(item)
	ShowAllButton.config(text= "VOIR TOUS LES JEUX", command= ShowAllGames)
	
# def updaterecord():
# 	global searchEntry, ResultGrid
# 	searching = searchEntry.get() 
# 	curseur = connexion.cursor()
		
	
# 	for record in ResultGrid.get_children(): 
# 		ResultGrid.delete(record)

# 	if searching != "":
# 		req = "select * from series where Serie_TitreVF like %s"
# 		data = searching +'%',
# 		curseur.execute(req, data)
# 		response = curseur.fetchall()
		
# 		for i, n in enumerate(response):
# 			ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[3], n[4], n[5],n[6]), tags=n[1])
	
	# elif tableNumber == 2:
		
	# 	req = "select * from films where Titre like %s"
	# 	data = searching +'%',
	# 	curseur.execute(req, data)
	# 	response = curseur.fetchall()
	
	# 	for i, n in enumerate(response):
	# 		ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[4], n[2], n[3],n[5]), tags=n[1])
	
	# elif tableNumber == 3:	
	# 	req = "select * from videogames  where Videogames_Titre like %s"
	# 	data = searching + 's', 
	# 	curseur.execute(req, data)
	# 	response = curseur.fetchall()
	
	# 	for i, n in enumerate(response):
	# 			ResultGrid.insert(parent="",index=i, iid=i, values=(n[1], n[2], n[3], n[4],n[5]), tags=n[1])
	



	 
	
	

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
ShowAllButton.pack(side= LEFT) 	
global searchEntry
searchEntry= tk.Entry(MenuFrame, font=appFont)
searchEntry.pack(fill= Y)

global connexion 
try : 
	connexion = MC.connect(database="Eqlaflix", password= "isaac", user= "root")
except ProgrammingError: 
	try: 
		connexion = MC.connect(database="Eqlaflix", password= "python4life", user= "root")
	except:
		pass


	


choice = tk.StringVar()
optionlist= ["Trier par Nom", "Trier par Date de sortie"]
SortFrame = tk.Frame(WindowFrame)
sortinglist= tk.OptionMenu(SortFrame, choice,*optionlist)
choice.set(optionlist[0]) 
sortinglist.config(font=("Helvetica", 15), bg=appBG2, fg="white")
sortinglist.pack(side=LEFT)
WindowFrame.pack(side = TOP, fill = BOTH)
FrameH1.pack(side=TOP, fill= Y)
MenuFrame.pack(fill= Y)
SortFrame.pack(side=LEFT)
resultbox.pack(side= TOP, anchor = CENTER, fill= BOTH, expand= True)
TitleH1.pack()
TitleH2.pack()

#Creating Treeview
ResultGrid = ttk.Treeview(resultbox, height= root.winfo_screenheight())
ResultGrid.pack(fill= BOTH, expand= True)


#End of app method, close window and SQL server


root.mainloop()