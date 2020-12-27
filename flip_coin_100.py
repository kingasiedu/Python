import random
import itertools

results ={
    "head": 0,
    "Tails": 0,
}
sides = list(results.keys())

for i in range(1000):
    results[random.choice(sides)] += 1

print("Heads:", results["head"])
print("Tails:", results["Tails"])


