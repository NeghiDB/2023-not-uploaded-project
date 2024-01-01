# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 04:09:24 2023

@author: deLaw
"""

import random

# Define the courses
courses = [
    ('Math', ['Monday', 'Tuesday', 'Wednesday'], ['9:00', '10:00', '11:00'], ['Room A', 'Room B'], ['Level 1', 'Level 2']),
    ('Science', ['Monday', 'Tuesday', 'Wednesday'], ['9:00', '10:00', '11:00'], ['Room C', 'Room D'], ['Level 1', 'Level 2']),
    ('English', ['Monday', 'Tuesday', 'Wednesday'], ['9:00', '10:00', '11:00'], ['Room E', 'Room F'], ['Level 1', 'Level 2']),
    ('History', ['Monday', 'Tuesday', 'Wednesday'], ['9:00', '10:00', '11:00'], ['Room G', 'Room H'], ['Level 1', 'Level 2']),
    ('Art', ['Monday', 'Tuesday', 'Wednesday'], ['9:00', '10:00', '11:00'], ['Room I', 'Room J'], ['Level 1', 'Level 2']),
    ('Music', ['Monday', 'Tuesday', 'Wednesday'], ['9:00', '10:00', '11:00'], ['Room K', 'Room L'], ['Level 1', 'Level 2']),
]

# Define the population size and number of generations
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.1

# Define the fitness function
def calculate_fitness(schedule):
    conflicts = 0
    for i, course1 in enumerate(schedule):
        for course2 in schedule[i+1:]:
            if (course1[1] == course2[1] and course1[2] == course2[2]) or (course1[3] == course2[3] and course1[2] == course2[2]) or (course1[3] == course2[3] and course1[1] == course2[1]):
                if course1[4] == course2[4]:
                    conflicts += 1
    return 1 / (conflicts + 1)

# Define the initial population
def create_schedule():
    schedule = []
    for course in courses:
        day = random.choice(course[1])
        time = random.choice(course[2])
        room = random.choice(course[3])
        level = random.choice(course[4])
        schedule.append((course[0], day, time, room, level))
    return schedule

population = [create_schedule() for _ in range(POPULATION_SIZE)]

# Define the selection function
def selection(population):
    return random.choices(population, k=2, weights=[calculate_fitness(schedule) for schedule in population])

# Define the crossover function
def crossover(schedule1, schedule2):
    schedule = []
    for i, course1 in enumerate(schedule1):
        course2 = schedule2[i]
        if random.random() > 0.5:
            course = course1
        else:
            course = course2
        schedule.append(course)
    return schedule

# Define the mutation function
def mutation(schedule):
    index = random.randint(0, len(schedule)-1)
    course = courses[index]
    day = random.choice(course[1])
    time = random.choice(course[2])
    room = random.choice(course[3])
    level = random.choice(course[4])
    schedule[index] = (course[0], day, time, room, level)
    return schedule

# Define the evolution function
def evolve(population):
    for i in range(NUM_GENERATIONS):
        print("Generation", i+1)
        new_population = []
        for j in range(int(POPULATION_SIZE/2)):
            schedule1 = selection(population)
            schedule2 = selection(population)
            schedule = crossover(schedule1, schedule2)
            if random.random() < MUTATION_RATE:
                schedule = mutation(schedule)
            new_population.append(schedule)
            schedule = crossover(schedule2, schedule1)
            if random.random() < MUTATION_RATE:
                schedule = mutation(schedule)
            new_population.append(schedule)
        population = new_population
        population.sort(key=lambda x: calculate_fitness(x), reverse=True)
        print("Best schedule:", population[0])
        print("Fitness:", calculate_fitness(population[0]))
        print("---------------------")
    return population[0]
    
