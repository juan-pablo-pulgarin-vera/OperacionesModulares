def Sumar(numero1, numero2, modulo):
    
    print("El resultado de la suma modular es:", (numero1+numero2)%modulo)

def Restar(numero1, numero2, modulo):
    print("El resultado de la resta modular es:", (numero1-numero2)%modulo)


def Multiplicar(numero1, numero2, modulo):
    print("El resultado de la multiplicación modular es:", (numero1*numero2)%modulo)


def Elevar(numero1, numero2, modulo):
    print("El resultado de la exponenciación modular es:", (numero1**numero2%modulo))

def InversoModular(numero1, modulo):
    print("El resultado de la inverso modular es:", (numero1*numero1**-1)%modulo)

n=1
while n != 0:
    print("-----------------------------")
    print("¿Qué operacón desea realizar?")
    print("-----------------------------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Exponencial")
    print("5. Inverso modular")
    print("-----------------------------")
    print("0. Salir")
    print("-----------------------------")
    n = int(input("Seleccione una opcion: "))
    if n == 0:
        print("Salió correctamente")
        exit()
    if n == 1:
      try:
        num1 = int(input("Ingrese el primer valor "))
        num2 = int(input("Ingrese el segundo valor "))   
        mod =  int(input("Ingrese el modulo "))

        if mod == 0:
          print("La división por cero no es valida")
        else:
          Sumar(num1, num2, mod)
      except:
        print("El valor ingresado solo puede ser númerico")
    if n == 2:
      try:
        num1 = int(input("Ingrese el primer valor "))
        num2 = int(input("Ingrese el segundo valor "))   
        mod =  int(input("Ingrese el modulo "))
        if mod == 0:
          print("La división por cero no es valida")
        else:
          Restar(num1, num2, mod)
      except:
        print("El valor ingresado solo puede ser númerico")
    if n == 3:
      try:
        num1 = int(input("Ingrese el primer valor "))
        num2 = int(input("Ingrese el segundo valor "))   
        mod =  int(input("Ingrese el modulo "))
        if mod == 0:
          print("La división por cero no es valida")
        else:
          Multiplicar(num1, num2, mod)
      except:
        print("El valor ingresado solo puede ser númerico")
    if n == 4:
      try:
        num1 = int(input("Ingrese el primer valor "))
        num2 = int(input("Ingrese el segundo valor "))   
        mod =  int(input("Ingrese el modulo "))
        if mod == 0:
          print("La división por cero no es valida")
        else:
          Elevar(num1, num2, mod)
      except:
        print("El valor ingresado solo puede ser númerico")
    if n == 5:
      try:
        num1 = int(input("Ingrese el primer valor "))
        mod = int(input("Ingrese el modulo ")) 
        if mod == 0:
          print("La división por cero no es valida")
        else: 
          InversoModular(num1, mod)
      except:
        print("El valor ingresado solo puede ser númerico")