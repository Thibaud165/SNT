import datetime

maintenant = datetime.datetime.now()
annee_actuelle = maintenant.year
mois_actuel = maintenant.month
jour_actuel = maintenant.day

annee_naissance = int(input("Année de naissance : "))
mois_naissance = int(input("Mois de naissance : "))
jour_naissance = int(input("Jour de naissance : "))

ans = annee_actuelle - annee_naissance
mois = mois_actuel - mois_naissance
jours = jour_actuel - jour_naissance

if jours < 0:
    jours += 30
    mois -= 1

if mois < 0:
    mois += 12
    ans -= 1

print(f"Votre âge : {ans} ans, {mois} mois et {jours} jours.")