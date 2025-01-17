import math
import random

def main():
    n = 22
    p = 6
    cp = .5
    mp = .03
    xMin = 0
    xMax = 1

    population = initialize_population(n, p)
    population = reproduction(population, cp, mp)
    list_of_value = []
    for i in range(len(population)):
        x = (binary_base10(population[i], xMin, xMax))
        list_of_value.append(x)


    print_population(population, list_of_value)
    selection(list_of_value)


def selection(x_list):
    y_list = []
    roulette = []
    for i in x_list:
        y = 2 ** (-2 * ((i - 0.1) / 0.9) ** 2) * (math.sin(5 * math.pi * i)) ** 6
        y_list.append(y)

    # I will have to return an y value for every individual x, and make a list out of it
    # sort the list
    y_list.sort()

    for index in range(len(y_list)):
        roulette.extend([y_list[index]] * (index + 1))

    survivers = []
    for i in range(int(len(y_list) / 2)):  # appending the random chosen index to surviers
        survivers.append(random.choice(roulette))
        roulette = list(filter((survivers[i]).__ne__, roulette))
    print("index of survivers: ", survivers)

    # empty = []
    # for index in survivers:  # converts surviver index to the individuals from population
    #     empty.append(population[index])




    # for index in range(list)
        #select_list [i] = yList * i+1

    # return  2**(-2*((x-0.1)/0.9)**2)*(math.sin(5*math.pi*x))**6



def binary_base10(bits, xMin, xMax):
    soma = 0
    for i in range(len(bits) - 1):
        soma += bits[i] * 2 ** i

    x_value = xMin + (soma * ((xMax-xMin) / float((pow(2, len(bits))) - 1)))

    return x_value


# recycled from problem 1
def initialize_population(n, p):

    parentPopulation = [[0] * n for _ in range(p)]

    for i in range(p):
        for j in range(n):
            num = random.randint(0, 1)
            parentPopulation[i][j] = num

    return parentPopulation


def print_population(population, list):
    for i in range(len(population)):
        print(population[i], list[i])


def reproduction(population, cp, mp):

    children = []
    for index in range(0, len(population), 2):
        result1 = []
        result2 = []

        crossing_number = random.randint(1, len(population[0]) - 2)

        if random.random() > cp:
            for i in range(0, crossing_number):  # ranges from 0 to the crossing number doing swaps
                # print(i)
                result1.append(population[index][i])
                result2.append(population[index+1][i])

            for j in range(crossing_number, len(population[0])):
                result1.append(population[index+1][j])
                result2.append(population[index][j])

        else:
            result1 = population[index]
            result2 = population[index+1]

        children.append(result1)
        children.append(result2)

    # ------------ Cross-over ---------------
    for child in children:
        child = mutate_multiple(child,mp)
        population.append(child)

    return population


def mutate_multiple(child, mp):
    for j in range(len(child)):

        if random.random() < mp:
            child[j] = 1 - child[j]
        else:
            continue

    return child

main()