from Classes import gaPlot, City, ga
import random
import matplotlib.pyplot as plt

cityList = []

for i in range(0,50):
    cityList.append(City(x=int(random.random() * 1000), y=int(random.random() * 1000)))

gaPlot(population=cityList, pop_size=100, elite_size=20, mutation_rate=0.01, generations=100)

# ga(population=cityList, pop_size=10, elite_size=5, mutation_rate=0.01, generations=100)

# for number of cities on 15,20,25,30,35,40,45,50
# values = []
# pop_size = []
# for i in range(40,400 ,5):
#     values.append(gaPlot(population=cityList, pop_size=i, elite_size=20, mutation_rate=0.01, generations=50))
#     pop_size.append(i)
#
# print(values,pop_size)
# plt.plot(values, pop_size)
# plt.show()

