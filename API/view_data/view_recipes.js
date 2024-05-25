const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'recipe.html');

router.get('/recipes', (req, res) => {
    res.sendFile(filePath);
});

router.post('/recipes', cookieJwtAuth, (req, res) => {
    const query = `
        SELECT r.recipe_name, r.recipe_type, c.cuisine_name, ingr.ingredient_name, r.recipe_desc, r.level, r.no_of_portions, r.recipe_img
        FROM recipe r
        LEFT JOIN ingredients ingr 
        ON r.primary_ingredient_id = ingr.ingredient_id
        LEFT JOIN cuisine c
        ON r.cuisine_of_recipe = c.cuisine_id
    `;
    DB.connection.query(query, (err, results) => { 
        if (err) {
            console.error('Error fetching recipes data:', err);
            return res.status(500).send('Internal Server Error');
        }

        // console.log(results);
        
        res.status(200).json(results); 
    });
});

const edit_recipe = path.join(__dirname, '..', '..', 'frontend', 'edit-recipes.html');

router.get('/cook/recipes', (req, res) => {
    res.sendFile(edit_recipe);
});

router.post('/cook/recipes', cookieJwtAuth, (req, res) => {
    const { username } = req.user;

    const recipeListQuery = `
        SELECT r.recipe_id
        FROM cook c
        LEFT JOIN cook_executes_recipe cer 
        ON c.cook_id = cer.cook_cook_id
        LEFT JOIN recipe r
        ON cer.recipe_recipe_id = r.recipe_id
        WHERE c.username = ?
    `;

    const recipeCharQuery = `
        SELECT r.recipe_name, r.recipe_type, c.cuisine_name, ingr.ingredient_name, r.recipe_desc, r.level, r.no_of_portions, r.recipe_img
        FROM recipe r
        LEFT JOIN ingredients ingr 
        ON r.primary_ingredient_id = ingr.ingredient_id
        LEFT JOIN cuisine c
        ON r.cuisine_of_recipe = c.cuisine_id
        WHERE r.recipe_id IN (?)
    `;

    DB.connection.query(recipeListQuery, [username], (err, recipeListRes) => { 
        if (err) {
            console.error('Error fetching recipes data:', err);
            return res.status(500).send('Internal Server Error');
        }

        const recipeIds = recipeListRes.map(row => row.recipe_id);
        // console.log(recipeIds);

        DB.connection.query(recipeCharQuery, [recipeIds], (err, results) => { 
            if (err) {
                console.error('Error fetching recipes data:', err);
                return res.status(500).send('Internal Server Error');
            }
    
            // console.log(results);
            
            res.status(200).json(results); 
        });
    });
});

router.post('/recipes/edit', cookieJwtAuth, (req, res) => {
    const { recipe_name, recipe_type, cuisine_name, ingredient_name, recipe_desc, level, no_of_portions } = req.body;
    const { username } = req.user;

    const recipeIdQuery = `
        SELECT r.recipe_id
        FROM recipe r
        LEFT JOIN cook_executes_recipe cer 
        ON r.recipe_id = cer.recipe_recipe_id
        LEFT JOIN cook c
        ON cer.cook_cook_id = c.cook_id
        WHERE c.username = ? AND r.recipe_name = ?
    `;

    DB.connection.query(recipeIdQuery, [username, recipe_name], (err, results) => {
        if (err) {
            console.error('Error updating recipe:', err);
            return res.status(500).send('Internal Server Error');
        }

        if (results.length === 0) {
            return res.status(404).send('Recipe not found');
        }

        const recipe_id = results[0].recipe_id;

        const updateRecipeQuery = `
            UPDATE recipe AS r
            LEFT JOIN ingredients AS ingr ON r.primary_ingredient_id = ingr.ingredient_id
            LEFT JOIN cuisine AS c ON r.cuisine_of_recipe = c.cuisine_id
            SET 
                r.recipe_name = ?,
                r.recipe_type = ?,
                c.cuisine_name = ?,
                ingr.ingredient_name = ?,
                r.recipe_desc = ?,
                r.level = ?,
                r.no_of_portions = ?
            WHERE r.recipe_id = ?
        `;

        DB.connection.query(updateRecipeQuery, [recipe_name, recipe_type, cuisine_name, ingredient_name, recipe_desc, level, no_of_portions, recipe_id], (err, results) => {
            if (err) {
                // console.error('Error updating recipe:', err);
                return res.status(500).send('Internal Server Error');
            }

            res.status(200).redirect('/dacontest/cook/recipes');
        });
    });
});

