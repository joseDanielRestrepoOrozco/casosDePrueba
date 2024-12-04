import unittest
from datetime import datetime


def reservar_habitaciones(cantidad, fecha, estadia):
    errores = []
    fecha_objetivo = datetime.strptime(fecha, "%d-%m-%Y").date()
    hoy = datetime.today().date()

    # Validar cantidad de habitaciones
    if not (isinstance(cantidad, int) and 1 <= cantidad <= 5):
        errores.append("Cantidad de habitaciones invalida")
    # Validar fecha
    if fecha_objetivo < hoy:
        errores.append("Fecha invalida")
    # Validar duración de estadía
    if not (isinstance(estadia, int) and 1 <= estadia <= 30):
        errores.append("Duracion de estadia invalida")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Validación exitosa"}


class TestValidarReserva(unittest.TestCase):
    def test_caso_c1_todos_validos(self):
        """Caso C1: Todos los datos válidos"""
        resultado = reservar_habitaciones(4, "4-5-2025", 25)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_habitaciones_menor_a_1(self):
        """Caso C2: Habitaciones < 1"""
        resultado = reservar_habitaciones(-1, "4-5-2025", 25)
        self.assertFalse(resultado["exito"])
        self.assertIn("Cantidad de habitaciones invalida", resultado["errores"])

    def test_caso_c3_habitaciones_mayor_a_5(self):
        """Caso C3: Habitaciones > 5"""
        resultado = reservar_habitaciones(78, "4-5-2025", 25)
        self.assertFalse(resultado["exito"])
        self.assertIn("Cantidad de habitaciones invalida", resultado["errores"])

    def test_caso_c4_fecha_invalida(self):
        """Caso C4: Fecha inválida (anterior a la fecha actual)"""
        resultado = reservar_habitaciones(4, "4-5-2023", 25)
        self.assertFalse(resultado["exito"])
        self.assertIn("Fecha invalida", resultado["errores"])

    def test_caso_c5_duracion_menor_a_1(self):
        """Caso C5: Duración < 1"""
        resultado = reservar_habitaciones(4, "4-5-2025", -22)
        self.assertFalse(resultado["exito"])
        self.assertIn("Duracion de estadia invalida", resultado["errores"])

    def test_caso_c6_duracion_mayor_a_30(self):
        """Caso C6: Duración > 30"""
        resultado = reservar_habitaciones(4, "4-5-2025", 35)
        self.assertFalse(resultado["exito"])
        self.assertIn("Duracion de estadia invalida", resultado["errores"])


unittest.main(argv=[''], exit=False)
