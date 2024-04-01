const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const router = express.Router();
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/admin_functions', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;

    res.render(path.join(__dirname, '..', 'frontend', 'admin_functions'), { token });
});

module.exports = router;
