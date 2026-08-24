import json

def sauvegarder_json(datasets, chemin_fichier):
    if len(datasets) == 0:
        print("Aucun dataset à sauvegarder.")
    else:
        with open(chemin_fichier, "w") as fichier:
            json.dump(datasets, fichier, indent=4)
        print(f"Datasets sauvegardés dans {chemin_fichier} avec succès.")


def recharger_json(chemin_fichier):
    try:
        with open(chemin_fichier, "r") as fichier:
            lignes = json.load(fichier)

            if len(lignes) == 0:
                print(f"Le fichier {chemin_fichier} est vide.")
            else:
                print(f"\n===== Datasets chargés depuis {chemin_fichier} =====")
                for ligne in lignes:
                    print(f"- {ligne['nom']} | {ligne['domaine']} | {ligne['lignes']} lignes | {ligne['format']}")
    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'existe pas encore. Sauvegardez d'abord des datasets.")