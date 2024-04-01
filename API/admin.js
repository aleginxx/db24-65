const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const router = express.Router();
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/admin', cookieJwtAuth, (req, res) => {
    const { admin_id, admin_username } = req.user;

    const query = 'SELECT * FROM administrator WHERE admin_id = ?'; 
    DB.connection.query(query, [admin_id], (err, results) => { 
        if (err) {
            console.error('Error fetching admin data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            return res.status(404).send('Admin not found');
        }
        const admin = results[0]; 
        const token = req.cookies.token;

        res.render(path.join(__dirname, '..', 'frontend', 'admin'), { admin, token });

    });
});

module.exports = router;
