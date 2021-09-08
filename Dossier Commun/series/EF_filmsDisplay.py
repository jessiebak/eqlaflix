import os 
import sys
from series.Execute_Req import *

os.system("cls")



# Cette fonction renvoit la requette correspondante au choix des élements à afficher 
def DisplayOptionsReq(_filmHeaderToPrint):
    _req = "select IDSerie, " 
    for i in range(len(_filmHeaderToPrint)-1) : 
        _req += sqlFilm[_filmHeaderToPrint[i]] +", "
    _req += sqlFilm[_filmHeaderToPrint[len(_filmHeaderToPrint)-1]] +  " from series  order by Serie_TitreVF asc;"
    return _req




# Cette fonction renvoit la requette correspondante au choix des élements à afficher (destinée pour SEarch )
def DisplaySearchReq(_filmHeaderToPrint):
    _req = "select IDSerie, " 
    for i in range(len(_filmHeaderToPrint)-1) : 
        _req += sqlFilm[_filmHeaderToPrint[i]] +", "
    _req += sqlFilm[_filmHeaderToPrint[len(_filmHeaderToPrint)-1]] +  " from series "
    return _req




# _filmHeadertoPrint = FilmHeaderToPrint()
# Execute_Req(DisplayOptionsReq(_filmHeadertoPrint), filmHeader, _filmHeadertoPrint)


# print(DisplayOptionsReq(_filmHeadertoPrint))


# IDSerie  Serie_TitreVF         Serie_TitreVO        Serie_DateSortie      Series_Episode      Serie_Saisons    Serie_Description    Serie_ActeurPrincipal
