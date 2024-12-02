import unittest

"""
Codigo:
E1: Válido (longitud de exactamente 8 caracteres alfanumericos).
E2: Inválido (<8 caracteres).
E3: Inválido (>8 caracteres).
E4: Inválido (no alfanumerico).

Cantidad:
E5: Válido (número entero entre 1 y 1000).
E6: Inválido (<1).
E7: Inválido (>1000).
E8: Inválido (no entero).

Precio:
E9: Válida (numero positivo mayor a 0).
E10: Inválida (<0).
E11: Inválida (no numerico).
"""

# Función de registro de usuario (simulación)
def validar_productos(codigo, cantidad, precio):
    errores = []
    # Validar codigo
    if not(len(codigo) == 8 and codigo.isalnum()):
        errores.append("Codigo inválido")
    # Validar cantidad
    if not (isinstance(cantidad, int) and 1 <= cantidad <= 1000):
        errores.append("Cantidad inválida")
    # Validar precio
    if not (isinstance(precio, (int, float)) and precio > 0):
        errores.append("Precio inválido")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Validación exitosa"}

class TestValidarProducto(unittest.TestCase):
    def test_caso_c1_todos_validos(self):
        """caso C1: Todos los datos son validos"""
        resultado = validar_productos("asdc1234", 500, 19.99)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_codigo_menor_a_8(self):
        """caso C2: codigo menor a 8 caracteres"""
        resultado = validar_productos("asdc123", 500, 19.99)
        self.assertFalse(resultado["exito"])
        self.assertIn("Codigo inválido", resultado["errores"])

    def test_caso_c3_codigo_mayor_a_8(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("asdc12356", 500, 19.99)
        self.assertFalse(resultado["exito"])
        self.assertIn("Codigo inválido", resultado["errores"])

    def test_caso_c4_codigo_mayor_a_8(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("1234!@#$", 500, 19.99)
        self.assertFalse(resultado["exito"])
        self.assertIn("Codigo inválido", resultado["errores"])

    def test_caso_c5_cantidad_menor_a_1(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("abcd1234", -1, 19.99)
        self.assertFalse(resultado["exito"])
        self.assertIn("Cantidad inválida", resultado["errores"])

    def test_caso_c6_cantidad_mayor_a_1000(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("abcd1234", 1024, 19.99)
        self.assertFalse(resultado["exito"])
        self.assertIn("Cantidad inválida", resultado["errores"])

    def test_caso_c7_cantidad_no_entero(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("abcd1234", 345.65, 19.99)
        self.assertFalse(resultado["exito"])
        self.assertIn("Cantidad inválida", resultado["errores"])

    def test_caso_c8_precio_menor_a_cero(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("abcd1234", 345, -15.65)
        self.assertFalse(resultado["exito"])
        self.assertIn("Precio inválido", resultado["errores"])

    def test_caso_c9_precio_no_es_numerico(self):
        """caso C3: codigo mayor a 8 caracteres"""
        resultado = validar_productos("abcd1234", 345, "ABC")
        self.assertFalse(resultado["exito"])
        self.assertIn("Precio inválido", resultado["errores"])

unittest.main(argv=[''], exit=False)