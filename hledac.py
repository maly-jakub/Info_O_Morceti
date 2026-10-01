from datetime import datetime

with open("info.txt", "r", encoding="utf-8") as soubor:
    
    seznam = []
    
    for radek in soubor:
        udaje = radek.strip().split(";")
        seznam.append(udaje)
        
        jmeno = udaje[0]
        hmotnost = int(udaje[1])
        datum = datetime.strptime(udaje[2], '%Y-%m-%d')
        cena = float(udaje[3])
        pohlavi = udaje[4]
        
        cena_se_slevou = cena * 0.9
        
        if pohlavi == "m":
            pohlavi_text = "Sameček"
        if pohlavi == "z":
            pohlavi_text = "Samička"
                
        print(f"{pohlavi_text} morčete jménem: {jmeno}")
        print(f"- váží: {hmotnost}g")
        print(f"- datum narození: {datum.strftime('%Y-%m-%d')}")
        print(f"- cena se slevou 10%: {cena_se_slevou} Kč")