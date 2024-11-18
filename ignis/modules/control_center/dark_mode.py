from services.material import MaterialService
from .qs_button import QSButton

material = MaterialService.get_default()


def dark_mode_button() -> QSButton:
    return QSButton(
        label="Power saving mode",
        icon_name="battery-profile-performance",
        #on_activate=lambda x: material.set_dark_mode(True),
        #on_deactivate=lambda x: material.set_dark_mode(False),
        #active=material.bind("dark-mode"),
    )
