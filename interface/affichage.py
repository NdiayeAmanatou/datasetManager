def afficher_datasets(ma_liste_dataset):
    if len(ma_liste_dataset) == 0:
        print("Aucun dataset n'est enregistre ")
    else:
        print("\n====listes des datasets====")
        for dataset in ma_liste_dataset:
            print(f"Nom          : {dataset['nom']}")
            print(f"Domaine      : {dataset['domaine']}")
            print(f"Lignes       : {dataset['lignes']}")
            print(f"Colonnes     : {dataset['colonnes']}")
            print(f"Taille       : {dataset['taille']} Mo")
            print(f"Format       : {dataset['format']}")
            print(f"Public       : {dataset['public']}")