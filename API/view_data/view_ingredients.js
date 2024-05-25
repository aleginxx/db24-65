const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'ingredients.html');

router.get('/ingredients', (req, res) => {
    res.sendFile(filePath);
});

router.post('/ingredients', cookieJwtAuth, (req, res) => {
    const query = `
        SELECT * FROM ingredients;
    `;
    DB.connection.query(query, (err, results) => { 
        if (err) {
            console.error('Error fetching recipes data:', err);
            return res.status(500).send('Internal Server Error');
        }
        
        // console.log("Results: ", results);
        res.status(200).json(results); 
    });
});

module.exports = router;
