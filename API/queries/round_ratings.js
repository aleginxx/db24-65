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
            CONCAT(judge.first_name, ' ', judge.last_name) AS judge_name,
            GROUP_CONCAT(DISTINCT CONCAT(contestant.first_name, ' ', contestant.last_name) ORDER BY contestant.last_name ASC) AS contestant_names,
            AVG(r.rating_value) AS mean_rating_value
        FROM mydb.ratings r
        JOIN mydb.cook judge ON r.judge_id = judge.cook_id
        JOIN mydb.cook contestant ON r.contestant_id = contestant.cook_id
        GROUP BY r.judge_id
        HAVING COUNT(DISTINCT r.contestant_id) > 1
        ORDER BY mean_rating_value DESC
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
                contestant_names: row.contestant_names,
                mean_rating_value: row.mean_rating_value
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

module.exports = router;