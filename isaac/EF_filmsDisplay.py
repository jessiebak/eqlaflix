import os 
import sys
from Execute_Req import *

os.system("cls")



# Cette fonction renvoit la requette correspondante au choix des élements à afficher 
def DisplayOptionsReq(_filmHeaderToPrint):
    _req = "select idfilm, " 
    for i in range(len(_filmHeaderToPrint)-1) : 
        _req += sqlFilm[_filmHeaderToPrint[i]] +", "
    _req += sqlFilm[_filmHeaderToPrint[len(_filmHeaderToPrint)-1]] +  " from films left join genrefilm on films.genre = genrefilm.idgenre where deleted = 0 order by titre asc;"
    return _req




# Cette fonction renvoit la requette correspondante au choix des élements à afficher (destinée pour SEarch )
def DisplaySearchReq(_filmHeaderToPrint):
    _req = "select idfilm, " 
    for i in range(len(_filmHeaderToPrint)-1) : 
        _req += sqlFilm[_filmHeaderToPrint[i]] +", "
    _req += sqlFilm[_filmHeaderToPrint[len(_filmHeaderToPrint)-1]] +  " from films left join genrefilm on films.genre = genrefilm.idgenre where deleted = 0 "
    return _req




# _filmHeadertoPrint = FilmHeaderToPrint()
# Execute_Req(DisplayOptionsReq(_filmHeadertoPrint), filmHeader, _filmHeadertoPrint)


# print(DisplayOptionsReq(_filmHeadertoPrint))