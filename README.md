# scheduller_project

This is a project based on python and flask framework.

This project is an AI Project focusing on Genetic Algorithm to solve schedulling of a class semester with all the common filtering.
The installation is simple just clone this repository and follow this documentation.

## Requirement and installation

Since i'm using Makefile for simplification of the installation and running of this application so make sure to download Make dependencies. If you haven't installed then follow these easy installation steps on this link 'https://linuxhint.com/install-use-make-windows/'

Other than Makefile this Application is also using PostgreSQL as the database. So make sure to download PostgreSQL or change the configuration to support your choice of database such as mySQL or MariaDB.

## How to Run and early setup

Since we are using Make file so please read the documentation in Makefile, However if you only want to do the simple installation then follow these easy steps. (make sure to install MAKE first!)

If this is your first time using this application then you need to initialize all the dependencies needed in these flask application by typing this command on your terminal or powershell.

`make init ` => this command purpose is to initialize the dependencies needed

`make migrate ` => this command purpose is to create the migration script and initialize table

`make default ` => this command is the main command to run and import sql into database (use `make run` if you do not wish to reset the database)


If you simply want to run the Application just use command `make run` or `make default` if you want to reset the database too.
