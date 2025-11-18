# Calculadora básica en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"
    
def potencia(a: float, b: float) -> float:
    """Calcula a elevado a la b."""
    return a ** b

def elevar_al_cubo(a: float) -> float:
    """Calcula el cubo de un número."""
    return a ** 3

def main():
    print("Calculadora básica")
    
    # Pedir números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Mostrar opciones
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Elevar al cubo (del primer número)")

    opcion = input("Selecciona la operación (1/2/3/4/5/6): ")
    
    if opcion == "1":
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == "2":
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == "4":
        print(f"Resultado: {division(num1, num2)}")
    elif opcion == "5":
        print(f"Resultado: {potencia(num1, num2)}")
    elif opcion == "6":
        print(f"Resultado: {elevar_al_cubo(num1)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
