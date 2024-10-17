#
#  A R C  - Z E N          Qtile        config v.1.0
#
#   Author:  ArcZen >_ enos muthiani
#
#
#   Date:    28.07.24
#


#  █████╗     ██████╗      ██████╗              ███████╗    ███████╗    ███╗   ██╗
# ██╔══██╗    ██╔══██╗    ██╔════╝    ▄ ██╗▄    ╚══███╔╝    ██╔════╝    ████╗  ██║
# ███████║    ██████╔╝    ██║          ████╗      ███╔╝     █████╗      ██╔██╗ ██║
# ██╔══██║    ██╔══██╗    ██║         ▀╚██╔▀     ███╔╝      ██╔══╝      ██║╚██╗██║
# ██║  ██║    ██║  ██║    ╚██████╗      ╚═╝     ███████╗    ███████╗    ██║ ╚████║
# ╚═╝  ╚═╝    ╚═╝  ╚═╝     ╚═════╝              ╚══════╝    ╚══════╝    ╚═╝  ╚═══╝


import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.widget import Spacer, backlight
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from typing import List, Union

from libqtile import hook

# Import theme `arczen`
from theme.arczen import init_colors


# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"

home: str = os.path.expanduser("~")
terminal: str = guess_terminal() or "Alacritty"
browser: str = "firefox"


# D E F  - COLORS
BORDER_COLOR: str = "#020D181A"
ACTIVE_BORDER_COLOR: str = "#0B1D28"

# D E F  - FONT
MAIN_FONT: str = "0xProto Nerd Font Mono"


# Sticky windows
sticky_windows = []


@lazy.function
def toggle_sticky_windows(qtile, window=None):
    if window is None:
        window = qtile.current_screen.group.current_window
    if window in sticky_windows:
        sticky_windows.remove(window)
    else:
        sticky_windows.append(window)
    return window


@hook.subscribe.setgroup
def move_sticky_windows():
    for window in sticky_windows:
        window.togroup()
    return


@hook.subscribe.client_killed
def remove_sticky_windows(window):
    if window in sticky_windows:
        sticky_windows.remove(window)


# Below is an example how to make Firefox Picture-in-Picture windows automatically sticky.
@hook.subscribe.client_managed
def auto_sticky_windows(window):
    info = window.info()
    if (
        info["wm_class"] == ["Toolkit", "firefox"]
        and info["name"] == "Picture-in-Picture"
    ):
        sticky_windows.append(window)


# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█


# K E Y S - Keybindings in sxhkd file  plus these
keys = [
    # D E F A U L T S
    # -------------------------- Basics ---------------------------------------- #
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Full Screen mode"),
    Key([mod], "q", lazy.window.kill(), desc="Quit Application"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Quit Application"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    # -------------------------- Qtile layout ---------------------------------------- #
    Key([mod], "n", lazy.layout.normalize(), desc="Normalize Current Layout"),
    Key([mod], "space", lazy.next_layout(), desc="Change Layouts"),
    # -------------------------- Workspace Controls ---------------------------------------- #
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in the current stack pane"),
    Key(
        [mod],
        "Down",
        lazy.layout.down(),
        desc="Move focus down in the current stack pane",
    ),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to the left active window"),
    Key(
        [mod],
        "Right",
        lazy.layout.right(),
        desc="Move focus to the right active window",
    ),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to the left active window"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to the right active window"),
    # -------------------------- Window Controls ---------------------------------------- #
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Resize windows to Right",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Resize windows to Right",
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Resize windows to left",
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Resize windows to left",
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Resize windows to Upper Screen",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Resize windows to lower Screen",
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Resize windows to Upper Screen",
    ),
    # -------------------------- Layout Actions ---------------------------------------- #
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key(
        [mod, "shift"],
        "f",
        lazy.layout.flip(),
        desc="Flip the current layout (MonadTall/MonadWide)",
    ),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up(), desc="Flip the BSP layout up"),
    Key([mod, "mod1"], "j", lazy.layout.flip_down(), desc="Flip the BSP layout down"),
    Key([mod, "mod1"], "l", lazy.layout.flip_right(), desc="Flip the BSP layout right"),
    Key([mod, "mod1"], "h", lazy.layout.flip_left(), desc="Flip the BSP layout left"),
    # -------------------------- BSP Window Action ---------------------------------------- #
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move window up in BSP layout",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down in BSP layout",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window left in BSP layout",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window right in BSP layout",
    ),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key(
        [mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up in MonadTall/MonadWide layout",
    ),
    Key(
        [mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down in MonadTall/MonadWide layout",
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.swap_left(),
        desc="Move window left in MonadTall/MonadWide layout",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.swap_right(),
        desc="Move window right in MonadTall/MonadWide layout",
    ),
    # -------------------------- Floating Layout ---------------------------------------- #
    Key(
        [mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle floating layout for focused window",
    ),
    # C U S T O M
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"),
        desc="brightness UP",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"),
        desc="brightness Down",
    ),
    # P O W E R M E N U
    Key(
        [mod],
        "p",
        lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/powermenu.sh")),
        desc="Is to Display powermenu",
    ),
]


# Key functions
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen is True:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen is True:
            qtile.cmd_to_screen(i + 1)


keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key(
        [mod, "shift"],
        "Right",
        lazy.function(window_to_next_screen, switch_screen=True),
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.function(window_to_previous_screen, switch_screen=True),
    ),
])

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

