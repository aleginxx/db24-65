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
    const { username } = req.user;

    const query = `
        SELECT r.round_year, 
            r.round_number, 
            r.round_img, 
            CONCAT_WS(' ', c.first_name, c.last_name) AS cook_name
        FROM round r
        LEFT JOIN cook c ON r.round_winner = c.cook_id;
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

router.post('/contests/byYear', cookieJwtAuth, (req, res) => {
    const round_year = req.body.year;

    const query = `
        SELECT r.round_year, 
            r.round_number, 
            r.round_img, 
            CONCAT_WS(' ', c.first_name, c.last_name) AS cook_name
        FROM round r
        LEFT JOIN cook c ON r.round_winner = c.cook_id
        WHERE r.round_year = ?;
    `;
    DB.connection.query(query, [round_year], (err, results) => { 
        if (err) {
            console.error('Error fetching recipes data:', err);
            return res.status(500).send('Internal Server Error');
        }
        
        // console.log("Results: ", results);
        res.status(200).json(results); 
    });
});

router.post('/contests/byName', cookieJwtAuth, (req, res) => {
    const round_name = req.body.name;

    const query = `
        SELECT r.round_year, 
            r.round_number, 
            r.round_img, 
            CONCAT_WS(' ', c.first_name, c.last_name) AS cook_name
        FROM round r
        LEFT JOIN cook c ON r.round_winner = c.cook_id
        WHERE CONCAT_WS(' ', c.first_name, c.last_name) = ? OR c.first_name = ? OR c.last_name = ?;
    `;
    DB.connection.query(query, [round_name, round_name, round_name], (err, results) => { 
        if (err) {
            console.error('Error fetching recipes data:', err);
            return res.status(500).send('Internal Server Error');
        }
        
        // console.log("Results: ", results);
        res.status(200).json(results); 
    });
});

module.exports = router;
