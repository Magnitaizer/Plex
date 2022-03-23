#!/bin/sh

echo '#!/bin/sh' >> /home/nuc/.xinitrc
echo ' ' >> /home/nuc/.xinitrc
echo 'exec plexmediaplayer' >> /home/nuc/.xinitrc
chown nuc /home/nuc/.xinitrc
echo 'if [[ ! ${DISPLAY} && ${XDG_VTNR} == 1 ]]; then' >> /home/nuc/.bash_profile
echo '     exec startx' >> /home/nuc/.bash_profile
echo 'fi' >> /home/nuc/.bash_profile
sed -i '38s+.*ExecStart.*+ExecStart=-/sbin/agetty -a nuc %I $TERM+' /etc/systemd/system/getty.target.wants/getty@tty1.service
sed -i 's+GRUB_TIMEOUT=5+GRUB_TIMEOUT=0+g' /etc/default/grub
grub-mkconfig -o /boot/grub/grub.cfg
systemctl disable display-manager.service
passwd -d nuc
pacman -S base-devel xorg-xinit xorg git
#git clone https://aur.archlinux.org/trizen.git /home/nuc
#chown nuc /home/nuc/trizen
#cd /home/nuc/trizen
#makepkg -sri
#trizen -S plex-media-player