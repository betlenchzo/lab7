mar=float(input("markeriin too: "))
pen=float(input("vzegnii too: "))
liq=float(input("ugaalgiin nuntag: "))
dis=float(input("Hunglultiin huwi: ")) /100
niit=(mar * 5.08) + (pen * 7.20) + (liq * 1.20)
vne = niit * (1 - dis)
print(vne)