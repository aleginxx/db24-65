-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ingredients` (
  `ingredient_id` INT NOT NULL AUTO_INCREMENT,
  `ingredient_name` VARCHAR(45) NOT NULL,
  `ingredient_grams_of_fat` INT NOT NULL,
  `ingredient_grams_of_protein` INT NOT NULL,
  `ingredient_grams_of_carbs` INT NOT NULL,
  `ingredient_calories_per_gram` INT NOT NULL,
  `ingredient_img` LONGTEXT NOT NULL,
  PRIMARY KEY (`ingredient_id`),
  UNIQUE INDEX `ingredient_id_UNIQUE` (`ingredient_id` ASC) ,
  UNIQUE INDEX `ingredient_name_UNIQUE` (`ingredient_name` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cuisine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cuisine` (
  `cuisine_id` INT NOT NULL AUTO_INCREMENT,
  `cuisine_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cuisine_id`),
  UNIQUE INDEX `cuisine_id_UNIQUE` (`cuisine_id` ASC) ,
  UNIQUE INDEX `cuisine_name_UNIQUE` (`cuisine_name` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe` (
  `recipe_id` INT NOT NULL AUTO_INCREMENT,
  `recipe_name` VARCHAR(45) NOT NULL,
  `recipe_type` VARCHAR(45) NOT NULL,
  `cuisine_of_recipe` INT NOT NULL,
  `level` INT NOT NULL,
  `recipe_desc` MEDIUMTEXT NOT NULL,
  `no_of_portions` INT NULL,
  `primary_ingredient_id` INT NOT NULL,
  `recipe_img` LONGTEXT NULL,
  PRIMARY KEY (`recipe_id`),
  UNIQUE INDEX `recipe_id_UNIQUE` (`recipe_id` ASC) ,
  INDEX `fk_recipe_ingredients1_idx` (`primary_ingredient_id` ASC) ,
  INDEX `fk_recipe_cuisine1_idx` (`cuisine_of_recipe` ASC) ,
  CONSTRAINT `fk_recipe_ingredients1`
    FOREIGN KEY (`primary_ingredient_id`)
    REFERENCES `mydb`.`ingredients` (`ingredient_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_cuisine1`
    FOREIGN KEY (`cuisine_of_recipe`)
    REFERENCES `mydb`.`cuisine` (`cuisine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`types_of_meal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`types_of_meal` (
  `meal_type_id` INT NOT NULL AUTO_INCREMENT,
  `meal_type_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`meal_type_id`),
  UNIQUE INDEX `meal_type_id_UNIQUE` (`meal_type_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_belongs_to_types_of_meal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_belongs_to_types_of_meal` (
  `recipe_recipe_id` INT NOT NULL,
  `types_of_meal_meal_type_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `types_of_meal_meal_type_id`),
  INDEX `fk_recipe_has_types_of_meal_types_of_meal1_idx` (`types_of_meal_meal_type_id` ASC) ,
  INDEX `fk_recipe_has_types_of_meal_recipe_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_types_of_meal_recipe`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_types_of_meal_types_of_meal1`
    FOREIGN KEY (`types_of_meal_meal_type_id`)
    REFERENCES `mydb`.`types_of_meal` (`meal_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tags` (
  `tag_id` INT NOT NULL AUTO_INCREMENT,
  `tag_desc` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`tag_id`),
  UNIQUE INDEX `tag_id_UNIQUE` (`tag_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_has_tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_has_tags` (
  `recipe_recipe_id` INT NOT NULL,
  `tags_tag_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `tags_tag_id`),
  INDEX `fk_recipe_has_tags_tags1_idx` (`tags_tag_id` ASC) ,
  INDEX `fk_recipe_has_tags_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_tags_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_tags_tags1`
    FOREIGN KEY (`tags_tag_id`)
    REFERENCES `mydb`.`tags` (`tag_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tips` (
  `tips_id` INT NOT NULL AUTO_INCREMENT,
  `tip_desc` LONGTEXT NOT NULL,
  UNIQUE INDEX `tips_id_UNIQUE` (`tips_id` ASC) ,
  PRIMARY KEY (`tips_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_offers_tips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_offers_tips` (
  `recipe_recipe_id` INT NOT NULL,
  `tips_tips_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `tips_tips_id`),
  INDEX `fk_recipe_has_tips_tips1_idx` (`tips_tips_id` ASC) ,
  INDEX `fk_recipe_has_tips_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_tips_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_tips_tips1`
    FOREIGN KEY (`tips_tips_id`)
    REFERENCES `mydb`.`tips` (`tips_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`steps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`steps` (
  `step_id` INT NOT NULL AUTO_INCREMENT,
  `step_desc` LONGTEXT NOT NULL,
  PRIMARY KEY (`step_id`),
  UNIQUE INDEX `step_id_UNIQUE` (`step_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_has_steps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_has_steps` (
  `recipe_recipe_id` INT NOT NULL,
  `steps_step_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `steps_step_id`),
  INDEX `fk_recipe_has_steps_steps1_idx` (`steps_step_id` ASC) ,
  INDEX `fk_recipe_has_steps_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_steps_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_steps_steps1`
    FOREIGN KEY (`steps_step_id`)
    REFERENCES `mydb`.`steps` (`step_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_time`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_time` (
  `total_time` INT NOT NULL,
  `preparation_time` INT NOT NULL,
  `execution_time` INT NOT NULL,
  PRIMARY KEY (`total_time`, `preparation_time`, `execution_time`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_takes_time`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_takes_time` (
  `recipe_recipe_id` INT NOT NULL,
  `recipe_time_total_time` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `recipe_time_total_time`),
  INDEX `fk_recipe_has_recipe_time_recipe_time1_idx` (`recipe_time_total_time` ASC) ,
  INDEX `fk_recipe_has_recipe_time_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_recipe_time_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_recipe_time_recipe_time1`
    FOREIGN KEY (`recipe_time_total_time`)
    REFERENCES `mydb`.`recipe_time` (`total_time`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`food_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`food_group` (
  `food_group_id` INT NOT NULL,
  `food_group_name` VARCHAR(45) NOT NULL,
  `food_group_desc` VARCHAR(45) NULL,
  `food_group_categorization` VARCHAR(45) NOT NULL,
  `food_group_img` LONGTEXT NOT NULL,
  PRIMARY KEY (`food_group_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ingredients_belongs_to_food_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ingredients_belongs_to_food_group` (
  `ingredients_ingredient_id` INT NOT NULL,
  `food_group_food_group_id` INT NOT NULL,
  PRIMARY KEY (`ingredients_ingredient_id`, `food_group_food_group_id`),
  INDEX `fk_ingredients_has_food_group_food_group1_idx` (`food_group_food_group_id` ASC) ,
  INDEX `fk_ingredients_has_food_group_ingredients1_idx` (`ingredients_ingredient_id` ASC) ,
  CONSTRAINT `fk_ingredients_has_food_group_ingredients1`
    FOREIGN KEY (`ingredients_ingredient_id`)
    REFERENCES `mydb`.`ingredients` (`ingredient_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingredients_has_food_group_food_group1`
    FOREIGN KEY (`food_group_food_group_id`)
    REFERENCES `mydb`.`food_group` (`food_group_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_uses_ingredients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_uses_ingredients` (
  `recipe_recipe_id` INT NOT NULL,
  `ingredients_ingredient_id` INT NOT NULL,
  `quantity_in_grams` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `ingredients_ingredient_id`),
  INDEX `fk_recipe_has_ingredients_ingredients1_idx` (`ingredients_ingredient_id` ASC) ,
  INDEX `fk_recipe_has_ingredients_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_ingredients_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_ingredients_ingredients1`
    FOREIGN KEY (`ingredients_ingredient_id`)
    REFERENCES `mydb`.`ingredients` (`ingredient_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`dietary_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dietary_info` (
  `dietary_info_id` INT NOT NULL AUTO_INCREMENT,
  `fat_grams_per_portion` INT NOT NULL,
  `portein_grams_per_portion` INT NOT NULL,
  `carbs_grams_per_portion` INT NOT NULL,
  `calories_per_portion` INT NOT NULL,
  PRIMARY KEY (`dietary_info_id`),
  UNIQUE INDEX `dietary_info_id_UNIQUE` (`dietary_info_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_has_dietary_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_has_dietary_info` (
  `recipe_recipe_id` INT NOT NULL,
  `dietary_info_dietary_info_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `dietary_info_dietary_info_id`),
  INDEX `fk_recipe_has_dietary_info_dietary_info1_idx` (`dietary_info_dietary_info_id` ASC) ,
  INDEX `fk_recipe_has_dietary_info_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_dietary_info_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_dietary_info_dietary_info1`
    FOREIGN KEY (`dietary_info_dietary_info_id`)
    REFERENCES `mydb`.`dietary_info` (`dietary_info_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_subject` (
  `subject_id` INT NOT NULL AUTO_INCREMENT,
  `subject_name` VARCHAR(45) NOT NULL,
  `subject_desc` MEDIUMTEXT NOT NULL,
  `subject_img` LONGTEXT NOT NULL,
  PRIMARY KEY (`subject_id`),
  UNIQUE INDEX `subject_id_UNIQUE` (`subject_id` ASC) ,
  UNIQUE INDEX `subject_name_UNIQUE` (`subject_name` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_belongs_to_subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_belongs_to_subject` (
  `recipe_recipe_id` INT NOT NULL,
  `recipe_subject_subject_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `recipe_subject_subject_id`),
  INDEX `fk_recipe_has_recipe_subject_recipe_subject1_idx` (`recipe_subject_subject_id` ASC) ,
  INDEX `fk_recipe_has_recipe_subject_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_recipe_subject_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_recipe_subject_recipe_subject1`
    FOREIGN KEY (`recipe_subject_subject_id`)
    REFERENCES `mydb`.`recipe_subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cook`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cook` (
  `cook_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `birth_date` DATE NOT NULL,
  `age` INT NOT NULL,
  `years_of_experience` INT NOT NULL,
  `position` VARCHAR(45) NOT NULL,
  `cook_img` LONGTEXT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cook_id`),
  UNIQUE INDEX `cook_id_UNIQUE` (`cook_id` ASC) ,
  UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) ,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cook_executes_recipe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cook_executes_recipe` (
  `cook_cook_id` INT NOT NULL,
  `recipe_recipe_id` INT NOT NULL,
  PRIMARY KEY (`cook_cook_id`, `recipe_recipe_id`),
  INDEX `fk_cook_has_recipe_recipe1_idx` (`recipe_recipe_id` ASC) ,
  INDEX `fk_cook_has_recipe_cook1_idx` (`cook_cook_id` ASC) ,
  CONSTRAINT `fk_cook_has_recipe_cook1`
    FOREIGN KEY (`cook_cook_id`)
    REFERENCES `mydb`.`cook` (`cook_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cook_has_recipe_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cook_knows_cuisine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cook_knows_cuisine` (
  `cuisine_cuisine_id` INT NOT NULL,
  `cook_cook_id` INT NOT NULL,
  `years_of_expertise` INT NOT NULL,
  PRIMARY KEY (`cuisine_cuisine_id`, `cook_cook_id`),
  INDEX `fk_cuisine_has_cook_cook1_idx` (`cook_cook_id` ASC) ,
  INDEX `fk_cuisine_has_cook_cuisine1_idx` (`cuisine_cuisine_id` ASC) ,
  CONSTRAINT `fk_cuisine_has_cook_cuisine1`
    FOREIGN KEY (`cuisine_cuisine_id`)
    REFERENCES `mydb`.`cuisine` (`cuisine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cuisine_has_cook_cook1`
    FOREIGN KEY (`cook_cook_id`)
    REFERENCES `mydb`.`cook` (`cook_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`round` (
  `round_id` INT NOT NULL AUTO_INCREMENT,
  `round_year` INT NOT NULL,
  `round_number` INT NOT NULL,
  `round_img` LONGTEXT NULL,
  PRIMARY KEY (`round_id`),
  UNIQUE INDEX `roubnd_id_UNIQUE` (`round_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cooks_participate_in_round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cooks_participate_in_round` (
  `cook_cook_id` INT NOT NULL,
  `round_round_id` INT NOT NULL,
  `recipe_cuisine_id` INT NOT NULL,
  PRIMARY KEY (`cook_cook_id`, `round_round_id`),
  INDEX `fk_cook_has_round_round1_idx` (`round_round_id` ASC) ,
  INDEX `fk_cook_has_round_cook1_idx` (`cook_cook_id` ASC) ,
  INDEX `fk_cooks_participate_in_round_cuisine1_idx` (`recipe_cuisine_id` ASC) ,
  CONSTRAINT `fk_cook_has_round_cook1`
    FOREIGN KEY (`cook_cook_id`)
    REFERENCES `mydb`.`cook` (`cook_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cook_has_round_round1`
    FOREIGN KEY (`round_round_id`)
    REFERENCES `mydb`.`round` (`round_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cooks_participate_in_round_cuisine1_idx`
    FOREIGN KEY (`recipe_cuisine_id`)
    REFERENCES `mydb`.`recipe` (`cuisine_of_recipe`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cooks_judge_round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cooks_judge_round` (
  `cook_cook_id` INT NOT NULL,
  `round_round_id` INT NOT NULL,
  PRIMARY KEY (`cook_cook_id`, `round_round_id`),
  INDEX `fk_cook_has_round_round2_idx` (`round_round_id` ASC) ,
  INDEX `fk_cook_has_round_cook2_idx` (`cook_cook_id` ASC) ,
  CONSTRAINT `fk_cook_has_round_cook2`
    FOREIGN KEY (`cook_cook_id`)
    REFERENCES `mydb`.`cook` (`cook_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cook_has_round_round2`
    FOREIGN KEY (`round_round_id`)
    REFERENCES `mydb`.`round` (`round_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cuisines_chosen_for_round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cuisines_chosen_for_round` (
  `cuisine_cuisine_id` INT NOT NULL,
  `round_round_id` INT NOT NULL,
  PRIMARY KEY (`cuisine_cuisine_id`, `round_round_id`),
  INDEX `fk_cuisine_has_round_round1_idx` (`round_round_id` ASC) ,
  INDEX `fk_cuisine_has_round_cuisine1_idx` (`cuisine_cuisine_id` ASC) ,
  CONSTRAINT `fk_cuisine_has_round_cuisine1`
    FOREIGN KEY (`cuisine_cuisine_id`)
    REFERENCES `mydb`.`cuisine` (`cuisine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cuisine_has_round_round1`
    FOREIGN KEY (`round_round_id`)
    REFERENCES `mydb`.`round` (`round_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ratings` (
  `rating_id` INT NOT NULL AUTO_INCREMENT,
  `round_id` INT NOT NULL,
  `contestant_id` INT NOT NULL,
  `judge_id` INT NOT NULL,
  `rating_value` INT NOT NULL,
  PRIMARY KEY (`rating_id`),
  UNIQUE INDEX `rating_id_UNIQUE` (`rating_id` ASC) ,
  INDEX `fk_ratings_round1_idx` (`round_id` ASC) ,
  INDEX `fk_ratings_cook1_idx` (`contestant_id` ASC) ,
  INDEX `fk_ratings_cook2_idx` (`judge_id` ASC) ,
  CONSTRAINT `fk_ratings_round1`
    FOREIGN KEY (`round_id`)
    REFERENCES `mydb`.`round` (`round_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ratings_cook1`
    FOREIGN KEY (`contestant_id`)
    REFERENCES `mydb`.`cook` (`cook_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ratings_cook2`
    FOREIGN KEY (`judge_id`)
    REFERENCES `mydb`.`cook` (`cook_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`equipment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`equipment` (
  `equipment_id` INT NOT NULL AUTO_INCREMENT,
  `equipment_name` VARCHAR(45) NOT NULL,
  `instructions` MEDIUMTEXT NOT NULL,
  `equipment_img` LONGTEXT NOT NULL,
  PRIMARY KEY (`equipment_id`),
  UNIQUE INDEX `equipment_id_UNIQUE` (`equipment_id` ASC) ,
  UNIQUE INDEX `instructions_UNIQUE` (`instructions` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`recipe_requires_equipment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`recipe_requires_equipment` (
  `recipe_recipe_id` INT NOT NULL,
  `equipment_equipment_id` INT NOT NULL,
  PRIMARY KEY (`recipe_recipe_id`, `equipment_equipment_id`),
  INDEX `fk_recipe_has_equipment_equipment1_idx` (`equipment_equipment_id` ASC) ,
  INDEX `fk_recipe_has_equipment_recipe1_idx` (`recipe_recipe_id` ASC) ,
  CONSTRAINT `fk_recipe_has_equipment_recipe1`
    FOREIGN KEY (`recipe_recipe_id`)
    REFERENCES `mydb`.`recipe` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipe_has_equipment_equipment1`
    FOREIGN KEY (`equipment_equipment_id`)
    REFERENCES `mydb`.`equipment` (`equipment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`administrator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`administrator` (
  `admin_id` INT NOT NULL AUTO_INCREMENT,
  `admin_username` VARCHAR(45) NOT NULL,
  `admin_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`admin_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`admin_id` ASC) ,
  UNIQUE INDEX `username_UNIQUE` (`admin_username` ASC) )
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
