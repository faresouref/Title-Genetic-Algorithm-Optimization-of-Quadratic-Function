from random import randint, uniform, choice

def func(x):
    return x**2 - 4*x + 3

search_space = (-5.0, 5.0)  

population_size = 100 
generations = 50     

def fitness(chromosome):
    x = chromosome['x']
    return -func(x)   

population = []
for i in range(population_size):
    x = uniform(*search_space)   
    chromosome = {'x': x}
    population.append(chromosome)

for generation in range(generations):
    fitness_scores = [fitness(chromosome) for chromosome in population]
    
    num_parents = int(population_size * 0.1)
    parents = [population[i] for i in sorted(range(population_size),
    key=lambda i: fitness_scores[i])[:num_parents]]

    offspring = []
    while len(offspring) < population_size - num_parents:
        parent1 = choice(parents)
        parent2 = choice(parents)
        child = {'x': 0}
        child['x'] = (parent1['x'] + parent2['x']) / 2
        if randint(0, 1):
            child['x'] += uniform(-0.5, 0.5)
        offspring.append(child)
    population = parents + offspring
    
best_chromosome = max(population, key=lambda chromosome: fitness(chromosome))

print("Optimization function:")
print("f(x) = x^2 - 4x + 3")
print("Search space:")
print(search_space)
print("Solution:")
print("x =", best_chromosome['x'])
print("f(x) =", -fitness(best_chromosome))