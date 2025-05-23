#!/usr/bin/env bash


#
#   A R C  - Z E N          Rofi - App as root         THEME v.0.1
#
#   Author:  ArcZen >_ enos muthiani
#
#
#   Date:    23.07.24
#

source "$HOME"/.config/rofi/applets/shared/theme.bash
theme="$type/$style"


# Theme Elements
prompt='Applications'
mesg='Run App as Root'

	list_col='1'
	list_row='6'
	win_width='120px'

# Options
layout=`cat ${theme} | grep 'USE_ICON' | cut -d'=' -f2`
if [[ "$layout" == 'NO' ]]; then
	option_1=" Alacritty"
	option_2=" Thunar"
	option_3=" Geany"
	option_4=" Ranger"
	option_5=" Vim"
else
	option_1=""
	option_2=""
	option_3=""
	option_4=""
	option_5=""
fi

# Rofi CMD
rofi_cmd() {
	rofi -theme-str "window {width: $win_width;}" \
		-theme-str "listview {columns: $list_col; lines: $list_row;}" \
		-theme-str 'textbox-prompt-colon {str: "";}' \
		-dmenu \
		-p "$prompt" \
		-mesg "$mesg" \
		-markup-rows \
		-theme ${theme}
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$option_1\n$option_2\n$option_3\n$option_4\n$option_5" | rofi_cmd
}

# Execute Command
run_cmd() {
	polkit_cmd="pkexec env PATH=$PATH DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY"
	if [[ "$1" == '--opt1' ]]; then
		${polkit_cmd} alacritty
	elif [[ "$1" == '--opt2' ]]; then
		${polkit_cmd} dbus-run-session thunar
	elif [[ "$1" == '--opt3' ]]; then
		${polkit_cmd} geany
	elif [[ "$1" == '--opt4' ]]; then
		${polkit_cmd} alacritty -e ranger
	elif [[ "$1" == '--opt5' ]]; then
		${polkit_cmd} alacritty -e vim
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $option_1)
		run_cmd --opt1
        ;;
    $option_2)
		run_cmd --opt2
        ;;
    $option_3)
		run_cmd --opt3
        ;;
    $option_4)
		run_cmd --opt4
        ;;
    $option_5)
		run_cmd --opt5
        ;;
esac
