import pandas as pd
import mysql.connector 
import random

db_connection = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)

# Load data from 'cuisine.csv' into table 'cuisine'
query = """
LOAD DATA INFILE 'cuisine.csv'
INTO TABLE cuisine
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cuisine_id, cuisine_name)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'ingredients.csv' into table 'ingredients'
query = """
LOAD DATA INFILE 'ingredients.csv'
INTO TABLE ingredients
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ingredient_id, ingredient_name, ingredient_grams_of_fat, ingredient_grams_of_protein, ingredient_grams_of_carbs, ingredient_calories_per_gram, ingredient_img)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe.csv' into table 'recipe'
query = """
LOAD DATA INFILE 'recipe.csv'
INTO TABLE recipe
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_id, recipe_name, recipe_type, cuisine_of_recipe, level, recipe_desc, no_of_portions, primary_ingredient_id, recipe_img)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

query="""
INSERT INTO `mydb`.`recipe` (recipe_id, recipe_name, recipe_type, cuisine_of_recipe, level, recipe_desc, no_of_portions, primary_ingredient_id, recipe_img)
VALUES (136, 'Sardine Mediterranean Pasta', 'cooking', 9, 2, 'Mediterranean-inspired pasta dish featuring savory sardines, olives, tomatoes, and capers in a flavorful herb-infused sauce.', 5, 77, 'IMG_20180814_172611816_HDR.jpg (https://v5.airtableusercontent.com/v3/u/26/26/1710374400000/-lh5WIZeJEWw0UKrHyAQCg/g5DKUzcyyaOUGOC3EHIcK7rZ3agO9jIabL7JuRhI1Op6yKm-sp3VI3WFN6gXXqGBd0tosDpIv7YRph50M-8ZR9zZj9FJ33lUd0DbHZwSMZBXIYNnlz49alKPIlVWtfki/X5pkScPT3_JZzaFkyFXnPhOJ4huP4mGgQRReMfi0UyU)');
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()


