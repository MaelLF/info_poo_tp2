from classdef import *
def main():
    jeu = Jeu()
        #  jeu._Jeu__distribution()
        # a=jeu.joueur1.list_carte[0]
        #  print (a)
        #  print (a.get_val(),a.get_symb())
        #  a.set_symb('Trèfle')
        # a.set_val(12)
        # print(a)
        # print (int(a.est_plus_grand(Carte(14,'Trèfle'))))
    tab=[]
    for i in range (0,1000):
        jeu=Jeu()
        tab.append(jeu._Jeu__round())
    print(tab.count(0),tab.count(1),tab.count(2),tab.count(-1))

if __name__ == '__main__':
    main()