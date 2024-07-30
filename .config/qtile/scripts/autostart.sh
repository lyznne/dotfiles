#!/bin/bash 

echo("Qtile Running ....")
echo("")
function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# Set Wallapapers 
feh --bg-fill ~/Pictures/wallpapers/backiee-293452-landscape.jpg & 

# start <> fot cheatsheet.

#start sxhkd to replace Qtile native key-bindings
run sxhkd -c ~/Rice/dotfiles/.config/qtile/sxhkd/sxhkdrc &



#starting utility applications at boot time
run nm-applet &
#run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
# picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

#starting user applications at boot time
run volumeicon &