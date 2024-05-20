#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

recipe_filepath = 'C:/Users/Gina/Downloads/Recipes-All Recipes.csv'
df = pd.read_csv(recipe_filepath)
df.head()


# In[5]:


columns_to_drop = ['Rating', 'Cookbook', 'Page #', 'Link', 'Last Made', 'Make It Next']
df.drop(columns = columns_to_drop, inplace = True)
df.head()


# In[6]:


ease_of_prep_mapping = {
    'Super Simple': 1,
    'Fairly Easy': 2,
    'Average': 3,
    'Hard': 4,
    'Very Difficult': 5
}

df['Ease of Prep'] = df['Ease of Prep'].map(ease_of_prep_mapping)
df.insert(0, 'recipe_id', range(1, len(df) + 1))
df.head()


# In[7]:


null_columns = df.columns[df.isnull().any()]
print("Columns containing null entries:")
print(null_columns)


# In[8]:


modified_recipe = 'modified_recipe.csv'
df.to_csv(modified_recipe, index=False)

df.head()


# In[188]:


recipe_descriptions = [
    ('Jamaican Jerk Chicken', 'Traditional Jamaican dish featuring marinated chicken grilled to perfection with a spicy and aromatic jerk seasoning.'),
    ('Pasta Salad', 'Refreshing salad made with cooked pasta, fresh vegetables, and a tangy vinaigrette dressing, perfect for picnics or potlucks.'),
    ('Lasagna', 'Classic Italian dish made with layers of lasagna noodles, rich tomato sauce, creamy béchamel, and savory cheese, baked to golden perfection.'),
    ('Hearty Pancakes', 'Fluffy pancakes made with hearty ingredients like oats, whole wheat flour, and buttermilk, perfect for a satisfying breakfast.'),
    ('Summer Garden Couscous Salad', 'Light and vibrant salad made with fluffy couscous, fresh garden vegetables, and a zesty lemon dressing, ideal for summer gatherings.'),
    ('Squash Corn Chowder', 'Creamy and comforting chowder soup made with tender squash, sweet corn kernels, and aromatic herbs, a hearty meal for chilly evenings.'),
    ('White beans, tomatoes, and spinach', 'Healthy and flavorful dish made with tender white beans, juicy tomatoes, and nutritious spinach, seasoned with garlic and herbs.'),
    ('Spaghetti', 'Classic Italian pasta dish featuring al dente spaghetti noodles tossed in a rich tomato sauce and garnished with fresh basil and Parmesan cheese.'),
    ('Scones', 'Delicate and buttery pastries made with flour, butter, and cream, perfect for serving with jam and clotted cream for an elegant afternoon tea.'),
    ('Pizza', 'Iconic Italian dish consisting of a thin crust topped with tomato sauce, melted cheese, and various toppings, baked to crispy perfection in a hot oven.'),
    ('Stir-Fry', 'Quick and flavorful dish made by stir-frying vegetables, meat, and noodles in a hot wok with savory sauces and spices, perfect for busy weeknights.'),
    ('Rustic Italian Tortellini Soup', 'Hearty soup made with cheese-filled tortellini pasta, vegetables, and Italian herbs, simmered in a flavorful tomato broth, a comforting meal for chilly days.'),
    ('Swedish Meatballs', 'Classic Swedish dish featuring tender meatballs made with a mixture of ground beef and pork, served with a creamy gravy and lingonberry jam, a festive favorite.'),
    ('Barley Beef Skillet', 'Nourishing and satisfying skillet meal made with lean beef, pearl barley, and vegetables, seasoned with herbs and spices for a comforting one-pot dinner.'),
    ('Southwest Beef & Rice Skillet', 'Flavorful skillet dish made with seasoned ground beef, rice, black beans, corn, and peppers, topped with cheese and fresh cilantro, a family-friendly meal.'),
    ('Glazed Pork Chops with Corn Bread Dressing', 'Juicy pork chops coated in a sweet and tangy glaze, served with fluffy cornbread dressing and steamed vegetables, a delicious and comforting meal.'),
    ('Fried Rice', 'Classic Chinese dish made with cooked rice stir-fried with vegetables, eggs, and a variety of proteins, seasoned with soy sauce and aromatics, a versatile and satisfying meal.'),
    ('Zesty Sausage & Beans', 'Hearty and flavorful dish made with spicy sausage, tender beans, and aromatic spices, simmered in a zesty tomato sauce, perfect for a cozy dinner.'),
    ('Prosciutto Pasta Toss', 'Simple yet elegant pasta dish made with al dente spaghetti, crispy prosciutto, sweet peas, and Parmesan cheese, tossed in a light lemon-butter sauce, a quick and delicious meal.'),
    ('Cashew Chicken with Noodles', 'Asian-inspired dish made with tender chicken, crunchy cashews, and vegetables, stir-fried with noodles in a savory sauce, a delicious and satisfying meal.'),
    ('Herb Chicken with Honey Butter', 'Tender chicken breasts seasoned with a blend of herbs and spices, pan-seared to perfection, and served with a drizzle of honey butter, a delightful combination of flavors.'),
    ('French Toast', 'Classic breakfast dish made with thick slices of bread soaked in a mixture of eggs, milk, and vanilla, then fried until golden brown and served with syrup and powdered sugar.'),
    ('Swedish Pancakes', 'Thin and delicate pancakes made with a simple batter of flour, eggs, milk, and sugar, served with lingonberry jam and whipped cream, a traditional Swedish breakfast.'),
    ('Baked Cheddar Eggs & Potatoes', 'Eggs baked with diced potatoes, cheddar cheese, and savory herbs, a hearty and delicious breakfast or brunch dish.'),
    ('Baked Mostaccioli', 'Baked pasta dish made with mostaccioli noodles, marinara sauce, Italian sausage, and cheese, baked until bubbly and golden brown, a comforting and satisfying meal.'),
    ('Ravioli with Snap Peas', 'Delicious pasta dish made with cheese-filled ravioli, crisp snap peas, and cherry tomatoes, tossed in a light lemon-butter sauce and garnished with fresh basil.'),
    ('Cloverleaf Rolls', 'Soft and fluffy dinner rolls shaped into charming cloverleafs, perfect for serving with butter or as a side to soups and salads.'),
    ('Greek Yogurt and Honey Blueberry Muffins', 'Moist and tender muffins made with Greek yogurt, honey, and fresh blueberries, a wholesome and delicious treat for breakfast or snack time.'),
    ('Whole Grain Waffles', 'Nutritious waffles made with whole grain flour, buttermilk, and a hint of cinnamon, served with fresh fruit and maple syrup for a wholesome breakfast.'),
    ('Lemon Bars', 'Tangy and sweet dessert bars made with a buttery shortbread crust and a zesty lemon filling, dusted with powdered sugar for a delightful treat.'),
    ('Qahaq Cookies', 'Traditional Middle Eastern cookies made with a spiced dough flavored with sesame seeds, anise, and orange blossom water, shaped into rings and baked until golden brown.'),
    ('Blondies with Nutella', 'Chewy and indulgent blondies made with brown sugar, butter, and swirls of creamy Nutella, a decadent treat for chocolate lovers.'),
    ('Hot Chocolate', 'Rich and creamy beverage made with milk, cocoa powder, and sugar, topped with whipped cream and chocolate shavings for a cozy and comforting drink.'),
    ('Chocolate Mousse', 'Elegant dessert made with rich chocolate, whipped cream, and eggs, chilled until light and airy, perfect for a special occasion or romantic dinner.'),
    ("S'mores Cookie Bars", 'Irresistible dessert bars inspired by the classic campfire treat, featuring layers of graham cracker crust, chocolate chips, and toasted marshmallows.'),
    ('Orange Chicken', 'Flavorful Chinese dish featuring crispy chicken pieces coated in a tangy orange sauce, served with steamed rice and garnished with green onions, a delicious and satisfying meal.'),
    ('Tostadas', 'Crispy corn tortillas topped with seasoned ground beef, refried beans, shredded lettuce, cheese, and salsa, a delicious and satisfying Mexican-inspired dish.'),
    ('Black Bean Stuffed Sweet Potatoes', 'Nutritious and flavorful dish featuring baked sweet potatoes stuffed with seasoned black beans, cheese, avocado, and salsa, a satisfying vegetarian meal.'),
    ('Asian Shredded Beef', 'Tender beef brisket slow-cooked in a flavorful Asian-inspired sauce, shredded and served over rice or noodles for a hearty and delicious meal.'),
    ('Capellini with sausage, spinach, and jalapeno', 'Delicious pasta dish featuring capellini pasta tossed with spicy Italian sausage, fresh spinach, and jalapeno peppers, a flavorful and satisfying meal.'),
    ('Crispy Chicken with Kale', 'Crispy breaded chicken breasts served with sautéed kale and a tangy Dijon mustard sauce, a delicious and nutritious dinner option.'),
    ('Roast Chicken Grain Bowl', 'Hearty grain bowl featuring roasted chicken, quinoa, roasted vegetables, and a creamy tahini dressing, a wholesome and satisfying meal.'),
    ('Chicken thighs with barley and peas', 'Comforting one-pot meal made with tender chicken thighs, pearl barley, sweet peas, and aromatic herbs, a hearty and nutritious dinner option.'),
    ('Rice noodles with meatballs and bok choy', 'Flavorful Asian-inspired dish featuring rice noodles, tender meatballs, crisp bok choy, and a savory broth, a delicious and satisfying meal.'),
    ('Paprika Pork with Roasted Potatoes and Dill Cream', 'Tender pork loin seasoned with smoked paprika and served with crispy roasted potatoes and a creamy dill sauce, a flavorful and comforting dinner.'),
    ('Chicken cutlets with carrot and kale salad', 'Juicy chicken cutlets served with a vibrant salad of shredded carrots, kale, and red cabbage tossed in a tangy vinaigrette, a nutritious and delicious meal.'),
    ('Gnocchi and sweet potatoes', 'Comforting pasta dish made with pillowy gnocchi, roasted sweet potatoes, and caramelized onions, tossed in a creamy Parmesan sauce, a delicious and satisfying dinner.'),
    ("Shepherd's Pie", 'Classic comfort food dish made with ground beef or lamb, vegetables, and mashed potatoes, baked until golden brown and bubbly, a hearty and satisfying meal.'),
    ('Garlic Parmesan Chicken', 'Juicy chicken breasts coated in a flavorful garlic Parmesan crust, baked until golden brown and served with roasted vegetables, a delicious and easy weeknight dinner.'),
    ('Turkey Pot Pie', 'Hearty and comforting pot pie made with tender turkey, mixed vegetables, and a creamy gravy, topped with flaky pie crust, a delicious way to use leftover turkey.'),
    ('Balsamic Bacon Brussels Sprouts', 'Crispy Brussels sprouts roasted with bacon and drizzled with balsamic glaze, a flavorful and irresistible side dish for any meal.'),
    ('Lemon Red Potatoes', 'Tender roasted red potatoes tossed with olive oil, lemon zest, garlic, and fresh herbs, a bright and flavorful side dish for any occasion.'),
    ('Potato and Corn Chowder', 'Creamy and comforting chowder made with tender potatoes, sweet corn kernels, and smoky bacon, a hearty and satisfying soup for chilly days.'),
    ('Thai Chicken', 'Flavorful Thai-inspired dish featuring tender chicken, bell peppers, and onions stir-fried in a sweet and spicy sauce, served over rice or noodles, a delicious and satisfying meal.'),
    ('Italian Fagoli Vegetable Soup', 'Hearty and flavorful soup made with beans, vegetables, pasta, and Italian herbs, a comforting and nutritious meal for any occasion.'),
    ('Blueberry Pie', 'Classic dessert made with sweet, juicy blueberries baked in a flaky pie crust until golden brown and bubbling, a delicious and irresistible treat for any occasion.'),
    ('Chocolate Pudding', 'Creamy and indulgent dessert made with rich chocolate, milk, and sugar, chilled until thick and creamy, a classic comfort food treat.'),
    ('Browned Butter Beets', 'Sweet and earthy beets roasted until tender and caramelized, then tossed in nutty browned butter and fresh herbs, a delicious and nutritious side dish.'),
    ('Turkey Soup with Homemade Noodles', 'Comforting soup made with leftover turkey, hearty vegetables, and tender homemade noodles, a delicious way to use up holiday leftovers.'),
    ('Home fries', 'Crispy and golden brown potatoes sautéed with onions and seasoned with herbs and spices, a classic breakfast side dish that pairs perfectly with eggs and bacon.'),
    ('Chocolate Raspberry Torte', 'Decadent dessert featuring layers of rich chocolate cake filled with raspberry preserves and topped with chocolate ganache, a luxurious treat for chocolate lovers.'),
    ('Golden Latte', 'Warm and comforting beverage made with turmeric, ginger, cinnamon, and milk, a soothing and nutritious drink with anti-inflammatory properties.'),
    ('Fig Shake', 'Creamy and delicious shake made with ripe figs, Greek yogurt, honey, and vanilla, a refreshing and nutritious treat for breakfast or snack time.'),
    ('Lentil Soup', 'Hearty and flavorful soup made with lentils, vegetables, and aromatic spices, a nutritious and satisfying meal for any occasion.'),
    ('Buckwheat Tabboulah', 'Nutritious and flavorful salad made with cooked buckwheat, fresh herbs, vegetables, and a tangy lemon dressing, a delicious and satisfying side dish or light meal.'),
    ('Lentil Rice Bowls with Egg', 'Wholesome and nutritious rice bowls made with cooked lentils, brown rice, sautéed vegetables, and a fried egg on top, a delicious and satisfying vegetarian meal.'),
    ('Italian Vegetable Lentil Soup', 'Hearty and flavorful soup made with lentils, vegetables, and Italian herbs, a comforting and nutritious meal for any occasion.'),
    ('One Pot Chicken & Potatoes', 'Easy and flavorful one-pot meal made with chicken, potatoes, and vegetables, seasoned with herbs and spices and baked until golden brown and crispy.'),
    ('Sweet Korean Lentils', 'Tender and flavorful lentils cooked in a sweet and spicy Korean-inspired sauce, served over rice with sautéed vegetables and a fried egg, a delicious and satisfying vegetarian meal.'),
    ('Buckwheat Beetroot Salad', 'Colorful and nutritious salad made with cooked buckwheat, roasted beets, creamy goat cheese, and toasted walnuts, tossed in a tangy vinaigrette, a delicious and satisfying dish.'),
    ('New Potato Lentil Salad', 'Refreshing and nutritious salad made with tender new potatoes, cooked lentils, fresh herbs, and a tangy mustard vinaigrette, a delicious side dish for any meal.'),
    ('Ham & Potato Soup', 'Comforting soup made with tender potatoes, chunks of ham, and vegetables simmered in a creamy broth, a hearty and satisfying meal for chilly days.'),
    ('Lemon Dill Potatoes', 'Tender roasted potatoes seasoned with lemon, garlic, and dill, a bright and flavorful side dish for any meal.'),
    ('BBQ Lentils', 'Hearty and flavorful lentils cooked in a tangy barbecue sauce, served over rice or baked potatoes for a delicious and satisfying vegetarian meal.'),
    ('Healthy Buckwheat Soup', 'Nourishing and flavorful soup made with cooked buckwheat, vegetables, and herbs, a comforting and nutritious meal for any occasion.'),
    ('Buckwheat Chicken Pilaf', 'Savory and satisfying pilaf made with cooked buckwheat, tender chicken, and vegetables, seasoned with aromatic spices and herbs, a delicious and nutritious meal.'),
    ('Vegetable Noodle Soup', 'Hearty and flavorful soup made with noodles, vegetables, and aromatic herbs, a comforting and nutritious meal for any occasion.'),
    ('Bacon and Honey Potato Salad', 'Creamy and flavorful potato salad made with crispy bacon, sweet honey, and tangy mustard, a delicious side dish for any barbecue or picnic.'),
    ('Pretzel Sticks', 'Crispy and golden brown pretzel sticks served with mustard for dipping, a delicious and addictive snack for any occasion.'),
    ('Golden French Lentil Soup', 'Nourishing and flavorful soup made with French lentils, vegetables, and herbs, a comforting and nutritious meal for any occasion.'),
    ("Lentil Shepherd's Pie", 'Hearty and flavorful pie made with cooked lentils, vegetables, and mashed potatoes, baked until golden brown and bubbly, a delicious vegetarian version of the classic dish.'),
    ('Honey Lime Chicken', 'Juicy and flavorful chicken breasts marinated in a sweet and tangy honey-lime sauce, grilled to perfection and served with rice and vegetables, a delicious and easy meal for summer.'),
    ('Lentil Curry', 'Spicy and aromatic curry made with cooked lentils, tomatoes, coconut milk, and Indian spices, a flavorful and satisfying vegetarian meal served with rice or naan.'),
    ('Dutch Oven Bread', 'Rustic and crusty bread baked in a Dutch oven until golden brown and delicious, a simple and satisfying recipe for homemade bread.'),
    ('Potato Apple Roast', 'Delicious and comforting roast made with tender potatoes, sweet apples, and savory herbs, a flavorful and hearty dish for any occasion.'),
    ('Baking Powder Biscuits', 'Light and fluffy biscuits made with flour, baking powder, and butter, perfect for serving with butter and jam for breakfast or alongside soup or stew for dinner.'),
    ('Sugar Cookies', 'Classic cookies made with butter, sugar, and vanilla, rolled out and cut into festive shapes before baking until golden brown and delicious, a delightful treat for any occasion.'),
    ('Potato Curry', 'Spicy and flavorful curry made with tender potatoes, tomatoes, and Indian spices, a comforting and satisfying vegetarian meal served with rice or naan.'),
    ("Bucatini all'Amatriciana", 'Classic Italian pasta dish made with bucatini noodles, pancetta, onions, tomatoes, and pecorino cheese, a flavorful and satisfying meal for pasta lovers.'),
    ('Brioche Chocolate Rolls', 'Soft and fluffy brioche rolls filled with rich chocolate, perfect for serving as a sweet breakfast treat or indulgent dessert.'),
    ('Naan', 'Soft and chewy Indian flatbread made with flour, yeast, and yogurt, perfect for serving alongside curries or as a base for wraps and sandwiches.'),
    ('Lemon Poppy Seed Scones', 'Buttery and tender scones made with lemon zest and poppy seeds, perfect for serving with tea or coffee for breakfast or brunch.'),
    ('Balsamic Dijon Root Vegetables', 'Colorful and flavorful roasted root vegetables tossed in a tangy balsamic Dijon vinaigrette, a delicious and nutritious side dish for any meal.'),
    ('Best Baked Chicken Legs', 'Juicy and flavorful chicken legs seasoned with a blend of herbs and spices, baked until crispy and golden brown, a delicious and easy dinner option for any night of the week.'),
    ('Spanish Lentil Soup', 'Hearty and flavorful soup made with Spanish pardina lentils, chorizo sausage, and vegetables, a comforting and satisfying meal for any occasion.'),
    ('Chocolate Chip Irish Soda Bread', 'Traditional Irish soda bread studded with chocolate chips, perfect for serving as a sweet breakfast or dessert option alongside a cup of tea or coffee.'),
    ('Malteese Gilatti', 'Traditional Maltese pastries filled with ricotta cheese, chocolate chips, and candied fruit, perfect for serving as a sweet treat or dessert.'),
    ('Buckwheat Carrot and Onion', 'Nutritious and flavorful salad made with cooked buckwheat, shredded carrots, and caramelized onions, tossed in a tangy vinaigrette, a delicious and satisfying side dish.'),
    ('Sweet Potatoes with Yogurt and Chickpeas', 'Nourishing and flavorful dish made with roasted sweet potatoes, creamy yogurt, and spiced chickpeas, a delicious and satisfying vegetarian meal.'),
    ('Spanish Chickpeas', 'Flavorful and aromatic dish made with Spanish chickpeas, tomatoes, onions, and spices, a comforting and nutritious meal served with rice or crusty bread.'),
    ('Lemon Fettuchini', 'Delicious pasta dish made with al dente fettuccine noodles tossed in a creamy lemon sauce with garlic, Parmesan cheese, and fresh herbs, a flavorful and satisfying meal.'),
    ('Chickpea Masala', 'Spicy and flavorful Indian dish made with chickpeas cooked in a rich tomato-based sauce with onions, garlic, ginger, and aromatic spices, a satisfying vegetarian meal served with rice or naan.'),
    ('Chickpea Broccoli Pesto', 'Healthy and flavorful dish made with cooked chickpeas, roasted broccoli, and creamy pesto sauce, a delicious and satisfying vegetarian meal.'),
    ('Thai Veggie Soup', 'Hearty and flavorful soup made with Thai-inspired flavors like coconut milk, curry paste, and lemongrass, packed with vegetables and tofu for a delicious and satisfying meal.'),
    ('Buttery Herb Chicken', 'Juicy and flavorful chicken breasts seasoned with a blend of butter, garlic, and fresh herbs, pan-seared to perfection and served with roasted vegetables, a delicious and easy dinner option.'),
    ('Rosemary Parsnips', 'Tender and flavorful parsnips roasted with olive oil, garlic, and fresh rosemary, a delicious and aromatic side dish for any meal.'),
    ('Balsamic Potatoes and Asparagus', 'Delicious and nutritious side dish made with roasted potatoes and asparagus tossed in a tangy balsamic glaze, a flavorful addition to any meal.'),
    ('Quinoa Brussels Sweet Potato Salad', 'Nutritious and flavorful salad made with cooked quinoa, roasted Brussels sprouts and sweet potatoes, dried cranberries, and toasted pecans, tossed in a tangy vinaigrette.'),
    ('Thai Peanut Cabbage Quinoa', 'Hearty and flavorful salad made with cooked quinoa, shredded cabbage, carrots, and red bell pepper, tossed in a creamy Thai-inspired peanut sauce, a delicious and satisfying vegetarian meal.'),
    ('Lemon Garlic Asparagus with Orzo', 'Light and flavorful dish made with tender asparagus spears sautéed with garlic and lemon zest, tossed with cooked orzo pasta and fresh herbs, a delicious and nutritious meal.'),
    ('Moroccan Sweet Potato Lentil Stew', 'Hearty and flavorful stew made with tender sweet potatoes, lentils, and aromatic Moroccan spices, a comforting and satisfying vegetarian meal served with crusty bread or couscous.'),
    ('Chia Crusted Salmon', 'Delicious and nutritious salmon fillets coated in a crunchy chia seed crust, baked until crispy and golden brown, a flavorful and healthy meal option.'),
    ('Pinto Beans and Tomatillo Cilantro Lime Rice', 'Flavorful and satisfying dish made with cooked pinto beans, tomatillo cilantro lime rice, and fresh toppings like avocado, salsa, and sour cream, a delicious and nutritious vegetarian meal.'),
    ('Thai Squash Soup', 'Velvety and aromatic soup made with roasted butternut squash, coconut milk, Thai curry paste, and aromatic spices, a comforting and flavorful meal for chilly days.'),
    ('Roasted Carrot & Peanut Sauce', 'Colorful and flavorful dish made with roasted carrots, creamy peanut sauce, and fresh herbs, a delicious and nutritious vegetarian meal served over rice or noodles.'),
    ('Majoram White Wine Chicken', 'Tender and flavorful chicken breasts cooked in a creamy white wine sauce with fresh marjoram and garlic, a delicious and elegant meal for any occasion.'),
    ('Marjoram Carrots', 'Sweet and savory side dish made with tender roasted carrots seasoned with fresh marjoram, garlic, and olive oil, a delicious and aromatic addition to any meal.'),
    ('Soy Mustard Salmon', 'Flavorful and nutritious salmon fillets marinated in a tangy soy mustard sauce, grilled or baked to perfection and served with steamed vegetables, a delicious and healthy meal option.'),
    ('Chive Butter Radishes', 'Crisp and flavorful radishes tossed in melted chive butter and roasted until tender and caramelized, a delicious and unique side dish for any meal.'),
    ('Mango Chutney', 'Sweet and tangy condiment made with ripe mangoes, onions, vinegar, and spices, a delicious accompaniment to curries, grilled meats, and sandwiches.'),
    ('Vegetarian Chili', 'Hearty and flavorful chili made with beans, vegetables, and spices, simmered until thick and flavorful, a comforting and satisfying meal for any occasion.'),
    ('Sweet Potato Breakfast Burritos', 'Hearty and satisfying breakfast burritos made with scrambled eggs, roasted sweet potatoes, black beans, and cheese, wrapped in warm tortillas and served with salsa.'),
    ('Roasted Sweet Potato Lentil Salad', 'Nutritious and flavorful salad made with roasted sweet potatoes, cooked lentils, baby spinach, and a tangy balsamic vinaigrette, a delicious and satisfying vegetarian meal.'),
    ('Cornbread', 'Moist and flavorful cornbread made with cornmeal, flour, buttermilk, and honey, baked until golden brown and served with butter, a classic Southern side dish.'),
    ('Brussel Honey Lentil Quinoa', 'Nutritious and flavorful salad made with cooked lentils and quinoa, shredded Brussels sprouts, dried cranberries, and toasted almonds, tossed in a sweet honey mustard vinaigrette.'),
    ('Lentil Sweet Potato Curry', 'Hearty and flavorful curry made with cooked lentils, sweet potatoes, and aromatic Indian spices, a satisfying and nutritious vegetarian meal served with rice or naan.'),
    ('Gnocci and white beans', 'Comforting pasta dish made with pillowy gnocchi, tender white beans, and spinach, tossed in a creamy Parmesan sauce, a delicious and satisfying dinner option.'),
    ('Pad Thai', 'Classic Thai noodle dish made with stir-fried rice noodles, tofu, eggs, and vegetables, flavored with a tangy tamarind sauce and garnished with peanuts and fresh herbs, a flavorful and satisfying meal.'),
    ('Kung Pao Chicken', 'Spicy and flavorful Chinese dish made with tender chicken, peanuts, vegetables, and chili peppers, stir-fried in a savory sauce, a delicious and satisfying meal for any occasion.'),
    ('Mediterranean Tuna Steaks', 'Flavorful and nutritious tuna steaks marinated in a blend of Mediterranean spices, grilled until tender and served with a tangy lemon-herb sauce, a delicious and healthy meal option.'),
    ('Spicy Black Bean Nachos', 'Hearty and flavorful nachos made with crispy tortilla chips, spicy black beans, melted cheese, and fresh toppings like salsa, avocado, and cilantro, a delicious and satisfying snack or appetizer.'),
    ('Tomato Basil Soup', 'Classic soup made with ripe tomatoes, fresh basil, onions, and garlic, simmered until thick and flavorful, a comforting and delicious meal served with crusty bread or grilled cheese sandwiches.'),
    ('Chewy Chocolate Chip Cookies', 'Classic cookies made with brown sugar, butter, and plenty of chocolate chips, baked until golden brown and chewy, a delicious and satisfying treat for any occasion.'),
    ('Quinoa Peanut Kale Curry', 'Flavorful and nutritious curry made with cooked quinoa, tender kale, chickpeas, and peanuts, simmered in a creamy coconut milk sauce with Indian spices, a satisfying and delicious vegetarian meal.'),
    ('Sweet Potato Lentil Curry with Pickled Onion', 'Hearty and flavorful curry made with tender sweet potatoes, cooked lentils, and aromatic Indian spices, served with tangy pickled onions and fresh cilantro, a delicious and satisfying vegetarian meal.'),
    ('Sardine Mediterranean Pasta', 'Mediterranean-inspired pasta dish featuring savory sardines, olives, tomatoes, and capers in a flavorful herb-infused sauce.'),
    ('Prosciutto apple flatbread pizza', 'Delicious flatbread pizza topped with thinly sliced prosciutto, sweet apple slices, tangy goat cheese, and a drizzle of balsamic glaze for a delightful flavor combination.'),
    ('Dill Cucumber Salmon', 'Elegant dish showcasing tender salmon fillets seasoned with fresh dill and served with refreshing cucumber slices, offering a light and flavorful meal.'),
    ('Vegetable Couscous', 'Healthy and vibrant couscous dish loaded with a colorful array of vegetables, herbs, and spices, providing a nutritious and satisfying meal.'),
    ('Talapia Tacos', 'Tasty tacos filled with tender tilapia fish fillets seasoned with zesty spices, topped with crunchy cabbage slaw and creamy avocado for a delightful Tex-Mex experience.'),
    ('Roasted Mackerel', 'Simple and flavorful mackerel dish roasted to perfection with a blend of aromatic herbs and citrus, offering a deliciously light and nutritious meal.'),
    ('Lentil Salsa Soup', 'Hearty soup featuring protein-rich lentils simmered with vibrant salsa and aromatic spices, creating a comforting and flavorful dish perfect for chilly days.'),
    ('Pesto Tomato Penne', 'Satisfying pasta dish tossed in fragrant pesto sauce made with fresh basil, garlic, and pine nuts, complemented by juicy cherry tomatoes for a burst of flavor.'),
    ('Black Bean Soup', 'Rich and comforting soup made with hearty black beans, aromatic spices, and flavorful vegetables, offering a nourishing and satisfying meal option.'),
    ('Balsamic Pork Chops', 'Tender pork chops marinated in a tangy balsamic glaze, then grilled to perfection, resulting in succulent and flavorful meat that pairs perfectly with your favorite side dishes.'),
]


