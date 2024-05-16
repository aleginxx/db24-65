const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'round-ratings.html');

router.get('/round-ratings', (req, res) => {
    res.sendFile(filePath);
});

router.post('/top-5-ratings', (req, res) => {
    const query = `
    SELECT 
        CONCAT(c.first_name, ' ', c.last_name) AS judge_name,
        CONCAT(cc.first_name, ' ', cc.last_name) AS contestant_name,
        AVG(r.rating_value) AS overall_score
    FROM ratings r
    INNER JOIN cook c ON r.judge_id = c.cook_id
    INNER JOIN cook cc ON r.contestant_id = cc.cook_id
    GROUP BY r.judge_id, r.contestant_id
    ORDER BY overall_score DESC
    LIMIT 5;
    `;

    // console.log("Executing query:", query);

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = results.map(row => ({
                judge_name: row.judge_name,
                contestant_name: row.contestant_name,
                overall_score: row.overall_score
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

module.exports = router;