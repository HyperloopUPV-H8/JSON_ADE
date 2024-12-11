import os
import json

def validate_json_structure(data):
    errors = []

    
    if "board_id" in data:
        if not isinstance(data["board_id"], int):
            errors.append(f"'board_id' debe ser un entero, pero se encontró: {type(data['board_id']).__name__}.")

    if "board_ip" in data:
        if not isinstance(data["board_ip"], str):
            errors.append(f"'board_ip' debe ser una cadena, pero se encontró: {type(data['board_ip']).__name__}.")

    
    if "measurements" in data:
        if not isinstance(data["measurements"], list):
            errors.append("La clave 'measurements' debe ser una lista.")
        else:
            for measurement in data["measurements"]:
                if isinstance(measurement, dict):  
                    required_keys = ["id", "name", "type"]
                    for key in required_keys:
                        if key not in measurement:
                            errors.append(f"Falta la clave '{key}' en un objeto de 'measurements'.")
                    if "id" in measurement and not isinstance(measurement["id"], str):
                        errors.append(f"El 'id' debe ser una cadena en: {measurement}")
                    if "name" in measurement and not isinstance(measurement["name"], str):
                        errors.append(f"El 'name' debe ser una cadena en: {measurement}")
                    if "type" in measurement and not isinstance(measurement["type"], str):
                        errors.append(f"El 'type' debe ser una cadena en: {measurement}")
                    if "safeRange" in measurement and not isinstance(measurement.get("safeRange", []), list):
                        errors.append(f"'safeRange' debe ser una lista en: {measurement}")
                    if "warningRange" in measurement and not isinstance(measurement.get("warningRange", []), list):
                        errors.append(f"'warningRange' debe ser una lista en: {measurement}")
                    if "podUnits" in measurement and not isinstance(measurement["podUnits"], str):
                        errors.append(f"El 'podUnits' debe ser una cadena en: {measurement}") #esto se puede quitar (json 516)
                elif not isinstance(measurement, str): 
                    errors.append("Cada elemento en 'measurements' debe ser un objeto o una cadena (nombre de archivo).")

    
    if "packets" in data:
        if not isinstance(data["packets"], list):
            errors.append("La clave 'packets' debe ser una lista.")
        else:
            for packet in data["packets"]:
                if isinstance(packet, dict):  
                    required_keys = ["id", "name", "type"]
                    for key in required_keys:
                        if key not in packet:
                            errors.append(f"Falta la clave '{key}' en un objeto de 'packets'.")
                    if "id" in packet and not isinstance(packet["id"], str):
                        errors.append(f"El 'id' debe ser una cadena en: {packet}")
                    if "name" in packet and not isinstance(packet["name"], str):
                        errors.append(f"El 'name' debe ser una cadena en: {packet}")
                    if "type" in packet and not isinstance(packet["type"], str):
                        errors.append(f"El 'type' debe ser una cadena en: {packet}")
                    if "variables" in packet:
                        if not isinstance(packet["variables"], list):
                            errors.append(f"'variables' debe ser una lista en: {packet}")
                        else:
                            for variable in packet["variables"]:
                                if not isinstance(variable, dict):
                                    errors.append(f"Cada elemento en 'variables' debe ser un objeto en: {packet}")
                                if "name" not in variable:
                                    errors.append(f"Falta la clave 'name' en un objeto de 'variables' en: {packet}")
                elif not isinstance(packet, str):  
                    errors.append("Cada elemento en 'packets' debe ser un objeto o una cadena (nombre de archivo).")

    return errors

def validate_json_folder(folder_path):
    
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".json"):  
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        errors = validate_json_structure(data)
                        if errors:
                            print(f"Errores encontrados en {file_path}:")
                            for error in errors:
                                print(f"- {error}")
                        else:
                            print(f"{file_path} está bien estructurado.")
                except json.JSONDecodeError as e:
                    print(f"Error al decodificar JSON en {file_path}: {e}")
                except Exception as e:
                    print(f"Error al procesar el archivo {file_path}: {e}")


if __name__ == "__main__":
    
    validate_json_folder("C:/Users/jesus/JSON_ADE/boards") #folder_path como input o desde la misma carpeta del .py? ns