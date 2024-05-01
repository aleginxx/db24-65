const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'delete.html');

router.get('/delete', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    res.sendFile(filePath);
});

router.post('/delete', (req, res) => {
    const tableName = req.body.table; // Extracting the table name from the request body
    console.log(req.body);
    const query = `SELECT * FROM ${tableName}`; // Constructing the SQL query
    
    // Execute the query and handle the response
    DB.connection.query(query, (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).send('Error retrieving table data.');
        } else {
            const columns = Object.keys(result[0]);
            const primaryKey = columns[0]; 
            
            //console.log(primaryKey);
            res.json({ columns: columns, primaryKey: primaryKey, data: result });
        }
    });
});

router.post('/update-delete', cookieJwtAuth, (req, res) => {
    const tableName = req.body.tableName;
    const primaryKey = req.body.primaryKey;
    const rowID = req.body.rowID;

    console.log(req.body);

    if (!['ingredients', 'recipe', 'cuisine', 'tags', 'tips', 'steps', 'recipe_time', 'food_group', 'dietary_info', 'recipe_subject', 'cook', 'round'].includes(tableName)) {
        // If it's not one of the tables with constraints, directly execute the DELETE query
        let query = `DELETE FROM ${tableName} WHERE ${primaryKey} = ${rowID}`;
        DB.query(query, (err, result) => {
            if (err) {
                console.error('Error executing query:', err);
                res.status(500).json({ success: false, error: 'Error executing query' });
            } else {
                res.json({ success: true });
            }
        });
    } else {
        deleteRelatedEntries(tableName, rowID);
        res.json({ success: true });
    }
});

function deleteRelatedEntries(table_name, key_value) {
    let query = "";

    if (table_name === 'ingredients') {
        query = `
            DELETE FROM recipe_uses_ingredients WHERE ingredient_ingredient_id = ${key_value};
            DELETE FROM ingredients_belongs_to_food_group WHERE ingredient_ingredient_id = ${key_value};
            DELETE FROM ingredients WHERE ingredient_id = ${key_value};
        `;
    } else if (table_name === 'recipe') {
        query = `
            DELETE FROM recipe_requires_equipment WHERE recipe_recipe_id = ${key_value};
            DELETE FROM cook_executes_recipe WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_belongs_to_subject WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_subject WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_subject WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_has_dietary_info WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_uses_ingredients WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_takes_time WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_time WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_has_steps WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_offers_tips WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_has_tags WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe_belongs_to_types_of_meal WHERE recipe_recipe_id = ${key_value};
            DELETE FROM recipe WHERE recipe_id = ${key_value};
        `;
    } else if (table_name === 'cuisine') {
        query = `
            DELETE FROM cuisines_chosen_for_round WHERE cuisine_cuisine_id = ${key_value};
            DELETE FROM cook_knows_cuisine WHERE cuisine_cuisine_id = ${key_value};
            DELETE FROM cuisine WHERE cuisine_id = ${key_value};
        `;
    } else if (table_name === 'tags') {
        query = `
            DELETE FROM recipe_has_tags WHERE tags_tag_id = ${key_value};
            DELETE FROM tags WHERE tag_id = ${key_value};
        `;
    } else if (table_name === 'tips') {
        query = `
            DELETE FROM recipe_offers_tips WHERE tips_tips_id = ${key_value};
            DELETE FROM tips WHERE tips_id = ${key_value};
        `;
    } else if (table_name === 'steps') {
        query = `
            DELETE FROM recipe_has_steps WHERE steps_step_id = ${key_value};
            DELETE FROM steps WHERE step_id = ${key_value};
        `;
    } else if (table_name === 'recipe_time') {
        query = `
            DELETE FROM recipe_takes_time WHERE recipe_time_total_time = ${key_value};
            DELETE FROM recipe_time WHERE total_time = ${key_value};
    `;
    } else if (table_name === 'food_group') {
        query = `
            DELETE FROM ingredients_belongs_to_food_group WHERE food_group_food_group_id = ${key_value};
            DELETE FROM food_group WHERE food_group_id = ${key_value};
        `;        
    } else if (table_name === 'dietary_info') {
        query = `
            DELETE FROM recipe_has_dietary_info WHERE dietary_info_id = ${key_value};
            DELETE FROM dietary_info WHERE food_group_id = ${key_value};
        `;        
    } else if (table_name === 'recipe_subject') {
        query = `
            DELETE FROM recipe_belongs_to_subject WHERE recipe_subject_subject_id = ${key_value};
            DELETE FROM recipe_subject WHERE subject_id = ${key_value};
        `;        
    } else if (table_name === 'cook') {
        query = `
            DELETE FROM cooks_judge_round WHERE cook_cook_id = ${key_value};
            DELETE FROM cooks_participate_in_round WHERE cook_cook_id = ${key_value};
            DELETE FROM cook_knows_cuisine WHERE cook_cook_id = ${key_value};
            DELETE FROM cook_executes_recipe WHERE cook_cook_id = ${key_value};
            DELETE FROM ratings WHERE contestant_id = ${key_value};
            DELETE FROM ratings WHERE judge_id = ${key_value};
            DELETE FROM cook WHERE cook_id = ${key_value};
        `;        
    } else if (table_name === 'round') {
        let query = `
            DELETE FROM cuisines_chosen_for_round WHERE round_round_id = ${key_value};
            DELETE FROM cooks_judge_round WHERE round_round_id = ${key_value};
            DELETE FROM cooks_participate_in_round WHERE round_round_id = ${key_value};
            DELETE FROM ratings WHERE round_id = ${key_value};
            DELETE FROM round WHERE round_id = ${key_value};
        `;        
    } 

    DB.query(query, (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).json({ success: false, error: 'Error executing query' });
        } else {
            res.json({ success: true });
        }
    });
}

module.exports = router;