const recipeAddPath = path.join(__dirname, '..', '..', 'frontend', 'add-recipe.html');

router.get('/recipe/add', (req, res) => {
    res.sendFile(recipeAddPath);
});

router.post('/recipe/add', cookieJwtAuth, (req, res) => {
    const {recipe_name, recipe_type, cuisine, level, recipe_desc, no_of_portions, primary_ingredient, recipe_img} = req.body;

    console.log("Body: ", req.body); 

    const insertIngredientQuery = `
        INSERT INTO ingredients (ingredient_name)
        SELECT ? WHERE NOT EXISTS (SELECT 1 FROM ingredients WHERE ingredient_name = ?);
    `;

    const findIngredientIdQuery = `SELECT ingredient_id FROM ingredients WHERE ingredient_name = ?`;

    const insertCuisineQuery = `
        INSERT INTO cuisine (cuisine_name)
        SELECT ? WHERE NOT EXISTS (SELECT 1 FROM cuisine WHERE cuisine_name = ?);
    `;

    const findCuisineIdQuery = `SELECT cuisine_id FROM cuisine WHERE cuisine_name = ?`;

    const insertRecipeQuery = `
        INSERT INTO recipe (recipe_name, recipe_type, cuisine_of_recipe, primary_ingredient_id, recipe_desc, level, no_of_portions, recipe_img)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    `;

    DB.connection.query(insertIngredientQuery, [primary_ingredient, primary_ingredient], (err, insertIngredientResults) => { 
        if (err) {
            if (err.code === 'ER_DUP_ENTRY') {
                console.error('Ingredient already exists:', primary_ingredient);;
            } else {
                console.error('Error inserting ingredient:', err);
                return res.status(500).send('Internal Server Error');
            }
        }

        DB.connection.query(findIngredientIdQuery, [primary_ingredient], (err, ingredientIdResults) => { 
            if (err) {
                console.error('Error fetching ingredient id:', err);
                return res.status(500).send('Internal Server Error');
            }
            
            const primary_ingredient_id = ingredientIdResults[0].ingredient_id;

            DB.connection.query(insertCuisineQuery, [cuisine, cuisine], (err, insertCuisineResults) => { 
                if (err) {
                    if (err.code === 'ER_DUP_ENTRY') {
                        console.log('Cuisine already exists:', cuisine);;
                    } else {
                        console.error('Error inserting cuisine:', err);
                        return res.status(500).send('Internal Server Error');
                    }
                }

                DB.connection.query(findCuisineIdQuery, [cuisine], (err, cuisineIdResults) => { 
                    if (err) {
                        console.error('Error fetching cuisine id:', err);
                        return res.status(500).send('Internal Server Error');
                    }

                    // console.log("Cuisine Id Results: ", cuisineIdResults);
                    const cuisineId = cuisineIdResults[0].cuisine_id;

                    DB.connection.query(insertRecipeQuery, [recipe_name, recipe_type, cuisineId, primary_ingredient_id, recipe_desc, level, no_of_portions, recipe_img], (err, insertRecipeResults) => { 
                        if (err) {
                            console.error('Error inserting recipe:', err);
                            return res.status(500).send('Internal Server Error');
                        }

                        res.status(200).redirect('/dacontest/recipes');
                    });
                });
            }); 
        });
    });
});

module.exports = router;
