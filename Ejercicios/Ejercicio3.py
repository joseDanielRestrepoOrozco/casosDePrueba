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