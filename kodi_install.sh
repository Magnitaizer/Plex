#!/bin/sh

sudo passwd -d $USER
sudo apt update &&  sudo apt upgrade -y && sudo apt autoremove -y
sudo apt install base-devel kodi --noconfirm

git clone https://github.com/Magnitaizer/Plex.git /home/$USER/Kodi

pip install pynput

if grep -q 'exec kodi' "/home/$USER/.xinitrc"; then
  echo 'skipping this part...'
else
  echo ' ' >> /home/$USER/.xinitrc
  echo 'exec python3 Plex/local_control.py &' >> /home/$USER/.xinitrc
  echo 'xset s off -dpms' >> /home/$USER/.xinitrc
  echo 'exec kodi' >> /home/$USER/.xinitrc
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

sudo systemctl disable display-manager.service
