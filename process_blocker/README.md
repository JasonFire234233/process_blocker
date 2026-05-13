# process_blocker
# FocusGuard 🛡️

Un bloqueador de aplicaciones ligero y configurable para Windows.
Diseñado como alternativa gratuita y open source a Cold Turkey y Freedom.

## ¿Qué hace?

FocusGuard corre en segundo plano y cierra automáticamente las aplicaciones
que tu definas, ayudándote a mantener el foco mientras trabájas o estudias.

- ✅ Ligero: menos de 15 MB de RAM
- ✅ Configurable: editá un archivo JSON para agregar o quitar apps
- ✅ Sin telemetría, sin cuentas, sin suscripciones

## Requisitos

- Windows 10 o superior
- Python 3.10 o superior

## Instalación

1. Clone el repositorio:
   git clone https://github.com/JasonFire234233/process_blocker.git
   cd BloqueadorApps/process_blocker

2. Creá un entorno virtual e instalá dependencias:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

## Configuración

Edite `config.json` para definir qué apps bloquear y cada cuántos segundos revisar:

{
    "blocked_apps": [
        "spotify.exe",
        "discord.exe"
    ],
    "check_interval": 30
}

Para encontrar el nombre exacto de un proceso, abrí el Administrador de tareas
(Ctrl + Shift + Esc) → pestaña "Detalles".

## Uso

Con el entorno virtual activado:

   python main.py

Para detenerlo: Ctrl + C

## Licencia

MIT — libre para usar, modificar y distribuir.

## Donaciones

Si este proyecto te resulta útil y querés apoyarlo, podés invitarme un café:
[☕ Buy Me a Coffee](https://buymeacoffee.com)

Este proyecto es y será siempre gratuito.