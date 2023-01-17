import random


sides = ["heads", "tails"]
side_weights = [0.20, 0.80]

# Equal weights for each choice (e.g. 50/50)
print('Fair Coin')
for _ in range(0, 9):
    print(random.choice(sides))



sides = ["heads", "tails"]
side_weights = [0.20, 0.80]
# Unequal weights for each choice (e.g. NOT 50/50)
print('Unfair Coin')
for _ in range(0, 9):
    print(random.choices(population=sides, weights=side_weights,k=1)[0])