# Load data from 'recipe_ingredients.csv' into table 'recipe_uses_ingredients'
query = """
LOAD DATA INFILE 'recipe_ingredients.csv'
INTO TABLE recipe_uses_ingredients
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, ingredients_ingredient_id, quantity_in_grams)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'tips.csv' into table 'tips'
query = """
LOAD DATA INFILE 'tips.csv'
INTO TABLE tips
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(tips_id, tip_desc)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_tips.csv' into table 'recipe_offers_tips'
query = """
LOAD DATA INFILE 'recipe_tips.csv'
INTO TABLE recipe_offers_tips
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, tips_tips_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'types_of_meal.csv' into table 'types_of_meal'
query = """
LOAD DATA INFILE 'types_of_meal.csv'
INTO TABLE types_of_meal
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(meal_type_id, meal_type_name)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_meal.csv' into table 'recipe_belongs_to_types_of_meal'
query = """
LOAD DATA INFILE 'recipe_meal.csv'
INTO TABLE recipe_belongs_to_types_of_meal
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, types_of_meal_meal_type_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'steps.csv' into table 'steps'
query = """
LOAD DATA INFILE 'steps.csv'
INTO TABLE steps
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(step_id, step_desc)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_steps.csv' into table 'recipe_has_steps'
query = """
LOAD DATA INFILE 'recipe_steps.csv'
INTO TABLE recipe_has_steps
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, steps_step_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'food_groups.csv' into table 'food_group'
query = """
LOAD DATA INFILE 'food_groups.csv'
INTO TABLE food_group
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(food_group_id, food_group_name, food_group_desc, food_group_categorization, food_group_img)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'ingredients_food_group.csv' into table 'ingredients_belongs_to_food_group'
query = """
LOAD DATA INFILE 'ingredients_food_group.csv'
INTO TABLE ingredients_belongs_to_food_group
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ingredients_ingredient_id, food_group_food_group_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'equipment.csv' into table 'equipment'
query = """
LOAD DATA INFILE 'equipment.csv'
INTO TABLE equipment
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(equipment_id, equipment_name, instructions, equipment_img)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_equipment.csv' into table 'recipe_requires_equipment'
query = """
LOAD DATA INFILE 'recipe_equipment.csv'
INTO TABLE recipe_requires_equipment
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, equipment_equipment_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'rounds.csv' into table 'round'
query = """
LOAD DATA INFILE 'rounds.csv'
INTO TABLE round
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(round_id, round_year, round_number, round_img)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'administrator.csv' into table 'administrator'
query = """
LOAD DATA INFILE 'administrator.csv'
INTO TABLE administrator
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(admin_id, admin_username, admin_password)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'tags.csv' into table 'tags'
query = """
LOAD DATA INFILE 'tags.csv'
INTO TABLE tags
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(tag_id, tag_desc)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_tag.csv' into table 'recipe_has_tags'
query = """
LOAD DATA INFILE 'recipe_tag.csv'
INTO TABLE recipe_has_tags
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, tags_tag_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'time.csv' into table 'recipe_time'
query = """
LOAD DATA INFILE 'time.csv'
INTO TABLE recipe_time
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(total_time, preparation_time, execution_time)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_takes_time.csv' into table 'recipe_takes_time'
query = """
LOAD DATA INFILE 'recipe_takes_time.csv'
INTO TABLE recipe_takes_time
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, recipe_time_total_time)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data into tables 'dietary_info' and 'recipe_has_dietary_info' using a procedure
batch_size = 100
total_recipes = 143

for offset in range(0, total_recipes, batch_size):
    batch_query = """
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
        )
    LIMIT {}, {}
    """.format(offset, batch_size)

    cursor = db_connection.cursor()
    cursor.execute(batch_query)
    db_connection.commit()

insert_query = """
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
"""

cursor = db_connection.cursor()
cursor.execute(insert_query)
db_connection.commit()

# Load data from 'subject.csv' into table 'recipe_subject'
query = """
LOAD DATA INFILE 'subject.csv'
INTO TABLE recipe_subject
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(subject_id, subject_name, subject_desc, subject_img)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'recipe_subject.csv' into table 'recipe_belongs_to_subject'
query = """
LOAD DATA INFILE 'recipe_subject.csv'
INTO TABLE recipe_belongs_to_subject
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(recipe_recipe_id, recipe_subject_subject_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'cook.csv' into table 'cook'
query = """
LOAD DATA INFILE 'cook.csv'
INTO TABLE cook
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cook_id, first_name, last_name, phone_number, birth_date, age, years_of_experience, position, cook_img, username, @password)
SET password = TRIM(TRAILING '\r' FROM @password);
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'cook_executes_recipe.csv' into table 'cook_executes_recipe'
query = """
LOAD DATA INFILE 'cook_executes_recipe.csv'
INTO TABLE cook_executes_recipe
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cook_cook_id, recipe_recipe_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data from 'cook_knows_cuisine.csv' into table 'cook_knows_cuisine'
query = """
LOAD DATA INFILE 'cook_knows_cuisine.csv'
INTO TABLE cook_knows_cuisine
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cook_cook_id, cuisine_cuisine_id, years_of_expertise)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

