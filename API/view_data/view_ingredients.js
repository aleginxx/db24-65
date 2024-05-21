const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/recipes', cookieJwtAuth, (req, res) => {
    const query = `SELECT * FROM ingredients`;
    DB.connection.query(query, (err, results) => { 
        if (err) {
            console.error('Error fetching ingredients data:', err);
            return res.status(500).send('Internal Server Error');
        }
        
        res.render(path.join(__dirname, '..', '..', 'frontend', 'ingredients'), { ingredients: results });
    });
});

module.exports = router;
