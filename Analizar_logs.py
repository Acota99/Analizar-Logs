import re

def detectar_fuerza_bruta(ruta_archivo, limite_intentos=3):
    print(f"[*] Analizando bitácora de seguridad: {ruta_archivo}")
    print("-" * 50)
    
    intentos_fallidos = {}
    
    try:
        # Abrimos el archivo de logs en modo lectura
        with open(ruta_archivo, 'r') as log:
            for linea in log:
                # Buscamos la frase típica de error de acceso en servidores Linux
                if "Failed password" in linea:
                    # Extraemos la IP del atacante usando una Expresión Regular
                    match_ip = re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", linea)
                    
                    if match_ip:
                        ip_atacante = match_ip.group()
                        # Sumamos un intento fallido a esa IP
                        intentos_fallidos[ip_atacante] = intentos_fallidos.get(ip_atacante, 0) + 1
                        
        print("[!] Reporte de IPs sospechosas (Posible ataque de diccionario/fuerza bruta):")
        
        amenazas_detectadas = 0
        for ip, conteo in intentos_fallidos.items():
            if conteo >= limite_intentos:
                print(f" ALERTA: La IP {ip} falló {conteo} veces.")
                amenazas_detectadas += 1
                
        if amenazas_detectadas == 0:
            print("  Todo limpio. No se detectaron ataques.")
            
    except FileNotFoundError:
        print("[-] Error: No se encontró el archivo de logs. Revisa la ruta.")

# --- Ejecución ---
if __name__ == "__main__":
    # Nombre del archivo que vamos a analizar
    archivo_log = "auth.log" 
    
    detectar_fuerza_bruta(archivo_log)