#!/bin/bash

sudo apt udate
sudo apt upgrade -y

apps="
vim
git
python-pip
python3-pip
ipython3
neovim
zathura
curl
"

sudo apt install -y $apps

curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

cd ~/
git clone https://github.com/Orenjonas/dotfiles.git
git clone https://github.com/Orenjonas/scripts.git





