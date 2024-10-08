# Exit immediately if a command exits with a non-zero status
set -e

apt-get update
# apt install golang-go

# Install Git if not already installed
if ! command -v git &> /dev/null
then
    apt-get install -y git
fi

# Set shorter terminal prompt to just display the directory name
echo "export PS1='\W: '" >> ~/.bashrc

# Source the updated .bashrc to apply the changes immediately
source ~/.bashrc

git config --global user.name "Chetan Budathoki"
git config --global user.email "chetanbudathoki@outlook.com"



