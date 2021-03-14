#Seul la fusion des blocs n'a pas était fait

class Bloc:
    def __init__(self,addr_debut, taille, drapeau):
        self.addr_debut=addr_debut
        self.taille=taille
        self.drapeau=drapeau 

class Memoire: #Le constructeur créé la mémoire donc pas besoin de fonction
    def __init__(self,nbMots):
        self.nbMots=nbMots
        self.liste= [Bloc(0,nbMots,"FREE")] #On créé le bloc via son constructeur et on le met dans la liste

    def allocation(self, taille): #Question 2
        """Alloue la mémoire"""
        for bloc in self.liste:
            if bloc.drapeau == "FREE" and bloc.taille >= taille: #On alloue la mémoire sur le bloc libre
                bloc.taille=bloc.taille-taille
                if bloc.taille == 0:
                    self.liste.remove(bloc)
                self.liste.append(Bloc(bloc.addr_debut+bloc.taille,taille,"USED"))
                self.liste=sorted(self.liste, key=lambda memoire: memoire.addr_debut) 
                return 
        print("Espace insufisant")   

    def liberation(self,addr):#Question 3
        for bloc in self.liste:
            if bloc.addr_debut==addr and bloc.drapeau=="USED":
                bloc.drapeau="FREE"
                return 
            if bloc.addr_debut == addr and bloc.drapeau == "FREE":
                print("Espace déjà libre")
                return
        print("Cette adresse n'existe pas !")

    def defragmentation(self):#Question 4
        liste2=[]
        for bloc in self.liste:
            if bloc.drapeau=="USED":
                if liste2==[]:
                    bloc.addr_debut=0
                    liste2.append(bloc)
                else:
                    bloc.addr_debut=liste2[-1].addr_debut+liste2[-1].taille
                    liste2.append(bloc)
        for bloc in self.liste:
            if bloc.drapeau == "FREE":
                if liste2 == []:
                    bloc.addr_debut = 0
                    liste2.append(bloc)
                else:
                    bloc.addr_debut = liste2[-1].addr_debut+liste2[-1].taille
                    liste2.append(bloc)

        self.liste=liste2
       

    def affiche(self):
        print("Etat de la mémoire : ")
        for bloc in self.liste:
            print(f"Adresse : {bloc.addr_debut} | taille : {bloc.taille} | {bloc.drapeau}")


memoire = Memoire(10) #Question 1
memoire.affiche()
print("\n")
memoire.allocation(3)
memoire.affiche()
print("\n")
memoire.allocation(5)
memoire.affiche()
print("\n")
memoire.allocation(2)
memoire.affiche()

print("\n")
memoire.liberation(0)
memoire.affiche()
print("\n")
memoire.defragmentation()
memoire.affiche()

