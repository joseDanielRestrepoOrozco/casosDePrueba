'''
Un sistema de tránsito registra vehículos con las siguientes reglas:

Placa: debe ser un texto de 6 o 7 caracteres.
Año de fabricación: debe ser entre 1980 y el año actual.
Tipo de vehículo: debe ser "automóvil", "camión", "moto" o "bus".

Clases de Equivalencia
Placa:
E1: Válida (6 o 7 caracteres).
E2: Inválida (<6 caracteres).
E3: Inválida (>7 caracteres).

Año de Fabricación:
E4: Válido (entre 1980 y el año actual).
E5: Inválido (menor a 1980).
E6: Inválido (mayor al año actual).

Tipo de Vehículo:
E7: Válido ("automóvil", "camión", "moto", "bus").
E8: Inválido (cualquier otro valor).
'''

import unittest
from datetime import datetime

# Función de registro de vehículo (simulación)
def registrar_vehiculo(placa, ano_fabricacion, tipo_vehiculo):
    errores = []
    ano_actual = datetime.now().year
    
    # Validar placa
    if not (6 <= len(placa) <= 7):
        errores.append("Placa inválida")
    
    # Validar año de fabricación
    if not (1980 <= ano_fabricacion <= ano_actual):
        errores.append("Año de fabricación inválido")
    
    # Validar tipo de vehículo
    if tipo_vehiculo not in ["automóvil", "camión", "moto", "bus"]:
        errores.append("Tipo de vehículo inválido")
    
    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Registro exitoso"}

# Clase de pruebas unitarias
class TestRegistroVehiculo(unittest.TestCase):

    def test_caso_c1_todos_validos(self):
        """Caso C1: Todos los datos válidos"""
        resultado = registrar_vehiculo("ABC123", 2000, "automóvil")
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_placa_invalida(self):
        """Caso C2: Placa inválida (menos de 6 caracteres)"""
        resultado = registrar_vehiculo("ABC12", 2000, "automóvil")
        self.assertFalse(resultado["exito"])
        self.assertIn("Placa inválida", resultado["errores"])

    def test_caso_c3_placa_mas_de_7_caracteres(self):
        """Caso C3: Placa inválida (más de 7 caracteres)"""
        resultado = registrar_vehiculo("ABC12345", 2000, "automóvil")
        self.assertFalse(resultado["exito"])
        self.assertIn("Placa inválida", resultado["errores"])

    def test_caso_c4_ano_menor_a_1980(self):
        """Caso C4: Año de fabricación inválido (menor a 1980)"""
        resultado = registrar_vehiculo("ABC123", 1979, "automóvil")
        self.assertFalse(resultado["exito"])
        self.assertIn("Año de fabricación inválido", resultado["errores"])

    def test_caso_c5_ano_mayor_al_actual(self):
        """Caso C5: Año de fabricación inválido (mayor al año actual)"""
        ano_actual = datetime.now().year
        resultado = registrar_vehiculo("ABC123", ano_actual + 1, "automóvil")
        self.assertFalse(resultado["exito"])
        self.assertIn("Año de fabricación inválido", resultado["errores"])

    def test_caso_c6_tipo_vehiculo_invalido(self):
        """Caso C6: Tipo de vehículo inválido"""
        resultado = registrar_vehiculo("ABC123", 2000, "bicicleta")
        self.assertFalse(resultado["exito"])
        self.assertIn("Tipo de vehículo inválido", resultado["errores"])

if __name__ == '__main__':
    unittest.main()
