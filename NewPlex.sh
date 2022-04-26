#!/bin/sh

sudo passwd -d $USER
sudo pacman -Syu  --noconfirm
sudo pacman -S base-devel xorg-xinit xorg python-pip --noconfirm #(patch) 

git clone https://github.com/Magnitaizer/Plex.git /home/$USER/Plex

paru -S plex-media-player --noconfirm

pip install pynput

if grep -q 'exec plexmediaplayer' "/home/$USER/.xinitrc"; then
  echo 'skipping this part...'
else
  echo ' ' >> /home/$USER/.xinitrc
  echo 'exec python3 Plex/local_control.py &' >> /home/$USER/.xinitrc
  echo 'exec plexmediaplayer' >> /home/$USER/.xinitrc
fi

if grep -q 'exec startx' "/home/$USER/.bash_profile"; then
  echo 'skipping this part...'
else
  echo ' ' >> /home/$USER/.bash_profile
  echo 'if [[ ! ${DISPLAY} && ${XDG_VTNR} == 1 ]]; then' >> /home/$USER/.bash_profile
  echo '     exec startx' >> /home/$USER/.bash_profile
  echo 'fi' >> /home/$USER/.bash_profile
fi

if grep -q 'defaults.pcm.card 0' "/etc/asound.conf"; then
  echo 'skipping this part...'
else
  echo ' ' >> /etc/asound.conf
  echo 'defaults.pcm.card 0' >> /etc/asound.conf
  echo 'defaults.pcm.device 3' >> /etc/asound.conf
  echo 'defaults.ctl.card 0' >> /etc/asound.conf
fi

sudo sed -i --follow-symlinks "38s+.*ExecStart.*+ExecStart=-/sbin/agetty -a "$USER' %I $TERM+' /etc/systemd/system/getty.target.wants/getty@tty1.service

sudo sed -i 's+GRUB_TIMEOUT=5+GRUB_TIMEOUT=0+g' /etc/default/grub

sudo grub-mkconfig -o /boot/grub/grub.cfg

xset -dpms

xset s off

sudo systemctl disable display-manager.service

