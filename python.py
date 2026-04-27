print("Votre date de naissance (jour/mois/annee) :")
naissance_complete = input(">>> ")
print()
print("Date actuelle (jour/mois/annee) :")
actuelle_complete = input(">>> ")
print()

# Decoupage des date en liste pour faire les calcules
naissance_liste = naissance_complete.split("/")
actuelle_liste = actuelle_complete.split("/")

# Calcule de l'age
age_jour = int(actuelle_liste[0]) - int(naissance_liste[0])
age_mois = int(actuelle_liste[1]) - int(naissance_liste[1]) + 12
age_annee = int(actuelle_liste[2]) - int(naissance_liste[2])

# Verification
if age_annee >= 0 and age_mois >= 0 and age_jour >= 0:
  print("Vous avez :")
  print(age_annee, "ans")
  print(age_mois, "mois")
  print(age_jour, "jours")
  print()

else:
  print("Erreur, age trop bas")