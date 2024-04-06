const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'admin_functions.html');

router.get('/admin_functions', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    res.sendFile(filePath);
});

router.get('/edit-data', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    res.sendFile(filePath);
});

router.post('/edit-data', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;

    console.log(req.body);
    return res.status(200).end();

});

module.exports = router;
