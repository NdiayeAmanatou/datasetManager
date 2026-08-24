import csv
ma_liste_dataset=[]
def sauvegarder_csv():
    if len(ma_liste_dataset) ==0:
        print(" il n'y a aucun dataset a sauvegarder")
    else:
        with open("datasets.csv" , "w" , newline="") as fichier:
            writer = csv.DictWriter(fichier, fieldnames=["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"])
            writer.writeheader()
            for d in ma_liste_dataset:
                writer.writerow(d)
        print("Datasets sauvegardés dans datasets.csv avec succès.")    

def recharger_csv():
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
