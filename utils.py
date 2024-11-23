import os
import sys
import json
import emoji
import psutil
import string
import random
import pathlib
import datetime

CATCH_ALL_EMAILS = [
    'profesionales-1@viviendasyparticulares.com',
    'profesionales-2@viviendasyparticulares.com',
    'profesionales-3@viviendasyparticulares.com',
    'profesionales-4@viviendasyparticulares.com',
    'profesionales-5@viviendasyparticulares.com',
    'equipo-1@viviendasyparticulares.com',
    'equipo-2@viviendasyparticulares.com',
    'equipo-3@viviendasyparticulares.com',
    'equipo-4@viviendasyparticulares.com',
    'ventas-1@viviendasyparticulares.com',
    'ventas-2@viviendasyparticulares.com',
    'ventas-3@viviendasyparticulares.com',
    'soporte-1@viviendasyparticulares.com',
    'soporte-2@viviendasyparticulares.com',
    'marketing-1@viviendasyparticulares.com',
    'marketing-2@viviendasyparticulares.com',
    'profesionales-6@viviendasyparticulares.com',
    'profesionales-7@viviendasyparticulares.com',
    'profesionales-8@viviendasyparticulares.com',
    'profesionales-9@viviendasyparticulares.com',
    'profesionales-10@viviendasyparticulares.com',
    'equipo-5@viviendasyparticulares.com',
    'equipo-6@viviendasyparticulares.com',
    'equipo-7@viviendasyparticulares.com',
    'equipo-8@viviendasyparticulares.com',
    'equipo-9@viviendasyparticulares.com',
    'equipo-10@viviendasyparticulares.com',
    'ventas-4@viviendasyparticulares.com',
    'ventas-5@viviendasyparticulares.com',
    'ventas-6@viviendasyparticulares.com',
    'ventas-7@viviendasyparticulares.com',
    'ventas-8@viviendasyparticulares.com',
    'ventas-9@viviendasyparticulares.com',
    'ventas-10@viviendasyparticulares.com',
    'soporte-3@viviendasyparticulares.com',
    'soporte-4@viviendasyparticulares.com',
    'soporte-5@viviendasyparticulares.com',
    'soporte-6@viviendasyparticulares.com',
    'soporte-7@viviendasyparticulares.com',
    'soporte-8@viviendasyparticulares.com',
    'soporte-9@viviendasyparticulares.com',
    'soporte-10@viviendasyparticulares.com',
    'marketing-3@viviendasyparticulares.com',
    'marketing-4@viviendasyparticulares.com',
    'marketing-5@viviendasyparticulares.com',
    'marketing-6@viviendasyparticulares.com',
    'marketing-7@viviendasyparticulares.com',
    'marketing-8@viviendasyparticulares.com',
    'marketing-9@viviendasyparticulares.com',
    'marketing-10@viviendasyparticulares.com',
    'admin-1@viviendasyparticulares.com',
    'admin-2@viviendasyparticulares.com',
    'admin-3@viviendasyparticulares.com',
    'admin-4@viviendasyparticulares.com',
    'admin-5@viviendasyparticulares.com',
    'admin-6@viviendasyparticulares.com',
    'admin-7@viviendasyparticulares.com',
    'admin-8@viviendasyparticulares.com',
    'admin-9@viviendasyparticulares.com',
    'admin-10@viviendasyparticulares.com',
    'gestion-1@viviendasyparticulares.com',
    'gestion-2@viviendasyparticulares.com',
    'gestion-3@viviendasyparticulares.com',
    'gestion-4@viviendasyparticulares.com',
    'gestion-5@viviendasyparticulares.com',
    'gestion-6@viviendasyparticulares.com',
    'gestion-7@viviendasyparticulares.com',
    'gestion-8@viviendasyparticulares.com',
    'gestion-9@viviendasyparticulares.com',
    'gestion-10@viviendasyparticulares.com',
    'info-1@viviendasyparticulares.com',
    'info-2@viviendasyparticulares.com',
    'info-3@viviendasyparticulares.com',
    'info-4@viviendasyparticulares.com',
    'info-5@viviendasyparticulares.com',
    'info-6@viviendasyparticulares.com',
    'info-7@viviendasyparticulares.com',
    'info-8@viviendasyparticulares.com',
    'info-9@viviendasyparticulares.com',
    'info-10@viviendasyparticulares.com',
    'consultas-1@viviendasyparticulares.com',
    'consultas-2@viviendasyparticulares.com',
    'consultas-3@viviendasyparticulares.com',
    'consultas-4@viviendasyparticulares.com',
    'consultas-5@viviendasyparticulares.com',
    'consultas-6@viviendasyparticulares.com',
    'consultas-7@viviendasyparticulares.com',
    'consultas-8@viviendasyparticulares.com',
    'consultas-9@viviendasyparticulares.com',
    'consultas-10@viviendasyparticulares.com',
    'contacto-1@viviendasyparticulares.com',
    'contacto-2@viviendasyparticulares.com',
    'contacto-3@viviendasyparticulares.com',
    'contacto-4@viviendasyparticulares.com',
    'contacto-5@viviendasyparticulares.com',
    'contacto-6@viviendasyparticulares.com',
    'contacto-7@viviendasyparticulares.com',
    'contacto-8@viviendasyparticulares.com',
    'contacto-9@viviendasyparticulares.com',
    'contacto-10@viviendasyparticulares.com'
]

