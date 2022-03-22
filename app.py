import random
import math

cities = [(1,2),(20,4),(5,6),(8,10)]
order = [i for i in range(len(cities))]
population = []

def shuffleACopy(x):
    b = x[:]  # make a copy of the keys
    random.shuffle(b)  # shuffle the copy
    return b  # return the copy
#this creat population from order
def create_population(list,num):
    pop = [shuffleACopy(list) for x in range(num * 10)]
    for member in pop:
        if member not in population and len(population) <= num:
            population.append(member)
    return population

#function for calculate the distence for population
def calculate_dist(cities, population):
    dist = 0
    for i in range(len(population)-1):
        x1 = cities[population[i]][0]
        x2 = cities[population[i + 1]][0]
        y1 = cities[population[i]][1]
        y2 = cities[population[i + 1]][1]

        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        dist +=dist
    return(dist)

new_pop = create_population(order,100)
# print(new_pop)
# print(len(new_pop))
# print(calculate_dist(cities, new_pop[0]))

def fitness_func(population):
    test = [(population[i], calculate_dist(cities, population[i])) for i in range(len(population))]
        # [{str(population[i]):calculate_dist(cities,population[i])} for i in range(len(population)]
    print(test)






fitness_func(new_pop)







# print(create_population(order,24))

