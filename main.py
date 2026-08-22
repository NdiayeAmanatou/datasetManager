# PARTIE 1 : Types de base, variables, Entrées/sorties
# Saisie des métadonnées 
nom = input("Quel est le nom du datatset: ")
domaine = input(" Precisez Domaine : ")
nb_lignes = int(input("Donnez le nombre de ligne: "))
nb_colonnes = int(input("Donner le nombre de colonnes : "))
taille_mo = float(input("Donner la taille en Mo : "))
format_fichier = input(" Donner le format (csv ou json) : ").lower()
public_saisie = input("Public (true ou false) : ").lower()

# Conversion de "true"/"false" (texte) en booléen Python
public = public_saisie == "true"

# 4) Affichez ensuite un résumé formaté. 
print("\n===== Résumé du dataset =====")
print(f"Nom          : {nom}")
print(f"Domaine      : {domaine}")
print(f"Lignes       : {nb_lignes}")
print(f"Colonnes     : {nb_colonnes}")
print(f"Taille       : {taille_mo} Mo")
print(f"Format       : {format_fichier}")
print(f"Public       : {public}")
