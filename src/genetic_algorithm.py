import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from base_solver import CubeSolver

class GeneticAlgorithmSolver(CubeSolver):
    def __init__(self, population_size, num_iterations):
        super().__init__()
        self.population_size = population_size
        self.num_iterations = num_iterations
        self.population = self.generate_population(population_size)

    def generate_population(self, pop_size):
        return [self.generate_random_initial_state() for _ in range(pop_size)]

    def selection(self, population):
        fitness_values = [-self.calculate_objective(ind) for ind in population]
        total_fitness = sum(fitness_values)
        if total_fitness == 0:
            selection_probs = [1 / len(population)] * len(population)
        else:
            selection_probs = [fitness / total_fitness for fitness in fitness_values]
        chosen_index = random.choices(
            population=range(len(population)),
            weights=selection_probs,
            k=1
        )[0]
        return population[chosen_index]


    def crossover(self, parent1, parent2):
        size = len(parent1)
        cxpoint1 = random.randint(0, size - 2)
        cxpoint2 = random.randint(cxpoint1 + 1, size - 1)
        child1 = [None] * size
        child2 = [None] * size
        child1[cxpoint1:cxpoint2] = parent1[cxpoint1:cxpoint2]
        current_pos = cxpoint2 % size
        parent2_pos = cxpoint2 % size
        while None in child1:
            if parent2[parent2_pos % size] not in child1:
                child1[current_pos % size] = parent2[parent2_pos % size]
                current_pos += 1
            parent2_pos += 1
        child2[cxpoint1:cxpoint2] = parent2[cxpoint1:cxpoint2]
        current_pos = cxpoint2 % size
        parent1_pos = cxpoint2 % size
        while None in child2:
            if parent1[parent1_pos % size] not in child2:
                child2[current_pos % size] = parent1[parent1_pos % size]
                current_pos += 1
            parent1_pos += 1
        return child1, child2

            
    def mutate(self, individual, mutation_rate=0.5):
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                swap_index = random.randint(0, len(individual) - 1)
                individual[i], individual[swap_index] = individual[swap_index], individual[i]
        return individual

    def run(self):
        best_solution = None
        best_fitness = float('-inf')
        avg_fitness_per_iteration = []
        max_fitness_per_iteration = []
        fitness_values_per_iteration = []

        for state in self.population:
            initial_value = self.calculate_objective(state)
            if initial_value > best_fitness:
                best_fitness = initial_value
                best_initial_state = state

        start_time = datetime.now()

        plt.ion()  
        
        fig = plt.figure(figsize=(14, 12))
        gs = fig.add_gridspec(nrows=3, ncols=1, height_ratios=[1, 1, 2])

        ax1 = fig.add_subplot(gs[0])
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Objective Value')
        ax1.set_title('Genetic Algorithm Performance (Average and Max Fitness)')

        ax2 = fig.add_subplot(gs[1])
        fig.subplots_adjust(hspace=0.5)
        ax2.set_xlabel('Iteration')
        ax2.set_ylabel('Fitness Value')
        ax2.set_title('Fitness Value of Each Individual per Iteration')
        gs2 = gs[2].subgridspec(1, 5)
        cube_axes = [fig.add_subplot(gs2[0, i]) for i in range(5)]
        self.visualize_state(best_initial_state, axes=cube_axes)

        for iteration in range(self.num_iterations):
            fitness_values = [self.calculate_objective(ind) for ind in self.population]
            fitness_values_per_iteration.append(fitness_values)
            max_fitness = max(fitness_values)
            avg_fitness = sum(fitness_values) / len(fitness_values)

            avg_fitness_per_iteration.append(avg_fitness)
            max_fitness_per_iteration.append(max_fitness)
            
            if max_fitness > best_fitness:
                best_fitness = max_fitness
                best_solution = self.population[fitness_values.index(max_fitness)]
            ax1.clear()
            ax1.plot(range(len(avg_fitness_per_iteration)), avg_fitness_per_iteration, label='Average Fitness', color='blue')
            ax1.plot(range(len(max_fitness_per_iteration)), max_fitness_per_iteration, label='Max Fitness', color='green')
            ax1.set_xlabel('Iteration')
            ax1.set_ylabel('Fitness Value')
            ax1.set_title('Genetic Algorithm Performance')
            ax1.legend()
            ax2.clear()
            for i, fitness_vals in enumerate(fitness_values_per_iteration):
                ax2.scatter([i] * len(fitness_vals), fitness_vals, color='blue', alpha=0.3, s=10)
            ax2.set_xlabel('Iteration')
            ax2.set_ylabel('Fitness Value')
            ax2.set_title('Fitness Value of Each Individual per Iteration')
            # for ax in cube_axes:
            #     ax.clear()
            # self.visualize_state(best_solution, axes=cube_axes)
            plt.pause(0.1) 

            new_population = []
            while len(new_population) < self.population_size:
                parent1 = self.selection(self.population)
                parent2 = self.selection(self.population)
                child1, child2 = self.crossover(parent1, parent2)
                temp = self.mutate(child1)
                new_population.append(temp)
                if len(new_population) < self.population_size:
                    temp = self.mutate(child2)
                    new_population.append(temp)
            self.population = new_population
            print(f"Iteration {iteration + 1}/{self.num_iterations} - Best Fitness: {-best_fitness}")
            print("ukuran",self.population_size)
        plt.ioff()
        fig2 = plt.figure(figsize=(12, 6))
        fig2.suptitle('Initial and Final States')

        gs_init_final = fig2.add_gridspec(2, 5)

        axes_initial = [fig2.add_subplot(gs_init_final[0, i]) for i in range(5)]
        axes_final = [fig2.add_subplot(gs_init_final[1, i]) for i in range(5)]

        best_final_value = float('-inf')
        for state in self.population:
            final_value = self.calculate_objective(state)
            if final_value > best_final_value:
                best_final_value = final_value
                best_final_state = state
        self.visualize_state(best_initial_state, axes=axes_initial)
        self.visualize_state(best_final_state, axes=axes_final)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds() * 1000

        fig2.text(0.5, 0.05, f'Final Objective Value: {best_final_value} | Duration: {duration} ms | Population Size: {self.population_size} | Iteration: {self.num_iterations}', ha='center', fontsize=10)

        for ax in axes_initial:
            ax.set_title('Initial State', fontsize=8)
        for ax in axes_final:
            ax.set_title('Final State', fontsize=8)

        plt.show()

        return best_solution

