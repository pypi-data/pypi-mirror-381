#!/bin/bash

# This function simplifies setting up Gnome 3 shortcuts from terminal

# $1       name of the shortcut
# $2       command to execute
# $3       keyboard shortcut

# src: https://askubuntu.com/a/597414/279745 and https://gitlab.com/tukusejssirs/lnx_scripts/-/blob/master/bash/functions/gshort.sh

# TODO
# - before shortcut creation, check if:
#   - the shortcut is not used already in custom shortcuts;
#   - the command is not used already in custom shortcuts;
# - sometimes is uses the very same $num multiple times;


gshort(){
    set -o errexit
	local name="$1"
	local command="$2"
	local shortcut="$3"
	local value test value_new
	value="$(gsettings get org.gnome.settings-daemon.plugins.media-keys custom-keybindings)"
	test="$(sed "s/\['//;s/', '/,/g;s/'\]//" <<< "$value" | tr ',' '\n' | grep -oP ".*/custom\K[0-9]*(?=/$)")"

	if [ "$(echo "$value" | grep -o "@as")" = "@as" ]; then
		local num=0
		value_new="['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom${num}/']"
	else
		local i=1

		until [ "$num" != "" ]; do
			if [ "$(grep -o $i <<< "$test")" != "$i" ]; then
				local num=$i
			fi
			i="$(echo 1+$i | bc)";
		done

		value_new="$(gsettings get org.gnome.settings-daemon.plugins.media-keys custom-keybindings | sed "s#']\$#', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom${num}/']#")"
	fi

    echo setting custom-keybinding ${num} to ${command} with ${shortcut}

	gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "$value_new"
	gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom${num}/ name "$name"
	gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom${num}/ command "$command"
	gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom${num}/ binding "$shortcut"
}

gshort $1 $2 $3