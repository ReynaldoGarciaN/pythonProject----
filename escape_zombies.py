#Debe tener un desafio aritmetico con numeros random
#Debe tener uno o varios objetos que debe coger el usuaio y validar despues
#puede tardar lo ques sea

titulo = "Salvanse quien pueda"

import random

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print(  "\n" "llegan a la ciudad y no sabian que era habitado solo por zombies y extraterrestres" "\n"
  "\n" "entraron a la ciudad yfueron atacados por los zombies; y tu amigo murio tu lograste escapar de los zombies" " \n")

print("algo llama tu atencion una especie de mapa en un pergamino antiguo esta en una vitrina" "\n"
"te preguntas que es? debe ser valioso tendras que tomarlo y o solo huyes?")

mapa = input("tomaas el pergamino" "\n"
                "A - si lo tomo" "\n"
                "B - solo me llevo mas armas " "\n ")

pergamino = False

if mapa == "A":
    pergamino = True
    print("Decides tomar el pergamino")
elif mapa == "B":
    print ("no te llevaste el mapa")
else:
    print("no elegiste nada, haz muerto")
    exit()


opcion = input("hay dos opciones opciones" "\n"
				"A - Miras una zona diferente pero es zona de extraterrestres"    "\n"
			    "B - Por la misma zona de los zombies (escondiendote)" "\n")


if opcion == "A":
    print("los extraterrestres son superavanzados, rapidamente te raptan te hacen la siguiente pregunta")
    number = random.randint(1,100)
    edad = int(input("dime tu edad: "))
    suma = int(input("si quieres salir con vida realiza la suma de tu edad mas {}: ".format(number)))
    if suma == number + edad:
        print("has acertado")
        number = random.randint(1, 100)
        multi = float(input("Ahora divide tu edad entre dos y multiplicaco por {}: ".format(number)))
        if multi == number * edad / 2:
            print("este es tu pase y tu bienvenida a nuestra ciudad, has ganado")
        else:
            print("Has fallado" "\n"
                  "Eres para experimento, por desperdicio de masa gris moriras en tres  dias o menos")
    else:
        print("Has fallado" "\n"
                  "Eres para experimento, por desperdicio de masa gris moriras en tres  dias o menos")
elif opcion == "B":
       print("avanzas unas calles y miras una casa con armas constudiiada solo por un zombie")
       atacar_evitar = input("hay dos opciones opciones" "\n"
				"A - Lo evitas "    "\n"
			    "B - Lo enfrentas " "\n")
       if atacar_evitar == "A":
           print("error, esta calle esta plagada de zombies, cuidado ya estas muerto")
           exit()
       elif atacar_evitar == "B" and pergamino:
           print ("al enfrentarlo lograste vencer al zombie, entras a la casa y encuentras armas armas" "\n"
                  "agarras cuanto puedes y sigues avanzando" "\n"
                  "se te acabaron las municiones, bajas a a una red de alcantarillas" "\n"
                  "llevas el pergamino, es un mapa te has salvado")
       else:
           print("Logras vencer se te acaban las municiones" "\n"
            "caes a una alcantarilla" "\n"
             "Necesitas el mapa, mueres")
           exit()
else:
    print("Elige una opcion valida")







