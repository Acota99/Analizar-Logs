Analizador de Logs & Detector de Fuerza Bruta (SSH)

Un script de seguridad en Python diseñado para automatizar el monitoreo de servidores Linux (Blue Team / Defensa). La herramienta analiza archivos de bitácoras del sistema (`auth.log`) utilizando expresiones regulares (RegEx) para identificar y alertar sobre posibles ataques de diccionario o fuerza bruta contra el servicio SSH.

Características
* **Análisis de RegEx:** Extrae con precisión las direcciones IP de los atacantes directamente de las líneas de error estándar de los demonios SSH.
* **Umbral de Alertas:** Clasifica y cuenta los intentos fallidos, detonando alertas únicamente cuando una dirección IP supera un límite de sospecha configurable (reduciendo falsos positivos).
* **Ejecución Local:** Procesa archivos de texto plano localmente, ideal para tareas programadas (cron jobs) de monitoreo en la infraestructura.

Uso
1. Descarga el archivo `analizar_logs.py` y el archivo de prueba `auth.log` en la misma carpeta.
2. Ejecuta el script desde tu terminal: python3 Analizar_logs.py
3. El script leerá el archivo de muestra y arrojará las alertas correspondientes sobre las IPs simuladas que rebasaron el límite de intentos.

Entorno de Implementación

Desarrollado para la administración segura de infraestructura y servidores. Este tipo de scripts es fundamental para la supervisión de nodos de red expuestos y la respuesta a incidentes en tiempo real, facilitando el trabajo del equipo de soporte y operaciones IT.
