#!/bin/sh

sudo passwd -d $USER
sudo pacman -Syu  --noconfirm
sudo pacman -S base-devel xorg-xinit xorg git --noconfirm
git clone https://aur.archlinux.org/trizen.git /home/$USER/trizen
cd /home/$USER/trizen
makepkg -sri --noconfirm
trizen -S plex-media-player --noconfirm
echo '#!/bin/sh' >> /home/$USER/.xinitrc
echo ' ' >> /home/$USER/.xinitrc
echo 'exec plexmediaplayer' >> /home/$USER/.xinitrc
echo ' ' >> /home/$USER/.bash_profile
echo 'if [[ ! ${DISPLAY} && ${XDG_VTNR} == 1 ]]; then' >> /home/$USER/.bash_profile
echo '     exec startx' >> /home/$USER/.bash_profile
echo 'fi' >> /home/$USER/.bash_profile
sudo sed -i --follow-symlinks "38s+.*ExecStart.*+ExecStart=-/sbin/agetty -a "$USER' %I $TERM+' /etc/systemd/system/getty.target.wants/getty@tty1.service
sudo sed -i 's+GRUB_TIMEOUT=5+GRUB_TIMEOUT=0+g' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo systemctl disable display-manager.service
sudo systemctl mask systemd-udev-settle
sudo reboot