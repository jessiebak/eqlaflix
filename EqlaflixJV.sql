
charset utf8;
DROP DATABASE IF EXISTS EQLAFLIX;  
CREATE DATABASE EQLAFLIX;
USE EQLAFLIX;
DROP TABLE IF EXISTS Videogames;
CREATE TABLE Videogames
(	
	IDVideogames INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 	
	Videogames_Titre VARCHAR(150) NOT NULL,   
	Videogames_DateSortie date not null,
	Videogames_Développeur VARCHAR(50),
    Videogames_Editeur VARCHAR(50),
    Videogames_Categorie VARCHAR(150),
);

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Grand Theft Auto V",'2013-09-13',"Rockstar North","Rockstar Games","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Sea of Thieves", '2018-03-20',"Rare Studio","XBox Game Studios", "Action-Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Dead by daylight",'2016-06-16', "Behaviour Interactive","Starbreeze Studios", "Survival horror")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Minecraft",'2011-11-19',"Notch", "Mojang Studio","Sandbox")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Cyberpunk 2077",'2020-12-10',"CD Projekt RED","CD Projekt","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Red Dead Redemption", '2010-05-18',"Rockstar San Diego","Rockstar Games","Action-Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Red Dead Redemption II",'2018-09-26', "Rockstar Studio","Rockstar Games","Action-Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("The Elder Scrolls V: Skyrim",'2011-11-11', "Bethesda Game Studios","Bethesda Softworks","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Assassin's Creed Valhalla",'2020-11-10',"Ubisoft Montréal","Ubisoft","Action-Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("No Man's Sky",'2016-08-10',"Hello Games","Hello Games","Science-Fiction")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Far Cry V",'2018-03-27',"Ubisoft Montréal","Ubisoft","Actioin-Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Planet Zoo",'2019-11-05',"Frontier Developments","Frontier Developments","Simulation")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Les Sims IV",'2014-09-04',"Maxis","Electronic Arts","Simulation")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Horizon Zero Dawn",'2017-03-01',"Guerilla Games","Sony Interactive Entertainment","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Dying light",'2015-02-26',"Techland","Warner Bros","Survival horror")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Battlefield IV",'2013-10-31',"DICE","Electronic Arts","FPS")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Kerbal Space Program", '2011-01-17',"Squad","Private Division","Simulation")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Mount and Blade Warband",'2010-03-30',"TaleWorlds","Paradox Interactive","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Mount and Blade II: Bannerlord",'2020-03-30',"Taleworlds","TaleWorlds","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Star Wars Battlefront 2",'2017-11-17',"Dice Studios","Electronic Arts","FPS")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Sid Meier's Civilization VI",'2016-10-21', "Firaxis Games","2K Games","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("The Binding of Isaac",'2011-09-28',"Edmund McMillen","Edmund McMillen","Action-Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Resident Evil II",'2019-01-25',"Capcom","Capcom","Survival horror")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Heart of Iron IV",'2016-06-06', "Paradox Developments Studios","Paradox Interactive", "Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Age of Empire III",'2005-04-11',"Ensemble Studios","Microsoft Game Studios","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Dark Souls III",'2016-04-12',"From Software","From Software","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("The Witcher III: Wild Hunt",'2015-05-19',"CD Projekt RED","Bandai Namco","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Stardew Valley",'2016-02-26',"Concerned Ape","Chucklefish Games","RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Total War: Rome II",'2013-09-03',"Creative Assembly","Sega","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Total War: Warhammer II",'2017-09-28',"Creative Assembly","Sega","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("FIFA 2021",'2020-10-09',"EA Canada","EA Sports","Simulation")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Microsoft Flight Simulator 2020",'2020-08-18',"Asobo Studios","XBox Game Studios","Simulaltion")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Gwent: The Witcher card game",'2018-09-18',"CD Projekt RED","CD Projekt","Jeu de cartes")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("The Sinking City",'2019-06-27',"Frogware","Nacon","Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Cities: Skyline",'2015-03-10',"Colossal Order","Paradox Interactive","Gestion")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Anno 1800",'2019-04-16',"Ubisoft Blue Byte","Ubisoft","Gestion")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("The Elder Scrolls IV: Oblivion",'2006-03-24',"Bethesda Game Studios","2K Games","RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Call of Duty Modern Warfare",'2019-10-25',"Infinity Ward","Activision","FPS")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Crusader Kings III",'2020-09-01',"Paradox Developments Studios","Paradox Interactive","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Half-Life II",'2004-11-16',"Valve Corporation","Valve Corporation","FPS")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Bioshock Infinite",'2013-03-26',"Irrational Games","2K Games","Aventure")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Portal II",'2011-04-19',"Valve","Valve","Réflexion")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Diablo III",'2012-05-15',"Blizzard Entertainment","Activision Blizzard","Action-RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Borderlands III",'2012-09-21',"Gearbox Software","2K Games","RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Mass Effetc III",'2012-03-09',"Bioware","Electronic Arts")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Company of Heroes",'2006-09-29',"Relic Entertainment","Sega","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Divinity: Original Sin II",'2017-09-14',"Larian Studios","Larian Studios","RPG")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Starcraft II: Wings of liberty",'2010-07-27',"Blizzard Entertainment","Blizzard Entertainment","Stratégie")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Hitman II",'2018-11-14',"IO Interactive","Warner Bros Interactive Entertainment","Infiltration")

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie,Videogames_Description) 
VALUES ("Metal Gear Solid V: the Phantom Pain",'2015-09-01',"Kojima Productions","Konami","Infiltration")

