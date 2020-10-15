#!/bin/bash

# Script for installing my apps on a fresh linux install (with applitude)

sudo apt udate
sudo apt upgrade -y

apps="
git
zathura
curl
ctags
r-base
texlive-latex-extra
texlive-science
texlive-fonts-extra
texlive-lang-european
latexmk
xdotool
cargo
"

sudo apt install -y $apps

curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

cd ~/
git clone https://github.com/Orenjonas/dotfiles.git
git clone https://github.com/Orenjonas/scripts.git


mkdir ~/.vim
touch ~/.vim/after.vim



