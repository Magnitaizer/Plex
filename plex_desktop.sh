#!/bin/sh

sudo passwd -d $USER
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt install python3-pip snapd -y

sudo snap install plex-htpc

pip install pynput

git clone https://github.com/Magnitaizer/Plex.git

if grep -q 'AutomaticLogin = plex' "/etc/gdm3/custom.conf"; then
  echo 'skipping this part...'
else
  sudo sed -i --follow-symlinks "s+AutomaticLogin+AutomaticLogin = plex+g" /etc/gdm3/custom.conf
  sudo sed -i --follow-symlinks "s+AutomaticLoginEnable+AutomaticLoginEnable = true+g" /etc/gdm3/custom.conf
fi

cp /home/$USER/Plex/plex-htpc.desktop     /home/$USER/.config/autostart/
cp /home/$USER/Plex/pycontrol.desktop /home/$USER/.config/autostart/
