import random
import math
import plotly.graph_objs as go
import plotly.offline as py


class Individual:
    bits = []

    def __init__(self, bits, function):
        self.bits = bits
        self.x = binary_base10(bits, 0, 1)
        self.y = function(self.x)

    def __str__(self):
        return f"{self.bits}, (x = {self.x}, y = {self.y})"



def main():
    n = 22
    p = 16
    xMin = 0
    xMax = 1
    cp = .7
    mp = .3
    num_generations = 1000

    g = lambda x: round(pow(2, -2 * pow(((x - 0.1) / 0.9), 2)) * pow((math.sin(5 * math.pi * x)), 6), 5)

    # Initialize the population
    population = create_population(p, n, g)

    # Print initial population
    print("Initial Population:")
    printPopulation(population)



    # Lists to store best fitness of each generation
    best_fitness_per_generation = []

    # Evolution loop
    for generation in range(num_generations):
        print("\nGeneration:", generation + 1)

        # Selection
        selected_individuals = selection(population)

        # Reproduction
        population = reproduction(selected_individuals, cp, mp, n, g)

        # Sort the population based on fitness
        population = sorted(population, key=lambda x: x.y)

        # Store the best fitness of the current generation
        best_fitness_per_generation.append(population[0].y)

        # Print the fittest individual in the current generation
        print("Fittest Individual:", population[0])

    # Print final population
    print("\nFinal Population:")
    printPopulation(population)

    # Plot the best fitness per generation
    plot_fitness(num_generations, best_fitness_per_generation)

def plot_fitness(num_generations, best_fitness_per_generation):
    generations = list(range(1, num_generations + 1))

    trace = go.Scatter(
        x=generations,
        y=best_fitness_per_generation,
        mode='lines+markers',
        name='Best Fitness',
        marker=dict(
            color='blue',
            size=8
        )
    )

    layout = go.Layout(
        title='Best Fitness per Generation',
        xaxis=dict(title='Generation'),
        yaxis=dict(title='Best Fitness'),
        hovermode='closest'
    )

    fig = go.Figure(data=[trace], layout=layout)
    py.plot(fig, filename='best_fitness.html')



    # population = sorted(population, key=lambda x: x.y)


def binary_base10(bits, xMin, xMax):
    soma = 0
    for i in range(len(bits) - 1, 0, -1):
        soma += bits[i] * 2 ** i

    x_value = xMin + (soma * ((xMax-xMin) / float((pow(2, len(bits))) - 1)))

    return x_value

def initializing_bits(n):
    individual = []

    for i in range(n):
        individual.append(random.randint(0,1))

    return individual

def create_population(p, n ,g):
    population = []
    for i in range(p):
        population.append(Individual(initializing_bits(n), g))

    return population

def printPopulation(population):
    for i in population:
        print(i)

def selection(population):
    roulette = []

    # I will have to return an y value for every individual x, and make a list out of it
    # sort the list
    sorted_population = sorted(population, key=lambda x: x.y)

    for index in range(len(sorted_population)):
        roulette.extend([sorted_population[index]] * (index + 1))

    survivors = []
    for i in range(int(len(sorted_population) / 2)):
        z = random.choice(roulette)# appending the random chosen index to surviers
        survivors.append(z)
        roulette = filter(z.__ne__, roulette)
        roulette = list(roulette)

    return survivors



def reproduction(population, cp, mp, n, g):
    children = []
    for index in range(0, len(population), 2):
        result1 = []
        result2 = []

        crossing_number = int(n/2)

        if random.random() < cp:
            for i in range(0, crossing_number):  # ranges from 0 to the crossing number doing swaps
                result1.append(population[index].bits[i])
                result2.append(population[index + 1].bits[i])

            for j in range(crossing_number, len(population[0].bits)):
                result1.append(population[index + 1].bits[j])
                result2.append(population[index].bits[j])

        else:
            result1 = population[index].bits
            result2 = population[index + 1].bits

        children.append(Individual(result1, g))
        children.append(Individual(result2, g))

    # ------------ Cross-over ---------------
    for child in children:
        child.bits = mutate_one(child.bits, mp)
        population.append(Individual(child.bits, g))

    return population


def mutate_multiple(bits, mp):
    for j in range(len(bits)):
        if random.random() < mp:
            bits[j] = 1 - bits[j]

    return bits

def mutate_one(bits, mp):
    if random.random() < mp:
        selected_gen = random.randint(0, len(bits)-1)
        bits[selected_gen] = 1 - bits[selected_gen]

    return bits


main()