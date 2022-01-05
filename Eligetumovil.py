
titulo = "Elige tu movil"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

opcion = input("Te gustaria tener  un iOS o Android?\n"
               "A - iOS \n"
               "B - Android \n")
money = input("Tienes dinero ?\n"
               "A - Si \n"
               "B - No \n")
camara = input("Te gustaria que tenga camara de gama alta?\n"
               "A - Si \n"
               "B - No \n")

if opcion == "A":
    if money == "A" and camara == "A":
       print("Comprate el iphone ULtra Pro Max")
    else:
        print("Comprate iPhone segunda mano")
elif opcion == "B":
    if money == "A" and camara == "A":
       print("Comprate google pixel super camera")
    elif money == "A" and camara == "B":
        print("comprate Android calidad precio")
    else:
        print("Comprate Android chino 100e")

