edad = int(input("Indique su edad: "))
tipo_de_carnet = input("Digame su tipo de carnet (E para estudiantes / P Pensionista / F Familia grande / Nada): ")

if (25 <= edad <= 35 and tipo_de_carnet == "E" ) or \
        edad <= 10 or \
        (edad >= 65 and tipo_de_carnet == "P") or \
        (tipo_de_carnet == "F"):
    print("se aplica el descuento")
else:
    print("no aplica descuento")