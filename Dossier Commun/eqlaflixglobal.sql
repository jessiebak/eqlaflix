/* On utilise l'encodage UTF8 */
charset utf8;

/*
CREATION DE LA DB ON LA SUPPRIME SI ELLE EXISTE DEJA
Ca permettra de vite relancer le script de création et vous permettre de corriger ici.
Le plus simple est donc de supprimer la base de données pour vous faire gagner du temps.
*/
DROP DATABASE IF EXISTS eqlaflix;
CREATE DATABASE eqlaflix;

/* On Change de base de données */
use eqlaflix;

SET FOREIGN_KEY_CHECKS=0;




/* Creation de la Table Genre pour les films. */

DROP TABLE IF EXISTS `GenreFilm`;
CREATE TABLE GenreFilm (
  IdGenre smallint UNSIGNED not null auto_increment UNIQUE primary key, 
  nom varchar(50) UNIQUE not null, 
  description varchar(255)
); 

insert into GenreFilm (nom) values 
       ('Action'),
    ('Animation'), 
    ('Aventure'),
    ('Biographique'),
    ('Catastrophe'),
    ('Comédie'),
    ('Comédie Dramatique'),
    ('Comédie Musicale'),
    ("Comédie Policiére"),
    ('Comédie Romantique'),
    ('Court Métrage'),
    ('Dessin Animé'),
    ('Documentaire'),
    ('Drame'),
    ('Drame Psychologique'),
    ('Epouvante'),
    ('Erotique'),
    ('Espionnage'),
    ('Essai'),
    ('Fantastique'),
    ('Film à Sketches'),
    ('Film Musical'),
    ('Guerre'),
    ('Historique'),
    ('Horreur'),
    ('Karaté'),
    ('Manga'),
    ('Melodrame'),
    ('Muet'),
   ('Par Parties'),
    ('Péplum'),
    ('Policier'),
    ('Politique'),
    ('Programme'),
    ('Romance'),
    ('satirique'),
   ('Science Fiction'),
    ('Sérial'),
    ('Spectacle'),
    ('Téléfilm'),
    ('Théâtre'),
    ('Thriller'),
    ('Western'); 




















/*
DROP TABLE IF EXITS 'films'; 
CREATION DE LA TABLE flims
IdFilm: entier 
Titre :
Genre: 
Realisateur :  
DateSortie :
BoxOffice :  
*/
CREATE TABLE Films(
    IdFilm int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    Titre varchar(255),
    Genre smallint UNSIGNED,
    Realisateur varchar(255) not null,
    DateSortie date NOT NULL,
    BoxOffice int UNSIGNED NOT NULL,
    pays varchar(150),
    -- pays int(11),
    Deleted boolean default FALSE,
    -- FOREIGN KEY(pays) REFERENCES Pays(Id_Pays),
    FOREIGN KEY(Genre) REFERENCES GenreFilm(IdGenre)
);


