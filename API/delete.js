const express = require('express');
const router = express.Router();
const DB = require('./db'); // Adjust the path as necessary

router.post('/delete', (req, res) => {
    const tableName = req.body.tableName;
    const rowID = req.body.rowID;
    const primaryKey = req.body.primaryKey;

    // Function to delete dependencies
    const deleteDependencies = (table, id, callback) => {
        switch (table) {
            case 'cook':
                deleteCookDependencies(id, callback);
                break;
            case 'recipe':
                deleteRecipeDependencies(id, callback);
                break;
            // Add more cases for other tables with dependencies
            default:
                callback();
        }
    };

    const deleteCookDependencies = (cookID, callback) => {
        const queries = [
            `DELETE FROM cook_executes_recipe WHERE cook_id = ?`,
            `DELETE FROM cook_knows_cuisine WHERE cook_id = ?`,
            `DELETE FROM cooks_judge_round WHERE cook_id = ?`,
            `DELETE FROM cooks_participate_in_round WHERE cook_id = ?`
        ];

        executeQueries(queries, cookID, callback);
    };

    const deleteRecipeDependencies = (recipeID, callback) => {
        const queries = [
            `DELETE FROM cook_executes_recipe WHERE recipe_id = ?`,
            `DELETE FROM recipe_belongs_to_subject WHERE recipe_id = ?`,
            `DELETE FROM recipe_belongs_to_types_of_meal WHERE recipe_id = ?`,
            `DELETE FROM recipe_has_dietary_info WHERE recipe_id = ?`,
            `DELETE FROM recipe_has_steps WHERE recipe_id = ?`,
            `DELETE FROM recipe_has_tags WHERE recipe_id = ?`,
            `DELETE FROM recipe_offers_tips WHERE recipe_id = ?`,
            `DELETE FROM recipe_requires_equipment WHERE recipe_id = ?`,
            `DELETE FROM recipe_uses_ingredients WHERE recipe_id = ?`
        ];

        executeQueries(queries, recipeID, callback);
    };

    const executeQueries = (queries, id, callback) => {
        let completed = 0;
        queries.forEach((query) => {
            DB.connection.query(query, [id], (err, result) => {
                if (err) {
                    console.error('Error executing query:', err);
                    callback(err);
                    return;
                }
                completed += 1;
                if (completed === queries.length) {
                    callback();
                }
            });
        });
    };

    // First, delete dependencies
    deleteDependencies(tableName, rowID, (err) => {
        if (err) {
            res.status(500).json({ error: 'Error deleting dependencies' });
            return;
        }

        // Then delete the main entity
        const deleteQuery = `DELETE FROM ${tableName} WHERE ${primaryKey} = ?`;

        DB.connection.query(deleteQuery, [rowID], (err, result) => {
            if (err) {
                console.error('Error executing delete query:', err);
                res.status(500).json({ error: 'Error executing delete query' });
            } else {
                res.status(200).json({ success: true });
            }
        });
    });
});

module.exports = router;
