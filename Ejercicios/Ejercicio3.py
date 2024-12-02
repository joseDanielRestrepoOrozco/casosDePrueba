'''
Ejercicio 3: Validación de Formularios Bancarios
Descripción:
Un formulario bancario requiere los siguientes datos:

Número de cuenta: debe ser un número de 10 dígitos.
Monto de transferencia: debe ser mayor a 0 y menor o igual a 10,000.
Código de seguridad: debe ser un número de 3 dígitos.
Tareas:
Define las clases de equivalencia para las tres entradas.
Diseña 5 casos de prueba, asegurándote de incluir valores inválidos.
Describe detalladamente un caso válido y uno inválido.

Clases de Equivalencia

Número de Cuenta:
E1: Válido (10 dígitos).
E2: Inválido (<10 dígitos).
E3: Inválido (>10 dígitos).
E4: Inválido (no numérico).

Monto de Transferencia:
E5: Válido (mayor a 0 y menor o igual a 10,000).
E6: Inválido (≤0).
E7: Inválido (>10,000).

Código de Seguridad:
E8: Válido (3 dígitos).
E9: Inválido (<3 dígitos).
E10: Inválido (>3 dígitos).
E11: Inválido (no numérico).
'''

import unittest

# Función de validación de formulario bancario (simulación)
def validar_formulario_bancario(numero_cuenta, monto_transferencia, codigo_seguridad):
    errores = []
    
    # Validar número de cuenta
    if not (numero_cuenta.isdigit() and len(numero_cuenta) == 10):
        errores.append("Número de cuenta inválido")
    
    # Validar monto de transferencia
    if not (0 < monto_transferencia <= 10000):
        errores.append("Monto de transferencia inválido")
    
    # Validar código de seguridad
    if not (codigo_seguridad.isdigit() and len(codigo_seguridad) == 3):
        errores.append("Código de seguridad inválido")
    
    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Validación exitosa"}

# Clase de pruebas unitarias
class TestValidacionFormularioBancario(unittest.TestCase):

    def test_caso_c1_todos_validos(self):
        """Caso C1: Todos los datos válidos"""
        resultado = validar_formulario_bancario("1234567890", 5000, "123")
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_numero_cuenta_invalido(self):
        """Caso C2: Número de cuenta inválido (menos de 10 dígitos)"""
        resultado = validar_formulario_bancario("123456789", 5000, "123")
        self.assertFalse(resultado["exito"])
        self.assertIn("Número de cuenta inválido", resultado["errores"])

    def test_caso_c3_monto_transferencia_invalido(self):
        """Caso C3: Monto de transferencia inválido (mayor a 10,000)"""
        resultado = validar_formulario_bancario("1234567890", 15000, "123")
        self.assertFalse(resultado["exito"])
        self.assertIn("Monto de transferencia inválido", resultado["errores"])

    def test_caso_c4_codigo_seguridad_invalido(self):
        """Caso C4: Código de seguridad inválido (menos de 3 dígitos)"""
        resultado = validar_formulario_bancario("1234567890", 5000, "12")
        self.assertFalse(resultado["exito"])
        self.assertIn("Código de seguridad inválido", resultado["errores"])

    def test_caso_c5_numero_cuenta_no_numerico(self):
        """Caso C5: Número de cuenta inválido (no numérico)"""
        resultado = validar_formulario_bancario("123456789A", 5000, "123")
        self.assertFalse(resultado["exito"])
        self.assertIn("Número de cuenta inválido", resultado["errores"])

if __name__ == '__main__':
    unittest.main()