#!/bin/sh

sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y

sudo apt --fix-broken install

sudo apt-get install jq curl avahi-daemon apparmor-utils udisks2 libglib2.0-bin network-manager dbus wget -y

sudo curl -fsSL get.docker.com | sh