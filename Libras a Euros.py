#se deja como comentario por si el usuario desea ingresar el tipo de cambio
#euro = float(input("tipo de cambio de hoy es"))

#Libra = float(input("introduce las libras "))




dolar_euro = 0.84
euro_libra = 1.17

opcion = input("que divisa desea convertir \n"
               "A - Dolar a euros \n"
               "B - euros a dolares \n"
               "C - Libra a Euros \n"
               "D - Euros a libras \n ")

texto_usuario = "Introduce la cantidad de {} a convertir "

if opcion == "A":
    qty_dolares = float(input(texto_usuario.format("dolares")))
    print("Total Euros son: {}".format(qty_dolares * dolar_euro))

elif opcion == "B":
        qty_euros = float(input(texto_usuario.format("euros")))
        print("Total dolares son: {}".format(qty_euros / dolar_euro))

elif opcion == "C":
        qty_libras = float(input(texto_usuario.format("libras")))
        print("Total libras son: {}".format(qty_libras * euro_libra))

elif opcion == "D":
        qty_euro = float(input(texto_usuario.format("euros")))
        print("Total euros son: {}".format(qty_euro / euro_libra))

else:
    print("Solo se puede convertir las divisas anteriores gracias")
    exit()





