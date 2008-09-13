#!/bin/sh


tema=`/usr/bin/gconftool-2 --get /desktop/gnome/interface/gtk_theme`
#/usr/bin/gconftool-2 --type string --set /desktop/gnome/interface/gtk_theme "Default"
/usr/bin/gconftool-2 --unset /desktop/gnome/interface/gtk_theme
/usr/bin/gconftool-2 --type string --set /desktop/gnome/interface/gtk_theme $tema
