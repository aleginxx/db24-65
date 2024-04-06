const express = require('express');
const path = require('path');
const router = express.Router();
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");

router.get('/home', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    const filePath = path.join(__dirname, '..', 'frontend', 'home.html');
    res.sendFile(filePath);
});

module.exports = router;
