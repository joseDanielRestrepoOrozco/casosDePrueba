import unittest

cadena1 = "Python123"
cadena2 = "Python 123"
cadena3 = "12345"
cadena4 = ""

print(cadena1.isalnum())  # True: solo contiene letras y números
print(cadena2.isalnum())  # False: contiene un espacio
print(cadena3.isalnum())  # True: solo contiene números
print(cadena4.isalnum())  # False: está vacía
