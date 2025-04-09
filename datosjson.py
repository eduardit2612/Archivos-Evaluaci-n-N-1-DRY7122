import json

archivo_json = 'myfile.json'

try:
    with open(archivo_json, 'r') as file:
        json_file = json.load(file)

    # Mostrar el token y el tiempo de expiración
    print("Token:", json_file['access_token'])
    print("Tiempo antes de que expire (en segundos):", json_file['expires_in'])

except FileNotFoundError:
    print(f"El archivo {archivo_json} no se encontró.")
except json.JSONDecodeError:
    print(f"Error al decodificar el archivo {archivo_json}. Asegúrese de que sea un archivo JSON válido.")
except KeyError as e:
    print(f"No se encontró la clave {e} en el JSON.")

