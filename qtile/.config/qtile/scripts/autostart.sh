#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# Set Wallapapers
# feh --bg-fill $HOME/.config/qtile/Wallpaper/Skyscraper.png &
# feh  --bg-fill $HOME/Pictures/wallpapers/4k-Fiery-Meteor-Shower-4K-Wallpaper.jpg &   
feh --bg-fill $HOME/Pictures/wallpapers/Imgur.png &

# start <> fot cheatsheet.

#start sxhkd to replace Qtile native key-bindings
run sxhkd -c ~/.config/sxhkd/sxhkdrc


#starting utility applications at boot time
run nm-applet &

# picom --config $HOME/.config/qtile/scripts/picom.conf &
picom --daemon --config $HOME/.config/picom/picom.conf &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/wired &
eval $(gnome-keyring-daemon --start)

#starting user applications at boot time
# run volumeicon &

# restart the layout using xrandr
