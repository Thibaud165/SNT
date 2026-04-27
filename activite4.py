mdp = 123
tentative_possible = 3

while tentative_possible != 0:
    if int(input("Mot de passe : ")) != mdp:
        tentative_possible -= 1
        print(f"\nMot de passe incorrect")
        print(tentative_possible, "tentative restantes\n")
        if tentative_possible == 0:
            print(f"accès interdit")
    else:
        print(f"\nretrait autorisé")
        break
