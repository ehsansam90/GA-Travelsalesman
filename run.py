from Classes import gaPlot, City, ga
import random

cityList = []

for i in range(0,20):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

gaPlot(population=cityList, pop_size=30, elite_size=5, mutation_rate=0.01, generations=1000)

# ga(population=cityList, pop_size=10, elite_size=5, mutation_rate=0.01, generations=10)