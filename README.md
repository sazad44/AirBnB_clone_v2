# 0x03 AirBnB: Deploy Static - Work In Progress
## Set-Up
### Server Config
Setting up the server with the correct configuration can be accomplished with
Puppet.
```sudo puppet apply 101-setup_web_static.pp```
A poorer version can be setup with bash.
```./0-setup_web_static.sh```
### File Deployment
Using Fabric, files can be pushed up to the server by:
1. Packing files into an archive and deploying them to the server.
```fab -f 3-deploy_web_static.py deploy -i ssh_private_key -u ubuntu```
* IMPORTANT: ```env.hosts``` needs to be edited inside of
```3-deploy_web_static.py``` to reflext the IP(s) of the servers being
deployed to.
### MySQL
Setup the MySQL server with ```setup_mysql_dev.sql``` using:
```cat setup_mysql_dev.sql | mysql -uroot -p```
Setup environment for DataBase usage with ```./export_setup```
Interact with the database through ```./console.py```
#### Commands
```Classes: User, State, City, Amenity, Place, Review```
```create <Class> [attribute=[value]]```, ```show <Class> <id>```,
```destroy <Class> <id>```, ```all <Class>```,
```update <Class> <id> [dictionary of attribute updates]```,
```count <Class>```
## Directories
### models
Python files for different classes and storage engines.
### tests
Unittests for classes and console.
### web_static
HTML/CSS files for webpage.
