SELECT r.round_year, r.round_number, COUNT(re.equipment_equipment_id) AS total_equipment_used
FROM round r
JOIN cuisines_chosen_for_round cc ON r.round_id = cc.round_round_id
JOIN cook_knows_cuisine ckc ON cc.cuisine_cuisine_id = ckc.cuisine_cuisine_id
JOIN recipe rcp FORCE INDEX (idx_cuisine_of_recipe) ON ckc.cuisine_cuisine_id = rcp.cuisine_of_recipe
JOIN recipe_requires_equipment re ON rcp.recipe_id = re.recipe_recipe_id
GROUP BY r.round_id
ORDER BY total_equipment_used DESC
LIMIT 1;
