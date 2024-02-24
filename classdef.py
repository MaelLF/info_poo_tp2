import random
val_carte ={2 : '2',3 : '3',4: '4', 5: '5',6:'6',7:'7',8:'8',9:'9',10:'10',11 :'Valet',12 : 'Dame', 13 : 'Roi',14 : "As",}
tab_symbol = ['Carreau','Coeur','Pique','Trèfle']

class Carte (object): #Définition de la classe
    def __init__(self,val=0,symb='NULL'): #La classe carte a deux composants
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

    def est_plus_grand(self,c):
        a = self.valeur - c.valeur
        if a==0 :
            return -1
        else :
            return self.valeur > c.valeur
    
    def __str__(self):
        return f'{val_carte[self.valeur]} de {self.symbole}'
    
class Joueur (object):
    def __init__(self,nom = 'sans nom'):
        self.nom = nom
        self.list_carte = []
        self.defausse =[]
        self.score = 0
    
    def get_score(self):
        return self.score
    
    def set_score (self,n):
        self.score = n
    
    def __ajouter_carte (self,carte = Carte()):
        self.list_carte.append(carte)

    def __ajouter_defausse (self,carte = Carte()):
        self.defausse.append(carte)
    
    def set_list_carte (self,packet=[]): #par défaut initialiser à liste vide
        self.liste_carte = packet

    def get_list_carte (self):
        return self.list_carte
    
    def __afficher_packet(self):
        for carte in self.list_carte :
            print(carte)


#////////////////////////////////////////////////////////////////////////////////////////////////
def afficher_mise(n):
    print('mise :')
    for carte in n :
        print(carte)

class Jeu (object):
    def __init__(self):
        self.joueur1 = Joueur()
        self.joueur2 = Joueur()
        self.deck =[]

    def __distribution(self):
        for symbol in tab_symbol :
            for i in range (2,15):
                self.deck.append(Carte(i,symbol))
        random.shuffle(self.deck)
        cards_per_player = len(self.deck) // 2
        self.joueur1.list_carte = self.deck[:cards_per_player]
        self.joueur2.list_carte = self.deck[cards_per_player:]
        self.joueur1.score = len(self.joueur1.list_carte)
        self.joueur2.score = len(self.joueur2.list_carte)

    def repioche (self,i):
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
                    
    def __round(self):
        print('Distribution')
        print(len(self.deck))
        self.__distribution()
        print('Premier round :')
        #for i in range (0,1):
        while(self.joueur1.score != 0 and self.joueur2.score!=0):
            mise =[]
            a=-1
            b=[]
            print('Round :')
            while(a==-1 ) :
                
                print(self.joueur1.list_carte[0],' vs ',self.joueur2.list_carte[0])
                a=self.joueur1.list_carte[0].est_plus_grand(self.joueur2.list_carte[0])
                if(a==1):
                    b=self.joueur1.list_carte.pop(0)
                    mise.append(b)
                    b=self.joueur2.list_carte.pop(0)
                    mise.append(b)
                    afficher_mise(mise)
                    if len(mise) == 3:
                        return -1
                    self.joueur1.defausse += mise
                    self.joueur1.score =len(self.joueur1.list_carte +self.joueur1.defausse)
                    self.joueur2.score = len(self.joueur2.list_carte +self.joueur2.defausse)
                    print('à gagner :',len(mise)/2,'points')
                    mise =[]
                if(a==0) :
                    b=self.joueur1.list_carte.pop(0)
                    mise.append(b)
                    b=self.joueur2.list_carte.pop(0)
                    mise.append(b)
                    afficher_mise(mise)
                    self.joueur2.defausse += mise
                    self.joueur2.score = len(self.joueur2.list_carte +self.joueur2.defausse)
                    self.joueur1.score =len(self.joueur1.list_carte +self.joueur1.defausse)
                    print('à gagner :',len(mise)/2,'points')
                    mise =[]

                if(a==-1):
                    if len(self.joueur1.list_carte)+ len(self.joueur1.defausse) < 3 :
                        return 0
                    if len(self.joueur2.list_carte)+ len(self.joueur2.defausse) < 3 :
                        return 0
                    if len(self.joueur2.list_carte) < 2 :
                        self.repioche(2)
                    for i in range(0, 2):
                        if len(self.joueur1.list_carte) > 0:
                            b = self.joueur1.list_carte.pop(0)
                            mise.append(b)
                        if len(self.joueur2.list_carte) > 0:
                            b = self.joueur2.list_carte.pop(0)
                            mise.append(b)
                    afficher_mise(mise)
                
                print('Score : ',self.joueur1.score,self.joueur2.score)
                print('len :',len(self.joueur1.list_carte),len(self.joueur2.list_carte))
                print('defausse,',len(self.joueur1.defausse), len(self.joueur2.defausse) )
                if len(self.joueur1.defausse) + len(self.joueur2.defausse) + len(self.joueur1.list_carte)+len(self.joueur2.list_carte)+len(mise)!=52 :
                    return -1
                res=self.repioche(1)
                if res :
                    return res
                
                print()
                print()
                print()


                

        


        
    


    

