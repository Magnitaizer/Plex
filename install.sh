#!/bin/sh

git clone https://github.com/Magnitaizer/Plex.git /home/$USER/Plex

sudo pacman -S base-devel python-pip flatpak unclutter libva-intel-driver --noconfirm
sudo pacman -R orca --noconfirm
sudo pacman -Syu  --noconfirm

pip install pynput

flatpak install flathub tv.plex.PlexHTPC -y

sudo sed -i 's+GRUB_TIMEOUT=5+GRUB_TIMEOUT=0+g' /etc/default/grub

sudo grub-mkconfig -o /boot/grub/grub.cfg

sudo systemctl enable sshd

mv /home/$USER/Plex/config /home/$USER/.config/i3/config


