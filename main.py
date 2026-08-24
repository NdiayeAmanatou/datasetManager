#importation des modules 
import menu
import gestion
import statistiques

# Programme Principal
continuer = True

while continuer:
    menu.afficher_menu()
    choix = input("votre choix: ")

    if choix == "1":
        gestion.ajouter_dataset()

    elif choix == "2":
        gestion.afficher_datasets()
        
#Partie 8 : le dataset recherché n'existe pas;
#10)Ajout des fonctionnalites (Rechercher)
    elif choix == "3":
        gestion.rechercher_dataset()

#10) Ajout des fonctionnalite (Trier)        
    elif choix == "4":
        gestion.trier_dataset()          

#10) Ajout des fonctionnalite (Modifier) 
    elif choix == "5":
        gestion.modifier_dataset()

 #10) Ajout des fonctionnalite (Supprimer)               
    elif choix == "6":
        gestion.supprimer_dataset()

#Partie 6 : 11) Affichage des statistiques                
    elif choix == "7":
        statistiques.statistiques(gestion.ma_liste_dataset, gestion.domaines_autorise)
        
#Partie 7 : fichiers
#12)sauvegarde des données dans le fichier datasets
    elif choix == "8":
        gestion.sauvegarder()

 #12)recharger et afficher les donnees  
 #Partie 8 : exceptions le fichier n'existe pas; 
 #Partie 8 : exceptions le fichier est vide;
    elif choix == "9":
        gestion.recharger()

    elif choix== "10":
        print("Quitter l'application")
        continuer = False
    else:
        print("choix invalide, veuillez reessayer.")