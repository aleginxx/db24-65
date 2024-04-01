<img align="left" width="60" height="100" src="https://lh5.googleusercontent.com/proxy/MRBDx8ZGLT3hSY5t3q2KhUkOG_Gzt5I7GlafOJ8LYyeep_qBNeylB6YoIZasv3_iTLDBCqOXg9Co3vtRMeDpDQAlV7wftJTaEOPXEjBocWE">
<p align="center">
  NATIONAL TECHNICAL UNIVERSITY OF ATHENS 
</p>
<p align="center">
  SCHOOL OF ELECTRICAL AND COMPUTER ENGINEER
</p>
<p align="center">
  DBMS LABORATORY
</p>
<p align="center">
  AC. YEAR 2023-2024
</p>
<p align="center">
  <b>Data Bases</b>
</p>
<p align="center">
  <b>Semester Project</b>
</p>



**Assignment**



A popular cooking competition has asked you to design and implement a system for storing and managing the information required for the operation of the competition regarding the recipes, materials and equipment required for the operation of the competition.

Through the related application, he wishes to handle cooking and pastry <u>recipes</u>. Each recipe is a cooking or pastry recipe. It also belongs to a [national cuisine](https://en.wikipedia.org/wiki/Category:Cuisine_by_country) (eg French, Italian) and has a level of difficulty (eg very easy =1 easy =2 , medium = 3, difficult = 4, very difficult = 5).

Each recipe has a name, short description and belongs to one or more <u>meal</u> types (eg breakfast, brunch, lunch, afternoon, dinner). The competition would also like each recipe to be categorized through additional, unlimited, <u>tags</u> for form/type of meal (eg brunch, quick-lunch, cold dish, etc.) and possibly have up to 3 useful tips (eg kept in the fridge for up 3 days).

The execution of a recipe requires specific <u>equipment</u> (eg bowl, sieve, blender, wire) regardless of quantities (eg 3 blenders). Each part/equipment has instructions for use (eg we use the wire when we want to give volume to a mixture).

The total time required to execute a recipe is broken down into preparation time and cooking time. Each recipe consists of 1 or more <u>steps</u>, which must be executed sequentially. Each step describes what the cook must do (eg put the eggs in a bowl and beat them with a whisk). After all the steps have been performed, certain quantities will result (eg 2 portions).

Each recipe requires specific <u>ingredients</u> in clearly or less clearly defined quantities (eg 100 g feta cheese, 2 eggs, 1 tsp oil, a little pepper, a little flour). The ingredients used in the recipes (food) are grouped into <u>Food Groups</u>. For food groups you can use either the [National Food and Drink Code](https://en.wikipedia.org/wiki/Food_code) - or from the [Prevention Institute, Environmental and Occupational Medicine](https://www.asset-scienceinsociety.eu/about/partners/prolepsis-institute-preventive-medicine-environmental-and-occupational-health). Each food group has a name and description.

Each recipe has a single ingredient that is designated as a base. Each recipe is characterized based on its basic material (eg if the basic material belongs to the food group 'Miscellaneous plant-based foods' then the recipe is classified as vegetarian, if the basic material is in the category 'Fish and their products' then the recipe is classified as seafood ).

Each recipe can have <u>nutritional information</u>. These are grams of fat per serving, grams of protein per serving, grams of carbohydrates per serving and number of calories per serving. The calories of each portion should be <u>dynamically</u> calculated based on the individual calories and proportions of the ingredients, as the ingredients/foods have a specific number of [calories](https://www.webmd.com/diet/healthtool-food-calorie-counter) per 100g or ml (eg strawberries 24 calories / 100g).

The competition groups, with its own criteria, the recipes into <u>thematic sections</u> (eg village recipes, risotto recipes, Easter sweets). Each recipe can be included in one or more than one such sections. Each section has a name (eg Easter sweets) and a description (eg Easter sweets ideal for the Easter table).

Each recipe has one or more [<u>cooks</u>](https://en.wikipedia.org/wiki/Cook_(profession)) who can perform a recipe. Each cook has a name, surname, contact phone number, date of birth, age, years of professional experience and specialization in one or more national cuisines. He also has a professional training qualification as follows: 3rd cook, 2nd cook, 1st cook, assistant chef, chef (chef).

The competition takes place annually in 10 <u>episodes/repeats</u>. In each episode, 10 national cuisines, 10 representative cooks from each cuisine, 3 judge cooks and 1 recipe from each national cuisine assigned to 1 cook are automatically selected at random by the system. (A cook/judge/national cuisine/recipe cannot participate in more than 3 episodes consecutively. Also, each cook participating in the competition must be assigned the recipe they are asked to perform.)

Each cook executes the recipe assigned to him and is <u>scored</u> by the 3 judges, based on an integer numerical scale of 1...5. The cook with the highest score is the winner. In case of a tie, the winner is the cook with the highest professional qualification. In case of a new tie, the winner will be announced at random.

All entities stored in your app should be accompanied by corresponding <u>images</u> (eg images for food groups, modules/recipes/ingredients/cooks/episodes, images for equipment/parts, etc.). Each image should also have a verbal description of what it depicts (eg Banana Protein Smoothie).

- *Application Users*: For each user, the system must verify their identity when accessing the application (via username / password).

  - *Administrator*: Registers and modifies all the required data. It can create a backup for the entire database (backup) and restore the system from it (restore).

  - *Cook*: Cooks have the ability to edit all the elements of the recipes assigned to them and also add a new recipe. They can also edit their personal information. They cannot modify other elements of the system eg recipes that have not been assigned to them.

The specifications of the data/information as well as the reports may not have been sufficiently defined by the tender. For the sake of completeness of your work you should record in detail the specifications of the system as well as your assumptions.

You will need to enter in the NW information for each of the entities. There should be enough data in the DB to successfully execute all requested queries and return the appropriate information. If the execution of a query does not return data then the corresponding query will not be scored. As an example, there should be more than 50 recipes, 100 ingredients, 50 cooks, 50 episodes. Recipe information can be obtained from https://www.airtable.com/universe/expHZcS7kWEyq5gUH/recipe-database

1. Draw the ER diagram resulting from the above description.

2. Draw the relational diagram and develop the NW.

  2.1. Define all the necessary constraints that will ensure the correctness of the BD. These are integrity constraints, keys, referential integrity, value field integrity, and user-defined constraints.
  
  2.2. Define appropriate indexes for the DB tables and justify your choice based on their usefulness for the queries in which they are used.

3. Through the application a user will be able to run and see the results for the following queries: 

  3.1. Average Ratings (score) per cook and National cuisine.
  
  3.2. For a given National cuisine and year, which cooks belong to it and which cooks were in episodes?
  
  3.3. Find the young cooks (age < 30) who have the most recipes.
  
  3.4. Find the cooks who have never been a judge on an episode.
  
  3.5. Which judges have been on the same number of episodes in a year with more than 3 appearances?
  
  3.6. Many recipes cover more than one label. Among field pairs (eg brunch and cold dish) that are common in recipes, find the top-3 (top-3) pairs that appeared in [episodes](https://mariadb.com/kb/en/index-hints-how-to-force-query-plans/) For this question, your answer should include, in addition to the query, an alternative Query Plan (eg with force index), the corresponding traces and your conclusions from studying them.
  
  3.7. Find all cooks who have appeared at least 5 times less than the cook with the most episodes.
  
  3.8. Which episode used the most parts (equipment)? Similarly to question 3.6, your answer should include, in addition to the query, alternative Query Plan (eg with force index), the corresponding traces and your conclusions from their study.
  
  3.9. List of average number of grams of carbohydrates in the competition per year?
