

cp ~/.config/nvim/init.vim ~/dotfiles
cp ~/.bash_aliases ~/dotfiles
cp ~/.bashrc ~/dotfiles


while read p; do
  git add $p
done <~/dotfiles/files_to_backup.txt # list of files/folders to symlink in homedir

cd ~/dotfiles

git commit -m "$1"

git push origin master

cd -
