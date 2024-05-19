const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'mean-score.html');

router.get('/score', (req, res) => {
    res.sendFile(filePath);
});

router.post('/score-cook', (req, res) => {
    const query = `
        SELECT c.cook_id, c.first_name, c.last_name, c.username, AVG(r.rating_value) AS mean_rating
        FROM cook c
        JOIN ratings r ON c.cook_id = r.contestant_id
        GROUP BY c.cook_id, c.first_name, c.last_name, c.username
    `;

    // console.log("Executing query:", query);

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const meanRatings = results.map(row => ({
                cook_id: row.cook_id,
                first_name: row.first_name,
                last_name: row.last_name,
                username: row.username,
                mean_rating: row.mean_rating
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(meanRatings);
        }
    });
});

router.post('/score-cuisine', (req, res) => {
    const query = `
        SELECT 
            TRIM(TRAILING '\r' FROM c.cuisine_name) AS cuisine_name,
            AVG(r.rating_value) AS mean_rating
        FROM 
            ratings r
        JOIN 
            round ro ON r.round_id = ro.round_id
        JOIN 
            cooks_participate_in_round cp ON r.contestant_id = cp.cook_cook_id AND r.round_id = cp.round_round_id
        JOIN 
            recipe rec ON cp.recipe_cuisine_id = rec.cuisine_of_recipe
        JOIN 
            cuisine c ON rec.cuisine_of_recipe = c.cuisine_id
        GROUP BY 
            cuisine_name;
    `;

    console.log("Executing query:", query);

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const meanRatings = results.map(row => ({
                cuisine_name: row.cuisine_name,
                mean_rating: row.mean_rating
            }));

            console.log("Mean Ratings:", meanRatings);

            res.status(200).json(meanRatings);
        }
    });
});

module.exports = router;
