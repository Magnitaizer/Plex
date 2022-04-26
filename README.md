# Plex installation
This script is initializing plex-media-player from AUR repository and uses your pc as plex media player without window manager getting started!
+ 1.Download https://osdn.net/projects/arch-linux-gui/downloads/77102/archlinux-gui-i3-2022.04-x86_64.iso/  and install it on your device
+ 2.After loading open a terminal and execute bash<(curl -L raw.githubusercontent.com/Magnitaizer/Plex/main/install.sh)
+ 3.To control this plex client via tcp client connect to machine_ip:5000 which you can see by pressing I button ,when Plex is loaded
+ 4.Enjoy!

P.S. if you have no sound, than you have to run 
aplay -l
and then change your card and devices parameters to audio device which you want to use in /etc/asound.conf
