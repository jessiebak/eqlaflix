menu_options = {
    1: 'Films',
    2: 'Séries',
    3: 'Jeux-vidéos',
    4: 'Quitter',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     pass

def option2():
	pass

def option3():	
	pass

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Entrez votre choix: '))
        except:
            print('Entrée incorrecte, réessayez.')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('A bientôt!')
            exit()
        else:
            print('Entrée incorrecte, entrez un chiffre entre 1 et 4.')