import psutil


def find_process(process_name: str) -> bool:
    """
    Busca si un proceso está corriendo por nombre.
    Retorna True si lo encuentra, False si no.

    process_name: nombre del ejecutable, ej: "spotify.exe"
    """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


def kill_process(process_name: str) -> bool:
    """
    Busca un proceso por nombre y lo termina.
    Retorna True si lo mató, False si no lo encontró.

    process_name: nombre del ejecutable, ej: "spotify.exe"
    """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                proc.kill()
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


if __name__ == "__main__":
    resultado = kill_process("notepad.exe")
    if resultado:
        print("Proceso terminado.")
    else:
        print("Proceso no encontrado.")