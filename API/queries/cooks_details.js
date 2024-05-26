const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'cook-details.html');

router.get('/cook-details', (req, res) => {
    res.sendFile(filePath);
});

router.post('/cooks_know_cuisines', (req, res) => {
    const cuisineName = req.body.cuisineName;

    let query;
    let queryParams;

    if (cuisineName) {
        cuisineNameFixed = req.body.cuisineName + '\r';
        query = `
            SELECT 
                CONCAT(c.first_name, ' ', c.last_name) AS cook_name, 
                c.username, 
                TRIM(TRAILING '\r' FROM cu.cuisine_name) AS cuisine_name
            FROM mydb.cook c
            JOIN mydb.cook_knows_cuisine ckc ON c.cook_id = ckc.cook_cook_id
            JOIN mydb.cuisine cu ON ckc.cuisine_cuisine_id = cu.cuisine_id
            WHERE cu.cuisine_name = ?
        `;
        queryParams = [cuisineNameFixed];
    } else {
        query = `
            SELECT 
                CONCAT(c.first_name, ' ', c.last_name) AS cook_name,
                c.username,
                GROUP_CONCAT(DISTINCT TRIM(TRAILING '\r' FROM cu.cuisine_name) SEPARATOR ', ') AS cuisine_name
            FROM mydb.cook c
            JOIN mydb.cook_knows_cuisine ckc ON c.cook_id = ckc.cook_cook_id
            JOIN mydb.cuisine cu ON ckc.cuisine_cuisine_id = cu.cuisine_id 
            GROUP BY cook_name, c.username
        `;
        queryParams = [];
    }

    DB.connection.query(query, queryParams, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            const cooksList = results.map(row => ({
                cook_name: row.cook_name,
                username: row.username,
                cuisine_name: row.cuisine_name
            }));
            res.status(200).json(cooksList);
        }
    });
});

router.post('/cooks_participate_in_rounds', (req, res) => {
    const roundYear = req.body.roundYear;

    let query;
    let queryParams;

    if (roundYear) {
        query = `
        SELECT CONCAT(c.last_name, ' ', c.first_name) AS cook_name, c.username, r.round_year, r.round_number,
            CASE
                WHEN cjr.cook_cook_id IS NOT NULL THEN 'Judge'
                ELSE 'Participant'
            END AS role
        FROM cooks_participate_in_round cpr
        JOIN cook c ON cpr.cook_cook_id = c.cook_id
        LEFT JOIN cooks_judge_round cjr ON cpr.cook_cook_id = cjr.cook_cook_id AND cpr.round_round_id = cjr.round_round_id
        JOIN round r ON cpr.round_round_id = r.round_id
        WHERE r.round_year = ?`;
        queryParams = [roundYear];
    } else {
        query = `
            SELECT 
                CONCAT(c.last_name, ' ', c.first_name) AS cook_name, 
                c.username, 
                GROUP_CONCAT(DISTINCT CONCAT(r.round_year, ':', r.round_number) SEPARATOR ', ') AS round_info,
                CASE
                    WHEN cpr.cook_cook_id IS NOT NULL THEN 'Participant'
                    WHEN cjr.cook_cook_id IS NOT NULL THEN 'Judge'
                END AS role
            FROM round r
            JOIN cook c ON 1=1
            LEFT JOIN cooks_participate_in_round cpr ON cpr.cook_cook_id = c.cook_id AND r.round_id = cpr.round_round_id
            LEFT JOIN cooks_judge_round cjr ON cjr.cook_cook_id = c.cook_id AND r.round_id = cjr.round_round_id
            WHERE (cpr.cook_cook_id IS NOT NULL OR cjr.cook_cook_id IS NOT NULL)
            GROUP BY cook_name, role, c.username;
        `;
        queryParams = [];
    }

    // console.log("Executing query:", query);

    DB.connection.query(query, queryParams, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            const cooks_list = results.map(row => ({
                cook_name: row.cook_name,
                username: row.username,
                role: row.role,
                round_info : row.round_info
            })); 

            res.status(200).json(cooks_list);
        }
    });

});

module.exports = router;