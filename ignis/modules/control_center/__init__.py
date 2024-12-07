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

def img(typ, pr):
    pro = 0
    if pr < 15:
        pro = 0
    if pr < 25:
        pro = 15
    if pr < 35:
        pro = 25
    if pr < 50:
        pro = 35
    if pr < 65:
        pro = 50
    if pr < 75:
        pro = 65
    if pr < 85:
        pro = 75
    if pr < 100:
        pro = 85
    if pr > 99:
        pro = 100
    # replace kuba with your username
    stri = "/home/kuba/.config/ignis/modules/control_center/" + typ + "/" + str(pro) + ".png"
    return Widget.Picture(
    image = stri,
    width=100,
    height=100
    )

def info() -> Widget.Box:
    return Widget.Box(
        vertical = False,
        halign = "center",
        vexpand = True,
        child = [
            img("cpu", psutil.cpu_percent()),
            img("ram", psutil.virtual_memory().percent),
            img("bat", 100)
            #img("bat", str(psutil.sensors_battery().percent))
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
