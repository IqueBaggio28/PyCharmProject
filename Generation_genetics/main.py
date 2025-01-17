import random
import plotly.express as px


def main():

    p = 8
    n = 12
    target = [0, 1, 0] * int(n/3)
    pc = .5
    mp = .01

    population = initialize_population(n,p)

    best_fitness = []
    fitness_sums = []
    loop = True
    generation = 0
    while loop:
        print("Generation: ", generation)
        print_population(population)

        population = select_from_population(population, target)
        population = reproduction(population,pc, mp)

        generation_fitness = [find_fitness(individual, target) for individual in population]
        best_fitness.append(max(generation_fitness))

        # Calculate and store the sum of fitness values for the current generation
        fitness_sums.append(sum(generation_fitness))


        for individual in population:
            if find_fitness(individual, target) >= len(target):
                loop = False
                print_population(population)
                print("Successful individual", population.index(individual), " :", individual)
                break
        generation += 1

    plot_fitness_sums(best_fitness, fitness_sums)







def initialize_population(n, p):
    parentPopulation = [[0] * n for _ in range(p)]

    for i in range(p):
        for j in range(n):
            num = random.randint(0, 1)
            parentPopulation[i][j] = num

    return parentPopulation

def print_population(population):
    for i in population:
        print(i)



def find_fitness(population, target):
    count = 0
    for j in range(len(population)):
        if population[j] == target[j]:
            count += 1

    return count

def select_from_population(population, target):
    roulette = []
    fitness = []
    for ind in population:
        fitness.append(find_fitness(ind, target))

    print("fitness of population: ", fitness)
    for ind_index in range(len(fitness)):  # creates a roulette with the quantity of fitness number for each index
        for x in range(fitness[ind_index]):
            roulette.append(ind_index)

    survivers = []
    for i in range(int(len(population)/2)):  # appending the random chosen index to surviers
        survivers.append(random.choice(roulette))
        roulette = list(filter((survivers[i]).__ne__, roulette))
    print("index of survivers: ", survivers)

    empty = []
    for index in survivers:  # converts surviver index to the individuals from population
        empty.append(population[index])

    return empty


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

    print_population(population)
    return population



    # ------------ mutation ---------------


def mutate_multiple(child, mp):
    for j in range(len(child)):

        if random.random() < mp:
            child[j] = 1 - child[j]
        else:
            continue

    return child

def mutate_one(child, mp):
    if random.random() < mp:
        selected_gen = random.randint(0, len(child)-1)
        child[selected_gen] = 1 - child[selected_gen]

    return child


# def plot_fitness_best(best_fitness):
#     fig = px.line(x=range(len(best_fitness)), y=best_fitness, title='Sum of Fitness Values Over Generations')
#     fig.update_layout(xaxis_title='Generation', yaxis_title='Sum of Fitness Values')
#     fig.show()

def plot_fitness_sums(best_fitness, fitness_sums):
    fig = px.line(x=range(len(best_fitness)), y=best_fitness, title='Sum of Fitness Values Over Generations')
    fig.add_scatter(x=list(range(len(fitness_sums))), y=fitness_sums, mode='lines', name='Sum of Fitness')
    fig.update_layout(xaxis_title='Generation', yaxis_title='Sum of Fitness Values')
    fig.show()



main()
