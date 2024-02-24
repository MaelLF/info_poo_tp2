import random


#Auteur : Le Floch Mael
#Date de création : 19 Fevrier 2024

#Objectif du programme : Création de classes permettant la simulation d'un jeu de bataille :
# -l'affichage des score des différents joueurs
# -la simulation d'une partie de bataille

# Il est a noté que des fonctions ont été ajouté et ont essentiellement servies au débugage du code


#Dictionnaire des valeurs d'un deck
val_carte ={2 : '2',3 : '3',4: '4', 5: '5',6:'6',7:'7',8:'8',9:'9',10:'10',11 :'Valet',12 : 'Dame', 13 : 'Roi',14 : "As"}

#Tableau des symboles possibles d'un deck
tab_symbol = ['Carreau','Coeur','Pique','Trèfle']

#////////////////////////////////////////////////////////////////////////////////////////////////

class Carte (object): #Définition de la classe
    def __init__(self,val=0,symb='NULL'): #La classe carte a deux composants par défaut la carte est un 0 de NULL
        self.valeur = val
        self.symbole = symb

    def get_val(self):    # Méthode publique d'obtention de la donnée valeur
        return self.valeur
    
    def set_val(self,n:int):    #Méthode publique de changement de la donnée valeur
        self.valeur = n
    
    def get_symb(self):    # Méthode publique d'obtention de la donnée valeur
        return self.symbole
    
    def set_symb(self,symb:str):    #Méthode publique de changement de la donnée valeur
        self.symbole = symb

    def __est_plus_grand(self,c): #Méthode de comparaison entre deux cartes si les cartes sont égales on retourne -1
        a = self.valeur - c.valeur #sinon on retourne 1 si la carte en argument est plus petite et 0 si elle est plus grande
        if a==0 :
            return -1
        else :
            return self.valeur > c.valeur
    
    def __str__(self):  #Méthode d'affichage de la carte
        return f'{val_carte[self.valeur]} de {self.symbole}'
    
#////////////////////////////////////////////////////////////////////////////////////////////////
    
class Joueur (object): #Définition de la classe
    def __init__(self,nom = 'sans nom'): #La classe Joueur a 4 arguments : le nom, le liste de carte, la défausse et le score du joueur
        self.nom = nom
        self.list_carte = []
        self.defausse =[]
        self.score = 0
    
    def get_score(self): #Méthode publique pour obtenir le score du joueur
        return self.score
    
    def set_score (self,n): #Méthode publique pour changer le score du joueur
        self.score = n
    
    def __ajouter_carte (self,carte = Carte()): #Méthode pour ajouter une carte à la liste de carte du joueur
        self.list_carte.append(carte)

    def __ajouter_defausse (self,carte = Carte()): #Méthpde pour ajouter une carte à la défausse du joueur
        self.defausse.append(carte)
    
    def set_list_carte (self,packet=[]): #Méthode publique pour changer la variable liste carte, par défaut initialiser à liste vide
        self.liste_carte = packet

    def get_list_carte (self): #Méthode publique pour obtenir la variable list_carte
        return self.list_carte
    
    def __afficher_packet(self): #Méthode d'affichage de la liste des cartes d'un joueur
        for carte in self.list_carte :
            print(carte)


#////////////////////////////////////////////////////////////////////////////////////////////////
#Fonction pour afficher n'importe quel packet n
def afficher_mise(n):
    print('mise :')
    for carte in n :
        print(carte)

#////////////////////////////////////////////////////////////////////////////////////////////////

