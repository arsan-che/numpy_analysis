import numpy as np

# Define cupcake recipe ingredients: [flour, sugar, eggs, butter, milk]
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# Load the recipes from a CSV file (assumes no header row)
recipes = np.genfromtxt('recipes.csv', delimiter=',')

# Extract the "eggs" column (3rd column, index 2)
eggs = recipes[:, 2]

# Print the full recipe array
print(recipes)
# Filter recipes that use exactly 1 egg
one_egg = recipes[eggs == 1]
print(one_egg)

# Select the 3rd recipe (index 2), assumed to be cookies
cookies = recipes[2, :]
print(cookies)
