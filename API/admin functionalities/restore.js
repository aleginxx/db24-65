const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');
const util = require('util');
const csv = require('csv-parser');
const DB = require('../database.js');

const readFileAsync = util.promisify(fs.readFile);

async function truncateTables() {
    try {
        const tables = [
            'recipe_requires_equipment',
            'equipment',
            'ratings',
            'cuisines_chosen_for_round',
            'cooks_judge_round',
            'cooks_participate_in_round',
            'round',
            'cook_knows_cuisine',
            'cook_executes_recipe',
            'cook',
            'recipe_belongs_to_subject',
            'recipe_subject',
            'recipe_has_dietary_info',
            'dietary_info',
            'recipe_uses_ingredients',
            'ingredients_belongs_to_food_group',
            'food_group',
            'recipe_takes_time',
            'recipe_time',
            'recipe_has_steps',
            'steps',
            'recipe_offers_tips',
            'tips',
            'recipe_has_tags',
            'tags',
            'recipe_belongs_to_types_of_meal',
            'types_of_meal',
            'recipe',
            'cuisine',
            'ingredients',
            'administrator'
        ];

        for (const table of tables) {
            await new Promise((resolve, reject) => {
                DB.connection.query(`DELETE FROM ${table}`, (error, results) => {
                    if (error) {
                        reject(error);
                    } else {
                        resolve();
                    }
                });
            });
        }

        console.log('All tables truncated successfully.');
    } catch (error) {
        console.error('Error truncating tables:', error);
    }
}

async function fillTablesFromCSV() {
    const csvFiles = [
        'administrator.csv', 
        'ingredients.csv',
        'cuisine.csv', 
        'recipe.csv', 
        'types_of_meal.csv',
        'recipe_belongs_to_types_of_meal.csv',
        'tags.csv',
        'recipe_has_tags.csv',
        'tips.csv',
        'recipe_offers_tips.csv',
        'steps.csv',
        'recipe_has_steps.csv',
        'recipe_time.csv',
        'recipe_takes_time.csv',
        'food_group.csv',
        'ingredients_belongs_to_food_group.csv',
        'recipe_uses_ingredients.csv',
        'dietary_info.csv',
        'recipe_has_dietary_info.csv',
        'recipe_subject.csv',
        'recipe_belongs_to_subject.csv',
        'cook.csv',
        'cook_executes_recipe.csv',
        'cook_knows_cuisine.csv',
        'round.csv',
        'cooks_participate_in_round.csv',
        'cooks_judge_round.csv',
        'cuisines_chosen_for_round.csv',
        'ratings.csv',
        'equipment.csv',
        'recipe_requires_equipment.csv'
    ];

    for (const file of csvFiles) {
        const tableName = file.split('.')[0];
        const filePath = path.join(__dirname, 'backup_data', file);

        try {
            const csvData = await readFileAsync(filePath, 'utf8');
            await new Promise((resolve, reject) => {
                DB.connection.query(`LOAD DATA INFILE ? INTO TABLE ${tableName} FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\\n'`, [filePath], (error, results) => {
                    if (error) {
                        reject(error);
                    } else {
                        resolve();
                    }
                });
            });

            console.log(`Data from ${file} inserted into ${tableName} successfully.`);
        } catch (error) {
            console.error(`Error inserting data from ${file} into ${tableName}:`, error);
        }
    }
}

router.post('/restore', async (req, res) => {
    try {
        await truncateTables();
        await fillTablesFromCSV();
        res.redirect('/dacontest/admin_functions');
    } catch (error) {
        console.error('Error restoring database:', error);
        res.status(500).send('Internal server error.');
    }
});

module.exports = router;
