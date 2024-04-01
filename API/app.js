const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const DB = require('./database.js');
const http = require('http');
const phpExpress = require('php-express')();
const { exec } = require('child_process');
const cookieParser = require("cookie-parser");


const port = 9876;
const app = express();

const base_url = '/dacontest';

app.use(cookieParser());

const healthcheck = require('./healthcheck.js');
app.use(base_url, healthcheck);

const backup = require('./backup.js');
app.use(base_url, backup);

const restore = require('./restore.js');
app.use(base_url, restore)

const login = require('./login.js');
app.use(base_url, login);

app.set('view engine', 'ejs');

const user = require('./user.js');
app.use(base_url, user);

//const home = require('./home.js');
//app.use(base_url, home);

http.createServer(app).listen(port, () => {
    console.log(`HTTP server running on port ${port}`);
});