# In[189]:


recipes_cuisine_association = [
    ('Jamaican Jerk Chicken', 18),
    ('Pasta Salad', 9),
    ('Lasagna', 1),
    ('Hearty Pancakes', 36),
    ('Summer Garden Couscous Salad', 7),
    ('Squash Corn Chowder', 24),
    ('White beans, tomatoes, and spinach', 3),
    ('Spaghetti', 14),
    ('Scones', 11),
    ('Pizza', 15),
    ('Stir-Fry', 41),
    ('Rustic Italian Tortellini Soup', 21),
    ('Swedish Meatballs', 8),
    ('Barley Beef Skillet', 19),
    ('Southwest Beef & Rice Skillet', 40),
    ('Glazed Pork Chops with Corn Bread Dressing', 48),
    ('Fried Rice', 47),
    ('Zesty Sausage & Beans', 22),
    ('Prosciutto Pasta Toss', 39),
    ('Cashew Chicken with Noodles', 3),
    ('Herb Chicken with Honey Butter', 10),
    ('French Toast', 29),
    ('Swedish Pancakes', 32),
    ('Baked Cheddar Eggs & Potatoes', 41),
    ('Baked Mostaccioli', 50),
    ('Ravioli with Snap Peas', 6),
    ('Cloverleaf Rolls', 28),
    ('Greek Yogurt and Honey Blueberry Muffins', 25),
    ('Whole Grain Waffles', 8),
    ('Lemon Bars', 38),
    ('Qahaq Cookies', 46),
    ('Blondies with Nutella', 47),
    ('Hot Chocolate', 29),
    ('Chocolate Mousse', 30),
    ("S'mores Cookie Bars", 14),
    ('Orange Chicken', 1),
    ('Tostadas', 27),
    ('Black Bean Stuffed Sweet Potatoes', 33),
    ('Asian Shredded Beef', 18),
    ('Capellini with sausage, spinach, and jalapeno', 3),
    ('Crispy Chicken with Kale', 4),
    ('Roast Chicken Grain Bowl', 47),
    ('Chicken thighs with barley and peas', 30),
    ('Rice noodles with meatballs and bok choy', 7),
    ('Paprika Pork with Roasted Potatoes and Dill Cream', 34),
    ('Chicken cutlets with carrot and kale salad', 2),
    ('Gnocchi and sweet potatoes', 33),
    ("Shepherd's Pie", 12),
    ('Garlic Parmesan Chicken', 16),
    ('Turkey Pot Pie', 29),
    ('Balsamic Bacon Brussels Sprouts', 35),
    ('Lemon Red Potatoes', 28),
    ('Potato and Corn Chowder', 19),
    ('Thai Chicken', 9),
    ('Italian Fagoli Vegetable Soup', 23),
    ('Blueberry Pie', 39),
    ('Chocolate Pudding', 32),
    ('Browned Butter Beets', 12),
    ('Turkey Soup with Homemade Noodles', 25),
    ('Home fries', 10),
    ('Chocolate Raspberry Torte', 49),
    ('Golden Latte', 50),
    ('Fig Shake', 39),
    ('Lentil Soup', 46),
    ('Buckwheat Tabboulah', 16),
    ('Lentil Rice Bowls with Egg', 3),
    ('Italian Vegetable Lentil Soup', 21),
    ('One Pot Chicken & Potatoes', 29),
    ('Sweet Korean Lentils', 8),
    ('Buckwheat Beetroot Salad', 2),
    ('New Potato Lentil Salad', 15),
    ('Ham & Potato Soup', 12),
    ('Lemon Dill Potatoes', 39),
    ('BBQ Lentils', 10),
    ('Healthy Buckwheat Soup', 17),
    ('Buckwheat Chicken Pilaf', 19),
    ('Vegetable Noodle Soup', 21),
    ('Bacon and Honey Potato Salad', 25),
    ('Pretzel Sticks', 30),
    ('Golden French Lentil Soup', 48),
    ('Lentil Shepherd\'s Pie', 5),
    ('Honey Lime Chicken', 13),
    ('Lentil Curry', 25),
    ('Dutch Oven Bread', 11),
    ('Potato Apple Roast', 23),
    ('Baking Powder Biscuits', 1),
    ('Sugar Cookies', 43),
    ('Potato Curry', 36),
    ('Bucatini all\'Amatriciana', 7),
    ('Brioche Chocolate Rolls', 39),
    ('Naan', 14),
    ('Lemon Poppy Seed Scones', 29),
    ('Balsamic Dijon Root Vegetables', 15),
    ('Best Baked Chicken Legs', 48),
    ('Spanish Lentil Soup', 30),
    ('Chocolate Chip Irish Soda Bread', 34),
    ('Malteese Gilatti', 28),
    ('Buckwheat Carrot and Onion', 17),
    ('Sweet Potatoes with Yogurt and Chickpeas', 11),
    ('Spanish Chickpeas', 45),
    ('Lemon Fettuchini', 14),
    ('Chickpea Masala', 46),
    ('Chickpea Broccoli Pesto', 28),
    ('Thai Veggie Soup', 26),
    ('Buttery Herb Chicken', 35),
    ('Rosemary Parsnips', 17),
    ('Balsamic Potatoes and Asparagus', 2),
    ('Quinoa Brussels Sweet Potato Salad', 22),
    ('Thai Peanut Cabbage Quinoa', 40),
    ('Lemon Garlic Asparagus with Orzo', 19),
    ('Moroccan Sweet Potato Lentil Stew', 47),
    ('Chia Crusted Salmon', 5),
    ('Pinto Beans and Tomatillo Cilantro Lime Rice', 43),
    ('Thai Squash Soup', 27),
    ('Roasted Carrot & Peanut Sauce', 13),
    ('Majoram White Wine Chicken', 18),
    ('Marjoram Carrots', 44),
    ('Soy Mustard Salmon', 38),
    ('Chive Butter Radishes', 36),
    ('Mango Chutney', 1),
    ('Vegetarian Chili', 14),
    ('Sweet Potato Breakfast Burritos', 2),
    ('Roasted Sweet Potato Lentil Salad', 40),
    ('Cornbread', 22),
    ('Brussel Honey Lentil Quinoa', 47),
    ('Lentil Sweet Potato Curry', 50),
    ('Gnocci and white beans', 8),
    ('Pad Thai', 31),
    ('Kung Pao Chicken', 13),
    ('Mediterranean Tuna Steaks', 12),
    ('Spicy Black Bean Nachos', 3),
    ('Tomato Basil Soup', 30),
    ('Chewy Chocolate Chip Cookies', 42),
    ('Quinoa Peanut Kale Curry', 32),
    ('Sweet Potato Lentil Curry with Pickled Onion', 48),
    ('Sardine Mediterranean Pasta', 18),
    ('Prosciutto apple flatbread pizza', 4),
    ('Dill Cucumber Salmon', 10),
    ('Vegetable Couscous', 22),
    ('Talapia Tacos', 6),
    ('Roasted Mackerel', 20),
    ('Lentil Salsa Soup', 11),
    ('Pesto Tomato Penne', 25),
    ('Black Bean Soup', 37),
    ('Balsamic Pork Chops', 34)
]


