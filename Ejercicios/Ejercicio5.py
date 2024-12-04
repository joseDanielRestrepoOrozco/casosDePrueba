import unittest
import re


# Función de validación de usuarios
def validar_usuario(nombre_usuario, correo_electronico, edad):
    errores = []

    # Validar nombre de usuario
    if not (5 <= len(nombre_usuario) <= 20):
        errores.append("Nombre de usuario inválido")
    # Validar correo electrónico
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo_electronico):
        errores.append("Correo electrónico inválido")
    # Validar edad
    if not (13 <= edad <= 120):
        errores.append("Edad inválida")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Validación exitosa"}


# Clase de pruebas unitarias
class TestValidacionUsuario(unittest.TestCase):

    def test_caso_c1_todos_validos(self):
        """Caso C1: Todos los datos válidos"""
        resultado = validar_usuario("usuario123", "user@example.com", 25)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_nombre_usuario_demasiado_corto(self):
        """Caso C2: Nombre de usuario inválido (menos de 5 caracteres)"""
        resultado = validar_usuario("usr", "user@example.com", 25)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre de usuario inválido", resultado["errores"])

    def test_caso_c3_nombre_usuario_demasiado_largo(self):
        """Caso C3: Nombre de usuario inválido (más de 20 caracteres)"""
        resultado = validar_usuario("usuario_muy_largo_12345", "user@example.com", 25)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre de usuario inválido", resultado["errores"])

    def test_caso_c4_correo_electronico_invalido(self):
        """Caso C4: Correo electrónico inválido"""
        resultado = validar_usuario("usuario123", "userexample.com", 25)
        self.assertFalse(resultado["exito"])
        self.assertIn("Correo electrónico inválido", resultado["errores"])

    def test_caso_c5_edad_invalida_menor(self):
        """Caso C5: Edad inválida (menor de 13)"""
        resultado = validar_usuario("usuario123", "user@example.com", 10)
        self.assertFalse(resultado["exito"])
        self.assertIn("Edad inválida", resultado["errores"])

    def test_caso_c6_edad_invalida_mayor(self):
        """Caso C6: Edad inválida (mayor de 120)"""
        resultado = validar_usuario("usuario123", "user@example.com", 150)
        self.assertFalse(resultado["exito"])
        self.assertIn("Edad inválida", resultado["errores"])



