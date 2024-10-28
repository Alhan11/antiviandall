import os

# ¡Squirtle, Squirtle! Lista de patrones y extensiones sospechosas
# Esta es la lista de "ataques" que vamos a usar para buscar malware, como si fueran movimientos de Pokémon
suspicious_patterns = ["malware", "virus", "trojan"]  # ¡Ataque Mordisco!
suspicious_extensions = [".exe", ".bat", ".cmd", ".vbs"]  # ¡Ataque de confusión!

# Elegimos el "campo de batalla", o sea, el directorio que vamos a escanear
scan_directory = "C:/ruta_a_carpeta"  # Cambia esta ruta según donde quieras escanear


def scan_files(directory):
    suspicious_files = []  # ¡Charizard se prepara para la batalla!
    for root, _, files in os.walk(directory):  # Pikachu usa Agilidad para recorrer todos los archivos
        for file in files:
            file_path = os.path.join(root, file)

            # ¡Charmander usa Llamarada! Comprobamos el nombre del archivo y su extensión
            if any(pattern in file.lower() for pattern in suspicious_patterns) or file.endswith(
                    tuple(suspicious_extensions)):
                suspicious_files.append(file_path)

            # ¡Jigglypuff usa Canto! Intentamos abrir el archivo para ver si contiene patrones sospechosos
            try:
                with open(file_path, "r", errors="ignore") as f:
                    content = f.read()
                    # ¡Psyduck usa Confusión! Buscamos patrones en el contenido
                    if any(pattern in content.lower() for pattern in suspicious_patterns):
                        suspicious_files.append(file_path)
            except:
                # Si no se puede leer el archivo (como si fuera un Snorlax durmiendo)
                continue

    return suspicious_files


# ¡Ash Ketchum revisa los resultados de la batalla!
suspicious_files = scan_files(scan_directory)
if suspicious_files:
    print("Archivos sospechosos encontrados:")  # ¡Pikachu encontró algo raro!
    for file in suspicious_files:
        print(f"- {file}")  # ¡Pide ayuda a tu equipo Pokémon para revisar este archivo!
else:
    print("No se encontraron archivos sospechosos.")  # ¡Todo claro! El equipo Pokémon puede descansar.