INSERT INTO Films(Titre , Genre, Realisateur, DateSortie, BoxOffice, pays )
VALUES('Titanic' , 14, 'James Cameron', '1997-01-01' , 20634793, 'americain' ), 
("Bienvenue chez les Ch'tis" , 14, 'Dany Boon', '2008-02-20' , 20489303, "francais" ),
("Intouchables" , null, "E. Toledano et O. Nakache",'2011-01-01' , 19490688, 'francais' ), 
("La Grande Vadrouille" , null, "Gérard Oury", '1966-01-01', 17273065, 'franco-britanique'), 
("Il était une fois dans l'Ouest" , 43, "Sergio Leone", '1968-01-01', 14862764, 'italo-americain' ), 
("Avatar" , 37, "James Cameron", '2009-01-01', 14677888, "americain" ), 
("Autant en emporte le vent" , null, "Victor Fleming", '1950-01-01', 14677888, "americain" ), 
("Astérix et Obélix : Mission Cléopâtre" , null, "Alain Chabat", '2002-01-01', 14559509, "franco-allemand" ), 
("Les Dix Commandements" , null, "Cecil B. DeMille", '1956-01-01', 14229745, "americain" ), 
("Ben-Hur" , null, "William Wyler", '1960-01-01', 13826124, "americain" ), 
("Les Visiteurs" , null, "Jean-Marie Poiré", '1993-01-01', 13782991, "francais" ), 
("Le Pont de la rivière Kwaï" , null, "David Lean", '1957-01-01', 13481750, "britanico-americain"  ), 
("Le Petit Monde de don Camillo" , null, "Julien Duvivier", '1952-01-01', 12791168, "franco-italien" ), 
("La Grande Illusion" , null, "Jean Renoir", '1937-01-01', 12500000, "francais" ), 
("Qu'est-ce qu'on a fait au Bon Dieu ?" , 6, "Philippe de Chauveron", '2014-01-01', 12366033, "francais" ), 
("Le Jour le plus long" , null, "Ken Annakin", '1962-01-01', 11933629, "americain" ), 
("Cendrillon" , 2, "Wilfred Jackson", '1950-01-01', 11873677, "" ),
("Le Corniaud" , 6, "Gérard Oury", '1965-01-01', 11739783, "franco-italo-espagnol" ),
("Star Wars, épisode VII : Le Réveil de la Force" , 37, "J. J. Abrams", '2015-01-01', 10507561, "americain" ),
("Les Bronzés 3 : Amis pour la vie" , null, "Patrice Leconte", '2006-01-01', 10355930, "francais" ),
("Taxi 2" , null, "Gérard Krawczyk", '2006-01-01', 10345901, "francais" ),
("Trois hommes et un couffin" , null, "Coline Serreau", '1985-01-01', 10251465, "francais" ),
("Les Canons de Navarone" , null, "J. Lee Thompson", '1961-01-01', 10197729, "anglo-americain" ),
("Le Roi lion (1994)" , 2, "Roger Allers", '1994-01-01', 10135871, "" ),
("Le Roi lion (2019)" , null, "Jon Favreau", '2019-01-01', 10017995, "americain" ),
("Les Misérables" , null, "Jean-Paul Le Chanois", '1957-01-01', 9940533,"franco-italo-allemand" ),
("La Guerre des boutons" , 6, "Yves Robert", '1962-01-01', 9936391, "francais" ),
("Le Docteur Jivago" , null, "David Lean", '1966-01-01', 9816054, "americain" ),
("Vingt Milles Lieues sous les mers" , null, "Richard Fleisher", '1954-01-01', 9619259, "americain" ),
("Sous le plus grand chapiteau du monde" , null, "Cecil B. DeMille", '1952-01-01', 9488114, "americain" ),
("Harry Potter à l'école des sorciers" , 20, "Chris Columbus", '2001-01-01', 9470490, "britanico-americain" ),
("Le Monde de Nemo" , 2, "Andrew Stanton", '2003-01-01', 9311689, "" ),
("Le Dîner de cons" , null, "Francis Veber", '1998-01-01', 9247001, 'francais' ),
("Harry Potter et la Chambre des secrets" , 20, "Chris Columbus", '2002-01-01', 9144701, "britano-americain " ),
("L'Ours" , null, "Jean-Jacques Annaud", '1988-01-01', 9136266, "francais" ),
("Le Grand Bleu" , null, "Luc Besson", '1988-01-01', 9074317, "franco-italo-americain" ),
("Astérix et Obélix contre César" , null, "Claude Zidi", '1999-01-01', 8948624, "franco-italo-allemand" ),
("Emmanuelle" , 17, "Just Jaeckin", '1974-01-01', 8893996, "francais" ),
("La Vache et le Prisonnier" , null, "Henri Verneuil", '1959-01-01', 8844199, "franco-italien" ),
("La Grande Évasion" , null, "John Sturges", '1963-01-01', 8756631, "americain" ),
("West Side Story" , 8, "Robert Wise", '1962-01-01', 8719610, "americain" ),
("Le Bataillon du ciel" , null, "Alexander Esway", '1947-01-01', 8649691, "francais" ),
("Le Fabuleux Destin d'Amélie Poulain" , 35, "Jean-Pierre Jeunet", '2001-01-01', 8636041, "franco-allemand"  ),
("Les Choristes" , 7, "Christophe Barratier", '2004-01-01', 8636016, "franco-allemand"),
("Pour qui sonne le glas" , null, "Sam Wood", '1947-01-01', 8274596, "americain"),
("Rien à déclarer" , null, "Dany Boon", '2011-01-01', 8150825, "franco-belge"),
("Violettes Imépriales" , 41, "Richard Pottier", '1952-01-01', 8125766, "franco-espagnol" ),
("Les Couloirs du temps : Les Visiteurs 2" , null, "Jean-Marie Poiré", '1998-01-01', 8043129, "francais"),
("Le Dictateur" , 36, "Charlie Chaplin", '1945-01-01', 8030641, "americain"),
("E.T. l'extra-terrestre" , 37, "Steven Spielberg", '1982-01-01', 7881332, "americain"),
("Un Indien dans la ville" , null, "Hervé Palud", '1994-01-01',  	7870802, "francais"),
("Tarzan" , 2, "Kevin Lima", '1999-01-01', 7859791, ''); 


 
CREATE TABLE Series
(	
	IDSerie INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 	
	Serie_TitreVF VARCHAR(150) NOT NULL,  
	Serie_TitreVO VARCHAR(150),  
	Serie_DateSortie date not null,
	Series_Episode SMALLINT, 
	Serie_Saisons TINYINT, 
	Serie_Description MEDIUMTEXT,
	Serie_ActeurPrincipal varchar(50)	
);

INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Love, Victor","2020-06-17", 20, 2, "Victor, un nouvel élève du lycée Creekwood, doit s'adapter à sa nouvelle vie et faire face aux problèmes à la maison. 
En plein questionnement sur son orientation sexuelle, il décide de se tourner vers Simon en espérant que ce dernier, qui a vécu les mêmes angoisses que lui auparavant, parviendra à l'aider à naviguer les eaux troubles de l'adolescenc");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Special","2019-04-12", 16, 2, "Couvé par sa mère, un jeune homosexuel atteint de paralysie cérébrale légère décide de prendre son destin en main, et réécrit son histoire pour vivre sa vraie vie, enfin.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Queer As Fuck","2000-12-03", 83, 5, "Sexe, amitié, amour, maladie, droits des homosexuels, carrière... Cinq amis homosexuels, Brian, Michael, Justin, Emmett et Ted, traversent les épreuves de la vie chacun à leur manière.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("London Spy","2015-11-09", 5, 1, "Danny, un jeune homme romantique et mal dans sa peau, tombe amoureux de l'énigmatique et asocial Alex. Lorsque ce dernier disparaît, Danny s'emploie à le retrouver. Les découvertes qu'il va faire sur la vie secrète de son amant, qui était en réalité un agent secret travaillant pour le compte du MI6, vont peu à peu le plonger au cœur d'une gigantesque machination qui le dépasse.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("SKAM (France)","2018-02-05", 82, 8, "A chaque saison, nous suivons le parcours d’un personnage et découvrons au fil des événements, la vie de ce groupe d’amies iconiques, mais aussi celle des garçons qu’elles côtoient.
");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("It's a sin! ","2021-01-22", 5, 1, "Ritchie, Roscoe et Colin débarquent à Londres en 1981. Les jeunes hommes vont commencer leur vie d'adulte avec un virus nouveau qui se propage dans la communauté gay. C’est l’histoire de leurs amis, de leurs amants et de leurs familles.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("The New Normal","2012-09-12", 22, 1, "Bryan et David souhaitent fonder une famille et cherchent la parfaite mère-porteuse. Lorsqu'ils choisissent Goldie, ils ont la mauvaise surprise de découvrir que la grand-mère républicaine de celle-ci est plus que présente dans sa vie. 
Et quand elle déménage avec sa fille en Californie pour se rapprocher des deux hommes, la vieille femme les suit évidemment...");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Champions","2018-03-18", 10, 1, "Vince a la vie rêvée de tout célibataire : il possède le cinquième plus grand club de gym de Brooklyn, enchaîne les aventures d'un soir avec de magnifiques jeunes femmes et vit en colocation avec son adorable frère, Matthew. 
Sa vie se complique lorsque son amourette du lycée, Priya, débarque avec leur fils de 15 ans, Michael, afin de l'inscrire dans l'école pour surdoués du quartier. Vince parviendra-t-il à gérer cet adolescent ambitieux et plein d'esprit ?");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Class","2016-10-22", 8, 1, "La Coal Hill Academy n'est pas une école comme les autres. Là-bas, étudiants et corps enseignant se croisent dans les couloirs du bâtiment, partageant leur quotidien peuplé de créatures étranges et rythmé par des voyages temporels.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Torchwood","2016-10-22", 41, 4, "A la tête de l'organisation Torchwood de Cardiff, le capitaine Jack Harkness et son équipe utilisent les technologies extra-terrestres pour venir à bout de problèmes qui dépassent le gouvernement et la police. Unis, ils se battent pour le futur de l'humanité. Car c'est au 21ème siècle que tout va se jouer...");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("#Philo","2015-09-14", 26, 3, "Un prof de philo sarcastique et ironique cherche des méthodes différentes pour encourager ses élèves à toujours refuser l'ordre établi.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Shameless (US)","2011-01-09", 136, 11, "Pour les enfants Gallagher, la vie est tout sauf un long fleuve tranquille... Fiona, l'aînée, âgée de 20 ans, élève du mieux possible sa soeur et ses quatre frères. Leur mère, Monica, les a abandonnés pour refaire sa vie avec une femme. Quant à leur père, Frank, paumé, chômeur et alcoolique, il dilapide l'argent des allocations familiales.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Degrassi: Nouvelle génération","2001-10-14", 392, 14, "Dans les années 80, les ados se passionnaient pour les trépidantes Années collèges de Joey, Spike, Snake et Lucy.
Aujourd'hui, Spike a une fille, Emma, 12 ans. Avec ses copains Tobby, JT, Liberty, Sean, Ashley, Paige, Terri, Spinner et Jimmy, ils forment la bande de Degrassi : Nouvelle Génération, s'assoient sur les mêmes bancs d'école que leurs parents. Pour eux tous, comme pour leurs aînés, l'amitié est la valeur sûre pour affronter tous les problèmes, chagrin d'amour ou violence familiale, pertes de repères ou maladie grave...");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("13 Reasons Why","2017-03-17", 49, 4, "Clay Jensen, un adolescent qui découvre sous son porche au retour du lycée une mystérieuse boîte portant son nom. À l'intérieur, des cassettes enregistrées par Hannah Baker, une camarade de classe qui s'est tragiquement suicidée deux semaines auparavant. Les enregistrements révèlent que la jeune fille, dont il était amoureux, a décidé de mettre fin à ses jours pour treize raisons. Clay est-il l'une de ces raisons ?");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Sex Education","2019-01-11", 16, 3, "La rebelle Maeve entraîne Otis, un ado vierge mais doté d'une mère sexologue, dans la création d'une cellule de thérapie sexuelle clandestine au sein de leur lycée...");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Grey's Anatomy","2006-03-27", 398, 18, "L'histoire de la vie personnelle et professionnelle de cinq internes en chirurgie et leurs superviseurs.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Skins (UK)","2007-12-06", 62, 7, "L'histoire d'un groupe d'adolescents britanniques qui essaient de grandir et de trouver l'amour et le bonheur malgré problèmes familiaux et difficultés liées à l'adolescence.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Physique ou Chimie","2009-02-04", 77, 7, "La vie de lycéens, se focalisant sur la drogue, la grossesse et la sexualité.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("90210 Beverly Hills : Nouvelle génération","2009-01-02", 114, 5, "Une famille originaire du Kansas déménage à Beverly Hills, où les deux enfants doivent s'adapter à la vie difficile au lycée.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("The Fosters","2013-06-03", 104, 5, "Un couple de lesbiennes - l'une est policière, l'autre enseignante dans une école privée - sont les heureuses mamans de trois enfants : un fils biologique et des jumeaux adoptés, une fille et un garçon. 
Leur équilibre familial est bousculé lorsqu'elles accueillent une adolescente rebelle au sein de leur foyer...");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Les 100","2015-01-20", 104, 7, "97 ans après qu'une guerre nucléaire ait détruit la civilisation, un vaisseau spatial contenant les derniers survivants de l'humanité envoie 100 délinquants mineurs sur Terre dans l'espoir de repeupler la planète.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("La Théorie du Y","2017-09-28", 21, 2, "Anna, bien qu'étant en couple avec Matteo, tombe sous le charme de Claire à une soirée..");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("De Celles Qui Osent","2017-06-28", 52, 5, "
L'histoire de trois amies, Jane, Kat et Sutton, qui travaillent pour Scarlet, un magazine féminin.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Man in an Orange Shirt","2017-07-31", 2, 1, "Deux histoires d'amour racontées à deux époques et défis différents : Michael et Thomas juste après la Seconde Guerre mondiale, et Adam et Steve aujourd'hui.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Fiertés","2018-05-03", 3, 1, "Série retraçant la veille de l'arrivée au pouvoir de François Mitterrand en 1981 jusqu'à l'adoption du mariage pour tous en 2013, tout en s'intéressant à la vie de famille et aux combats menés par les homosexuels.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Everything Sucks!","2018-02-16", 10, 1, "L'histoire de la dispute entre les membres du club vidéo d'un lycée de l'Oregon et du club théâtre.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Coyotes","2021-05-31", 6, 1, "L'histoire de la dispute entre les membres du club vidéo d'un lycée de l'Oregon et du club théâtre.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Elite","2018-10-05", 40, 4, "Après l'effondrement d'un lycée, un constructeur tente de redorer son image en proposant de payer les études de trois jeunes victimes dans une prestigieuse école privée.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Atypique","2017-08-11", 38, 4, "Quand un ado autiste décide de trouver une petite amie, sa soudaine soif d’indépendance crée dans toute sa famille une remise en question aussi radicale qu'inattendue.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Roswell: New Mexico","2019-01-15", 341, 2, "Une jeune femme née de parents migrants sans papiers retourne à contrecoeur dans sa ville natale : Roswell. Elle y découvre que son amour de jeunesse, désormais policier, est un extraterrestre ayant caché ses capacités toute sa vie. Tandis qu'ils se rapprochent à nouveau l'un de l'autre, une...");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Glee","2009-09-09", 121, 6, "Will Schuester décide de prendre la direction du club de chant de son établissement, laissé bien mal en point par son prédécesseur. 
Ravivant dans le même temps ses aspirations de jeunesse et la jalousie de sa femme, Will va déployer tout son enthousiasme afin de constituer un nouveau groupe, composé de plusieurs élèves n'ayant rien à voir les uns avec les autres. Losers, footballeurs, intellos, pom-pom girls..");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Britannia High","2008-10-30", 9, 1, "Le quotidien de 6 jeunes et talentueux artistes qui suivent des cours de danse, de chant, de théâtre au sein une école des arts et de la scène nommée Britannia High. 
Ces jeunes gens vont devoir combiner leurs vies personnelles, leurs cours et leurs ambitions pour devenir de vrais stars.");
INSERT INTO Series (Serie_TitreVF, Serie_DateSortie, Series_Episode, Serie_Saisons, Serie_Description) VALUES ("Please Like me","2013-02-28", 32, 4, "
Enfin adulte, Josh réalise que ses parents, dont il a toujours suivi les conseils, sont aussi perdus que lui face aux différents aléas de la vie..");


DROP TABLE IF EXISTS Videogames;
CREATE TABLE Videogames
(	
	IDVieogames INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 	
	Videogames_Titre VARCHAR(150) NOT NULL,   
	Videogames_DateSortie date not null,
	Videogames_Développeur VARCHAR(50),
    Videogames_Editeur VARCHAR(50),
    Videogames_Categorie VARCHAR(150)
);

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Grand Theft Auto V",'2013-09-13',"Rockstar North","Rockstar Games","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Sea of Thieves", '2018-03-20',"Rare Studio","XBox Game Studios", "Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Dead by daylight",'2016-06-16', "Behaviour Interactive","Starbreeze Studios", "Survival horror");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Minecraft",'2011-11-19',"Notch", "Mojang Studio","Sandbox");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Cyberpunk 2077",'2020-12-10',"CD Projekt RED","CD Projekt","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Red Dead Redemption", '2010-05-18',"Rockstar San Diego","Rockstar Games","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Red Dead Redemption II",'2018-09-26', "Rockstar Studio","Rockstar Games","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("The Elder Scrolls V: Skyrim",'2011-11-11', "Bethesda Game Studios","Bethesda Softworks","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Assassin's Creed Valhalla",'2020-11-10',"Ubisoft Montréal","Ubisoft","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("No Man's Sky",'2016-08-10',"Hello Games","Hello Games","Science-Fiction");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Far Cry V",'2018-03-27',"Ubisoft Montréal","Ubisoft","Actioin-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Planet Zoo",'2019-11-05',"Frontier Developments","Frontier Developments","Simulation");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Les Sims IV",'2014-09-04',"Maxis","Electronic Arts","Simulation");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Horizon Zero Dawn",'2017-03-01',"Guerilla Games","Sony Interactive Entertainment","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Dying light",'2015-02-26',"Techland","Warner Bros","Survival horror");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Battlefield IV",'2013-10-31',"DICE","Electronic Arts","FPS");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Kerbal Space Program", '2011-01-17',"Squad","Private Division","Simulation");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Mount and Blade Warband",'2010-03-30',"TaleWorlds","Paradox Interactive","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Mount and Blade II: Bannerlord",'2020-03-30',"Taleworlds","TaleWorlds","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Star Wars Battlefront 2",'2017-11-17',"Dice Studios","Electronic Arts","FPS");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Sid Meier's Civilization VI",'2016-10-21', "Firaxis Games","2K Games","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("The Binding of Isaac",'2011-09-28',"Edmund McMillen","Edmund McMillen","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Resident Evil II",'2019-01-25',"Capcom","Capcom","Survival horror");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Heart of Iron IV",'2016-06-06', "Paradox Developments Studios","Paradox Interactive", "Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Age of Empire III",'2005-04-11',"Ensemble Studios","Microsoft Game Studios","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Dark Souls III",'2016-04-12',"From Software","From Software","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("The Witcher III: Wild Hunt",'2015-05-19',"CD Projekt RED","Bandai Namco","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Stardew Valley",'2016-02-26',"Concerned Ape","Chucklefish Games","RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Total War: Rome II",'2013-09-03',"Creative Assembly","Sega","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Total War: Warhammer II",'2017-09-28',"Creative Assembly","Sega","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("FIFA 2021",'2020-10-09',"EA Canada","EA Sports","Simulation");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Microsoft Flight Simulator 2020",'2020-08-18',"Asobo Studios","XBox Game Studios","Simulaltion");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Gwent: The Witcher card game",'2018-09-18',"CD Projekt RED","CD Projekt","Jeu de cartes");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("The Sinking City",'2019-06-27',"Frogware","Nacon","Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Cities: Skyline",'2015-03-10',"Colossal Order","Paradox Interactive","Gestion");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Anno 1800",'2019-04-16',"Ubisoft Blue Byte","Ubisoft","Gestion");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("The Elder Scrolls IV: Oblivion",'2006-03-24',"Bethesda Game Studios","2K Games","RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Call of Duty Modern Warfare",'2019-10-25',"Infinity Ward","Activision","FPS");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Crusader Kings III",'2020-09-01',"Paradox Developments Studios","Paradox Interactive","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Half-Life II",'2004-11-16',"Valve Corporation","Valve Corporation","FPS");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Bioshock Infinite",'2013-03-26',"Irrational Games","2K Games","Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Portal II",'2011-04-19',"Valve","Valve","Réflexion");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Diablo III",'2012-05-15',"Blizzard Entertainment","Activision Blizzard","Action-RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Borderlands III",'2012-09-21',"Gearbox Software","2K Games","RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Mass Effetc III",'2012-03-09',"Bioware","Electronic Arts","Action-Aventure");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Company of Heroes",'2006-09-29',"Relic Entertainment","Sega","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Divinity: Original Sin II",'2017-09-14',"Larian Studios","Larian Studios","RPG");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Starcraft II: Wings of liberty",'2010-07-27',"Blizzard Entertainment","Blizzard Entertainment","Stratégie");

INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Hitman II",'2018-11-14',"IO Interactive","Warner Bros Interactive Entertainment","Infiltration");
INSERT INTO Videogames (Videogames_Titre,Videogames_DateSortie,Videogames_Développeur,Videogames_Editeur,Videogames_Categorie) 
VALUES ("Metal Gear Solid V: the Phantom Pain",'2015-09-01',"Kojima Productions","Konami","Infiltration");

