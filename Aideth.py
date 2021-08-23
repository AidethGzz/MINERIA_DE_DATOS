# Ejercicio 1

mat = 1748467
nombre = "Aideth"

print("\nMi nombre es " + nombre + " y mi matricula es " + str(mat))

# Ejercicio 2
'''
a = int(input("\nIntroduce un numero: "))
b = int(input("Introduce otro numero: "))

op = "0"
while (op != "6"):
    print("\nCalculadora básica\n")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Exponente\n6. Salir\n")
    op = input("Ingrese una opción: ")
    if (op == "1"):
        r = a + b
        print("\n" + str(a) + " + " + str(b) + " = " + str(r))
    elif (op == "2"):
        r = a - b
        print("\n" + str(a) + " - " + str(b) + " = " + str(r))
    elif (op == "3"):
        r = a*b
        print("\n" + str(a) + " * " + str(b) + " = " + str(r))
    elif (op == "4"):
        r = a/b
        print("\n" + str(a) + " / " + str(b) + " = " + str(r))
    elif (op == "5"):
        r = a**b
        print("\n" + str(a) + " ^ " + str(b) + " = " + str(r))
    elif (op == "6"):
        exit
    else:
        print("\nOpción incorrecta, vuelve a intentarlo")
'''
# Ejercicio 3

suma = 0
print("\n")
for i in range(3,33,3):
    print(i)
    suma = i + suma
print("\nLa suma de esta serie es: " + str(suma))

# Ejercicio 4

n = int(input("\nIngresa un número: "))

if (n % 2 == 0):
    print("\nEl numero " + str(n) + " es par")
else:
    print("\nEl numero " + str(n) + " es impar")

def primo(n):
    if n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

if primo(n):
    print("El número " + str(n) + " es primo")
else:
    print("El número " + str(n) + " no es primo")

# Ejercicio 5
'''
class Calculadora:
    a = 0.0
    b = 0.0
    r = 0.0
    
    def datos(self):
        self.a = input("\nIngresa un numero: ")
        self.a = float(self.a)
        self.b = input("Ingresa otro numero: ")
        self.b = float(self.b)
    
class Operaciones:
    
    def suma(self, a, b):
        self.r = calcu.a + calcu.b
        print("\n" + str(calcu.a) + " + " + str(calcu.b) + " = " + str(self.r))

    def resta(self, a, b):
        self.r = calcu.a - calcu.b
        print("\n" + str(calcu.a) + " - " + str(calcu.b) + " = " + str(self.r))
    
    def multiplicacion(self, a, b):
        self.r = calcu.a*calcu.b
        print("\n" + str(calcu.a) + " * " + str(calcu.b) + " = " + str(self.r))
    
    def division(self, a, b):
        self.r = calcu.a/calcu.b
        print("\n" + str(calcu.a) + " / " + str(calcu.b) + " = " + str(self.r))
    
    def exponente(self, a, b):
        self.r = calcu.a**calcu.b
        print("\n" + str(calcu.a) + " ^ " + str(calcu.b) + " = " + str(self.r))
        
calcu = Calculadora()
calcu.datos()
ope = Operaciones()

op = "0"
while (op != "6"):
    print("\nCalculadora básica\n")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Exponente\n6. Salir\n")
    op = input("Ingrese una opción: ")
    if (op == "1"):
        ope.suma(calcu.a, calcu.b)
    elif (op == "2"):
        ope.resta(calcu.a, calcu.b)
    elif (op == "3"):
        ope.multiplicacion(calcu.a, calcu.b)
    elif (op == "4"):
        ope.division(calcu.a, calcu.b)
    elif (op == "5"):
        ope.exponente(calcu.a, calcu.b)
    elif (op == "6"):
        exit
    else:
        print("\nOpción incorrecta, vuelve a intentarlo")
'''