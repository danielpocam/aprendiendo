import time 
import random

def salir():
    exit()
# print("Hola")
# time.sleep(3)
# print("Que haces")
# time.sleep(3)
# print("Hola alguien me oye")
# i=1
# while (i<=20):
#     print(i)
#     i=i+1

# i=1
# while (i<=20):
#     print(i)
#     i=i+1
    
# print("Numeros Impares")
# i=1
# while (i<=20):
#     print(i)
#     i=i+2


# segundos=int(input("¿Cuánto quieres esperar a que explote la bomba?:"))
# while (segundos>0):
#     print(str(segundos)+" segundos")
#     segundos=segundos-1
#     time.sleep(1)
# print("¡¡¡¡¡PATAPUMBA!!!!!")

# variable1=56789
# variable2="Daniel es un nino"
# variable3=["carlos", "pepito", "estela", "Amador"]

# # print(variable1)
# # print(variable2)
# # for elemento in variable3:
# #     print(elemento)
# print(variable3)
# variable3.append("Daniel")
# print(variable3)
# exit()


# resultado=input("Como te llamas:")
# print("hola "+resultado)

# pares=[0,2,4,6,8,"acabe en este numero"]
# impares=[1,3,5,7,9,"acaben en este numero"]
# while(True):
#     variable1=input("dime si quieres numeros pares o impares pon impares o pares:")
#     if (variable1=="pares"):
#         print("Son los numeros ")
#         print(pares)
#         exit()
#     elif (variable1=="impares"):
#         print("Son los numeros ") quedan %
#         print(impares)
#         exit()

# contraseña="MeGustaElQueso"
# intentos=4
# while(intentos>0):
#     contraseñaponla=input("Pon una contraseña:")
#     if(contraseñaponla==contraseña):
#         print("Contraseña correcta")
#         exit()
#     else:
#         intentos=intentos-1
#         print("Contraseña incorrecta, quedan %s intentos" % intentos)

# password="Dani"

# # def establecer_nueva_password():
# #     pw1=input("Pon una contraseña nueva: ")
# #     while len(pw1) < 4:
# #         print("Contraseña demasiado corta")
# #         pw1=input("Pon una contraseña nueva: ")
# #     with open('password.txt', 'w') as f:
# #         f.write(pw1)

    
# # ## INICIO AQUI 
# # with open('password.txt') as f:
# #     password = f.readline()
# # intentos=4
# # while(intentos>0):
# #     intento_de_password=input("Password:")
# #     if(intento_de_password==password):
# #         print("Pasword correct")
# #         password=establecer_nueva_password()       
# #     else:
# #         intentos=intentos-1
# #         print("Password incorecta, %s intentos" % intentos)
# #         print("Adios has fallado")
# #         time.sleep(1)
# #         print("adios has fallado.")
# #         time.sleep(1)
# #         print("adios has fallado..")
# #         time.sleep(1)
# #         print("adios has fallado...")
# #         time.sleep(1)
# #         print("adios has fallado.")
# #         time.sleep(1)
# #         print("adios has fallado..")

def a(frase, final="\n"):
    escribe_lento(frase, final)
    return

def esperar (tiempo):
    time.sleep(tiempo)
    return

def escribe_lento(frase, final="\n"):
    for letra in frase:
        print(letra,end="", flush=True)
        esperar(0.1)
    print(final,end="", flush=True)
    return
# a("s")
# salir()
##Pruebas
numero = random.randint(1, 2)
a("El " + str(numero)+" ha ganado")
gusta=input("¿Te ha gustado? en minusculas: ")
a("muchas gracias por  que "+gusta +" te gustado")
if gusta=="si":
    a("Ha costado mucho")
    esperar(2)
    exit()
if gusta=="no":
    a("Pues vaya")
    esperar(2)
    exit()



# # # INICIO " AQUI"
a("¡Hola! Me llamo Siri.")
esperar(2)
escribe_lento("Tengo ya la version 1.4.") 
esperar(2)
escribe_lento("Tu preguntador y respondedor personal inteligente.")
esperar(1)
escribe_lento("¿Cómo te llamas?: ", final="")
Variablenombre=input() 
escribe_lento("Encantada de conocerte "+Variablenombre)

escribe_lento(".......")
#\TODO
escribe_lento("¿Cuántos años tienes?: ", final="")
Variableaños=input()
escribe_lento("Hala tienes " +Variableaños+" años")
escribe_lento("Hasta la próxima "+Variablenombre)
escribe_lento("......")
esperar(2)
exit()