# In[211]:


import pandas as pd
from faker import Faker
import random

fake = Faker()

df = pd.read_csv(modified_recipe)

recipe_data = []
ingredients_data = []

ingredient_id_counter = 1
remaining_ingredients = 18 

def generate_ingredient(ingredient_name):
    global ingredient_id_counter
    
    if not any(ingredient['ingredient_name'] == ingredient_name for ingredient in ingredients_data):
        global ingredient_id_counter
        ingredient_id = ingredient_id_counter
        grams_of_fat = random.randint(1, 20)
        grams_of_protein = random.randint(1, 20)
        grams_of_carbs = random.randint(1, 20)
        calories_per_gram = random.randint(1, 10)
        ingredient_img = fake.image_url()
        
        ingredient_id_counter += 1
        
        ingredient_data = {
            'ingredient_id': ingredient_id,
            'ingredient_name': ingredient_name,
            'ingredient_grams_of_fat': grams_of_fat,
            'ingredient_grams_of_protein': grams_of_protein,
            'ingredient_grams_of_carbs': grams_of_carbs,
            'ingredient_calories_per_gram': calories_per_gram,
            'ingredient_img': ingredient_img
        }
        ingredients_data.append(ingredient_data)
    
def insert_into_ingredients(row):
    global remaining_ingredients  # Declare global variable here
    ingredients_list = row['Ingredients'].split(',') if isinstance(row['Ingredients'], str) else []
    for ingredient in ingredients_list:
        ingredient_name = ingredient.strip()
        if ingredient_name:
            generate_ingredient(ingredient_name)
            
    while remaining_ingredients > 0:
        ingredient_name = fake.word()
        generate_ingredient(ingredient_name)
        remaining_ingredients -= 1

