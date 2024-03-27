from collections import namedtuple
from random import choices
from typing import List, Callable

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
Thing = namedtuple('Thing', ['name', 'value', 'weight'])

things = [
    Thing('Laptop',500,2200),
    Thing('Headphones',150,160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad',40,333),
    Thing('Water Bottle',30,192),
]

more_things = [
    Thing('Mints',5,25),
    Thing('Socks',10,38),
    Thing('Tissues',15,80),
    Thing('Phone',500,200),
    Thing('Baseball Cap',100,70)
] + things

def generate_genome(length:int) -> Genome:
    return choices([0,1], k = length)

def generate_population(size:int, genome_length:int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

def fitness(genome:Genome,things :[Thing],weight_limit:int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of the same length")

    weight = 0
    value = 0
    for i , thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value
            if weight > weight_limit:
                return value


    return value

def selection_pair(population:Population, fitness_func: FitnessFunc) -> Population:
    """
    Selects two individuals from the population based on their fitness.
    """
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k = 2
    )