from ignis.widgets import Widget
from ignis.app import IgnisApp
from .volume import volume_control
from .quick_settings import quick_settings
from .user import user
from .media import media
from .notification_center import notification_center
from .brightness import brightness_slider
from .tray import tray
from datetime import date
import psutil
from ignis.services.system_tray import SystemTrayService

app = IgnisApp.get_default()

def get_label(percent) -> str:
    if percent > 75.0:
        return "● "
    if percent > 50.0: 
        return "◕ "
    if percent > 25.0: 
        return "◑ "
    if percent > 10.0:
        return "◔ "
    return "○ "


#ef cpu() -

def info() -> Widget.Box:
    return Widget.Box(
        vertical = False,
        halign = "center",
        vexpand = True,
        child = [
 #           Widget.
            Widget.Picture(
                image='/home/kuba/Muzyka/cpu/cpu6.png',
                width=70,
                height=70
            ),
            Widget.Picture(
                image='/home/kuba/Muzyka/ram/ram6.png',
                width=70,
                height=70
            )
            #Widget.Icon(image="cpufreq-icon", pixel_size=20),
            #Widget.Label(label = " ram: " + get_label(psutil.virtual_memory().percent)),
            #Widget.Label(label = " net: " + get_label(60)),
            # When on laptop comment the first line and uncomment the second
            #Widget.Label(label = " battery: " + get_label(100))
            #Widget.Label(label = "battery: " + str(psutil.sensors_battery().percent) + "%")
        ]
    )

def calendar() -> Widget.Box:
    day = date.today().strftime("%d/%m/%Y").split("/")
    return Widget.Box(
        vertical = True,
        css_classes = ["calendar"],
        child = [
            Widget.Calendar(
                day=int(day[0]) - 8,
                month=int(day[1]) - 1,
                year=int(day[2])
                ),
        ]
    )


def control_center_widget() -> Widget.Box:
    return Widget.Box(
        vertical=True,
        css_classes=["control-center"],
        child=[
            Widget.Box(
                vertical=True,
                css_classes=["control-center-widget"],
                child=[
                    media(),
                    quick_settings(),
                    volume_control(),
                    brightness_slider(),
                    tray(),
                    info(),
                    user(),
                    calendar(),    
                    

                ],
            ),
            notification_center(),
        ],
    )



def control_center() -> Widget.RevealerWindow:
    revealer = Widget.Revealer(
        transition_type="slide_left",
        child=control_center_widget(),
        transition_duration=300,
        reveal_child=True,
    )
    box = Widget.Box(
        child=[
            Widget.Button(
                vexpand=True,
                hexpand=True,
                css_classes=["unset"],
                on_click=lambda x: app.close_window("ignis_CONTROL_CENTER"),
            ),
            revealer,
        ],
    )
    return Widget.RevealerWindow(
        visible=False,
        popup=True,
        kb_mode="on_demand",
        layer="top",
        css_classes=["unset"],
        anchor=["top", "right", "bottom", "left"],
        namespace="ignis_CONTROL_CENTER",
        child=box,
        revealer=revealer,
    )
