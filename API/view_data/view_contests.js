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
        SELECT 
            r.round_year, 
            r.round_number, 
            r.round_img, 
            GROUP_CONCAT(DISTINCT CONCAT_WS(' ', cp.first_name, cp.last_name) SEPARATOR ', ') AS cook_names,
            GROUP_CONCAT(DISTINCT CONCAT_WS(' ', cj.first_name, cj.last_name) SEPARATOR ', ') AS judge_names
        FROM 
            round r
        LEFT JOIN 
            cooks_participate_in_round cpr ON cpr.round_round_id = r.round_id
        LEFT JOIN 
            cook cp ON cpr.cook_cook_id = cp.cook_id
        LEFT JOIN 
            cooks_judge_round cjr ON cjr.round_round_id = r.round_id
        LEFT JOIN 
            cook cj ON cjr.cook_cook_id = cj.cook_id
        GROUP BY 
            r.round_year, r.round_number
        ORDER BY 
            r.round_id;
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
        SELECT 
            r.round_year, 
            r.round_number, 
            r.round_img, 
            GROUP_CONCAT(DISTINCT CONCAT_WS(' ', cp.first_name, cp.last_name) SEPARATOR ', ') AS cook_names,
            GROUP_CONCAT(DISTINCT CONCAT_WS(' ', cj.first_name, cj.last_name) SEPARATOR ', ') AS judge_names
        FROM 
            round r
        LEFT JOIN 
            cooks_participate_in_round cpr ON cpr.round_round_id = r.round_id
        LEFT JOIN 
            cook cp ON cpr.cook_cook_id = cp.cook_id
        LEFT JOIN 
            cooks_judge_round cjr ON cjr.round_round_id = r.round_id
        LEFT JOIN 
            cook cj ON cjr.cook_cook_id = cj.cook_id
        WHERE 
            r.round_year = ?
        GROUP BY 
            r.round_year, r.round_number
        ORDER BY 
            r.round_number;
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

router.post('/contests/byCookName', cookieJwtAuth, (req, res) => {
    const round_name = req.body.name;

    const query = `
        SELECT 
            r.round_year, 
            r.round_number, 
            r.round_img, 
            GROUP_CONCAT(DISTINCT CONCAT_WS(' ', cp.first_name, cp.last_name) SEPARATOR ', ') AS cook_names,
            GROUP_CONCAT(DISTINCT CONCAT_WS(' ', cj.first_name, cj.last_name) SEPARATOR ', ') AS judge_names
        FROM 
            round r
        LEFT JOIN 
            cooks_participate_in_round cpr ON cpr.round_round_id = r.round_id
        LEFT JOIN 
            cook cp ON cpr.cook_cook_id = cp.cook_id
        LEFT JOIN 
            cooks_judge_round cjr ON cjr.round_round_id = r.round_id
        LEFT JOIN 
            cook cj ON cjr.cook_cook_id = cj.cook_id
        WHERE 
            CONCAT_WS(' ', cp.first_name, cp.last_name) = ? OR cp.first_name = ? OR cp.last_name = ?
        GROUP BY 
            r.round_year, r.round_number
        ORDER BY 
                r.round_year, r.round_number;
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
