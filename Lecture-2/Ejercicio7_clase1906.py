switcher ={
    1:"Enero",
    2:"Febrero",
    3:"Marzo" }

argument=int(input("Ingrese un número de mes: "))

nombredeMes= switcher.get(argument, "Mes invalida")
print(nombredeMes)