def create_folder_if_not_exists(path: str):
    if os.path.splitext(path)[1]:  # Si tiene una extensión, es un archivo
        folder_path = os.path.dirname(path)
    else:  # Si no tiene extensión, es un directorio
        folder_path = path

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return path

def resource_path(relative_path: str):
    """
    Get the absolute path to a resource, works for both development and PyInstaller.
    Args:
        relative_path (str): The relative path to the resource file.
    Returns:
        str: The absolute path to the resource file.
    """
    if hasattr(sys, '_MEIPASS'):   
        return os.path.join(sys._MEIPASS, relative_path)  # PyInstaller: The resource is inside the temporary folder _MEIPASS
    return os.path.join(os.path.abspath("."), relative_path) # Manual execution: The resource is in the current directory or its relative path

def delete_files_in_folder(folder_path: str) -> tuple[str, bool]:
    try:
        exclude_files = [".gitkeep"]

        if not os.path.exists(folder_path):
            return f"La carpeta {folder_path} no existe.", False

        has_files = False

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if filename in exclude_files:
                continue

            if os.path.isfile(file_path):
                has_files = True
                os.remove(file_path)

        if has_files:
            return "Todos los archivos fueron borrados exitosamente.", True
        else:
            return "No hay archivos para borrar en la carpeta.", False

    except Exception as e:
        return f"Error al eliminar archivos: {e}", False

def monitor_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    net_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    
    return cpu_usage, memory_usage

def get_file_extension(file_name: str) -> str:
    """
    Dado el nombre de un archivo, regresa la extensión del archivo.
    
    Args:
    file_name (str): El nombre o ruta del archivo.
    
    Returns:
    str: La extensión del archivo (incluyendo el punto) o una cadena vacía si no tiene extensión.
    """
    return pathlib.Path(file_name).suffix

def printr(message):
    """
    Imprime un mensaje en la consola con un prefijo que incluye la fecha y hora actual en el formato `YYYY-MM-DD HH:MM:SS`.

    Parámetros:
    - message (str): El mensaje que se desea imprimir.

    Ejemplo de uso:
    >>> printr("Este es un mensaje de prueba")
    [2024-08-08 12:34:56] Este es un mensaje de prueba
    """
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def getDefaultMessageByAdvertiser(advertiser: str, message_short: bool = False) -> str:
    try:
        advertiser = advertiser.lower()
        with open('data.json', 'r', encoding='utf-8') as f:
            messages = json.load(f)
    except FileNotFoundError:
        print("Error: data.json file not found.")
        return ""
    except json.JSONDecodeError:
        print("Error: Failed to decode the JSON file.")
        return ""
    
    if message_short:
        message = messages["message_short"].get(advertiser)
    else:
        message = messages["message"].get(advertiser)
    
    if not message:
        print(f"Advertiser '{advertiser}' not found in messages.")
        return ""

    return message

