echo "Update and upgrade"
apt update
apt upgrade -y

echo "Install Sudo"
apt install sudo -y

useradd -rm -d /home/dev -s /bin/bash -g root -G sudo -u 1000 dev && \
    echo 'dev:xxxx' | chpasswd && \
    echo 'root:xxxx' | chpasswd


echo "Install Neofetch"
apt install neofetch -y

echo "Install Vim"
apt install vim -y

echo "Install Git"
apt install git -y

echo "Install and setup SSH"
apt install openssh-server -y

# Set up configuration for SSH
mkdir /var/run/sshd && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    echo "export VISIBLE=now" >> /etc/profile
service ssh start