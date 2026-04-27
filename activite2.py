import random

user_name = input("Entrez un nom d'utilisateur : ")
user_score = 0
bot_score = 0

while bot_score != 3 or user_score != 3:
    action_joueur = input("Choisissez une action (pierre, feuille, ciseaux) : ")
    action_bot = random.choice(["pierre", "feuille", "ciseaux"])
    if action_joueur not in ["pierre", "feuille", "ciseaux"]:
        print(f"\nAction invalide, essayez à nouveau.")
    else:
        print(f"Le bot a choisi :", action_bot, "\n")
        if action_joueur == action_bot:
            print("Egalité !")
        elif (action_joueur == "pierre" and action_bot == "ciseaux") or (action_joueur == "feuille" and action_bot == "pierre") or (action_joueur == "ciseaux" and action_bot == "feuille"):
            print("Vous gagnez cette manche !")
            user_score += 1
        else:
            print("Le bot gagne cette manche !")
            bot_score += 1
        print(user_name, ":", user_score)
        print("Bot :", bot_score)
    print()


print("Score final :")
print(user_name, ":", user_score)
print("Bot :", bot_score)
if user_score > bot_score:
    print("Félicitations, vous avez gagné !")
else:
    print("Dommage, le bot a gagné !")