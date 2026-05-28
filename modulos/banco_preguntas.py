# modulos/banco_preguntas.py

BANCO_40_PREGUNTAS = [
    # ==========================================
    # MÓDULO I: TERMODINÁMICA E HIDRATOS (Preguntas 1 a 7)
    # ==========================================
    {
        "id": 1,
        "modulo": "Módulo I",
        "pregunta": "1. ¿Qué impacto operativo inmediato tiene el aumento de la presión en el Colector de Entrada respecto a la curva de equilibrio de hidratos?",
        "opciones": [
            "Aumenta la temperatura de formación, desplazando la operación hacia la zona de riesgo de cristalización.",
            "Disminuye la temperatura de disociación, permitiendo operar con mayor contenido de agua libre.",
            "No altera el equilibrio termodinámico, solo modifica el tiempo de residencia."
        ],
        "correcta": "Aumenta la temperatura de formación, desplazando la operación hacia la zona de riesgo de cristalización.",
        "feedback": "A presiones más elevadas, las moléculas de agua necesitan menor subenfriamiento para estructurar las 'jaulas' cristalinas (clatratos)."
    },
    {
        "id": 2,
        "modulo": "Módulo I",
        "pregunta": "2. En la ecuación cúbica de estado de Peng-Robinson, ¿qué representa físicamente el parámetro 'b'?",
        "opciones": [
            "Las fuerzas de atracción intermoleculares de la mezcla.",
            "El co-volumen molecular o espacio mínimo ocupado por las moléculas de gas real.",
            "El factor de acentricidad de los componentes pesados."
        ],
        "correcta": "El co-volumen molecular o espacio mínimo ocupado por las moléculas de gas real.",
        "feedback": "El co-volumen 'b' corrige el volumen ideal restando el espacio físico real que ocupan las propias moléculas de hidrocarburo."
    },
    {
        "id": 3,
        "modulo": "Módulo I",
        "pregunta": "3. Si el factor de compresibilidad Z es menor a 1.0 (Z < 1), ¿cuál es el comportamiento predominante del gas real?",
        "opciones": [
            "Las fuerzas de repulsión dominan y el gas ocupa más volumen que el ideal.",
            "Las fuerzas de atracción intermolecular predominan, facilitando la compresión del gas.",
            "El gas se comporta exactamente como un fluido perfecto no viscoso."
        ],
        "correcta": "Las fuerzas de atracción intermolecular predominan, facilitando la compresión del gas.",
        "feedback": "Cuando Z < 1, las fuerzas atractivas acercan las moléculas más de lo que predice la ley de gases ideales."
    },
    {
        "id": 4,
        "modulo": "Módulo I",
        "pregunta": "4. ¿Cuál es la función principal de la inyección de Metanol en el colector de gas húmedo?",
        "opciones": [
            "Actuar como inhibidor termodinámico disminuyendo el punto de congelamiento del agua.",
            "Incrementar la viscosidad del condensado para mejorar la decantación.",
            "Absorber el CO2 remanente por reacción química endotérmica."
        ],
        "correcta": "Actuar como inhibidor termodinámico disminuyendo el punto de congelamiento del agua.",
        "feedback": "El metanol se une a las moléculas de agua rompiendo los puentes de hidrógeno, desplazando la curva de hidratos a temperaturas mucho más frías."
    },
    {
        "id": 5,
        "modulo": "Módulo I",
        "pregunta": "5. ¿Qué diferencia fundamental existe entre un inhibidor termodinámico (como el MEG) y un inhibidor cinético (KHI) para hidratos?",
        "opciones": [
            "El MEG disuelve los hidratos ya formados y el KHI previene la corrosión asociada.",
            "El MEG desplaza la curva de equilibrio térmico, mientras que el KHI retrasa la nucleación y crecimiento de los cristales.",
            "El KHI altera la presión crítica de la mezcla y el MEG solo modifica la entalpía."
        ],
        "correcta": "El MEG desplaza la curva de equilibrio térmico, mientras que el KHI retrasa la nucleación y crecimiento de los cristales.",
        "feedback": "Los KHI actúan como polímeros que bloquean mecánicamente el crecimiento inicial del cristal sin cambiar las condiciones termodinámicas."
    },
    {
        "id": 6,
        "modulo": "Módulo I",
        "pregunta": "6. A presiones superiores a 7000 kPa, la precisión de las ecuaciones de estado cúbicas estándar decrece notablemente. ¿Qué modelo alternativo se prefiere para el cálculo preciso del factor Z de despacho?",
        "opciones": [
            "Ecuación de gases ideales ajustada por temperatura.",
            "Modelo AGA8 (American Gas Association Report No. 8).",
            "Ecuación original de Van der Waals sin coeficientes binarios."
        ],
        "correcta": "Modelo AGA8 (American Gas Association Report No. 8).",
        "feedback": "La norma AGA8 utiliza una formulación de coeficientes de virial extendida, diseñada específicamente para transferencias de custodia de alta precisión."
    },
    {
        "id": 7,
        "modulo": "Módulo I",
        "pregunta": "7. Si se analiza un gas natural rico en componentes C3 y C4, ¿cómo se posiciona su cricondembara en comparación con un gas seco (metano puro)?",
        "opciones": [
            "Se desplaza hacia valores de presión y temperatura sustancialmente más elevados, ampliando la región de dos fases.",
            "Permanece idéntica ya que el metano domina el 90% de la mezcla.",
            "Se desplaza verticalmente hacia abajo, reduciendo el riesgo de condensación retrógrada."
        ],
        "correcta": "Se desplaza hacia valores de presión y temperatura sustancialmente más elevados, ampliando la región de dos fases.",
        "feedback": "La presencia de componentes intermedios y pesados expande considerablemente la envolvente de fases (región de dos fases líquido-vapor)."
    },

    # ==========================================
    # MÓDULO II: HIDRÁULICA Y SEPARACIÓN (Preguntas 8 a 14)
    # ==========================================
    {
        "id": 8,
        "modulo": "Módulo II",
        "pregunta": "8. Según la ecuación de Souders-Brown, si la densidad del gas (ρg) aumenta debido a una sobrepresión, la velocidad máxima permitida del gas (vmax) dentro del separador:",
        "opciones": [
            "Aumenta linealmente con la presión.",
            "Disminuye, requiriendo vigilar el caudal de entrada para evitar arrastre.",
            "Permanecerá constante ya que depende solo de la malla coalescedora."
        ],
        "correcta": "Disminuye, requiriendo vigilar el caudal de entrada para mantener la eficiencia de separación.",
        "feedback": "Al aumentar ρg disminuye la diferencia de densidades (ρl - ρg), reduciendo la velocidad terminal de caída de las gotas líquidas."
    },
    {
        "id": 9,
        "modulo": "Módulo II",
        "pregunta": "9. ¿Cuál es el propósito mecánico y operativo del 'Deflector de Entrada' (Inlet Slug Deflector) en un separador bifásico?",
        "opciones": [
            "Reducir bruscamente el momento lineal del fluido entrante y realizar una pre-separación gruesa.",
            "Filtrar las partículas sólidas finas por un sistema de cartuchos de mallas.",
            "Aumentar la contrapresión del colector para regular la apertura de las SDV."
        ],
        "correcta": "Reducir bruscamente el momento lineal del fluido entrante y realizar una pre-separación gruesa.",
        "feedback": "El deflector disipa la energía cinética del bache de líquido entrante, direccionándolo hacia la sección de acumulación del fondo."
    },
    {
        "id": 10,
        "modulo": "Módulo II",
        "pregunta": "10. ¿Qué se entiende por 'Carry-over' en un separador de alta presión?",
        "opciones": [
            "La fuga de gas a través de la línea de purga de líquidos por mal cierre de la LCV.",
            "El arrastre de gotas líquidas suspendidas en la corriente de gas que sale por el tope.",
            "La acumulación de barros inertes que restringen el volumen útil del recipiente."
        ],
        "correcta": "El arrastre de gotas líquidas suspendidas en la corriente de gas que sale por el tope.",
        "feedback": "El carry-over satura las mallas demister y arrastra hidrocarburos líquidos aguas abajo, contaminando plantas de TEG o compresores."
    },
    {
        "id": 11,
        "modulo": "Módulo II",
        "pregunta": "11. ¿Qué condición hidrodinámica define la aparición de 'Carry-under' en el compartimiento de líquidos?",
        "opciones": [
            "Exceso de inyección de antiespumante químico.",
            "Arrastre de burbujas de gas atrapadas dentro de la fase líquida saliente debido a un bajo tiempo de residencia.",
            "El bloqueo mecánico de la válvula de control de contrapresión de gas (PCV)."
        ],
        "correcta": "Arrastre de burbujas de gas atrapadas dentro de la fase líquida saliente debido a un bajo tiempo de residencia.",
        "feedback": "Si el nivel de líquido es muy bajo o el caudal de salida es excesivo, el gas no llega a migrar hacia la superficie y viaja con el líquido."
    },
    {
        "id": 12,
        "modulo": "Módulo II",
        "pregunta": "12. En un Slug Catcher tipo 'Finger' (de dedos), ¿cómo se logra el control de separación primaria?",
        "opciones": [
            "Mediante múltiples cañerías paralelas con pendiente descendente que aprovechan la segregación gravitatoria a lo largo del recorrido.",
            "Por un sistema interno de platos de válvulas operados por pistones neumáticos.",
            "A través de filtros coalescedores cerámicos de alta pérdida de carga."
        ],
        "correcta": "Mediante múltiples cañerías paralelas con pendiente descendente que aprovechan la segregación gravitatoria a lo largo del recorrido.",
        "feedback": "La gran longitud de los tubos ('dedos') provee el volumen necesario para amortiguar baches y permite que el líquido decante de forma progresiva."
    },
    {
        "id": 13,
        "modulo": "Módulo II",
        "pregunta": "13. ¿Qué indicador instrumental en el separador advierte de manera directa el ensuciamiento u obstrucción de la malla desnebulizadora (Demister Pad)?",
        "opciones": [
            "Aumento de la temperatura en el fondo del recipiente.",
            "Un incremento anómalo en la presión diferencial (Delta P) medida entre la entrada y la salida de gas.",
            "Disminución drástica en la carrera de apertura de la válvula de control de nivel (LCV)."
        ],
        "correcta": "Un incremento anómalo en la presión diferencial (Delta P) medida entre la entrada y la salida de gas.",
        "feedback": "La acumulación de depósitos, parafinas o sales obstruye los canales libres del demister, generando una severa restricción de flujo y salto de presión."
    },
    {
        "id": 14,
        "modulo": "Módulo II",
        "pregunta": "14. Durante una maniobra de vaciado manual de líquidos pesados de un separador, si el lazo de control de presión de gas falla y se cierra por completo, ¿qué riesgo operacional inmediato corre el sistema?",
        "opciones": [
            "El colapso por vacío estructural del recipiente.",
            "Una sobrepresión en el cuerpo del separador por acumulación continua del gas de entrada.",
            "La vaporización instantánea de todo el condensado de fondo."
        ],
        "correcta": "Una sobrepresión en el cuerpo del separador por acumulación continua del gas de entrada.",
        "feedback": "Al bloquearse la salida de gas con alimentación abierta, la presión subirá rápidamente hacia el seteo de las válvulas de seguridad (PSV)."
    },

    # ==========================================
    # MÓDULO III: TRANSFERENCIA DE MASA Y TEG (Preguntas 15 a 21)
    # ==========================================
    {
        "id": 15,
        "modulo": "Módulo III",
        "pregunta": "15. ¿Qué fenómeno crítico ocurre si ingresan hidrocarburos líquidos o contaminantes a la torre contactora de TEG?",
        "opciones": [
            "Aumenta la eficiencia de absorción de agua.",
            "Se genera espumado (foaming) del solvente con severo arrastre por cabeza (carry-over).",
            "El glicol sufre congelamiento instantáneo en los platos superiores."
        ],
        "correcta": "Se genera espumado (foaming) del solvente con severo arrastre por cabeza (carry-over).",
        "feedback": "La contaminación altera la tensión interfacial del glicol, causando espuma. Esto eleva la Delta P de la torre y arrastra el glicol hacia el gas de venta."
    },
    {
        "id": 16,
        "modulo": "Módulo III",
        "pregunta": "16. ¿Cuál es el rango de temperatura óptimo de operación del Reboiler de TEG para lograr una regeneración efectiva sin degradar térmicamente el glicol?",
        "opciones": [
            "120 °C a 150 °C",
            "195 °C a 202 °C",
            "230 °C a 250 °C"
        ],
        "correcta": "195 °C a 202 °C",
        "feedback": "El agua se evapora a los 100 °C, pero para romper el enlace con el TEG se requieren ~200 °C. Por encima de 204 °C, el TEG se degrada de forma irreversible."
    },
    {
        "id": 17,
        "modulo": "Módulo III",
        "pregunta": "17. ¿Qué función cumple la inyección de 'Stripping Gas' en la base de la columna de regeneración de glicol?",
        "opciones": [
            "Reducir la presión parcial del vapor de agua, permitiendo elevar la pureza del glicol pobre por encima del 99.5%.",
            "Enfriar el glicol antes de que ingrese a las bombas de alta presión.",
            "Actuar como reactivo químico para neutralizar el sulfuro de hidrógeno (H2S)."
        ],
        "correcta": "Reducir la presión parcial del vapor de agua, permitiendo elevar la pureza del glicol pobre por encima del 99.5%.",
        "feedback": "El gas de despojamiento barre las moléculas de vapor de agua remanentes del sistema, logrando purezas de glicol ultra-pobre vitales para zonas criogénicas."
    },
    {
        "id": 18,
        "modulo": "Módulo III",
        "pregunta": "18. Para evitar la condensación de hidrocarburos gaseosos dentro de la torre contactora de TEG, ¿cómo debe ser la temperatura del glicol pobre de entrada respecto a la del gas húmedo?",
        "opciones": [
            "Idéntica o ligeramente inferior para maximizar el balance entálpico.",
            "Entre 3 °C y 5 °C por encima de la temperatura del gas de entrada.",
            "Al menos 15 °C por debajo para inducir un gradiente térmico inverso."
        ],
        "correcta": "Entre 3 °C y 5 °C por encima de la temperatura del gas de entrada.",
        "feedback": "Si el glicol entra más frío que el gas, enfriará la corriente de hidrocarburos llevándola por debajo de su punto de rocío y provocando condensación de líquidos y espumado."
    },
    {
        "id": 19,
        "modulo": "Módulo III",
        "pregunta": "19. ¿Cuál es la consecuencia operativa directa de tener una tasa de circulación de TEG excesivamente alta (ej. > 4.5 gal/lb H2O)?",
        "opciones": [
            "Sobrecarga térmica en el reboiler, aumento del consumo de combustible y mayor arrastre de VOCs en el gas de venteo.",
            "Secado excesivo del gas que daña los gasoductos por erosión molecular.",
            "Solidificación del glicol en las líneas de succión de las bombas."
        ],
        "correcta": "Sobrecarga térmica en el reboiler, aumento del consumo de combustible y mayor arrastre de VOCs en el gas de venteo.",
        "feedback": "Circular glicol de más exige mayor energía para calentarlo en el reboiler y satura innecesariamente el tanque de flasheo con gases disueltos."
    },
    {
        "id": 20,
        "modulo": "Módulo III",
        "pregunta": "20. ¿Qué propósito principal tiene el acumulador o tanque de Flash (Flash Drum) en el lazo de glicol rico?",
        "opciones": [
            "Almacenar el glicol de reserva para casos de paradas prolongadas de planta.",
            "Separar por caída de presión los hidrocarburos gaseosos atrapados en el glicol antes de que lleguen al reboiler.",
            "Filtrar mecánicamente las partículas de carbón activado en suspensión."
        ],
        "correcta": "Separar por caída de presión los hidrocarburos gaseosos atrapados en el glicol antes de que lleguen al reboiler.",
        "feedback": "El flash drum opera a baja presión (300-500 kPa) para que los gases disueltos en la contactora se liberen de forma segura y se recuperen como combustible o antorcha."
    },
    {
        "id": 21,
        "modulo": "Módulo III",
        "pregunta": "21. Si las bombas de glicol de tipo Kimray (energizadas por el propio glicol rico) comienzan a ciclar de forma errática o se detienen, ¿cuál es la primera verificación en campo?",
        "opciones": [
            "Revisar el nivel de incrustaciones de carbonatos en el tubo de fuego.",
            "Comprobar la limpieza de los filtros de partículas de la succión y verificar si hay gas entrampado en el bloque de válvulas piloto.",
            "Aumentar inmediatamente el flujo de stripping gas de la columna."
        ],
        "correcta": "Comprobar la limpieza de los filtros de partículas de la succión y verificar si hay gas entrampado en el bloque de válvulas piloto.",
        "feedback": "Las impurezas mecánicas traban las agujas y sellos internos de las bombas Kimray, deteniendo el lazo de deshidratación de forma repentina."
    },

    # ==========================================
    # MÓDULO IV: CRIOGENIA Y EXPANSIÓN (Preguntas 22 a 28)
    # ==========================================
    {
        "id": 22,
        "modulo": "Módulo IV",
        "pregunta": "22. Si un operador reduce la eficiencia isentrópica de un turboexpansor cerrando parcialmente los álabes (toberas de entrada), ¿qué ocurre con la temperatura de salida?",
        "opciones": [
            "Disminuye drásticamente alcanzando rangos más criogénicos por efecto Joule-Thomson.",
            "Será más alta que en una expansión ideal, limitando la recuperación profunda de líquidos pesados (LGN).",
            "Se mantiene idéntica, pero se reduce la potencia transmitida al compresor booster."
        ],
        "correcta": "Será más alta que en una expansión ideal (reversible), limitando la recuperación profunda de líquidos pesados (LGN).",
        "feedback": "A menor eficiencia isentrópica, mayor es la generación de entropía (irreversibilidades). El fluido retiene energía, resultando en una menor caída térmica."
    },
    {
        "id": 23,
        "modulo": "Módulo IV",
        "pregunta": "23. ¿Qué diferencia termodinámica fundamental existe entre la expansión en una válvula Joule-Thomson (JT) y en un Turboexpansor?",
        "opciones": [
            "La válvula JT realiza una expansión isentálpica (sin trabajo), mientras que el turboexpansor realiza una expansión isentrópica con extracción de trabajo útil.",
            "El turboexpansor mantiene la entalpía constante aumentando la entropía de la mezcla.",
            "La válvula JT extrae energía cinética transformándola en calor de compresión."
        ],
        "correcta": "La válvula JT realiza una expansión isentálpica (sin trabajo), mientras que el turboexpansor realiza una expansión isentrópica con extracción de trabajo útil.",
        "feedback": "La extracción de trabajo en el eje del turboexpansor genera caídas de temperatura drásticamente superiores a las de una simple restricción por válvula JT."
    },
    {
        "id": 24,
        "modulo": "Módulo IV",
        "pregunta": "24. ¿Cuál es el riesgo crítico de que la concentración de CO2 en el gas de entrada a la sección criogénica supere los límites de especificación (ej. > 0.5-1.0% molar)?",
        "opciones": [
            "Corrosión galvánica acelerada en los aeroenfriadores de salida.",
            "Congelamiento y solidificación del CO2 en los canales del intercambiador de placas (Cold Box) y platos superiores de la Demetinizadora.",
            "Aumento incontrolable de la presión de vapor en el fondo de la deetanizadora."
        ],
        "correcta": "Congelamiento y solidificación del CO2 en los canales del intercambiador de placas (Cold Box) y platos superiores de la Demetinizadora.",
        "feedback": "A temperaturas criogénicas (< -60 °C), el CO2 excede su límite de solubilidad y sublima, formando hielo seco que tapona los canales del intercambiador compacto."
    },
    {
        "id": 25,
        "modulo": "Módulo IV",
        "pregunta": "25. ¿Para qué se utiliza constructivamente un intercambiador de calor de placas de aluminio soldado (Cold Box) en lugar de uno de tubo y coraza tradicional en plantas criogénicas?",
        "opciones": [
            "Para tolerar fluidos corrosivos con alto contenido de azufre libre.",
            "Debido a su enorme área de transferencia por unidad de volumen y su capacidad de manejar múltiples corrientes en aproximaciones térmicas ultra-estrechas (< 2 °C).",
            "Porque permite el desarmado rápido en campo para limpieza mecánica con cepillos industriales."
        ],
        "correcta": "Debido a su enorme área de transferencia por unidad de volumen y su capacidad de manejar múltiples corrientes en aproximaciones térmicas ultra-estrechas (< 2 °C).",
        "feedback": "La eficiencia criogénica depende de recuperar el frío del gas residual contra el gas de carga; el Cold Box logra esto en configuraciones sumamente compactas."
    },
    {
        "id": 26,
        "modulo": "Módulo IV",
        "pregunta": "26. ¿Qué función operativa cumple el compresor de carga 'Booster' acoplado rígidamente al eje del Turboexpansor?",
        "opciones": [
            "Succionar los líquidos de fondo de la demetinizadora para bombearlos al fraccionamiento.",
            "Aprovechar la potencia mecánica generada por la expansión del gas para realizar una pre-compresión del gas residual (recompresión), optimizando la eficiencia de la planta.",
            "Inyectar gas de reciclo caliente hacia las toberas para evitar el sobrecalentamiento axial."
        ],
        "correcta": "Aprovechar la potencia mecánica generada por la expansión del gas para realizar una pre-compresión del gas residual (recompresión), optimizando la eficiencia de la planta.",
        "feedback": "El booster recupera el trabajo extraído en la expansión y lo reinyecta en la corriente de proceso, minimizando la potencia requerida por los compresores principales de venta."
    },
    {
        "id": 27,
        "modulo": "Módulo IV",
        "pregunta": "27. Si se observa presencia de hidrocarburos pesados (C6+) en el gas de alimentación de la criogénica, ¿cuál es el peligro latente en el separador frío?",
        "opciones": [
            "Formación de parafinas sólidas o geles de hidrocarburos pesados que obstruyen las mallas coalescedoras y líneas criogénicas.",
            "Incremento masivo en la dosificación requerida de inhibidores de corrosión anódica.",
            "La desactivación química permanente de las camas de tamices moleculares."
        ],
        "correcta": "Formación de parafinas sólidas o geles de hidrocarburos pesados que obstruyen las mallas coalescedoras y líneas criogénicas.",
        "feedback": "Los hidrocarburos pesados tienen puntos de congelamiento altos. Sometidos a -40 °C o menos, solidifican de inmediato inhabilitando los equipos."
    },
    {
        "id": 28,
        "modulo": "Módulo IV",
        "pregunta": "28. ¿Por qué el gas destinado a turboexpansión profunda debe deshidratarse mediante Tamices Moleculares hasta valores < 1 ppm de agua, en vez de usar una planta convencional de TEG?",
        "opciones": [
            "Porque el TEG reacciona químicamente con el metano a temperaturas inferiores a -20 °C.",
            "Porque las plantas de TEG solo reducen la humedad hasta ~60 mg/m³ (-15 °C de punto de rocío), lo cual causaría el bloqueo total por hielo de la zona criogénica (-100 °C).",
            "Para evitar el desgaste por cavitación molecular en los álabes del rodete del expansor."
        ],
        "correcta": "Porque las plantas de TEG solo reducen la humedad hasta ~60 mg/m³ (-15 °C de punto de rocío), lo cual causaría el bloqueo total por hielo de la zona criogénica (-100 °C).",
        "feedback": "La deshidratación por adsorción en tamices de zeolita (malla 4A) es el único método capaz de eliminar la humedad a niveles traza indispensables para evitar taponamientos criogénicos."
    },

    # ==========================================
    # MÓDULO V: DINÁMICA DE COMPRESIÓN (Preguntas 29 a 35)
    # ==========================================
    {
        "id": 29,
        "modulo": "Módulo V",
        "pregunta": "29. Describa el comportamiento aerodinámico del gas dentro de un compresor centrífugo cuando el punto de operación cruza a la izquierda de la Línea de Límite de Surge (SLL):",
        "opciones": [
            "El caudal volumétrico se estabiliza y la presión de descarga aumenta por encima del diseño.",
            "El flujo se invierte instantáneamente, circulando de forma retrógrada desde la descarga hacia la succión con severas fuerzas axiales.",
            "Los álabes entran en cavitación destructiva debido a la formación de burbujas de vapor."
        ],
        "correcta": "El flujo se invierte instantáneamente, circulando de forma retrógrada desde la descarga hacia la succión con severas fuerzas axiales.",
        "feedback": "El surge o bombeo ocurre cuando la contrapresión vence el empuje dinámico del rodete, generando una inversión cíclica del flujo que destruye sellos y cojinetes."
    },
    {
        "id": 30,
        "modulo": "Módulo V",
        "pregunta": "30. ¿Cuál es el rol operativo fundamental del lazo de control Anti-Surge en una turbocompresora?",
        "opciones": [
            "Mantener constante la presión de despacho regulando las RPM del motor de combustión.",
            "Medir el caudal y la relación de compresión para abrir preventivamente la Válvula de Reciclo Rápido (ASV) manteniendo el punto de operación en zona segura.",
            "Cortar el suministro de gas combustible en caso de alta temperatura en los cojinetes de empuje."
        ],
        "correcta": "Medir el caudal y la relación de compresión para abrir preventivamente la Válvula de Reciclo Rápido (ASV) manteniendo el punto de operación en zona segura.",
        "feedback": "La apertura de la ASV reinyecta gas de la descarga hacia la succión, aumentando el caudal volumétrico real que circula por el rodete por encima del límite crítico."
    },
    {
        "id": 31,
        "modulo": "Módulo V",
        "pregunta": "31. ¿Qué es el fenómeno de 'Choke' o 'Stone Wall' en la curva de performance de un compresor centrífugo?",
        "opciones": [
            "El punto de caudal máximo permitido donde la velocidad del gas en el ojo del impulsor alcanza la velocidad del sonido (Mach 1).",
            "La detención total del compresor por disparo automático de alta vibración axial.",
            "El bloqueo de la succión debido a la formación masiva de hidratos sólidos."
        ],
        "correcta": "El punto de caudal máximo permitido donde la velocidad del gas en el ojo del impulsor alcanza la velocidad del sonido (Mach 1).",
        "feedback": "En la condición de Choke, el caudal no puede incrementarse más, la eficiencia colapsa verticalmente y se producen severas ondas de choque internas."
    },
    {
        "id": 32,
        "modulo": "Módulo V",
        "pregunta": "32. ¿Por qué es obligatorio instalar un Separador de Succión (Scrubber) inmediatamente aguas arriba de un compresor centrífugo?",
        "opciones": [
            "Para estabilizar la firma térmica del gas antes de la etapa de compresión rotativa.",
            "Para eliminar cualquier traza o bache de hidrocarburos líquidos o agua libre que destruiría los álabes debido al impacto mecánico de un fluido incompresible.",
            "Para inyectar dosificaciones controladas de inhibidores de fricción molecular."
        ],
        "correcta": "Para eliminar cualquier traza o bache de hidrocarburos líquidos o agua libre que destruiría los álabes debido al impacto mecánico de un fluido incompresible.",
        "feedback": "Los líquidos son incompresibles. El impacto de una gota de líquido contra un rodete girando a miles de RPM causa erosión severa y rotura inmediata de álabes por desbalance dinámico."
    },
    {
        "id": 33,
        "modulo": "Módulo V",
        "pregunta": "33. ¿Qué función crítica cumplen los 'Sellos de Gas Seco' (Dry Gas Seals) en un compresor centrífugo de gas natural?",
        "opciones": [
            "Evitar que el aceite de lubricación de los cojinetes se mezcle con el gas de proceso en las cámaras internas.",
            "Sellar herméticamente el espacio entre el eje rotante y la carcasa presurizada del compresor utilizando gas de proceso filtrado de alta pureza como barrera.",
            "Refrigerar las etapas internas del compresor mediante la inyección radial de nitrógeno."
        ],
        "correcta": "Sellar herméticamente el espacio entre el eje rotante y la carcasa presurizada del compresor utilizando gas de proceso filtrado de alta pureza como barrera.",
        "feedback": "Los sellos de gas seco operan por ranuras dinámicas sin contacto físico, evitando fugas masivas de gas a la atmósfera de manera altamente tecnológica y limpia."
    },
    {
        "id": 34,
        "modulo": "Módulo V",
        "pregunta": "34. En una estación compresora con múltiples etapas en serie, ¿por qué es mandatorio instalar aeroenfriadores (Intercoolers) entre cada etapa de compresión?",
        "opciones": [
            "Para reducir el volumen específico del gas disminuyendo la temperatura, lo que minimiza la potencia requerida en la siguiente etapa de compresión y protege los materiales.",
            "Para inducir la licuación parcial del metano antes de la etapa final de despacho.",
            "Para cumplir con las pautas de impacto ambiental respecto al venteo de calor hacia la atmósfera."
        ],
        "correcta": "Para reducir el volumen específico del gas disminuyendo la temperatura, lo que minimiza la potencia requerida en la siguiente etapa de compresión y protege los materiales.",
        "feedback": "La compresión incrementa fuertemente la temperatura por trabajo termodinámico. El enfriamiento interetapa reduce el volumen de gas y optimiza el consumo energético."
    },
    {
        "id": 35,
        "modulo": "Módulo V",
        "pregunta": "35. ¿Qué variable física monitorea de forma primaria el transmisor de vibración axial en un compresor centrífugo y qué falla mecánica severa previene?",
        "opciones": [
            "Mide el desbalance estático del rodete previniendo la fisura estructural de la carcasa.",
            "Mide el desplazamiento microscópico del eje a lo largo de su centro longitudinal, previniendo el roce directo de los álabes contra el estator durante un evento de surge.",
            "Monitorea el pandeo del eje causado por variaciones violentas de la temperatura ambiente."
        ],
        "correcta": "Mide el desplazamiento microscópico del eje a lo largo de su centro longitudinal, previniendo el roce directo de los álabes contra el estator durante un evento de surge.",
        "feedback": "Las oscilaciones violentas del surge empujan el eje hacia adelante y atrás. Superar el límite admisible destruye las pastillas de los cojinetes de empuje (Tilting Pad Bearings)."
    },

    # ==========================================
    # MÓDULO VI: PROTECCIONES Y NORMA NAG-125 (Preguntas 36 a 40)
    # ==========================================
    {
        "id": 36,
        "modulo": "Módulo VI",
        "pregunta": "36. Bajo la filosofía de seguridad 'Fail-Safe' (NAG-125), ¿cómo deben actuar las válvulas de bloqueo (SDV) y despresurización (BDV) ante una pérdida de aire de instrumentos?",
        "opciones": [
            "Las SDV abren para liberar el inventario y las BDV cierran para confinar la planta.",
            "Tanto las SDV como las BDV permanecen bloqueadas en su última posición operativa.",
            "Las SDV cierran herméticamente (Fail-Close) para aislar fronteras y las BDV abren (Fail-Open) para despresurizar hacia la antorcha."
        ],
        "correcta": "Las SDV cierran herméticamente (Fail-Close) para aislar fronteras y las BDV abren (Fail-Open) para despresurizar hacia la antorcha.",
        "feedback": "La arquitectura 'desenergizar para disparar' asegura que por acción de resortes mecánicos internos, la planta quede automáticamente aislada y despresurizada ante fallas críticas de servicios."
    },
    {
        "id": 37,
        "modulo": "Módulo VI",
        "pregunta": "37. ¿Qué diferencia regulatoria e instrumental existe entre el DCS (Sistema de Control de Procesos) y el SIS (Sistema Instrumentado de Seguridad) según la NAG-125?",
        "opciones": [
            "El DCS y el SIS deben compartir el mismo procesador físico y la misma pantalla de operación para agilizar la toma de decisiones.",
            "El SIS debe estar lógica y físicamente desacoplado del DCS, operando con hardware dedicado y certificado (PLC de Seguridad SIL-2/3) independiente del control diario.",
            "El DCS maneja las paradas de emergencia globales de planta y el SIS regula los lazos PID de flujo."
        ],
        "correcta": "El SIS debe estar lógica y físicamente desacoplado del DCS, operando con hardware dedicado y certificado (PLC de Seguridad SIL-2/3) independiente del control diario.",
        "feedback": "La independencia del SIS garantiza que ante un colapso generalizado del DCS de control operativo, los lazos de protección automatizados actúen de manera infalible."
    },
    {
        "id": 38,
        "modulo": "Módulo VI",
        "pregunta": "38. ¿Qué protocolo estricto define la activación de una Parada de Emergencia Nivel 1 (ESD Nivel 1) en la planta?",
        "opciones": [
            "Parada localizada del tren de generación eléctrica auxiliar.",
            "Aislamiento total e inmediato de todas las fronteras de la planta (cierre de SDVs) y despresurización automatizada completa de los inventarios de gas de proceso hacia la antorcha a través de las BDVs.",
            "Apertura del bypass general del slug catcher para derivar la producción directo a gasoducto sin tratamiento."
        ],
        "correcta": "Aislamiento total e inmediato de todas las fronteras de la planta (cierre de SDVs) y despresurización automatizada completa de los inventarios of gas de proceso hacia la antorcha a través de las BDVs.",
        "feedback": "El ESD Nivel 1 es el máximo nivel de resguardo ante catástrofes, incendios o fugas masivas, minimizando la energía acumulada en las instalaciones en minutos."
    },
    {
        "id": 39,
        "modulo": "Módulo VI",
        "pregunta": "39. ¿Qué significa operativamente que una función de seguridad instrumentada tenga una lógica de votación '2oo3' (Dos de Tres) en los transmisores de presión de una planta?",
        "opciones": [
            "Que la válvula disparará solo si los tres transmisores fallan al mismo tiempo.",
            "Que el PLC de seguridad ejecutará el disparo de la planta si al menos dos de los tres sensores independientes validan de forma simultánea la condición de alarma.",
            "Que se promedian las dos lecturas más bajas ignorando de manera permanente la lectura del tercer sensor."
        ],
        "correcta": "Que el PLC de seguridad ejecutará el disparo de la planta si al menos dos de los tres sensores independientes validan de forma simultánea la condición de alarma.",
        "feedback": "La lógica 2oo3 equilibra perfectamente la seguridad y la disponibilidad operacional, evitando paradas espurias por falla de un único sensor y garantizando el disparo si hay una emergencia real."
    },
    {
        "id": 40,
        "modulo": "Módulo VI",
        "pregunta": "40. De acuerdo con las buenas prácticas de ingeniería de seguridad, ¿cuál es el propósito de realizar una prueba de recorrido parcial (Partial Stroke Testing - PST) a una válvula de corte crítico (SDV) mientras la planta está en plena operación?",
        "opciones": [
            "Calibrar el posicionador digital para modificar el set-point del lazo de flujo.",
            "Mover la válvula una fracción pequeña de su carrera (ej. 10%-15%) para verificar que el actuador no esté agarrotado o bloqueado mecánicamente, sin interrumpir el proceso.",
            "Comprobar el sello estanco de las empaquetaduras internas inyectando grasa selladora a presión."
        ],
        "correcta": "Mover la válvula una fracción pequeña de su carrera (ej. 10%-15%) para verificar que el actuador no esté agarrotado o bloqueado mecánicamente, sin interrumpir el proceso.",
        "feedback": "El PST permite detectar fallas ocultas (fricciones excesivas o resortes vencidos) incrementando el intervalo de prueba total y reduciendo la probabilidad de falla en demanda."
    }
]
