from .qs_button import QSButton
from ignis.services.notifications import NotificationService
import psutil

notifications = NotificationService.get_default()
#is_saving_active = False

def dnd_button() -> QSButton:
    return QSButton(
        label=notifications.bind("dnd", lambda value: "Do not disturb on " if value else "Do not disturb off"),
        icon_name=notifications.bind(
            "dnd",
            transform=lambda value: "battery-profile-performance"
            if value
            else "notification-symbolic",
        ),
        on_activate=lambda x: notifications.set_dnd(not notifications.dnd),
        on_deactivate=lambda x: notifications.set_dnd(not notifications.dnd),
        active=notifications.bind("dnd"),
    )

def process_status(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def powerman() -> QSButton:
    return QSButton(
    label="Power Saving",
    icon_name="battery-profile-powersave",
    on_activate=lambda x: system.os("your activation command"),
    on_deactivate=lambda x: system.os("your deactivation command"),
    active = process_status("your command name in top")
    )