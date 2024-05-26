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
    const query = `
        WITH CuisineParticipation AS (
            SELECT
                ccr.cuisine_cuisine_id,
                r.round_year,
                COUNT(*) AS participation_count
            FROM cuisines_chosen_for_round ccr
            JOIN round r ON ccr.round_round_id = r.round_id
            GROUP BY
                ccr.cuisine_cuisine_id,
                r.round_year
            HAVING participation_count >= 3
        ),
        CuisineYearPairs AS (
            SELECT
                cp1.cuisine_cuisine_id AS cuisine_id_1,
                cp1.round_year AS year_1,
                cp1.participation_count AS count_1,
                cp2.cuisine_cuisine_id AS cuisine_id_2,
                cp2.round_year AS year_2,
                cp2.participation_count AS count_2
            FROM CuisineParticipation cp1
            JOIN CuisineParticipation cp2 ON cp1.round_year = cp2.round_year - 1 AND cp1.participation_count = cp2.participation_count
        )
        SELECT
            c1.cuisine_name AS cuisine_name_1,
            c2.cuisine_name AS cuisine_name_2,
            cy.year_1,
            cy.count_1,
            cy.year_2,
            cy.count_2
        FROM CuisineYearPairs cy
        JOIN cuisine c1 ON cy.cuisine_id_1 = c1.cuisine_id
        JOIN cuisine c2 ON cy.cuisine_id_2 = c2.cuisine_id
        WHERE cy.cuisine_id_1 <> cy.cuisine_id_2
        ORDER BY cy.count_1 DESC, c1.cuisine_name, c2.cuisine_name;
    `;

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
            return;
        }

        const result_list = results.map(row => ({
            cuisine_name_1: row.cuisine_name_1,
            cuisine_name_2: row.cuisine_name_2,
            year_1: row.year_1,
            count_1: row.count_1,
            year_2: row.year_2,
            count_2: row.count_2
        }));

        res.status(200).json(result_list);
    });
});

router.post('/food-groups-not-used', (req, res) => {
    const query = `
        SELECT
            fg.food_group_id,
            fg.food_group_name
        FROM mydb.food_group fg
        LEFT JOIN mydb.ingredients_belongs_to_food_group ibfg ON fg.food_group_id = ibfg.food_group_food_group_id
        LEFT JOIN mydb.ingredients i ON ibfg.ingredients_ingredient_id = i.ingredient_id
        LEFT JOIN mydb.recipe_uses_ingredients rui ON i.ingredient_id = rui.ingredients_ingredient_id
        LEFT JOIN mydb.recipe r ON rui.recipe_recipe_id = r.recipe_id
        LEFT JOIN mydb.cooks_participate_in_round cpir ON r.cuisine_of_recipe = cpir.recipe_cuisine_id
        WHERE cpir.round_round_id IS NULL;
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