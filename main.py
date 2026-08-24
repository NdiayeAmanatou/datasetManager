import csv

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
    print("7. Statistiques")
    print("8. Sauvegarder dans un fichier CSV")
    print("9. Charger depuis le fichier CSV")
    print("10. Quitter")

    choix = input("votre choix: ")

    if choix == "1":
# Partie 1 : Types de base, variables, Entrées et sorties 
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
        
#Partie 8 : le dataset recherché n'existe pas;
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
                    break
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

 #10) Ajout des fonctionnalite (Supprimer)               
    elif choix == "6":
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

#Partie 6 : 11) Affichage des statistiques                
    elif choix == "7":
        if len(ma_liste_dataset) == 0:
            print("Aucun dataset n'est enregistré.")
        else:
            nb_datasets = len(ma_liste_dataset)
            nb_total_lignes = sum([d["lignes"] for d in ma_liste_dataset])
            moyenne_colonnes = sum([d["colonnes"] for d in ma_liste_dataset]) / len(ma_liste_dataset)
            nb_publics = len([d for d in ma_liste_dataset if d["public"] == True])
            nb_prives = len([d for d in ma_liste_dataset if d["public"] == False])
            nb_csv = len([d for d in ma_liste_dataset if d["format"] == "csv"])
            nb_json = len([d for d in ma_liste_dataset if d["format"] == "json"])
            repartition = {domaine: len([d for d in ma_liste_dataset if d["domaine"] == domaine]) for domaine in domaines_autorise}

            print("\n ----Statistiques---- ")
            print(f"Nombre de datasets : {nb_datasets}")
            print(f"Nombre total de lignes : {nb_total_lignes}")
            print(f"Nombre moyen de colonnes : {moyenne_colonnes:.0f}") 
            print(f"Datasets publics: {nb_publics}") 
            print(f"Datasets prives: {nb_prives}") 
            print(f"Nombre de datasets au format csv: {nb_csv}")  
            print(f"Nombre de datasets au format json: {nb_json}")  
            print("Répartition par domaine :")
            for domaine, nombre in repartition.items():
                print(f"  - {domaine} : {nombre}") 
#Partie 7 : fichiers
#12)sauvegarde des données dans le fichier datasets
    elif choix == "8":
        if len(ma_liste_dataset) ==0:
              print(" il n'y a aucun dataset a sauvegarder")
        else:
            with open("datasets.csv" , "w" , newline="") as fichier:
                writer = csv.DictWriter(fichier, fieldnames=["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"])
                writer.writeheader()
                for d in ma_liste_dataset:
                    writer.writerow(d)
            print("Datasets sauvegardés dans datasets.csv avec succès.")

 #12)recharger et afficher les donnees  
 #Partie 8 : exceptions le fichier n'existe pas; 
 #Partie 8 : exceptions le fichier est vide;
    elif choix == "9":
        try:
            with open("datasets.csv", "r") as fichier:
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

    elif choix== "10":
        print("Quitter l'application")
        continuer = False
    else:
        print("choix invalide, veuillez reessayer.")