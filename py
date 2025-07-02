import numpy as np

# Define cupcake recipe ingredients: [flour, sugar, eggs, butter, milk]
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# Load the recipes from a CSV file (assumes no header row)
recipes = np.genfromtxt('recipes.csv', delimiter=',')

# Extract the "eggs" column (3rd column, index 2)
eggs = recipes[:, 2]

# Print the full recipe array
print(recipes)