def convert_emojis_to_unicode(message: str) -> str:
    return emoji.demojize(message)

def set_executable_permission(file_path):
    """
    Cambia los permisos de un archivo para que sea ejecutable.
    
    :param file_path: Ruta del archivo al que se le cambiarán los permisos.
    """
    try:
        os.chmod(file_path, 0o755)  # Permisos de ejecución para el propietario, lectura/ejecución para otros
        return f"Permisos de ejecución añadidos correctamente a {file_path}"
    except FileNotFoundError:
        return f"El archivo {file_path} no existe."
    except PermissionError:
        return f"Permiso denegado al cambiar los permisos de {file_path}."
    except Exception as e:
        return f"Ocurrió un error: {e}"
    
def selenium_base_test(bot: str):
    try:
        from seleniumbase import Driver
        
        driver = Driver(uc=True)
        driver.uc_open_with_reconnect('https://www.google.com/', 2)
        driver.save_screenshot(resource_path(f"assets/test_screen_{bot}.png"))
        driver.quit()
    except Exception as e:
        print(e)

def handle_email_sequence(catch_all_emails, index_file):
    """Carga el índice, selecciona el siguiente correo, actualiza el índice y lo guarda."""
    
    # Verificar si la lista de correos está vacía
    if not catch_all_emails:
        raise ValueError("La lista de correos está vacía.")
    
    current_index = 0
    # Verificar si el archivo del índice existe
    if os.path.exists(index_file):
        try:
            with open(index_file, 'r') as f:
                current_index = int(f.read().strip())
                if current_index < 0 or current_index >= len(catch_all_emails):
                    print(f"Índice fuera de rango: {current_index}. Reiniciando a 0.")
                    current_index = 0
        except (ValueError, IOError) as e:
            print(f"Error al leer el índice. Detalles: {e}. Reiniciando a 0.")
            current_index = 0  # Reinicia el índice si hay algún error

    # Obtener el siguiente correo
    try:
        email = catch_all_emails[current_index]
        print(f"Enviando correo a: {email}")
    except IndexError as e:
        print(f"Error: índice fuera de rango {current_index} para la lista de correos.")
        raise e

    # Incrementar el índice de manera circular
    next_index = (current_index + 1) % len(catch_all_emails)
    try:
        with open(index_file, 'w') as f:
            f.write(str(next_index))
            print(f"Índice actualizado: {next_index}")
    except IOError as e:
        print(f"Error al guardar el índice: {e}")

    return email

def generate_spanish_phone_number():
    prefix = "91" # El prefijo "91" corresponde a números fijos de Madrid

    # Generar los 7 dígitos restantes de forma aleatoria
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"{prefix}{number}"

def generate_complex_gmail_aliases(email, max_aliases=100):
    # Separar el nombre de usuario y el dominio
    username, domain = email.split('@')

    # Lista para almacenar los alias
    aliases = set()

    # Generar alias usando puntos en diferentes posiciones
    for i in range(1, len(username)):
        alias_with_dot = username[:i] + '.' + username[i:]
        aliases.add(f"{alias_with_dot}@{domain}")

    # Generar alias usando el signo "+" con sufijos aleatorios (combinación de letras y números)
    for i in range(1, max_aliases + 1):
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        alias_with_plus = f"{username}+{random_suffix}@{domain}"
        aliases.add(alias_with_plus)

    # Generar alias combinando puntos y "+" para mayor complejidad
    for i in range(1, len(username)):
        alias_with_dot_plus = username[:i] + '.' + username[i:] + f"+{random_suffix}@{domain}"
        aliases.add(alias_with_dot_plus)

    return list(aliases)