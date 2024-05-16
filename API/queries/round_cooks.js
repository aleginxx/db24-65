const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'round-cooks.html');

router.get('/round-cooks', (req, res) => {
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


router.post('/cooks-same-participations', (req, res) => {
    const FIND_COOK_PAIRS_PROCEDURE = 'call FindCookPairsWithConsecutiveParticipation();';

    const query = FIND_COOK_PAIRS_PROCEDURE;

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
                            cook1_name: row.cook1_name,
                            cook2_name: row.cook2_name,
                            participation_count: row.participation_count,
                            year_range: row.year_range
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

router.post('/cooks-less-participations', (req, res) => {
    const query = `
    SELECT c1.first_name,
        c1.last_name,
        c1.phone_number,
        c1.birth_date,
        c1.age,
        c1.years_of_experience,
        c1.position,
        c1.username,
        c1.password,
        COUNT(cpr1.round_round_id) AS participation_count
    FROM cook c1
    LEFT JOIN cooks_participate_in_round cpr1 ON c1.cook_id = cpr1.cook_cook_id
    GROUP BY c1.cook_id
    HAVING COUNT(cpr1.round_round_id) < (
    SELECT COUNT(cpr2.round_round_id) - 5
    FROM cooks_participate_in_round cpr2
    GROUP BY cpr2.cook_cook_id
    ORDER BY COUNT(cpr2.round_round_id) DESC
    LIMIT 1
    )
    `;

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = results.map(row => ({
                first_name: row.first_name,
                last_name: row.last_name,
                username: row.username,
                participation_count: row.participation_count
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

router.post('/cooks-least-experience', (req, res) => {
    const query = `
    SELECT 
        Year,
        Round_Number,
        Total_Years_of_Experience
    FROM (
        SELECT 
            ROUND.round_year AS Year,
            ROUND.round_number AS Round_Number,
            SUM(COALESCE(Participants.years_of_experience, 0) + COALESCE(Judges.years_of_experience, 0)) AS Total_Years_of_Experience,
            ROW_NUMBER() OVER (PARTITION BY ROUND.round_year ORDER BY SUM(COALESCE(Participants.years_of_experience, 0) + COALESCE(Judges.years_of_experience, 0)) ASC) AS Rank
        FROM 
            round AS ROUND
        LEFT JOIN 
            cooks_participate_in_round AS PARTICIPANTS_ROUND 
            ON ROUND.round_id = PARTICIPANTS_ROUND.round_round_id
        LEFT JOIN 
            cooks_judge_round AS JUDGES_ROUND 
            ON ROUND.round_id = JUDGES_ROUND.round_round_id
        LEFT JOIN 
            cook AS Participants 
            ON PARTICIPANTS_ROUND.cook_cook_id = Participants.cook_id
        LEFT JOIN 
            cook AS Judges 
            ON JUDGES_ROUND.cook_cook_id = Judges.cook_id
        GROUP BY 
            ROUND.round_year, ROUND.round_number
    ) AS Ranked
    WHERE 
        Rank = 1
    ORDER BY 
        Year, Round_Number;
    `;

    DB.connection.query(query, (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ err: 'Error executing query' });
        } else {
            // console.log("Results: ", results);

            const result_list = results.map(row => ({
                Year: row.Year,
                Round_Number: row.Round_Number,
                Total_Years_of_Experience: row.Total_Years_of_Experience
            }));

            // console.log("Mean Ratings:", meanRatings);

            res.status(200).json(result_list);
        }
    });
});

module.exports = router;