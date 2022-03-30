#!/bin/sh

sudo passwd -d $USER
sudo pacman -Syu  --noconfirm
sudo pacman -S base-devel xorg-xinit xorg git python-pip --noconfirm
git clone https://aur.archlinux.org/trizen.git /home/$USER/trizen
cd /home/$USER/trizen
makepkg -sri --noconfirm
trizen -S plex-media-player --noconfirm
pip install plexapi
git clone https://github.com/Magnitaizer/Shalash.git /home/$USER/
sudo mv /home/$USER/Shalash/plexctl.service /etc/systemd/system/plexctl.service
sudo systemctl enable plexctl.service 

if grep -q 'exec plexmediaplayer' "/home/$USER/.xinitrc"; then
  echo 'skipping this part...'
else
  echo '#!/bin/sh' >> /home/$USER/.xinitrc
  echo ' ' >> /home/$USER/.xinitrc
  echo 'start-pulseaudio-x11 &' >> /home/$USER/.xinitrc
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

sudo sed -i --follow-symlinks "38s+.*ExecStart.*+ExecStart=-/sbin/agetty -a "$USER' %I $TERM+' /etc/systemd/system/getty.target.wants/getty@tty1.service

sudo sed -i 's+GRUB_TIMEOUT=5+GRUB_TIMEOUT=0+g' /etc/default/grub

sudo grub-mkconfig -o /boot/grub/grub.cfg

sudo systemctl disable display-manager.service

sudo systemctl mask systemd-udev-settle

sudo reboot