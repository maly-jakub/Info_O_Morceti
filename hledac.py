with open("info.txt", "r", encoding="utf-8") as soubor:
    for radek in soubor:
        udaje = radek.strip().split(";")
        print(udaje)