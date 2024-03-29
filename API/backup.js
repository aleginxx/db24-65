const express = require('express');
const router = express.Router();
const path = require('path');
const fs = require('fs');
const util = require('util');
const DB = require('./database.js');

const writeFileAsync = util.promisify(fs.writeFile);

async function exportTableToCSV(tableName, fileName) {
    try {
        const query = `SELECT * FROM ${tableName}`;
        DB.connection.query(query, async (error, results, fields) => {
            if (error) {
                console.error(`Error exporting table '${tableName}' to CSV:`, error);
                return;
            }

            const csvData = results.map(row => {
                return Object.values(row).map(value => {
                    if (typeof value === 'string' && value.includes(',')) {
                        return `"${value}"`;
                    }
                    return value;
                }).join(',');
            });

            const filePath = path.join(__dirname, 'backup_data', fileName);
            await writeFileAsync(filePath, csvData.join('\n'));
        });
    } catch(error) {
        console.error(`Error exporting table '${tableName}' to CSV:`, error);
    }
}

async function exportAllTablesToCSV() {
    const tables = [
        { tableName: 'cuisine', fileName: 'cuisine.csv'},
        { tableName: 'ingredients', fileName: 'ingredients.csv'},
        { tableName: 'recipe', fileName: 'recipe.csv'},
        { tableName: 'recipe_uses_ingredients', fileName: 'recipe_uses_ingredients.csv'},
        { tableName: 'tips', fileName: 'tips.csv'},
        { tableName: 'recipe_offers_tips', fileName: 'recipe_offers_tips.csv'},
        { tableName: 'types_of_meal', fileName: 'types_of_meal.csv'},
        { tableName: 'recipe_belongs_to_types_of_meal', fileName: 'recipe_belongs_to_types_of_meal.csv'},
        { tableName: 'steps', fileName: 'steps.csv'},
        { tableName: 'recipe_has_steps', fileName: 'recipe_has_steps.csv'},
        { tableName: 'food_group', fileName: 'food_group.csv'},
        { tableName: 'ingredients_belongs_to_food_group', fileName: 'ingredients_belongs_to_food_group.csv'},
        { tableName: 'equipment', fileName: 'equipment.csv'},
        { tableName: 'recipe_requires_equipment', fileName: 'recipe_requires_equipment.csv'},
        { tableName: 'round', fileName: 'round.csv'},
        { tableName: 'administrator', fileName: 'administrator.csv'},
        { tableName: 'tags', fileName: 'tags.csv'},
        { tableName: 'recipe_has_tags', fileName: 'recipe_has_tags.csv'},
        { tableName: 'recipe_time', fileName: 'recipe_time.csv'},
        { tableName: 'recipe_takes_time', fileName: 'recipe_takes_time.csv'},
        { tableName: 'dietary_info', fileName: 'dietary_info.csv'},
        { tableName: 'recipe_has_dietary_info', fileName: 'recipe_has_dietary_info.csv'},
        { tableName: 'recipe_subject', fileName: 'recipe_subject.csv'},
        { tableName: 'recipe_belongs_to_subject', fileName: 'recipe_belongs_to_subject.csv'},
        { tableName: 'cook', fileName: 'cook.csv'},
        { tableName: 'cook_executes_recipe', fileName: 'cook_executes_recipe.csv'},
        { tableName: 'cook_knows_cuisine', fileName: 'cook_knows_cuisine.csv'},
        { tableName: 'cuisines_chosen_for_round', fileName: 'cuisines_chosen_for_round.csv'},
        { tableName: 'cooks_participate_in_round', fileName: 'cooks_participate_in_round.csv'},
        { tableName: 'cooks_judge_round', fileName: 'cooks_judge_round.csv'},
        { tableName: 'ratings', fileName: 'ratings.csv'},
    ];

    for (const table of tables) {
        await exportTableToCSV(table.tableName, table.fileName);
    }
}

router.get('/backup', (req, res) => {
    exportAllTablesToCSV();

    console.log(`All tables exported  successfully.`);
});

module.exports = router;