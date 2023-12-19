MySQL

Concepts
For this project, we expect you to look at these concepts:

Database administration
Web stack debugging
[How to] Install mysql 5.7

Find public key here


https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html


Copy and paste it’s content into a file named signature.key(vi signature.key)


Follow These Commands


sudo apt-key add signature.key

sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C

sudo apt-get update

sudo apt-cache policy mysql-server

sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*


mysql --version

Resources
Read or watch:

What is a primary-replica cluster
MySQL primary replica setup
Build a robust database backup strategy
man or help:

mysqldump
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is the main role of a database
What is a database replica
What is the purpose of a database replica
Why database backups need to be stored in different physical locations
What operation should you regularly perform to make sure that your database backup strategy actually works
