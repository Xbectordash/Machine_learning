import random
import operator
import numpy as np


# Define the polynomial function
def polynomial(x):
    return x**4 + 5 * x ** 3 + 7 * x ** 2 + 18 * x - 12


# Define the fitness function
def fitness(x):
    # The fitness is the negative absolute value of the polynomial function
    # because we want to minimize the function (find roots)
    return -abs(polynomial(x))


# Define the genetic algorithm
def genetic_algorithm(population_size, generations, mutation_rate):
    # Initialize population with random values
    population = [random.uniform(-10, 10) for _ in range(population_size)]

    # Run the algorithm for a set number of generations
    for generation in range(generations):
        # Evaluate fitness for each individual
        fitness_results = list(map(fitness, population))

        # Create a mating pool
        mating_pool = [x for _, x in sorted(zip(fitness_results, population), key=operator.itemgetter(0), reverse=True)]

        # Perform crossover and mutation
        next_generation = []
        for i in range(0, population_size, 2):
            parent1 = mating_pool[i]
            parent2 = mating_pool[i + 1]
            # Crossover
            child1 = (parent1 + parent2) / 2
            child2 = (parent1 - parent2) / 2
            # Mutation
            child1 += child1 * mutation_rate * (1 if random.random() < 0.5 else -1)
            child2 += child2 * mutation_rate * (1 if random.random() < 0.5 else -1)
            next_generation.extend([child1, child2])

        # Update population
        population = next_generation

    # Return the best solution
    best_solution = max(population, key=fitness)
    return best_solution


# Parameters
population_size = 100
generations = 100
mutation_rate = 0.01

# Run the genetic algorithm
solution = genetic_algorithm(population_size, generations, mutation_rate)

# Print the solution
print(
    f"The solution to the polynomial equation is approximately x = {solution}, with a fitness of {fitness(solution)}.")
