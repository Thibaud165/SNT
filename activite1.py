import calendar
import datetime


def calculer_age(date_naissance, date_actuelle):
  if date_naissance > date_actuelle:
    return None

  annees = date_actuelle.year - date_naissance.year
  mois = date_actuelle.month - date_naissance.month
  jours = date_actuelle.day - date_naissance.day

  if jours < 0:
    mois_precedent = date_actuelle.month - 1 or 12
    annee_precedente = date_actuelle.year if date_actuelle.month > 1 else date_actuelle.year - 1
    jours += calendar.monthrange(annee_precedente, mois_precedent)[1]
    mois -= 1

  if mois < 0:
    mois += 12
    annees -= 1

  return annees, mois, jours


print("Votre date de naissance (jour/mois/annee) :")
naissance_complete = input(">>> ")
print()

try:
  naissance_date = datetime.datetime.strptime(naissance_complete, "%d/%m/%Y").date()
except ValueError:
  print("Erreur, format de date invalide")
else:
  actuelle_date = datetime.date.today()
  actuelle_complete = actuelle_date.strftime("%d/%m/%Y")

  print("Date actuelle (jour/mois/annee) :")
  print(">>>", actuelle_complete)
  print()

  age = calculer_age(naissance_date, actuelle_date)

  if age is None:
    print("Erreur, la date de naissance est dans le futur")
  else:
    age_annee, age_mois, age_jour = age
    print("Vous avez :")
    print(age_annee, "ans")
    print(age_mois, "mois")
    print(age_jour, "jours")
    print()