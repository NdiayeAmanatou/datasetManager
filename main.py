# importation des modules
import interface.menu as menu
import interface.affichage as affichage
import datasets.gestion as gestion
import datasets.statistiques as statistiques

# Programme Principal
continuer = True
while continuer:
    menu.afficher_menu()
    choix = input("votre choix: ")
    if choix == "1":
        gestion.ajouter_dataset()
    elif choix == "2":
        affichage.afficher_datasets(gestion.ma_liste_dataset)
    elif choix == "3":
        gestion.rechercher_dataset()
    elif choix == "4":
        gestion.trier_dataset()
    elif choix == "5":
        gestion.modifier_dataset()
    elif choix == "6":
        gestion.supprimer_dataset()
    elif choix == "7":
        statistiques.statistiques(gestion.ma_liste_dataset, gestion.domaines_autorise)
    elif choix == "8":
        gestion.sauvegarder()
    elif choix == "9":
        gestion.recharger()
    elif choix == "10":
        print("Quitter l'application")
        continuer = False
    else:
        print("choix invalide, veuillez reessayer.")