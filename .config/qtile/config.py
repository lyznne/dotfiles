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


# Imports
import os, socket, subprocess, re
from libqtile import qtile, layout, bar, widget, hook
from libqtile.config import Key, Match, Group, Screen, Drag


from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List, Union

# Import Theme
from themes.arczen import init_colors


# D E F
mod = "mod4"  # super / Win Key
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")
# terminal = guess_terminal()
terminal: str = "Alacritty"
browser = "brave"

# D E F  - COLORS
BORDER_COLOR: str = "#020D181A"
ACTIVE_BORDER_COLOR: str = "#020D19"
# D E F  - FONT
MAIN_FONT: str = "0xProto Nerd Font Mono"

PROMPT: str = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


# F U C T I O N S
def run_command():
    qtile.cmd_spawm("rofi -show drun")


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
]


# Key functions
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)


keys.extend(
    [
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
    ]
)


# FOR QWERTY KEYBOARDS
group_names: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ""]
# G R O U P S
groups = []
groups = [Group(f"{i+1}", label="󰏃") for i in range(len(group_names))]


# L A Y O U T S
def init_layout_theme() -> dict[str, Union[int, str]]:
    return {
        "border_width": 2,
        "margin": 8,
        "border_focus": ACTIVE_BORDER_COLOR,
        "border_normal": BORDER_COLOR,
    }


layout_theme = init_layout_theme()

layouts = [
    # layout.MonadTall(margin=8, border_width=2, border_focus=ACTIVE_BORDER_COLOR, border_normal=BORDER_COLOR),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(margin=8, border_width=2, border_focus=ACTIVE_BORDER_COLOR, border_normal="BORDER_COLOR),
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
def init_widgets_defaults():
    return dict(
        font=MAIN_FONT,
        fontsize=10,
        padding=3,
    )


widget_defaults = init_widgets_defaults()


# -------------------------- Bar Widgets ---------------------------------------- #
def init_bar_widgets():
    widgets_list = [
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
        widget.TextBox(
            text="  ",
            font=MAIN_FONT,
            fontsize="18",
            background=colors[6],
            foreground=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun -modi drun")
            },
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[6],
            foreground=colors[0],
        ),
        widget.GroupBox(
            font="Ubuntu Nerd Font",
            fontsize=16,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[3],
            highlight_method="block",
            this_current_screen_border=colors[6],
            block_highlight_text_color=colors[0],
        ),
        widget.Prompt(
            background=colors[2],
            foreground=colors[0],
            font="Iosevka Nerd Font",
            fontsize=18,
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize=33,
            padding=0,
            background=colors[0],
            foreground=colors[2],
        ),
        widget.WindowName(
            font="Iosevka Nerd Font",
            fontsize=15,
            background=colors[2],
            foreground=colors[0],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[2],
            foreground=colors[0],
        ),
        widget.Spacer(length=200),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[0],
            foreground=colors[9],
        ),
    ]
    return widgets_list


widgets_list = init_bar_widgets()
# S C R E E N S


def init_widgets_screen1():
    widgets_screen1 = init_bar_widgets()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_bar_widgets()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

# -------------------------- Spawn bar at multiple screens.---------------------------------------- #


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=26,
                opacity=0.7,
                margin=[8, 8, 0, 8],
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen2(),
                size=26,
                opacity=0.7,
                margin=[8, 8, 0, 8],
            )
        ),
    ]


screens = init_screens()

# M O U S E

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

# mouse = [
#     Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
#     Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
#     Click("M-2", lazy.window.bring_to_front()),
# ]

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
dgroups_key_binder = None
dgroups_app_rules = []


main = None


# hides the top bar when the archlinux-logout widget is opened
@hook.subscribe.client_new
def new_client(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


# shows the top bar when the archlinux-logout widget is closed
@hook.subscribe.client_killed
def logout_killed(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/Rice/dotfiles/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


# Floating Applications
floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus: bool = True
bring_front_click: bool = False
cursor_warp: bool = False


# Floating rules
floating_layout = layout.Floating(
    float_rules=[
        # +tip , Run the utility `xprop` to see the WM class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(wm_class="archlinux-logout"),
        Match(wm_class="xfce4-terminal"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)

focus_on_window_activation: str = "focus"  # or focus
auto_fullscreen: bool = True
wmname: str = "LG3D"
