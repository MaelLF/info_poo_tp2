import unittest
from classdef import *


#Auteur : Le Floch Mael
#Date de création : 19 Fevrier 2024

#Objectif : Tests unitaires du programme de simulation du jeu de bataille


class TestCarte(unittest.TestCase):

    def test_get_val (self):
        c=Carte(4,'Trèfle')
        self.assertEqual(4,c.get_val())
    
    def test_get_symb (self):
        c=Carte(4,'Trèfle')
        self.assertEqual('Trèfle',c.get_symb())

    def test_set_val (self):
        c=Carte(12,'Trèfle')
        c.set_val(4)
        self.assertEqual(4,c.get_val())
    
    def test_set_symb (self):
        c=Carte(4,'Trèfle')
        c.set_symb('Carreau')
        self.assertEqual('Carreau',c.get_symb())
        
    def test_est_plus_grand_1 (self):
        c=Carte(12)
        g=Carte(5)
        self.assertEqual(c._Carte__est_plus_grand(g),1)

    def test_est_plus_grand_0 (self):
        c=Carte(1)
        g=Carte(5)
        self.assertEqual(c._Carte__est_plus_grand(g),0)

    def test_est_plus_grand_moins1 (self):
        c=Carte(5)
        g=Carte(5)
        self.assertEqual(c._Carte__est_plus_grand(g),-1)





class TestJoueur(unittest.TestCase):

    def test_init(self):
        j = Joueur()
        self.assertEqual(j.nom, 'sans nom')
        self.assertEqual(j.list_carte, [])
        self.assertEqual(j.defausse, [])
        self.assertEqual(j.score, 0)

    def test_get_score(self):
        j = Joueur()
        self.assertEqual(j.get_score(), 0)

    def test_set_score(self):
        j = Joueur()
        j.set_score(10)
        self.assertEqual(j.get_score(), 10)

    def test_ajouter_carte(self):
        j = Joueur()
        carte = Carte(4, 'Trèfle')
        j._Joueur__ajouter_carte(carte)
        self.assertIn(carte, j.list_carte)

    def test_ajouter_defausse(self):
        j = Joueur()
        carte = Carte(4, 'Trèfle')
        j._Joueur__ajouter_defausse(carte)
        self.assertIn(carte, j.defausse)

    def test_set_list_carte(self):
        j = Joueur()
        liste_carte = [Carte(4, 'Trèfle'), Carte(7, 'Pique')]
        j.set_list_carte(liste_carte)
        self.assertEqual(j.list_carte, liste_carte)

    def test_get_list_carte(self):
        j = Joueur()
        liste_carte = [Carte(4, 'Trèfle'), Carte(7, 'Pique')]
        j.set_list_carte(liste_carte)
        self.assertEqual(j.get_list_carte(), liste_carte)



class TestJeu(unittest.TestCase):

    def test_init(self):
        jeu = Jeu()
        self.assertIsInstance(jeu.joueur1, Joueur)
        self.assertIsInstance(jeu.joueur2, Joueur)
        self.assertEqual(jeu.deck, [])

    def test_distribution(self):
        jeu = Jeu()
        jeu._Jeu__distribution()
        self.assertEqual(len(jeu.joueur1.list_carte), len(jeu.joueur2.list_carte))
        self.assertEqual(len(jeu.joueur1.list_carte) + len(jeu.joueur2.list_carte), 52)

    def test_repioche(self):
        jeu = Jeu()
        jeu._Jeu__distribution()
        jeu.joueur1.list_carte = []
        result = jeu._Jeu__repioche(2)
        self.assertEqual(result, 2)
        self.assertGreaterEqual(len(jeu.joueur1.list_carte), 0)


    def test_round(self):
        jeu = Jeu()
        result = jeu._Jeu__round()
        self.assertIn(result, [1, 2, 0])
    
    
unittest.main(argv=[''], verbosity=2,exit=False)