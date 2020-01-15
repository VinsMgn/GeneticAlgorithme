from random import random
from string import ascii_letters

choice = lambda x: x[int(random() * len(x))]


target = "Gabi est petit."
mutationChance = 0.1
bestIndivPercent = 0.2
nonbestIndivPercent = 0.05
nbOfIndiv = 500

maxGeneration = 100000
GRADED_INDIVIDUAL_RETAIN_COUNT = int(nbOfIndiv * bestIndivPercent)

targetSize = len(target)

# Precompute targetSize // 2
halfTargetSize = targetSize // 2

# Charmap of all allowed characters (A-Z a-z, space and !)
caracAllowed = ascii_letters + ' !\'.'

# Maximum fitness value
fitnessMax = targetSize


def get_random_char():
    return choice(caracAllowed)


def get_random_individual():
    return [get_random_char() for _ in range(targetSize)]


def get_random_population():
    return [get_random_individual() for _ in range(nbOfIndiv)]


def get_individual_fitness(individual):
    fitness = 0
    for c, expected_c in zip(individual, target):
        if c == expected_c:
            fitness += 1
    return fitness


def average_population_grade(population):
    total = 0
    for individual in population:
        total += get_individual_fitness(individual)
    return total / nbOfIndiv


def grade_population(population):
    """ Grade the population. Return a list of tuple (individual, fitness) sorted from most graded to less graded. """
    graded_individual = []
    for individual in population:
        graded_individual.append((individual, get_individual_fitness(individual)))
    return sorted(graded_individual, key=lambda x: x[1], reverse=True)


def evolve_population(population):
    # Récupérer les individus triés par ordre croissant
    raw_graded_population = grade_population(population)
    average_grade = 0
    solution = []
    graded_population = []
    for individual, fitness in raw_graded_population:
        average_grade += fitness
        graded_population.append(individual)
        if fitness == fitnessMax:
            solution.append(individual)
    average_grade /= nbOfIndiv

    if solution:
        return population, average_grade, solution
    # Tri des meilleurs individus
    parents = graded_population[:GRADED_INDIVIDUAL_RETAIN_COUNT]
    for individual in graded_population[GRADED_INDIVIDUAL_RETAIN_COUNT:]:
        if random() < nonbestIndivPercent:
            parents.append(individual)

    # Mutation de quelques individus
    for individual in parents:
        if random() < mutationChance:
            place_to_modify = int(random() * targetSize)
            individual[place_to_modify] = get_random_char()

    # Création d'une nouvelle génération avec les parents
    parents_len = len(parents)
    desired_len = nbOfIndiv - parents_len
    children = []
    while len(children) < desired_len:
        father = choice(parents)
        mother = choice(parents)
        if True:
            child = father[:halfTargetSize] + mother[halfTargetSize:]
            children.append(child)
            print(''.join(child))

    parents.extend(children)
    return parents, average_grade, solution


def main():
    population = get_random_population()

    # Mutation de la population
    i = 0
    solution = None
    while not solution and i < maxGeneration:
        population, average_grade, solution = evolve_population(population)
        i += 1

    average_grade = average_population_grade(population)
    print('Fitness finale : %.2f' % average_grade, '/ %d' % fitnessMax)

    # Affichage de la solution
    if solution:
        print('Solution trouvée avec %d generations.' % i, ''.join(solution[0]))
    else:
        print('Pas de solution trouvée après %d generations.' % i)
        print('- Dernière population trouvée :')
        for number, individual in enumerate(population):
            print(number, '->', ''.join(individual))


if __name__ == '__main__':
    main()
