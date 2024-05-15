const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'cooks.html');

router.get('/cooks', (req, res) => {
    res.sendFile(filePath);
});

router.post('/cooks-never-judge', (req, res) => {
    const query = `
        SELECT DISTINCT c.cook_id, c.first_name, c.last_name
        FROM cook c
        LEFT JOIN cooks_judge_round cj ON c.cook_id = cj.cook_cook_id
        WHERE cj.cook_cook_id IS NULL;
    `;

    // console.log("Executing query:", query);

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = results.map(row => ({
                first_name: row.first_name,
                last_name: row.last_name,
                age: row.age,
                num_recipes: row.num_recipes
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

module.exports = router;