def insert_into_recipe(row):
    recipe_id = row['recipe_id']
    recipe_name = row['Name']
    type_value = row['Type']
    if type_value in ['Dessert', 'Baking Basics']:
        recipe_type = 'pastry making'
    else:
        recipe_type = 'cooking'
    cuisine_of_recipe = next((cuisine for name, cuisine in recipes_cuisine_association if name == recipe_name), None)
    level = row['Ease of Prep']
    recipe_desc = next((desc for name, desc in recipe_descriptions if name == recipe_name), 'No description available')
    no_of_portions = random.randint(2, 8)
    primary_ingredient_id = random.randint(1, 101)
    recipe_img = row['Photo']
              
    recipe_data.append({
        'recipe_id': recipe_id,
        'recipe_name': recipe_name,
        'recipe_type': recipe_type,
        'cuisine_of_recipe' : cuisine_of_recipe,
        'level': level,
        'recipe_desc': recipe_desc,
        'no_of_portions': no_of_portions,
        'primary_ingredient_id': primary_ingredient_id,
        'recipe_img': recipe_img
    })
    
df.apply(insert_into_recipe, axis=1)
df.apply(insert_into_ingredients, axis=1)

recipe_df = pd.DataFrame(recipe_data)
recipe_df['cuisine_of_recipe'] = recipe_df['cuisine_of_recipe'].fillna(-1).astype(int)
ingredients_df = pd.DataFrame(ingredients_data)

recipe_df.to_csv('recipe.csv', index=False)
ingredients_df.to_csv('ingredients.csv', index=False)


# In[227]:


recipe = pd.read_csv('recipe.csv')
recipe.head()


# In[228]:


ingredients = pd.read_csv('ingredients.csv')
ingredients.head()


# In[235]:


sorted_column = recipe['cuisine_of_recipe'].sort_values()

sorted_string = ', '.join(map(str, sorted_column))

print(sorted_string)


# In[230]:


sorted_column = ingredients['ingredient_id'].sort_values()

sorted_string = ', '.join(map(str, sorted_column))

print(sorted_string)


# In[232]:


list_a = [4, 4, 5, 5, 6, 6, 7, 8, 9, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 16, 16, 17, 18, 18, 19, 19, 20, 20, 21, 21, 23, 23, 23, 26, 26, 26, 27, 28, 28, 29, 29, 30, 31, 32, 32, 34, 34, 35, 36, 37, 37, 38, 38, 40, 41, 42, 42, 42, 43, 45, 46, 47, 47, 47, 47, 47, 49, 49, 49, 52, 52, 53, 53, 54, 54, 55, 56, 57, 59, 59, 59, 59, 60, 60, 61, 62, 62, 63, 64, 68, 69, 69, 70, 70, 71, 71, 71, 72, 73, 73, 73, 73, 74, 74, 74, 75, 76, 76, 77, 78, 78, 78, 81, 81, 81, 83, 84, 85, 85, 85, 86, 86, 88, 89, 89, 90, 92, 93, 93, 94, 94, 95, 97, 98, 99, 100, 100, 100, 100]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

