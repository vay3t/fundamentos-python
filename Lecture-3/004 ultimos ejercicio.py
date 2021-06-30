Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> not (5!=4)
False
>>> not 5!=4
False
>>> not True
False
>>> 10+2
12
>>>     10+2
    
SyntaxError: unexpected indent
>>> 10 + 35 + 4
49
>>> 10 + 3 5 +4
SyntaxError: invalid syntax
>>> 3 5
SyntaxError: invalid syntax
>>> 35
35
>>> "35"
'35'
>>> type("35")
<class 'str'>
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/aumentoSueldo.py
Ingrese sueldo: 700
El sueldo que recibirá es  805.0
El sueldo que recibirá es 805.0
El sueldo que recibirá es 805.0 
El sueldo que recibirá es 805
El sueldo que recibirá es 805.000000 
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/Iguales.py
Ingrese el primer numero: 4
Ingrese el segundo numero: 2
Ingrese el tercer número: 7
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/Iguales.py
Ingrese el primer numero: 3
Ingrese el segundo numero: 2
Ingrese el tercer número: 5
SON IGUALES
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/003 numeros ordenados.py
Ingrese un número :7
Ingrese un número :6
 Los números en orden son:  6 7
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/003 numeros ordenados.py
Ingrese un número :5
Ingrese un número :8
 Los números en orden son:  5 8
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/004 IgualesYdistintos.py
Ingrese el primer numero: 8
Ingrese el segundo numero: 9
Ingrese el tercer número: 1
SON DISTINTOS
>>> 
= RESTART: C:/Users/TERESA/AppData/Local/Programs/Python/Python39/Clase 3 - 23-06-2021/004 IgualesYdistintos.py
Ingrese el primer numero: 2
Ingrese el segundo numero: 3
Ingrese el tercer número: 5
SON IGUALES
>>> a=range(3)
>>> a
range(0, 3)
>>> for x in range(3)
SyntaxError: invalid syntax
>>> for x in range(3):
	print("El numero es: ", x)

	
El numero es:  0
El numero es:  1
El numero es:  2
>>> for x in range(0,3):
	print("El numero es: ", x)

	
El numero es:  0
El numero es:  1
El numero es:  2
>>> for x in range(1,10):
	print("El numero es: ", x)

	
El numero es:  1
El numero es:  2
El numero es:  3
El numero es:  4
El numero es:  5
El numero es:  6
El numero es:  7
El numero es:  8
El numero es:  9
>>> for x in range(1,10,2):
	print("El numero es: ", x)

	
El numero es:  1
El numero es:  3
El numero es:  5
El numero es:  7
El numero es:  9
>>> for x in range(11,4):
	print("El numero es: ", x)

	
>>> for x in range(11,4,-1):
	print("El numero es: ", x)

	
El numero es:  11
El numero es:  10
El numero es:  9
El numero es:  8
El numero es:  7
El numero es:  6
El numero es:  5
>>> for x in range(11, 4, -3):
	print("El numero es: ", x)

	
El numero es:  11
El numero es:  8
El numero es:  5
>>> j
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    j
NameError: name 'j' is not defined
>>> j=0
>>> "hola mundo"
'hola mundo'
>>> "hola mundo'
SyntaxError: EOL while scanning string literal
>>> 'hola mundo'
'hola mundo'
>>> #hola mundo
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print("Esta línea esta cortada en dos lineas de menos de 79 caracteres "
      "Esta linea es la segunda linea")
Esta línea esta cortada en dos lineas de menos de 79 caracteres Esta linea es la segunda linea
>>> print("Esto es una prueba \
para partir la cadena ")
Esto es una prueba para partir la cadena 
>>> print("Esto es una prueba \\ hola")
Esto es una prueba \ hola
>>> print("En {semanas} semanas hay {7*semanas} días.")
En {semanas} semanas hay {7*semanas} días.
>>> semanas=4
>>> print(f"En {semanas} semanas hay {7*semanas} días.")
En 4 semanas hay 28 días.
>>> nombre="pepe"
>>> print(f"si se escribe {{nombre}*2} debe acompañarlo con {3*nombre}")
SyntaxError: f-string: single '}' is not allowed
>>> print(f"si se escribe {{nombre}*2} debe acompañarlo con {3*nombre}")
SyntaxError: f-string: single '}' is not allowed
>>> print(f"si se escribe {{nombre}} debe acompañarlo con {3*nombre}")
si se escribe {nombre} debe acompañarlo con pepepepepepe
>>> print(f"si se escribe {{nombre*2}} debe acompañarlo con {3*nombre}")
si se escribe {nombre*2} debe acompañarlo con pepepepepepe
>>> 'a' == 'A'
False
>>> 'a' < 'A'
False
>>> "Hola Mundo"[3]
'a'
>>> len("Hola Mundo")
10
>>> d="Hola Mundo"
>>> d[3]
'a'
>>> len(d)
10
>>> d[-3]
'n'
>>> d[]
SyntaxError: invalid syntax
>>> d[:]
'Hola Mundo'
>>> d[2:]
'la Mundo'
>>> d[:7]
'Hola Mu'
>>> d[3:5]
'a '
>>> len(d[3:5])
2
>>> d.isalpha()
False
>>> h="1234htjdk"
>>> h.isalpha()
False
>>> j="adshfkgjgir"
>>> j.isalpha()
True
>>> h.isalnum()
True
>>> h.capitalize()
'1234htjdk'
>>> k="tere"
>>> k.capitalize()
'Tere'
>>> k="1234"
>>> k.isdigit()
True
>>> k="tere"
>>> k.islower()
True
>>> k="TERe"
>>> k.islower()
False
>>> '    '.isspace()
True
>>> k="TERESA"
>>> k.isupper()
True
>>> k.lower()
'teresa'
>>> k.upper()
'TERESA'
>>> '   hola mundo'.lstrip()
'hola mundo'
>>> "hola mundo".replace("o","i")
'hila mundi'
>>> 'Hola mundo   '.rstrip()
'Hola mundo'
>>> 'hola,como, estas,bien'.split(",")
['hola', 'como', ' estas', 'bien']
>>> '12.345.345-2'.split("-")
['12.345.345', '2']
>>> rd('A')
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    rd('A')
NameError: name 'rd' is not defined
>>> ord('A')
65
>>> chr(65)
'A'
>>> ord('a')
97
>>> chr(97)
'a'
>>> "hola">"hola "
False
>>> "hola"=="hola"
True
>>> nums=[1,2,3]
>>> vals=nums
>>> vals
[1, 2, 3]
>>> i=3
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(i,10):
	print(i)

	
9
>>> i=3
>>> for i in range(i,10):
	print(i)

	
3
4
5
6
7
8
9
>>> a="Hola"
>>> a[2]='f'
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a[2]='f'
TypeError: 'str' object does not support item assignment
>>> 'a'.islower()
True
>>> 