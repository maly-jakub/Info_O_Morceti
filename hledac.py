from datetime import datetime
from decimal import Decimal

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