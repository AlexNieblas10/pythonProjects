import random

numeroAdivinar = random.randrange(1, 10)

def adivinalo(numeroAdivinar):
  numeroIntroducido=0
  while(numeroIntroducido != numeroAdivinar):
    numeroIntroducido=int(input("Introduce un numero del 1 al 10: "))
    if(numeroIntroducido < numeroAdivinar ):
      print("El numero introducino no es correcto intenta con un numero mas grande") 
    else:
      print("El numero introducido no es correcto intenta con un numero mas chico")
  
  print(f"Felicidades el numero {numeroAdivinar} es el correcto")

adivinalo(numeroAdivinar)