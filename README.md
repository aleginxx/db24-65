# DaContest

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white)


Github repository of Cooking Contest Website.

## Members of db24-65 project group:
- Georgia Alexopoulou | el20164
- Stylianos Mpouliaris Malatestas | el19214

# Installation

## Manual Installation
For more information, read all of the README files of the repository.
#### Database:

Open a program or server that hosts the MariaDB client of MySQL. We have chosen the xampp app.
Running script `DB Schema.sql`, we create schema `mydb`, containing the necessary tables according to the prequirements of the project, as well as necessary triggers.

```bash
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
```

#### DUMMY DATA:
Run file `dummy_data.py`, after placing the .csv files inside ```xampp/mysql/data/mydb```. 
Make sure you have all the necessary python libraries required to run this file, by running command
```bash
pip install -r requirements.txt
```
in terminal.

#### API:

Open file `API` and run commands
```bash
$env:MY_SECRET = "hello" // hello is now the chosen encryption word for this session
node app.js
```

The service can now be used in your computer. The url we use is `localhost:9876`. Below is a table of the ports associated with each service in the `HOST` machine:

  | SERVICE | PORT |
  | ------- | ---- |
  | MariaDB | 3306 |
  | API | 9876 |
  | Frontend - Apache | 8000 |