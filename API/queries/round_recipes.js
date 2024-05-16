const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'round-recipes.html');

router.get('/round-recipes', (req, res) => {
    res.sendFile(filePath);
});

router.post('/recipe-pair-tags', (req, res) => {
    const FIND_RECIPE_PAIRS_PROCEDURE = 'call FindTopRecipePairsWithCommonTags();';

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
                            recipe_name1: row.recipe_name1,
                            recipe_name2: row.recipe_name2,
                            appearances: row.appearances
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

router.post('/recipe-avg-carbs', (req, res) => {
    const FIND_RECIPE_PAIRS_PROCEDURE = 'call CalculateAverageCarbGramsPerYear();';

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
                            year: row.year,
                            avg_carb_grams : row.avg_carb_grams 
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

router.post('/most-difficult-rounds', (req, res) => {
    const MOST_DIFFICULT_ROUND_PROCEDURE = 'call CalculateAverageRating();';

    const query = MOST_DIFFICULT_ROUND_PROCEDURE;

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
                            round_year: row.round_year,
                            round_number : row.round_number,
                            average_rating: row.average_rating
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

router.post('/most-common-subject', (req, res) => {
    const query = `
        SELECT rs.subject_name, COUNT(*) as appearance_count
        FROM recipe_belongs_to_subject rbs
        JOIN recipe_subject rs ON rbs.recipe_subject_subject_id = rs.subject_id
        JOIN recipe r ON rbs.recipe_recipe_id = r.recipe_id
        JOIN cuisines_chosen_for_round ccr ON r.cuisine_of_recipe = ccr.cuisine_cuisine_id
        JOIN round ro ON ccr.round_round_id = ro.round_id
        GROUP BY rs.subject_name
        ORDER BY appearance_count DESC
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
                subject_name: row.subject_name,
                appearance_count: row.appearance_count
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

module.exports = router;