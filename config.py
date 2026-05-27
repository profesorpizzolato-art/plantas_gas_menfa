# config.py

# =====================================================================
# 1. ESPECIFICACIONES DE CALIDAD DE CUSTODIA (Puntos de Entrega / Red)
# =====================================================================
LIMITE_HUMEDAD = 64.0         # mg/m³ máximo permitido (Manual de Gas TGS)
LIMITE_H2S = 4.0              # ppm máximo para Gas Dulce (Contaminantes)
LIMITE_CO2 = 2.0              # % molar máximo permitido

# =====================================================================
# 2. LÍMITES DE SEGURIDAD OPERATIVA E INTERLOCKS (NAG-125 / Gasoductos)
# =====================================================================
PRESION_MAX_PLANTA = 6500.0   # kPa Máximo en Colector (Separación de Entrada)
PRESION_MAX_GASODUCTO = 7400.0 # kPa Límite típico de diseño (Manual de Gasoductos)
TEMP_MAX_REBOILER = 204.0     # °C Límite operativo para evitar degradación del TEG

# Control de Niveles de Líquido en Separadores / Slug Catchers
NIVEL_LIQUIDO_CRITICO = 90.0  # % Nivel máximo para disparo automático
NIVEL_MAX_SEPARADOR = 90.0    # Alias para asegurar compatibilidad modular

# =====================================================================
# 3. PARÁMETROS CRÍTICOS DE PLANTA CRIOGÉNICA (Complejo Cerri)
# =====================================================================
TEMP_CRITICA_TURBOEXP = -90.0 # °C Temperatura de diseño para extracción de licuables
