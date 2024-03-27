import random

# Define the range for potential roots
min_range = -10
max_range = 10

# Set the desired population size
population_size = 100

# Initialize the population with random guesses for roots
population = [random.uniform(min_range, max_range) for _ in range(population_size)]

print(population)

def fitness_function(chromosome, polynomial):
    # Calculate the polynomial value at the given root
    polynomial_value = sum(coef * (chromosome ** i) for i, coef in enumerate(polynomial))
    # The fitness score could be the inverse of the absolute error
    fitness_score = 1 / abs(polynomial_value)
    return fitness_score
