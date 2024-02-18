## Arduino_to_MySQL_Data_Logging_using_Python

In this work, we are sending data from the 'Arduino uno' over the serial port to a computer. The data received by the computer over the serial port is then logged into a table. This table is created within a database in MySQL. The entire job of serial communication and data logging is automated using a Python script.

## Systems used in this work

- Operating system: Ubuntu 18.04
- Arduino Uno development board
- Arduino IDE 
- MySQL 
- Python3

## Setting up the Computer Side

We need to install MySQL in our system. MySQL is an Open source database management system(DBMS)

1. MySQL Installation in Ubuntu 18.04 using terminal
- Check if Mysql is installed or not: 
    - $ mysql --version
- If not then follow below steps.
- Update the package manager: 
    - $ sudo apt update
- Install the mysql server application: 
    - $ sudo apt install mysql-server
- Checking whether the server is running or not: 
    - $ systemctl status mysql.service
- If not running, then start the service
    - $ sudo systemctl start mysql.service
- To load default secure settings and set pwd, run below command:
    - $ sudo mysql_secure_installation

2. Starting the mysql service
- Starting the MySQL service from the terminal
    - $ sudo mysql
- Enabling the pwd authentication by running below line of codes:
    - mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
    - mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'make_your_password';
    - mysql> FLUSH PRIVILEGES
- Now, exit the mysql terminal:
    - mysql> exit

### Opening MySQL and creating a database and a table

1. Now onwards, to open mysql you will need to run following command
    - $ mysql -u root -p
    - Enter your password to access mysql.
2. Create a database in mysql named test_db:
    - mysql> create database test_db
3. Select the database test_db to be used:
    - mysql> use test_db
4. Create a table named table1 in database test_db:
    - mysql> create table table1(value1 int, value2 int); 
    - mysql>  create table table2(value1 int, value2 int, value3 int, value4 int);
5. To see the list of tables in a database:
    - mysql> show tables
6. To see the contents of a table:
    - mysql> select *from table_name

### Installation of MySQL python libraries

1. Install mysqlclient using pip3 for python 3 and before that install python development package:
    - $ sudo apt install python3-dev default-libmysqlclient-dev build-essential
    - $ pip3 install mysqlclient

2. Install mysql connector:
    - $ sudo pip3 install mysql-connector-python

3. Install pyserial library for serial communication using pip3 for python 3:
    - $ sudo pip3 install pyserial

## 
