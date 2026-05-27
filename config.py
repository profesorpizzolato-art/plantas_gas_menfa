# config.py

# --- ESPECIFICACIONES DE CALIDAD DE CUSTODIA ---
LIMITE_HUMEDAD = 64.0         # mg/m³ máximo permitido (Especificación comercial de venta)
LIMITE_H2S = 4.0              # ppm máximo permitido para Gas Dulce
LIMITE_CO2 = 2.0              # % molar máximo permitido

# --- LÍMITES DE SEGURIDAD OPERATIVA E INTERLOCKS (NAG-125) ---
PRESION_MAX_PLANTA = 6500.0   # kPa máximos en Colector de Entrada antes de CDE
PRESION_MAX_GASODUCTO = 7400.0 # kPa Límite de diseño (Manual de Gasoductos)
TEMP_MAX_REBOILER = 204.0     # °C Límite operativo para evitar degradación del TEG
NIVEL_MAX_SEPARADOR = 90.0    # % Nivel máximo (Segundo interruptor de nivel)

# --- PLANTA CRIOGÉNICA ---
TEMP_CRITICA_TURBOEXP = -90.0 # °C Temperatura de diseño de la Demetinizadora
