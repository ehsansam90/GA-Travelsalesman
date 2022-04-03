from Classes import gaPlot, City
import random


cityList = []

for i in range(0,20):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

gaPlot(population=cityList, pop_size=100, elite_size=10, mutation_rate=0.01, generations=500)