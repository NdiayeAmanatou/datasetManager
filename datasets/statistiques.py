# statistiques.py
def statistiques(ma_liste_dataset, domaines_autorise):
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