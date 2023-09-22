import random


def adivinalo():
    menor = 1
    mayor = 10
    suNumero = False

    while (not suNumero):
        miNumero = random.randrange(menor, mayor)
        respuesta = input(f"¿Tu numero es el {miNumero}? s/n ")
        if (respuesta == "n"):
            mayorOmenor = input("¿Tu numero es mayor o menor? ")
            if (mayorOmenor == "mayor"):
                menor = miNumero
            else:
                mayor = miNumero
        else:
            suNumero = True
    print("Me lo pusiste muy facil :)")


adivinalo()