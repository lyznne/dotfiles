# ~/.config/qtile/minimal_config.py

from libqtile import layout, bar, widget
from libqtile.config import Screen
from libqtile import hook

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            ],
            24,
        ),
    ),
]

layouts = [layout.Max(), layout.Stack(num_stacks=2)]


@hook.subscribe.startup_once
def start_once():
    import subprocess

    subprocess.call(["xterm"])


# ~/.config/qtile/minimal_config.py

from libqtile import layout, bar, widget
from libqtile.config import Screen
from libqtile import hook

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            24,
        ),
    ),
]

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

@hook.subscribe.startup_once
def start_once():
    import subprocess
    subprocess.call(['xterm'])
# ~/.config/qtile/minimal_config.py

from libqtile import layout, bar, widget
from libqtile.config import Screen
from libqtile import hook

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            24,
        ),
    ),
]

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

@hook.subscribe.startup_once
def start_once():
    import subprocess
    subprocess.call(['xterm'])


