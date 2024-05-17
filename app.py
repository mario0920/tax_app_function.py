import tax

sal = int(input("Introduce Salariul: "))

rezultat = tax.calculateTax(sal, 0.18, "Impozit")

print("Impozitul salariului: ", rezultat["tax"])