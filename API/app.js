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

const backup = require('./admin functionalities/backup.js');
app.use(base_url, backup);

const restore = require('./admin functionalities/restore.js');
app.use(base_url, restore)

const login = require('./login.js');
app.use(base_url, login);

const signup = require('./signup.js');
app.use(base_url, signup);

const logout = require('./logout.js');
app.use(base_url, logout);

app.set('view engine', 'ejs');

const user = require('./user.js');
app.use(base_url, user);

const profile = require('./profile.js');
app.use(base_url, profile);

const admin = require('./admin functionalities/admin.js');
app.use(base_url, admin);

const admin_functions = require('./admin functionalities/admin_functions.js');
app.use(base_url, admin_functions);

const home = require('./home.js');
app.use(base_url, home);

const make_admin = require('./admin functionalities/make_admin.js');
app.use(base_url, make_admin);

const modify = require('./admin functionalities/modify.js');
app.use(base_url, modify);


http.createServer(app).listen(port, () => {
    console.log(`HTTP server running on port ${port}`);
});