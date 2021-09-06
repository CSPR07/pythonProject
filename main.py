
antwoord = input("Wil je het spel spelen? (ja/nee) ")

if antwoord.lower().strip() == "ja":

    antwoord = input("Je komt een pad tegen wil je naar links of naar rechts toe? (links/rechts) ").lower().strip()
    if antwoord == "links":
        antwoord = input("Boe! je komt een monster tegen. Wat doe je ren je of val je aan? (rennen/aanvallen) ")

        if antwoord == "aanvallen":
            print("Je probeert het monster aan te vallen maar je gaat dood in het process!")
        else:
            print("Goede keuze je bent veilig weggekomen.")

    elif antwoord == "rechts":
        print("Je gaat naar rechts maar als je een bosje passeert dan val je in een berenkuil en gaat dood!")

    else:
        print("Error dit kan niet!")

else:
    print("Dat is jammer :( ")
