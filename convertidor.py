#Funcion de conversion de celsius a fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) +32

#Funcion de conversion de fahrenheit a celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit-32) * 5/9

if __name__ == "__main__":
    #Pedimos al usuario que elija la conversion
    opcion = input("Que quieres convertir (1) Celsius o (2) fahrenheit? :" )

    #Pedimos al usuario la temperatura que quiere convertir 
    temperatura = float(input("Introduce la temperatura :"))
   
    if opcion == "1":
       resultado = celsius_a_fahrenheit(temperatura)
       print(f"{temperatura}ºC son {resultado}ºF")
    elif opcion == "2":
        resultado = fahrenheit_a_celsius(temperatura)
        print(f"{temperatura}ºF son {resultado}ºC")
    else:
        print("Opcion no valida")
        