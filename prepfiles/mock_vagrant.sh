adduser --disabled-password --gecos "" vagrant
touch /home/vagrant/.bashrc
usermod -aG sudo vagrant

cp -a . /vagrant/
chmod 777 -R /vagrant
chown -R vagrant /vagrant
