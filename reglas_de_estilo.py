
titulo = "bienvenido a test de gatos"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntos = 0

opcion = input("Te gustaria tener  un gato en casa?\n"
               "A - nunca \n"
               "B - tal vez \n"
               "C - si porsupuesto \n")

if opcion == "A":
    puntos +=0
elif opcion == "B":
    puntos +=10
elif opcion == "C":
    puntos +=20
else:
    print("las opciones son A, B , C")
    exit()

opcion = input("preferirias un perro un gato o una anaconda??\n"
               "A - Perro \n"
               "B - gato \n"
               "C - anaconda \n")

if opcion == "A":
    puntos +=10
elif opcion == "B":
    puntos +=20
elif opcion == "C":
    puntos +=0
else:
    print("las opciones son A, B, C")
    exit()

opcion = input("si tiens un gato cerca que haces?\n"
               "A - Lo alejas \n"
               "B - lo abrazas \n"
               "C - te es indiferen \n")

if opcion == "A":
    puntos +=0
elif opcion == "B":
    puntos +=20
elif opcion == "C":
    puntos +=10
else:
    print("las opciones son A, B, C")
    exit()


print("Tu puntuacion es: {}".format(puntos))

if puntos >= 50:
    print("Felicidades eres un amante de los gatos")
elif puntos >= 20:
    print("Excelente gustan los gatos")
else:
    print("Parece que no te gustan los gatos")

