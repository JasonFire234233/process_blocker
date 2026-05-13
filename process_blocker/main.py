import json
import time
import sys
from process_utils import kill_process


def load_config(path: str = "config.json") -> dict:
    """Lee la configuración desde un archivo JSON."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: no se encontró '{path}'.")
        print("Asegurate de que config.json existe en la misma carpeta.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: '{path}' tiene un formato JSON inválido.")
        print(f"Detalle: {e}")
        sys.exit(1)


def run_blocker():
    """Loop principal: revisa y bloquea procesos continuamente."""
    print("FocusGuard iniciado. Presioná Ctrl+C para detener.")

    try:
        while True:
            config = load_config()
            blocked = config.get("blocked_apps", [])
            interval = config.get("check_interval", 30)

            for app in blocked:
                if kill_process(app):
                    print(f"Bloqueado: {app}")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nFocusGuard detenido.")
        sys.exit(0)


if __name__ == "__main__":
    run_blocker()