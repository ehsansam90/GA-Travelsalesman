import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import operator

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        dis_x = abs(self.x - city.x)
        dis_y = abs(self.y - city.y)
        d = np.sqrt((dis_x**2)+(dis_y**2))
        return d

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"



class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0

    def route_distance(self):
        if self.distance ==0:
            path_distance = 0
            for i in range(0,len(self.route)):
                city_1 = self.route[i]
                city_2 = None
                if i +1 < len(self.route):
                    city_2 = self.route[i+1]
                else:
                    city_2 = self.route[0]
                path_distance +=city_1.distance(city_2)
            self.distance = path_distance
        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance() + 1) # +1 for possible same cities
        return self.fitness


def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route

def initial_population(pop_size, city_list): #pop_size is a sample population should be less than len(city_list)!
    population = []
    for i in range(0, pop_size):
        population.append(create_route(city_list))
    return population

def rank_routes(population): #determination of fitness function
    fitness_results = {}
    for i in range(0,len(population)):
        fitness_results[i] = Fitness(population[i]).route_fitness()
    return sorted(fitness_results.items(), key = operator.itemgetter(1), reverse = True)


def selection(pop_ranked, elite_size): #Seelction parents based on weighted probability on fitness ranked
    selection_results = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, elite_size):
        selection_results.append(pop_ranked[i][0])
    for i in range(0, len(pop_ranked) - elite_size):
        pick = 100 * random.random()
        for i in range(0, len(pop_ranked)):
            if pick <= df.iat[i, 3]:
                selection_results.append(pop_ranked[i][0])
                break
    return selection_results

def mating(population, selection_results):
    matingpool = []
    for i in range(0, len(selection_results)):
        index = selection_results[i]
        matingpool.append(population[index])
    # print(matingpool)
    return matingpool


def cross_over(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []

    gene_1 = int(random.random() * len(parent1))
    gene_2 = int(random.random() * len(parent1))

    start_gene = min(gene_1, gene_2)
    end_gene = max(gene_1, gene_2)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    child = child_p1 + child_p2
    return child


def breed_pop(matingpool, elite_size):
    children = []
    length = len(matingpool) - elite_size
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, elite_size):
        children.append(matingpool[i])

    for i in range(0, length):
        child = cross_over(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


def mutatation(individual, mutation_rate):
    for swapped in range(len(individual)):
        if (random.random() < mutation_rate):
            swap_value = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swap_value]

            individual[swapped] = city2
            individual[swap_value] = city1
    return individual


def mutate_pop(population, mutation_rate):
    mutated_pop = []

    for ind in range(0, len(population)):
        mutated_Ind = mutatation(population[ind], mutation_rate)
        mutated_pop.append(mutated_Ind)
    return mutated_pop

def next_generation(current_generation, elite_size, mutation_rate):
    pop_ranked = rank_routes(current_generation)
    selection_results = selection(pop_ranked, elite_size)
    matingpool = mating(current_generation, selection_results)
    children = breed_pop(matingpool, elite_size)
    next_generation = mutate_pop(children, mutation_rate)
    return next_generation


def ga(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)
    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))

    for i in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate)

    print("Final distance: " + str(1 / rank_routes(pop)[0][1]))
    best_routeIndex = rank_routes(pop)[0][0]
    best_route = pop[best_routeIndex]
    return best_route

cityList = []

for i in range(0,10):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))


def gaPlot(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)
    progress = []
    progress.append(1 / rank_routes(pop)[0][1])
    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))

    for i in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate)
        progress.append(1 / rank_routes(pop)[0][1])

    print("Final distance: " + str(1 / rank_routes(pop)[0][1]))
    final_order = pop[rank_routes(pop)[0][0]]
    print(population)
    print(final_order)

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()
    x = []
    y = []



    for i in range(len(final_order)):
        x.append(final_order[i].x)
        y.append(final_order[i].y)

    for i in range(0, len(x)):
        plt.plot(x[i:i + 2], y[i:i + 2], 'ro-')

    plt.show()

# gaPlot(population=cityList, popSize=100, elite_size=20, mutationRate=0.01, generations=500)
# ga(population=cityList, popSize=10, elite_size=20, mutationRate=0.01, generations=500)
