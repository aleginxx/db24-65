INSERT INTO dietary_info (dietary_info_id, fat_grams_per_portion, portein_grams_per_portion, carbs_grams_per_portion, calories_per_portion)
SELECT 
    ri.recipe_recipe_id AS dietary_info_id,
    SUM(i.ingredient_grams_of_fat * ri.quantity_in_grams) / r.no_of_portions AS total_fat,
    SUM(i.ingredient_grams_of_protein * ri.quantity_in_grams) / r.no_of_portions AS total_protein,
    SUM(i.ingredient_grams_of_carbs * ri.quantity_in_grams) / r.no_of_portions AS total_carbs,
    SUM(i.ingredient_calories_per_gram * ri.quantity_in_grams) / r.no_of_portions AS total_calories
FROM 
    recipe_uses_ingredients ri
JOIN 
    ingredients i ON ri.ingredients_ingredient_id = i.ingredient_id
JOIN 
    recipe r ON ri.recipe_recipe_id = r.recipe_id
GROUP BY 
    ri.recipe_recipe_id, r.no_of_portions
HAVING 
    NOT EXISTS (
        SELECT 1 
        FROM dietary_info di 
        WHERE di.dietary_info_id = ri.recipe_recipe_id
    );

INSERT INTO recipe_has_dietary_info (recipe_recipe_id, dietary_info_dietary_info_id)
SELECT 
    r.recipe_id,
    di.dietary_info_id
FROM 
    recipe r
JOIN 
    dietary_info di ON r.recipe_id = di.dietary_info_id
WHERE 
    NOT EXISTS (
        SELECT 1 
        FROM recipe_has_dietary_info rdi 
        WHERE rdi.recipe_recipe_id = r.recipe_id
    )
ORDER BY 
    r.recipe_id;
