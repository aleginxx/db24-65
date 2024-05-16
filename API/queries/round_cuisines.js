const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'round-cuisines.html');

router.get('/round-cuisines', (req, res) => {
    res.sendFile(filePath);
});

router.post('/top-cuisines-round', (req, res) => {
    const FIND_RECIPE_PAIRS_PROCEDURE = 'call FindCuisineWithConsecutiveEntries();';

    const query = FIND_RECIPE_PAIRS_PROCEDURE;

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = [];

            results.forEach(rowDataPacket => {
                if (Array.isArray(rowDataPacket)) {
                    rowDataPacket.forEach(row => {
                        result_list.push({
                            count_current_year: row.count_current_year,
                            current_year: row.current_year,
                            previous_year: row.previous_year,
                            count_previous_year : row.count_previous_year 
                        });
                    });
                  } else {
                    console.error("rowDataPacket is not an array");
                  }
            });

            // console.log("Final Results:", result_list);

            res.status(200).json(result_list);
        }
    });
});

router.post('/food-groups-not-used', (req, res) => {
    const query = `
        SELECT DISTINCT ig.food_group_food_group_id, fg.food_group_name
        FROM ingredients_belongs_to_food_group ig
        LEFT JOIN food_group fg ON ig.food_group_food_group_id = fg.food_group_id
        WHERE ig.food_group_food_group_id NOT IN (
            SELECT DISTINCT ccr.cuisine_cuisine_id
            FROM cuisines_chosen_for_round ccr
        );
    `;

    // console.log("Executing query:", query);

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = results.map(row => ({
                food_group_name: row.food_group_name
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

module.exports = router;