# FOR QWERTY KEYBOARDS
group_names: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# groups = [
#     Group(f"{i + 1}", label="󰏃") for i in range(9)
# ]
groups = [Group(f"{i + 1}", label="⬡") for i in range(9)]

# groups = [Group(f"{i + 1}", label="") for i in range(8)]

for i in groups:
    keys.extend([
        Key(
            [mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name),
        ),
        Key(
            [mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name),
        ),
    ])


def init_layout_theme():
    return {
        "margin": 2,
        "border_width": 1,
        "border_focus": ACTIVE_BORDER_COLOR,
        "border_normal": BORDER_COLOR,
    }


###𝙇𝙖𝙮𝙤𝙪𝙩###

layout_theme = init_layout_theme()


layouts = [
    # layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
]

# C O L O R S
colors = init_colors()


# W I D G E T S
# -------------------------- Default Widgets Conf ---------------------------------------- #
def init_widgets_defaults() -> dict[str, str | int | List[str]]:
    return dict(font=MAIN_FONT, fontsize=12, padding=3, background="#033C4B")


widget_defaults = init_widgets_defaults()


extension_defaults = [widget_defaults.copy()]


def open_launcher() -> None:
    qtile.cmd_spawn(
        "rofi -no-config -no-lazy-grab -show drun  -theme ~/.config/rofi/launcher.rasi"
    )


