import random
import time

cities = [(23,45),(12,45),(14,17),(29,22),(34,56)]
order = [i for i in range(len(cities))]
population = []

def shuffleACopy(x):
    b = x[:]  # make a copy of the keys
    random.shuffle(b)  # shuffle the copy
    return b  # return the copy

def create_population(list,num):
    pop = [shuffleACopy(list) for x in range(num * 10)]
    for member in pop:
        if member not in population and len(population) <= num:
            population.append(member)
    return population

new_pop = create_population(order,500)
print(len(new_pop))








# print(create_population(order,24))

