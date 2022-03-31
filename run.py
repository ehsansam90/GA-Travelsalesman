from Classes import geneticAlgorithmPlot, City
import random


cityList = []

for i in range(0,10):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

geneticAlgorithmPlot(population=cityList, popSize=50, eliteSize=20, mutationRate=0.01, generations=100)