DROP TEMPORARY TABLE IF EXISTS temp_top_recipe_pairs;
CREATE TEMPORARY TABLE temp_top_recipe_pairs (
    recipe_name1 VARCHAR(100),
    recipe_name2 VARCHAR(100),
    common_tags_count INT
);

INSERT INTO temp_top_recipe_pairs (recipe_name1, recipe_name2, common_tags_count)
SELECT r1.recipe_name AS recipe_name1, r2.recipe_name AS recipe_name2, COUNT(*) AS common_tags_count
FROM recipe_has_tags rht1 FORCE INDEX (recipe_id_UNIQUE)
JOIN recipe_has_tags rht2 FORCE INDEX (recipe_id_UNIQUE) ON rht1.tags_tag_id = rht2.tags_tag_id AND rht1.recipe_recipe_id < rht2.recipe_recipe_id
JOIN recipe r1 FORCE INDEX (PRIMARY) ON rht1.recipe_recipe_id = r1.recipe_id
JOIN recipe r2 FORCE INDEX (PRIMARY) ON rht2.recipe_recipe_id = r2.recipe_id
GROUP BY r1.recipe_id, r2.recipe_id
ORDER BY common_tags_count DESC
LIMIT 5; 

SELECT c1.recipe_name1, c1.recipe_name2, COUNT(*) AS appearances
FROM temp_top_recipe_pairs c1
JOIN cooks_participate_in_round cp1 FORCE INDEX (PRIMARY) ON cp1.recipe_cuisine_id = (SELECT cuisine_of_recipe FROM recipe WHERE recipe_name = c1.recipe_name1)
JOIN cooks_participate_in_round cp2 FORCE INDEX (PRIMARY) ON cp2.recipe_cuisine_id = (SELECT cuisine_of_recipe FROM recipe WHERE recipe_name = c1.recipe_name2)
GROUP BY c1.recipe_name1, c1.recipe_name2
ORDER BY appearances DESC
LIMIT 3; 