set_a = set(list_a)
set_b = set(list_b)

result = set_a - set_b

print(sorted(result))


# In[111]:


import random

recipe_ingredients_data = []

def get_ingredient_id(ingredient_name):
    ingredients_df = pd.read_csv('ingredients.csv')
    ingredient_row = ingredients_df[ingredients_df['ingredient_name'] == ingredient_name]
    
    if not ingredient_row.empty:
        return ingredient_row.iloc[0]['ingredient_id']
    else:
        return None

def create_recipe_ingredients_csv():
    modified_recipe = 'modified_recipe.csv'
    df = pd.read_csv(modified_recipe)
    
    # Get existing recipe IDs from the DataFrame
    existing_recipe_ids = set(df['recipe_id'])
    
    for recipe_id in range(1, 146):  # Iterate over recipe_id from 1 to 145
        if recipe_id in existing_recipe_ids:
            ingredients_list_series = df[df['recipe_id'] == recipe_id]['Ingredients']
            ingredients_list = ingredients_list_series.iloc[0]
            if not pd.isnull(ingredients_list):  # Check if ingredients_list is not NaN
                ingredients_list = ingredients_list.split(',')
                for ingredient_name in ingredients_list:
                    ingredient_name = ingredient_name.strip()
                    if ingredient_name:
                        ingredient_id = get_ingredient_id(ingredient_name)
                        if ingredient_id is not None:
                            quantity = random.randint(20, 500)
                            
                            recipe_ingredients_data.append({
                                'recipe_recipe_id': recipe_id,
                                'ingredients_ingredient_id': ingredient_id,
                                'quantity': quantity
                            })
        else:
            # If the recipe ID doesn't exist in the DataFrame, generate a placeholder entry
            recipe_ingredients_data.append({
                'recipe_recipe_id': recipe_id,
                'ingredients_ingredient_id': None,
                'quantity': None
            })

create_recipe_ingredients_csv()

recipe_ingredients_df = pd.DataFrame(recipe_ingredients_data)
    
recipe_ingredients_df.to_csv('recipe_ingredients.csv', index=False)


# In[112]:


recipe_ingredients = pd.read_csv('recipe_ingredients.csv')
recipe_ingredients.head()


# In[150]:


cuisine_data = []
cuisine_id_counter = 1

def insert_into_cuisine(cuisine_name) : 
    global cuisine_id_counter
    
    cuisine_data.append({'cuisine_id': cuisine_id_counter, 'cuisine_name': cuisine_name})
    
    cuisine_id_counter += 1
    

cuisines = [
    'Italian',
    'Mexican',
    'Indian',
    'Chinese',
    'Japanese',
    'French',
    'Thai',
    'Greek',
    'Mediterranean',
    'Spanish',
    'American',
    'Korean',
    'Vietnamese',
    'Brazilian',
    'Middle Eastern',
    'German',
    'British',
    'Caribbean',
    'African',
    'Cajun/Creole',
    'Swedish',
    'Irish',
    'European',
    'Moroccan',
    'Turkish',
    'Russian',
    'Australian',
    'Peruvian',
    'Argentinian',
    'Portuguese',
    'Indonesian',
    'Filipino',
    'Singaporean',
    'Malaysian',
    'Canadian',
    'Swiss',
    'Dutch',
    'Belgian',
    'Polish',
    'Israeli',
    'Lebanese',
    'Egyptian',
    'Ethiopian',
    'South African',
    'Kenyan',
    'Nigerian',
    'Ghanian',
    'Tunisian',
    'Algerian',
    'Senegalese'
]
    
for cuisine in cuisines:
    insert_into_cuisine(cuisine)
    
cuisine_df = pd.DataFrame(cuisine_data)
    
cuisine_df.to_csv('cuisine.csv', index=False)

cuisine = pd.read_csv('cuisine.csv')
cuisine.head()


# In[17]:


tips_data = [] 
tips_id_counter = 1
existing_tips = set()

def insert_into_tips(row):
    global tips_id_counter
    
    if pd.notna(row['Notes']) and row['Notes'].strip() != "":
        tip_desc = row['Notes']
        
        if tip_desc not in existing_tips:
            tips_id = tips_id_counter
            
            tips_id_counter += 1
            existing_tips.add(tip_desc)
            
            tips_data.append({
               'tips_id' : tips_id,
                'tip_desc' : tip_desc
            })

df.apply(insert_into_tips, axis=1)

tips_df = pd.DataFrame(tips_data)

tips_df.to_csv('tips.csv', index=False)


# In[18]:


recipe_tips_data = []

def get_tip_id(tip_desc):
    tips_df = pd.read_csv('tips.csv')
    tip_row = tips_df[tips_df['tip_desc'] == tip_desc]
    
    if not tip_row.empty:
        return tip_row.iloc[0]['tips_id']
    else:
        return None

def insert_recipe_tip():
    for index, row in df.iterrows():
        recipe_id = row['recipe_id']
        tips_list = row['Notes'].split(',') if isinstance(row['Notes'], str) else []
        
        tips_list = [tip.strip() for tip in tips_list if tip.strip()]
        
        # Ensure a minimum of 2 and a maximum of 5 tips
        if len(tips_list) < 2:
            additional_tips_needed = 2 - len(tips_list)
            all_tips_df = pd.read_csv('tips.csv')
            available_tips = all_tips_df[~all_tips_df['tip_desc'].isin(tips_list)]
            additional_tips = available_tips.sample(n=additional_tips_needed)['tip_desc'].tolist()
            tips_list.extend(additional_tips)
        elif len(tips_list) > 5:
            tips_list = random.sample(tips_list, 5)

        for tip_desc in tips_list:
            tips_id = get_tip_id(tip_desc)
            if tips_id is not None:
                recipe_tips_data.append({
                    'recipe_recipe_id': recipe_id,
                    'tips_tips_id': tips_id
                })

# Assuming 'df' is already defined elsewhere in your code
insert_recipe_tip()

recipe_tips_df = pd.DataFrame(recipe_tips_data)
recipe_tips_df.to_csv('recipe_tips.csv', index=False)


# In[19]:


recipe_tips = pd.read_csv('recipe_tips.csv')
recipe_tips.head()


# In[20]:


types_of_meal_data = [] 
meal_type_id_counter = 1
existing_meal_types = set()

def insert_into_types_of_meal(row):
    global meal_type_id_counter
    
    if pd.notna(row['Type']) and row['Type'].strip() != "":
        meal_type_name = row['Type']
        
        if meal_type_name not in existing_meal_types:
            meal_type_id = meal_type_id_counter
            
            meal_type_id_counter += 1
            existing_meal_types.add(meal_type_name)
            
            types_of_meal_data.append({
                'meal_type_id' : meal_type_id,
                'meal_type_name' : meal_type_name
            })

df.apply(insert_into_types_of_meal, axis=1)

types_of_meal_df = pd.DataFrame(types_of_meal_data)

types_of_meal_df.to_csv('types_of_meal.csv', index=False)


# In[21]:


types_of_meal = pd.read_csv('types_of_meal.csv')
types_of_meal.head()


# In[22]:


recipe_meal_data = []

def get_meal_type_id(meal_type_name):
    meal_type_row = types_of_meal_df[types_of_meal_df['meal_type_name'] == meal_type_name]
    
    if not meal_type_row.empty:
        return meal_type_row.iloc[0]['meal_type_id']
    else:
        return None

def insert_meal_type():
    
    for index, row in df.iterrows():
        recipe_id = row['recipe_id']
        meal_type_list = row['Type'].split(',') if isinstance(row['Type'], str) else []
        
        for meal_type_name in meal_type_list:
            meal_type_name = meal_type_name.strip()
            if meal_type_name:
                meal_type_id = get_meal_type_id(meal_type_name)
                if meal_type_id is not None:
                    recipe_meal_data.append({
                        'recipe_recipe_id': recipe_id,
                        'types_of_meal_meal_type_id': meal_type_id
                    })

                    
insert_meal_type()
                    
recipe_meal_df = pd.DataFrame(recipe_meal_data)
    
recipe_meal_df.to_csv('recipe_meal.csv', index=False)


# In[23]:


recipe_meal = pd.read_csv('recipe_meal.csv')
recipe_meal.head()


# In[24]:


instructions = [
    "Preheat the oven to 350°F.",
    "Chop the onions finely.",
    "Whisk together the eggs and milk.",
    "Heat the olive oil in a skillet over medium heat.",
    "Grate the cheese and set aside.",
    "Rinse the vegetables under cold water.",
    "Season the chicken with salt and pepper.",
    "Melt the butter in a saucepan over low heat.",
    "Peel and mince the garlic cloves.",
    "Cook the pasta according to package instructions.",
    "Sauté the onions until translucent.",
    "Mix the dry ingredients in a large bowl.",
    "Add the chopped tomatoes to the pan.",
    "Stir-fry the vegetables for 5 minutes.",
    "Beat the egg whites until stiff peaks form.",
    "Marinate the meat with soy sauce and ginger.",
    "Toast the bread until golden brown.",
    "Blanch the spinach in boiling water.",
    "Simmer the sauce for 10 minutes.",
    "Toss the salad with vinaigrette dressing.",
    "Grill the steak for 3 minutes on each side.",
    "Spread the peanut butter evenly on the toast.",
    "Steam the broccoli until tender.",
    "Fold the whipped cream into the pudding.",
    "Roast the peppers until charred.",
    "Drizzle the olive oil over the salad.",
    "Boil the potatoes until fork-tender.",
    "Glaze the ham with honey and mustard.",
    "Blend the ingredients until smooth.",
    "Stuff the peppers with the rice mixture.",
    "Garnish the dish with fresh herbs.",
    "Crack the eggs into a hot pan.",
    "Layer the lasagna noodles with sauce and cheese.",
    "Knead the dough until it's smooth.",
    "Dip the shrimp in the egg wash and breadcrumbs.",
    "Roll the sushi tightly with a bamboo mat.",
    "Sauté the mushrooms until golden brown.",
    "Whisk the sauce until thickened.",
    "Fold the omelette in half.",
    "Sprinkle the cinnamon over the apple slices.",
    "Crush the cookies into fine crumbs.",
    "Glaze the doughnuts with chocolate icing.",
    "Slice the cucumber into thin rounds.",
    "Mix the batter until there are no lumps.",
    "Season the soup with salt and pepper to taste.",
    "Arrange the fruit in a decorative pattern.",
    "Roast the nuts until fragrant.",
    "Spread the frosting evenly on the cake.",
    "Poach the eggs in simmering water.",
    "Garnish the dish with a sprig of parsley."
]

