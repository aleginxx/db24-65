# API

### Contents:

The API was constructed using the runtime environment [node.js](https://nodejs.org/en/) and the framework [express.js](https://expressjs.com/).

### Installation:

```bash
npm install
```

### Usage:
Before using the api, make sure the database `mydb` is already open in a MariaDB client. Then, in the API folder directory, run commands:

```bash
$env:MY_SECRET = "encryption word"
```
This command is used for the generation of the Jason Web Token upon login. Command : 
```bash
node app.js
```
makes the functionalities of the API directly accessible, either through the browser either through Postman.