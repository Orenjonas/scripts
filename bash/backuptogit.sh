cd ~/.config/nvim/vim-snippets/
git add .
git commit -m "update"
git push origin master

cp ~/.config/nvim/init.vim ~/dotfiles
cp ~/.bash_aliases ~/dotfiles
cp ~/.bashrc ~/dotfiles

cd ~/dotfiles

while read p; do
  git add $p
done <~/dotfiles/files_to_backup.txt

cd ~/dotfiles

git commit -m "$1"

git push origin master

cd -
