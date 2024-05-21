const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'contests.html');

router.get('/contests', (req, res) => {
    res.sendFile(filePath);
});

router.post('/contests', cookieJwtAuth, (req, res) => {
    const query = `
    SELECT round.*, CONCAT(cook.first_name, ' ', cook.last_name) AS full_name 
    FROM round 
    LEFT JOIN cook 
    ON round.round_winner = cook.cook_id;
    `;
    DB.connection.query(query, (err, results) => { 
        if (err) {
            console.error('Error fetching recipes data:', err);
            return res.status(500).send('Internal Server Error');
        }
        
        console.log("Results: ", results);
        res.status(200).json(results); 
    });
});

module.exports = router;
