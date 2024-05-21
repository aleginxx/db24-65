const express = require('express');
const router = express.Router();
const path = require('path');
const fs = require('fs');
const util = require('util');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

const writeFileAsync = util.promisify(fs.writeFile);
const queryAsync = util.promisify(DB.connection.query).bind(DB.connection);

async function exportTableToCSV(tableName, fileName) {
    try {
        const query = `SELECT * FROM ${tableName}`;
        const results = await queryAsync(query);

        const csvData = results.map(row => {
            return Object.values(row).map(value => {
                if (typeof value === 'string' && value.includes(',')) {
                    return `"${value}"`;
                } else if (value instanceof Date) {
                    const year = value.getFullYear();
                    const month = ('0' + (value.getMonth() + 1)).slice(-2); 
                    const day = ('0' + value.getDate()).slice(-2);
                    return `${year}-${month}-${day}`;
                }
                return value;
            }).join(',');
        }).join('\n');

        const filePath = path.join(__dirname, '..', 'backup_data', fileName);
        await writeFileAsync(filePath, csvData);
        console.log(`Exported table '${tableName}' to '${filePath}'`);
    } catch (error) {
        console.error(`Error exporting table '${tableName}' to CSV:`, error);
    }
}

async function exportAllTablesToCSV() {
    const tables = [
        { tableName: 'cuisine', fileName: 'cuisine.csv' },
        { tableName: 'ingredients', fileName: 'ingredients.csv' },
        { tableName: 'recipe', fileName: 'recipe.csv' },
        { tableName: 'recipe_uses_ingredients', fileName: 'recipe_uses_ingredients.csv' },
        { tableName: 'tips', fileName: 'tips.csv' },
        { tableName: 'recipe_offers_tips', fileName: 'recipe_offers_tips.csv' },
        { tableName: 'types_of_meal', fileName: 'types_of_meal.csv' },
        { tableName: 'recipe_belongs_to_types_of_meal', fileName: 'recipe_belongs_to_types_of_meal.csv' },
        { tableName: 'steps', fileName: 'steps.csv' },
        { tableName: 'recipe_has_steps', fileName: 'recipe_has_steps.csv' },
        { tableName: 'food_group', fileName: 'food_group.csv' },
        { tableName: 'ingredients_belongs_to_food_group', fileName: 'ingredients_belongs_to_food_group.csv' },
        { tableName: 'equipment', fileName: 'equipment.csv' },
        { tableName: 'recipe_requires_equipment', fileName: 'recipe_requires_equipment.csv' },
        { tableName: 'round', fileName: 'round.csv' },
        { tableName: 'administrator', fileName: 'administrator.csv' },
        { tableName: 'tags', fileName: 'tags.csv' },
        { tableName: 'recipe_has_tags', fileName: 'recipe_has_tags.csv' },
        { tableName: 'recipe_time', fileName: 'recipe_time.csv' },
        { tableName: 'recipe_takes_time', fileName: 'recipe_takes_time.csv' },
        { tableName: 'dietary_info', fileName: 'dietary_info.csv' },
        { tableName: 'recipe_has_dietary_info', fileName: 'recipe_has_dietary_info.csv' },
        { tableName: 'recipe_subject', fileName: 'recipe_subject.csv' },
        { tableName: 'recipe_belongs_to_subject', fileName: 'recipe_belongs_to_subject.csv' },
        { tableName: 'cook', fileName: 'cook.csv' },
        { tableName: 'cook_executes_recipe', fileName: 'cook_executes_recipe.csv' },
        { tableName: 'cook_knows_cuisine', fileName: 'cook_knows_cuisine.csv' },
        { tableName: 'cuisines_chosen_for_round', fileName: 'cuisines_chosen_for_round.csv' },
        { tableName: 'cooks_participate_in_round', fileName: 'cooks_participate_in_round.csv' },
        { tableName: 'cooks_judge_round', fileName: 'cooks_judge_round.csv' },
        { tableName: 'ratings', fileName: 'ratings.csv' },
    ];

    for (const table of tables) {
        await exportTableToCSV(table.tableName, table.fileName);
    }
}

router.get('/backup', (req, res) => {
    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const check_admin = `SELECT * FROM administrator WHERE admin_username = ?`;

    DB.connection.query(check_admin, [username_check], (err, results) => { 
      if (err) {
          console.error('Error fetching admin data:', err);
          return res.status(500).send('Internal Server Error');
      }
      if (results.length === 0) {
          return res.status(404).send('You do not have permission to access this page');
      }
      else {
        res.sendFile(filePath);
      }
    });
});

router.post('/backup', async (req, res) => {
    const token = req.cookies.token;

    if (!token) {
        return res.status(403).send('You do not have permission to access this page.');
    } 

    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const check_admin = `SELECT * FROM administrator WHERE admin_username = ?`;

    DB.connection.query(check_admin, [username_check], (err, results) => { 
      if (err) {
        console.error('Error checking admin_username:', error);
        res.status(500).send('An error occurred while processing your request.');
      }
      if (results.length === 0) {
        return res.status(404).send('You do not have permission to access this page');
      }
      else {
        exportAllTablesToCSV();
        res.send('Backup completed successfully.');
      }
    });
});

module.exports = router;
