#!/bin/bash

sudo apt udate
sudo apt upgrade -y

apps="
vim
git
python-pip
python3-pip
python-gpg
ipython3
neovim
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
"

sudo apt install -y $apps

curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

cd ~/
git clone https://github.com/Orenjonas/dotfiles.git
git clone https://github.com/Orenjonas/scripts.git


mkdir ~/.vim
touch ~/.vim/after.vim