def open_btop() -> None:
    qtile.cmd_spawn("alacritty --hold -e btop")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=14,
                    background="#033C4B",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/launch_Icon.png",
                    background="#033C4B",
                    mouse_callbacks={"Button1": open_launcher},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                ),

                widget.GroupBox(
                    fontsize=16,
                    borderwidth=0,
                    highlight_method="text",
                    active="#C274B1C2",
                    block_highlight_text_color="#BD2606",
                    highlight_color="#BD2606",
                    inactive="#C9D1FF12",
                    foreground="#C9D1FF19",
                    background="#046F5F",
                    this_current_screen_border="#BD2606",
                    this_screen_border="#BD2606",
                    other_current_screen_border="0A427F52",
                    other_screen_border="0A427F52",
                    urgent_border="#52548D",
                    rounded=True,
                    disable_drag=True,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=["~/.config/qtile/Assets/layout"],
                    background="#046F5F",
                    padding=4,
                    scale=0.55,
                ),
                widget.CurrentLayout(
                    background="#046F5F",
                    foreground="#C9D1FF",
                    font=MAIN_FONT,
                    fontsize=15,
                    padding=2,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.WindowName(
                    background="#046F5F",
                    foreground="#C9D1FF",
                    format=" {name}",
                    font=MAIN_FONT,
                    fontsize=14,
                    empty_group_string="  A R C * Z E N",
                    padding=0,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/1.png",
                    background="#52548D",
                ),
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/cpu.png",
                    background="#046F5F",
                    margin_y=4,
                ),
                widget.CPU(
                    font=MAIN_FONT,
                    format=" {load_percent:.1f}%  {freq_current}GHz",
                    fontsize=15,
                    margin=0,
                    padding=0,
                    background="#046F5F",
                    foreground="#C9D1FF1A",
                    mouse_callbacks={"Button1": open_btop},
                ),
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/2.png",
                    background="#52548D",
                ),
                widget.Systray(
                    background="#046F5F",
                    icon_size=24,
                    padding=3,
                    foreground="#C9D1FF",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                    background="#52548D",
                ),
                widget.Spacer(
                    length=0,
                    background="#046f5f",
                ),
                # RAM
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/misc/ram.png",
                    background="#046F5F",
                ),
                widget.Memory(
                    format="{MemUsed:.0f}MB  {MemTotal:.0f}MB",
                    font=MAIN_FONT,
                    fontsize=15,
                    padding=0,
                    background="#046F5F",
                    mouse_callbacks={"Button1": open_btop},
                    foreground="#ff7f17",
                ),
                widget.Spacer(
                    length=6,
                    background="#046f5f",
                ),
                # volume
                widget.Volume(
                    theme_path="/home/enos/.config/qtile/Assets/Volume/",
                    emoji=True,
                    background="#046F5F",
                ),
                widget.Spacer(
                    length=3,
                    background="#046f5f",
                ),
                widget.PulseVolume(
                    font=MAIN_FONT,
                    fontsize=15,
                    padding=0,
                    background="#046F5F",
                    foreground="#C9D1FF1A",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/1.png",
                    background="#4B427E",
                ),
                # battery
                widget.BatteryIcon(
                    theme_path="/home/enos/.config/qtile/Assets/Battery/",
                    update_interval=60,
                    background="#046F5F",
                ),
                widget.Battery(
                    fontsize=15,
                    background="#046F5F",
                    foreground="#D0A1D4",
                    format="{percent:2.0%}",
                    low_percentage=0.2,
                    low_foreground="#DC143C",
                    notify_below=0.2,
                ),
                widget.Spacer(
                    length=6,
                    background="#046f5f",
                ),
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/Bar-Icons/calendar.png",
                    background="#046F5F",
                    margin_y=3,
                    scale=True,
                ),
                widget.Spacer(
                    length=6,
                    background="#046f5f",
                ),
                widget.Clock(
                    format="%d-%m-%y ",
                    background="#046f5f",
                    font=MAIN_FONT,
                    fontsize=15,
                    padding=0,
                    foreground="#B1C6D8",
                ),
                widget.Image(
                    filename="/home/enos/.config/qtile/Assets/misc/clock.png",
                    background="#046F5F",
                    margin_y=3,
                    margin_x=5,
                    scale=True,
                ),
                widget.Clock(
                    format="%H:%M",
                    background="#046f5f",
                    foreground="#C9D1FF1A",
                    font=MAIN_FONT,
                    fontsize=15,
                    padding=0,
                ),
                widget.Spacer(
                    length=18,
                    background="#046f5f",
                ),
            ],
            30,  # Bar size (all axis)
            margin=[0, 8, 6, 8],  # Bar margin (Top,Right,Bottom,Left)
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False  # This basically puts your mouse in the center on the screen after you switch to another workspace
floating_layout = layout.Floating(
    border_focus="#00DC6C",
    border_normal="#1F1D2E",
    border_width=3,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)


# stuffrofi"
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(
        "/home/enos/.config/qtile/scripts/autostart.sh"
    )  # path to my script, under my user directory
    subprocess.call([home])


auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
