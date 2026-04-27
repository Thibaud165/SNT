print("===== Devrais-je acheter un nouveau téléphone ? =====")

while True:
    phone_broken = ""
    while phone_broken not in ["oui", "non"]: 
        phone_broken = input("Votre téléphone est-il cassé ? (oui/non) : ")

    if phone_broken == "oui":
        spare_phone = ""
        while spare_phone not in ["oui", "non"]:
            spare_phone = input("Avez-vous un téléphone de rechange ? (oui/non) : ")
        if spare_phone == "oui":
            print("\nVous ne devriez pas acheter pour l'instant")
        else:
            print("\nVous devriez acheter un nouveau téléphone")
        break
    else:
        want_upgrade = ""
        while want_upgrade not in ["oui", "non"]:
            want_upgrade = input("Voulez-vous changer de téléphone ? (oui/non) : ")
        if want_upgrade == "oui":
            can_afford = ""
            while can_afford not in ["oui", "non"]:
                can_afford = input("Avez-vous les moyens d'acheter un nouveau téléphone ? (oui/non) : ")
            if can_afford == "oui":
                print("\nVous devriez acheter un nouveau téléphone")
            else:
                print(f"\nVous devriez d'abord utiliser votre ancien téléphone")
            break
        else:
            print("\nRecommençons depuis le début.")
            continue