#entree="rien"
#n = 0
#while entree != "":
    #entree=input("Tapez un mot (ou juste 'Enter' pour quitter) : ")
   # n += 1
  #  if entree != "":
 #       print(n,entree)
#print("Au revoir !")
from dataclasses import dataclass
@dataclass

class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix= 200000)
    
    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse= 250, prix= 180000)

    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.afficher_nombre_voitures()
print(porsche)