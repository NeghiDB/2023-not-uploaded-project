# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 03:25:53 2023

@author: deLaw
"""

import random

# Define some variables
POPULATION_SIZE = 100
GENE_LENGTH = 5
MUTATION_RATE = 0.1
NUM_GENERATIONS = 50

# Define the possible timeslots
timeslots = ['Mon 9:00', 'Mon 10:00', 'Mon 11:00', 'Tue 9:00', 'Tue 10:00', 'Tue 11:00', 'Wed 9:00', 'Wed 10:00', 'Wed 11:00', 'Thu 9:00', 'Thu 10:00', 'Thu 11:00', 'Fri 9:00', 'Fri 10:00', 'Fri 11:00']

# Define the possible courses and their required timeslots
courses = {
    'MIS': ['Mon 9:00', 'Tue 9:00', 'Wed 9:00', 'Thu 9:00', 'Fri 9:00'],
    'Data Structure': ['Mon 10:00', 'Tue 10:00', 'Wed 10:00', 'Thu 10:00', 'Fri 10:00'],
    'Web Dev': ['Mon 11:00', 'Tue 11:00', 'Wed 11:00', 'Thu 11:00', 'Fri 11:00'],
    'Statistis': ['Mon 9:00', 'Wed 9:00', 'Fri 9:00'],
    'Java': ['Tue 9:00', 'Thu 9:00', 'Wed 11:00'],
    'Database': ['Tue 9:00', 'Fri 11:00'],
    'Statistical Comp': ['Tue 9:00',  'Fri 11:00'],
    'Computer Systems': ['Tue 9:00', 'Thu 9:00'],
    'HCI': ['Tue 9:00', 'Thu 9:00', 'Wed 11:00'],
    'GST': ['Tue 9:00', 'Thu 9:00', 'Fri 11:00'],
    'Physics': [ 'Fri 11:00', 'Thu 9:00', 'Wed 11:00'],
    'Maths': ['Tue 9:00', 'Thu 9:00', 'Fri 11:00'],
    'Research Meth': ['Tue 9:00', 'Thu 9:00'],
    'Comp Network': ['Tue 9:00', 'Thu 9:00', 'Fri 11:00'],
    'Software Eng': ['Tue 9:00', 'Thu 9:00', 'Wed 11:00'],
    'Algorithms': ['Tue 9:00', 'Thu 9:00'],
    'Net Centric': ['Tue 9:00', 'Thu 9:00'],
    'OOP': ['Tue 9:00', 'Thu 9:00', 'Fri 11:00'],
    'Operating System': ['Tue 9:00', 'Thu 9:00', 'Wed 11:00'],
    
    
}

# Define the fitness function
def fitness(chromosome):
    score = 0
    for course, timeslot in chromosome.items():
        if timeslot in courses[course]:
            score += 1
    return score

# Define the crossover function
def crossover(parent1, parent2):
    child = {}
    for gene in courses.keys():
        if random.random() < 0.5:
            child[gene] = parent1[gene]
        else:
            child[gene] = parent2[gene]
    return child

# Define the mutation function
def mutation(chromosome):
    for gene in courses.keys():
        if random.random() < MUTATION_RATE:
            chromosome[gene] = random.choice(timeslots)
    return chromosome

# Initialize the population
population = [{} for _ in range(POPULATION_SIZE)]
for chromosome in population:
    for gene in courses.keys():
        chromosome[gene] = random.choice(timeslots)

# Main loop
for generation in range(NUM_GENERATIONS):

    # Evaluate fitness
    fitness_scores = [fitness(chromosome) for chromosome in population]

    # Select parents
    parents = []
    for _ in range(POPULATION_SIZE // 2):
        parent1 = random.choices(population, weights=fitness_scores)[0]
        parent2 = random.choices(population, weights=fitness_scores)[0]
        parents.append((parent1, parent2))

    # Generate offspring
    offspring = []
    for parent1, parent2 in parents:
        child = crossover(parent1, parent2)
        child = mutation(child)
        offspring.append(child)

    # Replace population with offspring
    population = offspring

    # Print best solution
    best_chromosome = max(population, key=fitness)
    best_fitness = fitness(best_chromosome)
    print(f'Generation {generation + 1}: {best_chromosome} (fitness: {best_fitness})')
