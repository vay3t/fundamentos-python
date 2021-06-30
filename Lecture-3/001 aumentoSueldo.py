x=int(input("Ingrese sueldo: "))

if x<1000:
      x=x+x*0.15
      print("El sueldo que recibirá es ", x)
      print("El sueldo que recibirá es "+ str(x))
      print(f"El sueldo que recibirá es {x} ")
      print("El sueldo que recibirá es " + str(int(x)))
      print("El sueldo que recibirá es %f " % x)
