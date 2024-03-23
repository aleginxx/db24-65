const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const DB = require('./database.js');
const http = require('http');
const phpExpress = require('php-express')();
const { exec } = require('child_process');

const port = 9876;
const app = express();

const base_url = '/dacontest';

const healthcheck = require('./healthcheck.js');
app.use(base_url, healthcheck);

const login = require('./login.js');
app.use(base_url, login);

//const home = require('./home.js');
//app.use(base_url, home);

http.createServer(app).listen(port, () => {
    console.log(`HTTP server running on port ${port}`);
});