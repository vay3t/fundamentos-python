"""
Python 3.9.5
Ejercicio 1 - Variables, números y Strings
"""

# Comentarios
#
# Los comentarios son una parte importante al momento de programar# 

# Operadores aritméticos
>>> 3+5+6
14
>>> 2-5+6
3
>>> 2-(5+6) 
-9
>>> 5==5
True
>>> 5>=5
True
>>> 5!=5
False
>>> False and False
False
>>> 5>4 or 6!=5
True
>>> i=0
>>> i +=1
>>> i
1
>>> j =+1
>>> j +=1
>>> j
2

>>> z +=1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    z +=1
NameError: name 'z' is not defined
>>> z=2
>>> type(2)
<class 'int'>
>>> f="Hola Mundo"
>>> type(f)
<class 'str'>
>>> type(1.2)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> g='Hola Mundo'
>>> type(g)
<class 'str'>
>>> and=2
SyntaxError: invalid syntax
>>> t=7
>>> type(7)
<class 'int'>
>>> srt(t)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    srt(t)
NameError: name 'srt' is not defined
>>> str(t)
'7'
>>> h=str(t)
>>> type(h)
<class 'str'>
>>> type(t)
<class 'int'>
>>> mm=int(h)
>>> mm
7
>>> cadena="012345678"
>>> len(cadena)
9
>>> cadena="12"+cadena
>>> cadena
'12012345678'
>>> cadena="123"
>>> cadena
'123'
>>> cadena=7
>>> cadena
7
>>> type(cadena)
<class 'int'>
>>> cadena=True
>>> type(cadena)
<class 'bool'>
>>> 3tr=2
SyntaxError: invalid syntax
>>> a= input("Diga un nombre: ")
Diga un nombre: Teresa
>>> a
'Teresa'
>>> b= input("Ingrese un numero: ")
Ingrese un numero: 7
>>> type(b)
<class 'str'>
>>> 
