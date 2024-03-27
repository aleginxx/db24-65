SET FOREIGN_KEY_CHECKS = 0;

DELETE FROM `mydb`.`recipe_requires_equipment`; -- Done
DELETE FROM `mydb`.`equipment`; -- Done
DELETE FROM `mydb`.`ratings`;
DELETE FROM `mydb`.`cuisines_chosen_for_round`; -- Done
DELETE FROM `mydb`.`cooks_judge_round`;
DELETE FROM `mydb`.`cooks_participate_in_round`; -- Done
DELETE FROM `mydb`.`round`; -- Done
DELETE FROM `mydb`.`cook_knows_cuisine`; -- Done
DELETE FROM `mydb`.`cook_executes_recipe`; -- Done
DELETE FROM `mydb`.`cook`; -- Done
DELETE FROM `mydb`.`recipe_belongs_to_subject`; -- Done
DELETE FROM `mydb`.`recipe_subject`; -- Done
DELETE FROM `mydb`.`recipe_has_dietary_info`; -- Done
DELETE FROM `mydb`.`dietary_info`; -- Done
DELETE FROM `mydb`.`recipe_uses_ingredients`; -- Done
DELETE FROM `mydb`.`ingredients_belongs_to_food_group`; -- Done
DELETE FROM `mydb`.`food_group`; -- Done
DELETE FROM `mydb`.`recipe_takes_time`; -- Done
DELETE FROM `mydb`.`recipe_time`; -- Done
DELETE FROM `mydb`.`recipe_has_steps`; -- Done
DELETE FROM `mydb`.`steps`; -- Done
DELETE FROM `mydb`.`recipe_offers_tips`; -- Done
DELETE FROM `mydb`.`tips`; -- Done
DELETE FROM `mydb`.`recipe_has_tags`; -- Done
DELETE FROM `mydb`.`tags`;  -- Done
DELETE FROM `mydb`.`types_of_meal`; -- Done
DELETE FROM `mydb`.`recipe_belongs_to_types_of_meal`; -- Done
DELETE FROM `mydb`.`cuisine`; -- Done
DELETE FROM `mydb`.`recipe`; -- Done
DELETE FROM `mydb`.`ingredients`; -- Done
DELETE FROM `mydb`.`administrator`; -- Done

SET FOREIGN_KEY_CHECKS = 1;