class Jeu (object):#Définition de la classe
    def __init__(self):#La classe Jeu a 3 arguments : les deux joueurs et le deck de carte initial du jeu
        self.joueur1 = Joueur()
        self.joueur2 = Joueur()
        self.deck =[]

    def __distribution(self): #Méthode d'initialisation du deck et de partage des cartes
        for symbol in tab_symbol : #Double boucle d'initialisation des cartes (symbole et valeur)
            for i in range (2,15): 
                self.deck.append(Carte(i,symbol))
        random.shuffle(self.deck)    # Trie au hasard des cartes du deck
        cards_per_player = len(self.deck) // 2  #le deck est séparé en deux puis distribué
        self.joueur1.list_carte = self.deck[:cards_per_player]
        self.joueur2.list_carte = self.deck[cards_per_player:]
        self.joueur1.score = len(self.joueur1.list_carte)
        self.joueur2.score = len(self.joueur2.list_carte)

    def __repioche (self,i): #Méthode de repioche d'un joueur s'il lui reste moins de n cartes (vérifie aussi si le joeur a perdu : plus de carte dans la défausse) Retourne le joueur ayant gagné
        if len(self.joueur1.list_carte) < i :
            if self.joueur1.defausse == [] :
                return 2
            random.shuffle(self.joueur1.defausse)
            self.joueur1.list_carte = self.joueur1.list_carte + self.joueur1.defausse
            self.joueur1.defausse = []
        if len(self.joueur2.list_carte) <i :
            if self.joueur2.defausse == [] :
                return 1
            random.shuffle(self.joueur2.defausse)
            self.joueur2.list_carte = self.joueur2.list_carte + self.joueur2.defausse
            self.joueur2.defausse=[]
                    
    def __round(self): #Méthode de simulation d'une partie
        print('Distribution des cartes')
        self.__distribution()
        while(self.joueur1.score != 0 and self.joueur2.score!=0): #Tant que les deux joueurs ont des cartes on continue de joueur
            mise =[]   #Mise de cartes que les joueurs peuvent remporter
            a=-1       #Pour entrée dans la boucle secondaire, variable qui stocke si la carte du joueur 1 est plus grande que la carte du joueur 2 au sens de est_plus_grand
            b=[]       #Variable de stockage des cartes qui vont dans la mise
            print('Round :')
            while(a==-1 ) : #Rebouclage en cas d'égalité(s)
                
                print(self.joueur1.list_carte[0],' vs ',self.joueur2.list_carte[0])
                a=self.joueur1.list_carte[0]._Carte__est_plus_grand(self.joueur2.list_carte[0])

                if(a==1):   #Cas ou joueur 1 gagne le round
                    b=self.joueur1.list_carte.pop(0)
                    mise.append(b)
                    b=self.joueur2.list_carte.pop(0)
                    mise.append(b)
                    self.joueur1.defausse += mise
                    self.joueur1.score =len(self.joueur1.list_carte +self.joueur1.defausse)
                    self.joueur2.score = len(self.joueur2.list_carte +self.joueur2.defausse)
                    print('à gagner :',len(mise)/2,'points')
                    mise =[]

                if(a==0) : # Cas ou joueur 1 perd le round
                    b=self.joueur1.list_carte.pop(0)
                    mise.append(b)
                    b=self.joueur2.list_carte.pop(0)
                    mise.append(b)
                    self.joueur2.defausse += mise
                    self.joueur2.score = len(self.joueur2.list_carte +self.joueur2.defausse)
                    self.joueur1.score =len(self.joueur1.list_carte +self.joueur1.defausse)
                    print('à gagner :',len(mise)/2,'points')
                    mise =[]

                if(a==-1): #Cas d'égalité entre les deux joueurs

                    #Egalité dûe au fait qu'un joeur n'a pas assez de carte pour faire une bataille
                    if len(self.joueur1.list_carte)+ len(self.joueur1.defausse) < 3  or len(self.joueur2.list_carte)+ len(self.joueur2.defausse) < 3 : 
                        return 0
                    
                    #Cas général
                    if len(self.joueur2.list_carte) < 2 :
                        self.__repioche(2)
                    for i in range(0, 2):
                        if len(self.joueur1.list_carte) > 0:
                            b = self.joueur1.list_carte.pop(0)
                            mise.append(b)
                        if len(self.joueur2.list_carte) > 0:
                            b = self.joueur2.list_carte.pop(0)
                            mise.append(b)
                
                #Affichage de fin de round
                print('Score : ',self.joueur1.score,self.joueur2.score)
                res=self.__repioche(1)
                if res :
                    return res
                print()
                print()
                print()


                

        


        
    


    

