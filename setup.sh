#!/bin/bash

echo "======================= Update and upgrade ======================="
apt update
apt upgrade -y

echo "======================= Install Sudo ======================="
apt install sudo -y

echo "======================= Install Neofetch ======================="
apt install neofetch -y

echo "======================= Install Vim ======================="
apt install vim -y

echo "======================= Install Curl ======================="
apt install curl -y

echo "======================= Install Git ======================="
apt install git -y

echo "======================= Install and setup SSH ======================="
apt install openssh-server -y

useradd -rm -d /home/dev -s /bin/bash -g root -G sudo -u 1000 dev && \
    echo 'dev:test' | chpasswd && \
    echo 'root:test' | chpasswd

# Set up configuration for SSH
mkdir /var/run/sshd && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    echo "export VISIBLE=now" >> /etc/profile
service ssh start

echo "======================= Setup Exercism configuration ======================="
cd /home/dev/
mkdir exercism
wget "https://github.com/exercism/cli/releases/download/v3.3.0/exercism-3.3.0-linux-x86_64.tar.gz"
tar -xvzf exercism-3.3.0-linux-x86_64.tar.gz
mkdir -p ~/bin
mv exercism ~/bin
rm -rf *
echo 'export PATH=~/bin:$PATH' >> ~/.bash_profile
echo "source ~/.bash_profile">>~/.bashrc

echo "======================= Configurations finales ======================="
apt-get install dos2unix -y        
dos2unix /shell_color.txt       # S'assure que les metadata (notamment "^M") Windows sont converties en Unix (notamment "\n")
cat /shell_color.txt >> ~/.bashrc




sleep 3

