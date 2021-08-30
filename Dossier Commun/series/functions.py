

def ShowallSeriesonConsole():
	curseur = connexion.cursor()
	req = "select * from Series"
	curseur.execute(req)
	response = curseur.fetchall()
	
	for i,n in enumerate(response):
		resultat = f"n°{i+1} \t  Titre : {n[1]} \t Date de sortie: {n[3]}\t  Nombre d'épisodes: {n[4]} "
		print(resultat)
	curseur.execute("select count(*)  from Series")
	total= curseur.fetchone()
	print(f"Nombre total: {total}")
	
	curseur.close()
	connexion.close()

	ShowAllButton.configure(text= F"VOIR TOUTES LES SERIES: ({total[0] })")