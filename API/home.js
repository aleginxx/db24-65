const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const { exec } = require('child_process');
const app = express();
const http = require('http');
const jwt = require("jsonwebtoken");
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");
const router = express.Router();
router.use(bodyParser.urlencoded({ extended: true }));

router.get('/', (req, res) => {
    const filePath = path.join(__dirname, '..', 'frontend', 'index.html');
    res.sendFile(filePath);
});

router.get('/home', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;

    if (!token) {
        return res.status(404).send('You do not have permission to access this page');
    }
    const filePath = path.join(__dirname, '..', 'frontend', 'home.html');
    res.sendFile(filePath);
});

module.exports = router;
