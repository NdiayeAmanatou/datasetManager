# gestion.py
import csv

# Partie 4 : Tuples
#7) Création d'un tuple contenant les domaines autorisés. 
domaines_autorise = ("Santé", "Finance", "Agriculture", "Transport", "Education")

#Partie 5 : Listes
#9)Création d'une liste contenant les datasets. Chaque ajout est enregistré dans la liste
ma_liste_dataset=[]


# Partie 2: structure de controle
#5) Création d'un menu interactif (provisoire) 
def ajouter_dataset():
                nom = input("quel est le nom du dataset : ")
                
                #8) Vérifiez que le domaine saisi, à la question 3, appartient au tuple
                domaine = input("preciser le domaine : ")
                while domaine not in domaines_autorise:
                    print(f"Domaine invalide. Choix possibles : {domaines_autorise}")
                    domaine = input("preciser le domaine : ")
        
        #Partie 8: exceptions 
        #Saisit d'un texte au lieu d'un nombre (pour le nombre de ligne);
                while True:
                    try:
                        nb_lignes = int(input("donner le nombre de lignes : "))
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")
        #Saisit d'un texte au lieu d'un nombre (pour le nombre de colonne);
                while True:
                    try:
                        nb_colonnes = int(input("donner le nombre de colonnes : "))
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")
        
        #Saisit d'un texte au lieu d'un nombre (pour la taille en Mo);
                while True:
                    try:
                       taille_mo = float(input("donner la taille du fichier en Mo : "))
                       break
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")
                format_fichier = input("choisir le format (csv ou json) : ").lower()
                public_saisie = input("Public (true ou false) : ").lower()
                public = public_saisie == "true"
        
        #Partie 3 – Dictionnaires 
        #6)Création d'un dictionnaire pour stocker les métadonnées de chaque dataset 
                dataset = {
                    "nom": nom,
                    "domaine": domaine,
                    "lignes": nb_lignes,
                    "colonnes": nb_colonnes,
                    "taille": taille_mo,
                    "format": format_fichier,
                    "public": public
                }
         #10) Ajout des fonctionnalite (Ajouter)
                ma_liste_dataset.append(dataset)
                print(f"\nDataset '{nom}' ajouté avec succès !")
def afficher_datasets():
    if len(ma_liste_dataset)==0:
        print("Aucun dataset n'est enregistre ")
    else:
        print("\n====listes des datasets====")
# Partie 1 : Types de base, variables, Entrées et sorties 
        for dataset in ma_liste_dataset:
            print(f"Nom          : {dataset['nom']}")
            print(f"Domaine      : {dataset['domaine']}")
            print(f"Lignes       : {dataset['lignes']}")
            print(f"Colonnes     : {dataset['colonnes']}")
            print(f"Taille       : {dataset['taille']} Mo")
            print(f"Format       : {dataset['format']}")
            print(f"Public       : {dataset['public']}")
            
def supprimer_dataset():
    if len(ma_liste_dataset) == 0:
        print("Aucun dataset n'est enregistré.")
    else:
        nom_suppr = input("quel est le nom du dataset à supprimer : ")
        trouve = False
        for d in ma_liste_dataset:
            if d["nom"] == nom_suppr:
                    ma_liste_dataset.remove(d)
                    print("Le dataset est supprimé avec succès.")
                    trouve = True
                    break
            if not trouve:
                    print("Le dataset est introuvable.")
def rechercher_dataset():
            if len(ma_liste_dataset) == 0:
                print("Aucun dataset n'est enregistré.")
            else:
                nom_recherche = input(" quel est le nom du dataset que vous rechercher: ")
                trouve = False
                for d in ma_liste_dataset:
                    if d["nom"] == nom_recherche:
                        print(f"\n Dataset Trouvé : {d}")
                        trouve = True
                    break
                if not trouve:
                    print("Aucun dataset trouvé avec ce nom.")

def trier_dataset():
     if len(ma_liste_dataset)==0:
           print("il y'a aucun dataset a trier")
     else :
          dataset_tries= sorted(ma_liste_dataset , key=lambda d :d["nom"])
          for d in dataset_tries:
                     print(f"- {d['nom']} ") 

def modifier_dataset():
    if len(ma_liste_dataset) == 0:
           print("Aucun dataset n'est enregistré.")
    else:
        nom_modif = input("quel est le nom du dataset à modifier : ")
        trouve = False
        for d in ma_liste_dataset:
            if d["nom"] == nom_modif:
                d["lignes"] = int(input("entrer a nouveau le nombre de lignes : "))
                d["colonnes"] = int(input("entrer a nouveau le nombres de colonnes : "))
                d["taille"] = float(input("entrer a nouveau la taille en Mo : "))
                print("Dataset modifié avec succès.")
                trouve = True
                break
        if not trouve:
            print("Dataset introuvable.")

def sauvegarder():
    if len(ma_liste_dataset) ==0:
        print(" il n'y a aucun dataset a sauvegarder")
    else:
        with open("data/datasets.csv" , "w" , newline="") as fichier:
            writer = csv.DictWriter(fichier, fieldnames=["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"])
            writer.writeheader()
            for d in ma_liste_dataset:
                writer.writerow(d)
        print("Datasets sauvegardés dans datasets.csv avec succès.")    

def recharger():
    try:
        with open("data/datasets.csv", "r") as fichier:
            reader = csv.DictReader(fichier)
            lignes = list(reader)
            if len(lignes)==0:
                print("le fichier datasets est vide")
            else:
                print("\n===== Datasets chargés depuis datasets.csv =====")
            for ligne in reader:
                         print(f"- {ligne['nom']} | {ligne['domaine']} | {ligne['lignes']} lignes | {ligne['format']}")
    except FileNotFoundError:
        print("Le fichier datasets.csv n'existe pas encore. Sauvegardez d'abord des datasets ")   
