const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'round-equipment.html');

router.get('/round-equipment', (req, res) => {
    res.sendFile(filePath);
});

router.post('/round-equipment', (req, res) => {
    const query = `
        SELECT r.round_year, r.round_number, COUNT(re.equipment_equipment_id) AS total_equipment_used
        FROM round r
        JOIN cuisines_chosen_for_round cc ON r.round_id = cc.round_round_id
        JOIN cook_knows_cuisine ckc ON cc.cuisine_cuisine_id = ckc.cuisine_cuisine_id
        JOIN recipe rcp ON ckc.cuisine_cuisine_id = rcp.cuisine_of_recipe
        JOIN recipe_requires_equipment re ON rcp.recipe_id = re.recipe_recipe_id
        GROUP BY r.round_id
        ORDER BY total_equipment_used DESC
        LIMIT 1;
    `;

    // console.log("Executing query:", query);

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = results.map(row => ({
                round_year: row.round_year,
                round_number: row.round_number,
                total_equipment_used: row.total_equipment_used
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});


module.exports = router;