# Load data into table 'cuisines_chosen_for_round' using a procedure
def fill_cuisines_for_rounds():
    cursor = db_connection.cursor()

    cursor.execute("SELECT round_id FROM round")
    round_ids = cursor.fetchall()

    for round_id in round_ids:
        round_id = round_id[0]
        counter = 0
        consecutive_count = 0
        last_cuisine_id = None
        
        while counter < 10:
            cursor.execute("""
                SELECT c.cuisine_id 
                FROM cuisine c
                INNER JOIN recipe r ON c.cuisine_id = r.cuisine_of_recipe
                WHERE c.cuisine_id NOT IN (
                    SELECT cuisine_cuisine_id 
                    FROM cuisines_chosen_for_round 
                    WHERE round_round_id >= %s - 2 AND round_round_id <= %s
                ) 
                ORDER BY RAND() 
                LIMIT 1
            """, (round_id, round_id))
            cuisines = cursor.fetchall()
            
            if cuisines:
                cuisine_id = cuisines[0][0]
                
                if cuisine_id == last_cuisine_id:
                    consecutive_count += 1
                else:
                    consecutive_count = 0 
                    last_cuisine_id = cuisine_id

                cursor.execute("INSERT INTO cuisines_chosen_for_round (cuisine_cuisine_id, round_round_id) VALUES (%s, %s)", (cuisine_id, round_id))
                counter += 1

                if counter >= 10:
                    break
                elif consecutive_count >= 3:
                    break
            else:
                break

    db_connection.commit()
    cursor.close()

fill_cuisines_for_rounds()

# Load data from 'cooks_participate_in_round.csv' into table 'cooks_participate_in_round'
query = """
LOAD DATA INFILE 'cooks_participate_in_round.csv'
INTO TABLE cooks_participate_in_round
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cook_cook_id, round_round_id, recipe_cuisine_id)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()


# Load data into table 'cooks_judge_round' using a procedure
cursor = db_connection.cursor()

def get_unique_cook_ids(round_id):
    cursor.execute("""
        SELECT c.cook_id
        FROM cook c
        LEFT JOIN cooks_participate_in_round p ON c.cook_id = p.cook_cook_id AND p.cook_cook_id = %s
        LEFT JOIN cooks_judge_round j ON c.cook_id = j.cook_cook_id AND j.round_round_id = %s
        WHERE p.cook_cook_id IS NULL AND j.cook_cook_id IS NULL
        ORDER BY RAND()
        LIMIT 3
    """, (round_id, round_id))
    return [row[0] for row in cursor.fetchall()]

def populate_cooks_judge_round():
    cursor.execute("SELECT round_id FROM round")
    for (round_id,) in cursor.fetchall():
        cook_ids = get_unique_cook_ids(round_id)
        for cook_id in cook_ids:
            cursor.execute("INSERT INTO cooks_judge_round (cook_cook_id, round_round_id) VALUES (%s, %s)", (cook_id, round_id))
            db_connection.commit()

populate_cooks_judge_round()

# Load data into table 'ratings' using a procedure
cursor = db_connection.cursor()

cursor.execute("SELECT round_id FROM round")
round_ids = cursor.fetchall()

for round_id in round_ids:
    cursor.execute("SELECT cook_cook_id FROM cooks_participate_in_round WHERE round_round_id = %s ORDER BY RAND() LIMIT 10", (round_id[0],))
    contestant_ids = cursor.fetchall()
    
    cursor.execute("SELECT cook_cook_id FROM cooks_judge_round WHERE round_round_id = %s", (round_id[0],))
    judge_ids = cursor.fetchall()
    
    num_judges = len(judge_ids)
    
    judge_counter = 0
    
    for contestant_id in contestant_ids:
        judge_id = judge_ids[judge_counter % num_judges][0]
        
        rating_value = random.randint(1, 5)
        
        cursor.execute("INSERT INTO ratings (round_id, contestant_id, judge_id, rating_value) VALUES (%s, %s, %s, %s)", (round_id[0], contestant_id[0], judge_id, rating_value))
        
        judge_counter += 1

db_connection.commit()

# Update table 'round' for the winner of each round
query = """
UPDATE mydb.round AS r
JOIN (
    SELECT round_id, contestant_id
    FROM mydb.ratings
    WHERE (round_id, rating_value) IN (
        SELECT round_id, MAX(rating_value)
        FROM mydb.ratings
        GROUP BY round_id
    )
) AS max_ratings ON r.round_id = max_ratings.round_id
SET r.round_winner = max_ratings.contestant_id;
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()

cursor.close()
db_connection.close()