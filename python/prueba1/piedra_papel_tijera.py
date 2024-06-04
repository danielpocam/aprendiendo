import time
print("Bienvenida al juego de papel o tijera")
sacas=input("¿Qué sacas? (piedra, papel o tijera): ")
if sacas==("piedra"):
    print("He sacado papel, pierdes")
if sacas==("papel"):
    print("He sacado tijera,, pierdes")
if sacas==("tijera"):
    print("He sacado piedra, pierdes")