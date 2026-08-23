# Partie 4 : Tuples
#7) Création d'un tuple contenant les domaines autorisés. 
domaines_autorise = ("Santé", "Finance", "Agriculture", "Transport", "Education")

#Partie 5 : Listes
#9)Création d'une liste contenant les datasets. Chaque ajout est enregistré dans la liste
ma_liste_dataset=[]
# Partie 2: structure de controle
#5) Création d'un menu interactif (provisoire) 
continuer = True

while continuer:
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Trier")
    print("5. Modifier")
    print("6. Supprimer")
    print("7. Quitter")

    choix = input("votre choix: ")

    if choix == "1":
# Partie 1 : Types de base, variables, Entrées et sorties 
        nom = input("quel est le nom du dataset : ")
        
        #8) Vérifiez que le domaine saisi, à la question 3, appartient au tuple
        domaine = input("preciser le domaine : ")
        while domaine not in domaines_autorise:
            print(f"Domaine invalide. Choix possibles : {domaines_autorise}")
            domaine = input("preciser le domaine : ")

        nb_lignes = int(input("donner le nombre de lignes : "))
        nb_colonnes = int(input("donner le nombre de colonnes : "))
        taille_mo = float(input("donner la taille en Mo : "))
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
 
        print("Affichage du dataset")
        print(f"Nom          : {dataset['nom']}")
        print(f"Domaine      : {dataset['domaine']}")
        print(f"Lignes       : {dataset['lignes']}")
        print(f"Colonnes     : {dataset['colonnes']}")
        print(f"Taille       : {dataset['taille']} Mo")
        print(f"Format       : {dataset['format']}")
        print(f"Public       : {dataset['public']}")

    elif choix == "2":
        print("Afficher les datasets")

#10)Ajout des fonctionnalites (Rechercher)
    elif choix == "3":
        if len(ma_liste_dataset) == 0:
            print("Aucun dataset n'est enregistré.")
        else:
            nom_recherche = input(" quel est le nom du dataset que vous rechercher: ")
            trouve = False
            for d in ma_liste_dataset:
                if d["nom"] == nom_recherche:
                    print(f"\n Dataset Trouvé : {d}")
                    trouve = True
            if not trouve:
                print("Aucun dataset trouvé avec ce nom.")
#10) Ajout des fonctionnalite (Trier)        
    elif choix == "4":
        if len(ma_liste_dataset)==0:
            print("il y'a aucun dataset a trier")
        else :
            dataset_tries= sorted(ma_liste_dataset , key=lambda d :d["nom"])
            for d in dataset_tries:
                print(f"- {d['nom']} ")            

#10) Ajout des fonctionnalite (Modifier) 
    elif choix == "5":
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
    elif choix == "6":
        print("Supprimer")
    elif choix == "7":
        print("Quitter l'application")
        continuer = False
    else:
        print("choix invalide, veuillez reessayer.")