steps_df = pd.DataFrame({'step_desc': instructions})

steps_df.to_csv('steps.csv', index=False)


# In[25]:


steps = pd.read_csv('steps.csv')
steps.insert(0, 'step_id', range(1, len(steps) + 1))

steps.to_csv('steps.csv', index=False)
steps = pd.read_csv('steps.csv')

steps.head()


# In[26]:


import csv
import random

# Define the list of recipe IDs and step IDs
recipe_ids = list(range(1, 146))
step_ids = list(range(1, 51))

# Initialize the list to store the pairs
recipe_steps_data = []

# Iterate over each recipe ID
for recipe_id in recipe_ids:
    # Select a random number of steps between 3 and 7
    num_steps = random.randint(3, 7)
    
    # Randomly select `num_steps` step IDs for the current recipe
    selected_steps = random.sample(step_ids, num_steps)
    
    # Create pairs of (recipe_id, step_id) and add them to the list
    for step_id in selected_steps:
        recipe_steps_data.append((recipe_id, step_id))

# Write the results to the CSV file
with open('recipe_steps.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['recipe_recipe_id', 'steps_step_id'])
    writer.writerows(recipe_steps_data)


# In[27]:


recipe_steps = pd.read_csv('recipe_steps.csv')
recipe_steps.head()


# In[28]:


food_groups = [
    'Fruits',
    'Vegetables',
    'Dairy products',
    'Grains',
    'Meat',
    'Poultry',
    'Seafood',
    'Nuts and seeds',
    'Legumes',
    'Herbs and spices',
    'Eggs',
    'Oils and fats',
    'Breads and cereals',
    'Beverages',
    'Snacks',
    'Condiments',
    'Desserts',
    'Soups and broths',
    'Pasta and noodles',
    'Fermented foods',
    'Frozen foods',
    'Canned foods',
    'Baked goods',
    'Breakfast foods',
    'Salads',
    'Sauces',
    'Sweets',
    'Pickled foods',
    'Deli meats',
    'Ethnic foods'
]

food_groups_df = pd.DataFrame({'step_desc': instructions})

steps_df.to_csv('steps.csv', index=False)

steps = pd.read_csv('steps.csv')
steps.insert(0, 'step_id', range(1, len(steps) + 1))

steps.to_csv('steps.csv', index=False)
steps = pd.read_csv('steps.csv')

steps.head()


# In[29]:


food_groups = [
    {'food_group_name': 'Fruits', 'food_group_desc': 'Naturally sweet and juicy foods that grow on trees or bushes.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Vegetables', 'food_group_desc': 'Edible plants that include leaves, stems, roots, flowers, and seeds.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Dairy products', 'food_group_desc': 'Products made from milk, such as cheese, yogurt, and butter.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Grains', 'food_group_desc': 'Edible seeds of grasses, including wheat, rice, oats, and barley.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Meat', 'food_group_desc': 'Animal flesh used as food, typically from mammals like beef, pork, and lamb.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Poultry', 'food_group_desc': 'Domesticated birds raised for meat, including chicken, turkey, and duck.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Seafood', 'food_group_desc': 'Edible aquatic animals and plants, including fish, shellfish, and seaweed.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Nuts and seeds', 'food_group_desc': 'Edible kernels found within hard shells, such as almonds, peanuts, and sunflower seeds.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Legumes', 'food_group_desc': 'Plants in the pea family that produce pods containing edible seeds, like beans, lentils, and chickpeas.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Herbs and spices', 'food_group_desc': 'Plants used to add flavor to food, often in dried or powdered form.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Eggs', 'food_group_desc': 'Reproductive bodies laid by female birds, typically used as food.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Oils and fats', 'food_group_desc': 'Liquids or semisolids derived from plants or animals, used in cooking and baking.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Breads and cereals', 'food_group_desc': 'Staple foods made from grains, typically baked into loaves or processed into flakes.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Beverages', 'food_group_desc': 'Drinks consumed for hydration, refreshment, or enjoyment, such as water, tea, coffee, and juice.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Snacks', 'food_group_desc': 'Small portions of food eaten between meals, often savory or sweet.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Condiments', 'food_group_desc': 'Sauces, spices, or other flavorful substances used to enhance the taste of food.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Desserts', 'food_group_desc': 'Sweet treats served after a meal, such as cakes, cookies, and ice cream.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Soups and broths', 'food_group_desc': 'Liquid dishes made by boiling ingredients like vegetables, meat, or grains.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Pasta and noodles', 'food_group_desc': 'Starchy foods made from wheat flour, water, and sometimes eggs, formed into various shapes.', 'food_group_categorization': 'Vegan'},
    {'food_group_name': 'Fermented foods', 'food_group_desc': 'Foods altered by microbial action, such as yogurt, kimchi, and sauerkraut.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Frozen foods', 'food_group_desc': 'Prepared meals, fruits, vegetables, or other foods that have been frozen for preservation.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Canned foods', 'food_group_desc': 'Foods preserved and stored in metal cans, jars, or other containers.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Baked goods', 'food_group_desc': 'Foods made by baking, including bread, cakes, pastries, and cookies.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Breakfast foods', 'food_group_desc': 'Foods commonly eaten in the morning, such as cereal, pancakes, and eggs.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Salads', 'food_group_desc': 'Mixed dishes made with a combination of vegetables, fruits, grains, and proteins.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Sauces', 'food_group_desc': 'Liquid or semi-solid condiments used to add flavor or moisture to food.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Sweets', 'food_group_desc': 'Confections or sugary treats, including candies, chocolates, and pastries.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Pickled foods', 'food_group_desc': 'Foods preserved by anaerobic fermentation in brine or vinegar, like pickles and olives.', 'food_group_categorization': 'Varies'},
    {'food_group_name': 'Deli meats', 'food_group_desc': 'Cooked or cured meats sliced and sold at a delicatessen, including ham, salami, and roast beef.', 'food_group_categorization': 'Non-vegan'},
    {'food_group_name': 'Ethnic foods', 'food_group_desc': 'Traditional foods and dishes associated with specific cultures or regions around the world.', 'food_group_categorization': 'Varies'}
]

food_groups_data = []

for i, food_group in enumerate(food_groups, start=1):
    food_group_id = i
    food_group_name = food_group['food_group_name']
    food_group_desc = food_group['food_group_desc']
    food_group_categorization = food_group['food_group_categorization']
    food_group_img = fake.image_url(width=200, height=200) 
    
    food_groups_data.append({
        'food_group_id': food_group_id,
        'food_group_name': food_group_name,
        'food_group_desc': food_group_desc,
        'food_group_categorization': food_group_categorization,
        'food_group_img': food_group_img
    })
    
food_groups_df = pd.DataFrame(food_groups_data)

food_groups_df.to_csv('food_groups.csv', index=False)


# In[30]:


food_groups = pd.read_csv('food_groups.csv')
food_groups.head()


# In[39]:


fg_column_name = 'food_group_name'

fg_column_data = food_groups[fg_column_name].tolist()

ingr_column_name = 'ingredient_name'

ingr_column_data = ingredients[ingr_column_name].tolist()

print(f"Print list of food groups:")
print(fg_column_data)
print(f"Print list of ingredients:")
print(ingr_column_data)


# In[31]:


food_groups = []
with open('food_groups.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        food_groups.append(row['food_group_id'])

ingredients = []
with open('ingredients.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ingredients.append(row['ingredient_id'])

entries = []
for ingredient in ingredients:
    food_group = random.choice(food_groups)
    entries.append((ingredient, food_group))

while len(entries) < 40:
    ingredient = random.choice(ingredients)
    food_group = random.choice(food_groups)
    entries.append((ingredient, food_group))

random.shuffle(entries)

with open('ingredients_food_group.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ingredients_ingredient_id', 'food_group_food_group_id'])
    writer.writerows(entries)


# In[32]:


ingredients_food_group = pd.read_csv('ingredients_food_group.csv')
ingredients_food_group.head()


# In[33]:


equipment_list = [
    {
        'equipment_name': 'Chef\'s knife',
        'instructions': 'Use for chopping, slicing, and dicing ingredients.'
    },
    {
        'equipment_name': 'Cutting board',
        'instructions': 'Place ingredients on the board for cutting and chopping.'
    },
    {
        'equipment_name': 'Mixing bowls',
        'instructions': 'Use for mixing ingredients or as containers for food preparation.'
    },
    {
        'equipment_name': 'Measuring cups',
        'instructions': 'Use to measure dry or liquid ingredients.'
    },
    {
        'equipment_name': 'Measuring spoons',
        'instructions': 'Use to measure small amounts of dry or liquid ingredients.'
    },
    {
        'equipment_name': 'Whisk',
        'instructions': 'Use for mixing and incorporating air into ingredients.'
    },
    {
        'equipment_name': 'Wooden spoon',
        'instructions': 'Use for stirring, mixing, and scraping ingredients.'
    },
    {
        'equipment_name': 'Spatula',
        'instructions': 'Use for flipping, lifting, and spreading ingredients.'
    },
    {
        'equipment_name': 'Ladle',
        'instructions': 'Use for serving soups, stews, and sauces.'
    },
    {
        'equipment_name': 'Tongs',
        'instructions': 'Use for grabbing and flipping ingredients while cooking.'
    },
    {
        'equipment_name': 'Rolling pin',
        'instructions': 'Use for rolling out dough for pastries, bread, or cookies.'
    },
    {
        'equipment_name': 'Grater',
        'instructions': 'Use to grate cheese, vegetables, or citrus zest.'
    },
    {
        'equipment_name': 'Vegetable peeler',
        'instructions': 'Use to peel the skin off vegetables or fruits.'
    },
    {
        'equipment_name': 'Can opener',
        'instructions': 'Use to open canned goods.'
    },
    {
        'equipment_name': 'Kitchen shears',
        'instructions': 'Use for cutting herbs, trimming meat, or opening packages.'
    },
    {
        'equipment_name': 'Colander',
        'instructions': 'Use for draining liquids from cooked pasta or washing vegetables.'
    },
    {
        'equipment_name': 'Strainer',
        'instructions': 'Use for straining liquids or sifting dry ingredients.'
    },
    {
        'equipment_name': 'Sifter',
        'instructions': 'Use to aerate and break up clumps in dry ingredients.'
    },
    {
        'equipment_name': 'Kitchen scale',
        'instructions': 'Use to measure ingredients by weight for precision.'
    },
    {
        'equipment_name': 'Blender',
        'instructions': 'Use to blend, puree, or emulsify ingredients.'
    },
    {
        'equipment_name': 'Food processor',
        'instructions': 'Use to chop, shred, slice, or puree ingredients.'
    },
    {
        'equipment_name': 'Stand mixer',
        'instructions': 'Use for mixing, beating, and kneading dough or batter.'
    },
    {
        'equipment_name': 'Hand mixer',
        'instructions': 'Use for mixing, beating, and whipping ingredients.'
    },
    {
        'equipment_name': 'Immersion blender',
        'instructions': 'Use to blend or puree ingredients directly in the pot or container.'
    },
    {
        'equipment_name': 'Pastry brush',
        'instructions': 'Use to brush egg wash, butter, or glaze onto pastries or meats.'
    },
    {
        'equipment_name': 'Basting brush',
        'instructions': 'Use to coat meat or poultry with drippings or marinade while cooking.'
    },
    {
        'equipment_name': 'Pastry cutter',
        'instructions': 'Use to cut butter or shortening into flour when making pastry dough.'
    },
    {
        'equipment_name': 'Garlic press',
        'instructions': 'Use to crush garlic cloves into small pieces or paste.'
    },
    {
        'equipment_name': 'Citrus juicer',
        'instructions': 'Use to extract juice from citrus fruits like lemons, limes, or oranges.'
    },
    {
        'equipment_name': 'Mortar and pestle',
        'instructions': 'Use to grind, crush, or mix spices, herbs, or grains.'
    },
    {
        'equipment_name': 'Microplane zester',
        'instructions': 'Use to grate citrus zest, cheese, or spices.'
    },
    {
        'equipment_name': 'Mandoline slicer',
        'instructions': 'Use to slice fruits or vegetables thinly and uniformly.'
    },
    {
        'equipment_name': 'Egg separator',
        'instructions': 'Use to separate egg yolks from egg whites.'
    },
    {
        'equipment_name': 'Potato masher',
        'instructions': 'Use to mash cooked potatoes, vegetables, or beans.'
    },
    {
        'equipment_name': 'Ice cream scoop',
        'instructions': 'Use to scoop and serve ice cream, sorbet, or mashed potatoes.'
    },
    {
        'equipment_name': 'Pizza cutter',
        'instructions': 'Use to cut pizza or flatbreads into slices.'
    },
    {
        'equipment_name': 'Cookie cutters',
        'instructions': 'Use to cut cookie dough into various shapes before baking.'
    },
    {
        'equipment_name': 'Piping bags and tips',
        'instructions': 'Use to pipe frosting, icing, or batter for decorating cakes or pastries.'
    },
    {
        'equipment_name': 'Pastry bag',
        'instructions': 'Use to pipe fillings, frosting, or batter for decorating desserts.'
    },
    {
        'equipment_name': 'Cake decorating comb',
        'instructions': 'Use to create textured designs on frosted cakes or desserts.'
    },
    {
        'equipment_name': 'Food thermometer',
        'instructions': 'Use to measure the internal temperature of food for doneness.'
    },
    {
        'equipment_name': 'Timer',
        'instructions': 'Use to set cooking or baking times for recipes.'
    },
    {
        'equipment_name': 'Kitchen torch',
        'instructions': 'Use to caramelize sugar, melt cheese, or brown meringue.'
    },
    {
        'equipment_name': 'Cooking twine',
        'instructions': 'Use to truss poultry, tie roasts, or secure stuffed meats.'
    },
    {
        'equipment_name': 'Meat tenderizer',
        'instructions': 'Use to pound or tenderize meat to make it more tender.'
    },
    {
        'equipment_name': 'Fish scaler',
        'instructions': 'Use to remove scales from fish before cooking.'
    },
    {
        'equipment_name': 'Oyster shucker',
        'instructions': 'Use to open oysters by prying apart the shell.'
    },
    {
        'equipment_name': 'Apple corer',
        'instructions': 'Use to remove the core from apples or pears.'
    },
    {
        'equipment_name': 'Melon baller',
        'instructions': 'Use to scoop out melon or other fruits into round balls.'
    },
    {
        'equipment_name': 'Nutcracker',
        'instructions': 'Use to crack open shells of nuts to access the nutmeat.'
    }
]


equipment_ids = list(range(1, len(equipment_list) + 1))

equipment_imgs = [fake.image_url() for _ in range(len(equipment_list))]

for i, equipment in enumerate(equipment_list):
    equipment['equipment_id'] = equipment_ids[i]
    equipment['equipment_img'] = equipment_imgs[i]

equipment = pd.DataFrame(equipment_list)

equipment = equipment[['equipment_id', 'equipment_name', 'instructions', 'equipment_img']]

equipment.to_csv('equipment.csv', index=False)


# In[34]:


equipment = pd.read_csv('equipment.csv')
equipment.head()


# In[35]:


recipe_ids = list(range(1, 145))
equipment_ids = list(range(1, 50))

recipe_equipment_data = []

for recipe_id in recipe_ids:
    num_equipment = random.randint(1, 3)
    
    selected_equipment = random.sample(equipment_ids, num_equipment)
    
    for equipment_id in selected_equipment:
        recipe_equipment_data.append({
            'recipe_recipe_id': recipe_id,
            'equipment_equipment_id': equipment_id
        })

recipe_equipment_df = pd.DataFrame(recipe_equipment_data)

recipe_equipment_df.to_csv('recipe_equipment.csv', index=False)


# In[36]:


recipe_equipment = pd.read_csv('recipe_equipment.csv')
recipe_equipment.head()


# In[37]:


rounds_data = []

for year in range(2010, 2024):  
    for round_number in range(1, 11):  # 10 rounds for each year
        round_id = len(rounds_data) + 1
        round_img = fake.image_url()
        rounds_data.append({
            'round_id': round_id,
            'round_year': year,
            'round_number': round_number,
            'round_img': round_img
        })

with open('rounds.csv', 'w', newline='') as csvfile:
    fieldnames = ['round_id', 'round_year', 'round_number', 'round_img']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for round_data in rounds_data:
        writer.writerow(round_data)


# In[38]:


rounds = pd.read_csv('rounds.csv')
rounds.head()


# In[39]:


admin_data = []

for admin_id in range(1, 5):
    admin_username = fake.user_name()
    admin_passw = fake.password()
    
    admin_data.append({
        'admin_id': admin_id,
        'admin_username': admin_username,
        'admin_password': admin_passw
    })
    
with open('administrator.csv', 'w', newline='') as csvfile:
    fieldnames = ['admin_id', 'admin_username', 'admin_password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for admin in admin_data:
        writer.writerow(admin)


# In[40]:


administrator = pd.read_csv('administrator.csv')
administrator.head()


# In[41]:


tags_data = [{'tag_desc': '#' + fake.word()} for _ in range(50)]

tags_df = pd.DataFrame(tags_data)

tags_df.to_csv('tags.csv', index=False)
tags_df = pd.read_csv('tags.csv')
tags_df['tag_id'] = range(1, len(tags_data) + 1)
tags_df = tags_df[['tag_id', 'tag_desc']]

tags_df.to_csv('tags.csv', index=False)


# In[42]:


tags = pd.read_csv('tags.csv')
tags.head()


# In[43]:


recipe_ids = list(range(1, 146))
tag_ids = list(range(1, 51))

recipe_tag_data = []

for recipe_id in recipe_ids:
    num_tags = random.randint(1, 5)
    
    selected_tags = random.sample(tag_ids, num_tags)
    
    for tag_id in selected_tags:
        recipe_tag_data.append({'recipe_recipe_id': recipe_id, 'tags_tag_id': tag_id})

recipe_tag_df = pd.DataFrame(recipe_tag_data)
recipe_tag_df.to_csv('recipe_tag.csv', index=False)


# In[44]:


recipe_tag = pd.read_csv('recipe_tag.csv')
recipe_tag.head()


# In[45]:


time_data = []

for _ in range(50):
    preparation_time = random.randint(20, 120)
    execution_time = random.randint(20, 120)
    total_time = preparation_time + execution_time
    
    time_data.append({
        'total_time': total_time,
        'preparation_time': preparation_time,
        'execution_time': execution_time
    })

fieldnames = ['total_time', 'preparation_time', 'execution_time']

with open('time.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    
    writer.writerows(time_data)


# In[46]:


recipe_time = pd.read_csv('time.csv')
recipe_time.head()


# In[47]:


recipe_ids = list(range(1, 146))
time_total_time = [row['total_time'] for row in time_data]

recipe_time_data = [{'recipe_recipe_id': recipe_id, 'recipe_time_total_time': random.choice(time_total_time)} for recipe_id in recipe_ids]

recipe_time_df = pd.DataFrame(recipe_time_data)

recipe_time_df.to_csv('recipe_takes_time.csv', index=False)


# In[48]:


recipe_takes_time = pd.read_csv('recipe_takes_time.csv')
recipe_takes_time.head()


# In[49]:


subjects_list = [
    {"subject_name": "Italian Classics", "subject_desc": "Recipes for traditional Italian dishes like lasagna and spaghetti."},
    {"subject_name": "Breakfast Delights", "subject_desc": "Start your day with delicious breakfast recipes like pancakes and French toast."},
    {"subject_name": "Comfort Food Favorites", "subject_desc": "Warm and satisfying comfort food recipes, perfect for cozy nights in."},
    {"subject_name": "Healthy Eating", "subject_desc": "Nutritious and delicious recipes for a balanced diet."},
    {"subject_name": "Vegetarian Delights", "subject_desc": "Meat-free recipes packed with flavor and goodness."},
    {"subject_name": "Quick and Easy Meals", "subject_desc": "Simple recipes that are ready in no time, perfect for busy weeknights."},
    {"subject_name": "Summer BBQ", "subject_desc": "Grilled recipes and summer favorites for outdoor gatherings."},
    {"subject_name": "Family Favorites", "subject_desc": "Recipes loved by the whole family, from kids to adults."},
    {"subject_name": "One-Pot Wonders", "subject_desc": "Easy recipes that require only one pot or pan, for minimal cleanup."},
    {"subject_name": "Dessert Extravaganza", "subject_desc": "Indulgent dessert recipes to satisfy your sweet tooth."},
    {"subject_name": "Holiday Specials", "subject_desc": "Festive recipes perfect for holiday celebrations."},
    {"subject_name": "Asian Cuisine", "subject_desc": "Delicious recipes inspired by Asian flavors and ingredients."},
    {"subject_name": "Mediterranean Feasts", "subject_desc": "Healthy and flavorful recipes from the Mediterranean region."},
    {"subject_name": "Slow Cooker Creations", "subject_desc": "Tasty recipes that simmer all day in the slow cooker for maximum flavor."},
    {"subject_name": "Gluten-Free Goodness", "subject_desc": "Recipes that are gluten-free and delicious for those with dietary restrictions."},
    {"subject_name": "Soup Season", "subject_desc": "Warm and comforting soup recipes for chilly days."},
    {"subject_name": "Appetizer Heaven", "subject_desc": "Tasty appetizers and finger foods perfect for parties and gatherings."},
    {"subject_name": "Seafood Sensations", "subject_desc": "Delicious seafood recipes featuring fresh fish and shellfish."},
    {"subject_name": "Vegan Vibes", "subject_desc": "Plant-based recipes that are vegan-friendly and full of flavor."},
    {"subject_name": "Holiday Baking", "subject_desc": "Bake up a storm with these festive holiday baking recipes."}
]


subject_ids = list(range(1, len(subjects_list) + 1))

subject_imgs = [fake.image_url() for _ in range(len(subjects_list))]

for i, subject in enumerate(subjects_list):
    subject['subject_id'] = subject_ids[i]
    subject['subject_img'] = subject_imgs[i]

subject = pd.DataFrame(subjects_list)

subject = subject[['subject_id', 'subject_name', 'subject_desc', 'subject_img']]

subject.to_csv('subject.csv', index=False)


# In[50]:


subject = pd.read_csv('subject.csv')
subject.head()


# In[51]:


recipe_ids = []

with open('recipe.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        recipe_ids.append(int(row['recipe_id']))

subject_ids = list(range(1, 21))  

recipe_subject_mapping = {}

for idx, recipe_id in enumerate(recipe_ids, start=1):
    subject_id = subject_ids[(idx - 1) % len(subject_ids)]
    recipe_subject_mapping[recipe_id] = subject_id

with open('recipe_subject.csv', 'w', newline='') as csvfile:
    fieldnames = ['recipe_id', 'subject_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for recipe_id, subject_id in recipe_subject_mapping.items():
        writer.writerow({'recipe_id': recipe_id, 'subject_id': subject_id})


# In[52]:


recipe_subject = pd.read_csv('recipe_subject.csv')
recipe_subject.head()


# In[55]:


import csv
import random
from faker import Faker

fake = Faker()

cooks_data = []
cook_id_counter = 1
positions = ['chef', 'sous-chef', 'first cook', 'second cook', 'third cook']
used_phone_numbers = set()  

while len(cooks_data) < 200:  
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    if phone_number in used_phone_numbers:
        continue
    used_phone_numbers.add(phone_number)
    birth_date = fake.date_of_birth(minimum_age=25, maximum_age=60)
    age = fake.random_int(min=25, max=60)
    years_of_experience = fake.random_int(min=1, max=10)
    position = random.choice(positions)
    cook_img = fake.image_url()
    username = fake.user_name()
    password = fake.password()
    
    cooks_data.append({
        'cook_id': cook_id_counter,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'birth_date': birth_date.strftime('%Y-%m-%d'), 
        'age': age,
        'years_of_experience': years_of_experience,
        'position': position,
        'cook_img': cook_img,
        'username': username,
        'password': password
    })
    
    cook_id_counter += 1

with open('cook.csv', 'w', newline='') as csvfile:
    fieldnames = ['cook_id', 'first_name', 'last_name', 'phone_number', 'birth_date', 'age', 'years_of_experience',
                  'position', 'cook_img', 'username', 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for cook in cooks_data:
        writer.writerow(cook)


# In[56]:


cook = pd.read_csv('cook.csv')
cook.head()


# In[58]:


recipe_ids = list(range(1, 146))
cook_ids = list(range(1, 201))

recipe_cook_data = []

for cook_id in cook_ids:
    num_recipes = random.randint(3, 10)
    selected_recipes = random.sample(recipe_ids, num_recipes)
    
    for recipe_id in selected_recipes:
        recipe_cook_data.append({'cook_cook_id': cook_id, 'recipe_recipe_id': recipe_id})

cook_executes_recipe_df = pd.DataFrame(recipe_cook_data)
cook_executes_recipe_df.to_csv('cook_executes_recipe.csv', index=False)


# In[59]:


cook_executes_recipe = pd.read_csv('cook_executes_recipe.csv')
cook_executes_recipe.head()


# In[272]:


cook_ids = list(range(1, 201))
cuisine_ids = list(range(1, 51))

cook_cuisine_data = []

for cook_id in cook_ids:
    num_cuisines = random.randint(3, 7)
    selected_cuisines = random.sample(cuisine_ids, num_cuisines)
    
    for cuisine_id in selected_cuisines:
        years_of_experience = random.randint(1, 20)
        cook_cuisine_data.append({'cook_cook_id': cook_id, 'cuisine_cuisine_id': cuisine_id, 'years_of_experience': years_of_experience})

with open('cook_knows_cuisine.csv', 'w', newline='') as csvfile:
    fieldnames = ['cook_cook_id', 'cuisine_cuisine_id', 'years_of_experience']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(cook_cuisine_data)


# In[273]:


cook_knows_cuisine = pd.read_csv('cook_knows_cuisine.csv')
cook_knows_cuisine.head()


# In[290]:


def fill_cooks_participate_in_round():
    cursor = db_connection.cursor()

    with open('cooks_participate_in_round.csv', 'w', newline='') as csvfile:
        fieldnames = ['cook_id', 'round_id', 'recipe_cuisine_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        cursor.execute("""
            SELECT ccr.round_round_id, ccr.cuisine_cuisine_id
            FROM cuisines_chosen_for_round ccr
            GROUP BY ccr.round_round_id, ccr.cuisine_cuisine_id
            ORDER BY ccr.round_round_id, ccr.cuisine_cuisine_id;
        """)
        rounds = cursor.fetchall()

        for round_id, cuisine_id in rounds:
            selected_cooks = set()  # To store selected cook_id for this round and avoid repetition
            cursor.execute("""
                SELECT ckc.cook_cook_id
                FROM cook_knows_cuisine ckc
                WHERE ckc.cuisine_cuisine_id = %s
                ORDER BY RAND();
            """, (cuisine_id,))
            cooks = cursor.fetchall()

            for cook_id, in cooks:
                if cook_id not in selected_cooks:
                    writer.writerow({'cook_id': cook_id, 'round_id': round_id, 'recipe_cuisine_id': cuisine_id})
                    selected_cooks.add(cook_id)
                    if len(selected_cooks) == 1:  # Stop selecting once 10 cooks are selected for this round
                        break

    db_connection.commit()

fill_cooks_participate_in_round()


# In[69]:


df = pd.read_csv('cooks_participate_in_round.csv')
df['cook_id'] = pd.to_numeric(df['cook_id'], errors='coerce')
df = df.dropna(subset=['cook_id'])
df['cook_id'] = df['cook_id'].astype(int)
df.to_csv('cooks_participate_in_round.csv', index=False)


# In[70]:


cooks_participate_in_round = pd.read_csv('cooks_participate_in_round.csv')
cooks_participate_in_round.head()


# In[71]:


# Function to check if a combination of values exists in both tables
# cooks_participate_in_round and cooks_judge_round
def check_combination(round_id, cook_id):
    cursor.execute("SELECT * FROM cooks_participate_in_round WHERE round_round_id = %s AND cook_cook_id = %s", (round_id, cook_id))
    result_participate = cursor.fetchone()

    cursor.execute("SELECT * FROM cooks_judge_round WHERE round_round_id = %s AND cook_cook_id = %s", (round_id, cook_id))
    result_judge = cursor.fetchone()

    if result_participate and result_judge:
        return True
    else:
        return False

# Check combinations for round_id ranging from 1 to 140 and cook_id ranging from 1 to 100
for round_id in range(1, 141):
    for cook_id in range(1, 101):
        if check_combination(round_id, cook_id):
            print(f"Combination ({round_id}, {cook_id}) exists in both tables.")


# In[ ]:





# In[ ]:





# In[250]:


import mysql.connector 

db_connection = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "mydb"
)


# In[215]:


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


# In[216]:


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


# In[236]:


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


# In[251]:


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


# In[242]:


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


# In[252]:


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


# In[253]:


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


# In[255]:


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


# In[254]:


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


# In[256]:


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


# In[257]:


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


# In[258]:


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


# In[259]:


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


# In[260]:


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


# In[261]:


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


# In[262]:


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


# In[263]:


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


# In[264]:


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


# In[265]:


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


# In[266]:


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


# In[267]:


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


# In[268]:


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


# In[269]:


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


# In[270]:


# Load data from 'cook.csv' into table 'cook'
query = """
LOAD DATA INFILE 'cook.csv'
INTO TABLE cook
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(cook_id, first_name, last_name, phone_number, birth_date, age, years_of_experience, position, cook_img, username, password)
"""

cursor = db_connection.cursor()

cursor.execute(query)

db_connection.commit()


# In[271]:


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


# In[274]:


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


# In[275]:


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


# In[294]:


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


# In[311]:


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


# In[313]:


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


# In[ ]:





# In[122]:


cursor.close()
db_connection.close()

