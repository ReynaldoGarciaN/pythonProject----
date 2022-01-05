numero1 = int(input("introduce numero 1: "))
numero2 = int(input("introduce numero 2: "))
numero3 = int(input("introduce numero 3: " ))

print(
    "el numero mas grande entre  {}, {}, y {} es: {}, y el mas pequeño es {}".format(numero1, numero2, numero3,
                                                                                     max(numero1, numero2, numero3),
                                                                                     min(numero1, numero2, numero3)))
