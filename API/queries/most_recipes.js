const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'most-recipes.html');

router.get('/most-recipes', (req, res) => {
    res.sendFile(filePath);
});

router.post('/most-recipes', (req, res) => {
    const query = `
        SELECT c.first_name, c.last_name, c.age, COUNT(r.recipe_id) AS num_recipes
        FROM cook c
        JOIN cook_executes_recipe ce ON c.cook_id = ce.cook_cook_id
        JOIN recipe r ON ce.recipe_recipe_id = r.recipe_id
        WHERE c.age < 30
        GROUP BY c.cook_id
        ORDER BY num_recipes DESC;
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