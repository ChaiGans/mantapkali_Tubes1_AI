import random
import matplotlib.pyplot as plt
from base_solver import CubeSolver
from datetime import datetime

class HillClimbingSolver(CubeSolver):
    def __init__(self, state=None):
        super().__init__(state)

    def generate_neighbors(self, state):
        neighbors = []
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                neighbor = state.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def steepest_ascent_hill_climbing(self, title = "Figure 1"):
        current_state = self.generate_random_initial_state()
        initial_state = current_state.copy() 
        current_value = self.calculate_objective(current_state)
        iteration = 0
        iterations = []
        objective_values = []
        start_time = datetime.now()

        plt.ion()
        fig = plt.figure(figsize=(10, 8))
        fig.canvas.manager.set_window_title(title)

        gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[1, 2])

        ax1 = fig.add_subplot(gs[0])
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Objective Value')
        ax1.set_title('Steepest Ascent Hill Climbing Objective Value over Iterations')

        gs2 = gs[1].subgridspec(1, 5)
        cube_axes = [fig.add_subplot(gs2[0, i]) for i in range(5)]

        self.visualize_state(current_state,axes=cube_axes)
        plt.pause(0.1)

        while True:
            iteration += 1
            iterations.append(iteration)
            objective_values.append(current_value)
            print("Iteration",iteration)
            ax1.clear()
            ax1.plot(iterations, objective_values, color='blue')
            ax1.set_xlabel('Iteration')
            ax1.set_ylabel('Objective Value')
            ax1.set_title('Steepest Ascent Hill Climbing Objective Value over Iterations')

            for ax in cube_axes:
                ax.clear()
            self.visualize_state(current_state, axes=cube_axes)

            plt.pause(0.1)

            neighbors = self.generate_neighbors(current_state)
            best_neighbor = None
            best_value = current_value

            for neighbor in neighbors:
                neighbor_value = self.calculate_objective(neighbor)
                if neighbor_value > best_value:
                    best_value = neighbor_value
                    best_neighbor = neighbor

            if best_value <= current_value:
                plt.ioff()
                fig2 = plt.figure(figsize=(12, 6))
                fig2.suptitle('Initial and Final States')

                gs_init_final = fig2.add_gridspec(2, 5)

                axes_initial = [fig2.add_subplot(gs_init_final[0, i]) for i in range(5)]
                axes_final = [fig2.add_subplot(gs_init_final[1, i]) for i in range(5)]

                self.visualize_state(initial_state, axes=axes_initial)
                self.visualize_state(current_state, axes=axes_final)

                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds() * 1000

                fig2.text(0.5, 0.05, f'Final Objective Value: {best_value} | Duration: {duration} ms | Iteration: {iteration}', ha='center', fontsize=10)

                for ax in axes_initial:
                    ax.set_title('Initial State', fontsize=8)
                for ax in axes_final:
                    ax.set_title('Final State', fontsize=8)

                plt.show()
                return current_state, iteration

            current_state = best_neighbor
            current_value = best_value

    def sideways_move_hill_climbing(self, title = "Sideways Move Hill Climbing", max_sideways_move = 20):
        current_state = self.generate_random_initial_state()
        current_value = self.calculate_objective(current_state)
        initial_state = current_state.copy() 
        iteration = 0
        iterations = []
        objective_values = []
        sideways_count = 0

        start_time = datetime.now()

        plt.ion()
        fig = plt.figure(figsize=(10, 8))
        fig.canvas.manager.set_window_title(title)

        gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[1, 2])

        ax1 = fig.add_subplot(gs[0])
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Objective Value')
        ax1.set_title('Sideways Move Hill Climbing Objective Value over Iterations')

        gs2 = gs[1].subgridspec(1, 5)
        cube_axes = [fig.add_subplot(gs2[0, i]) for i in range(5)]

        self.visualize_state(current_state,axes=cube_axes)
        plt.pause(0.1)

        while True:
            iteration += 1
            iterations.append(iteration)
            objective_values.append(current_value)

            ax1.clear()
            ax1.plot(iterations, objective_values, color='blue')
            ax1.set_xlabel('Iteration')
            ax1.set_ylabel('Objective Value')
            ax1.set_title('Sideways Move Hill Climbing Objective Value over Iterations')

            for ax in cube_axes:
                ax.clear()
            self.visualize_state(current_state, axes=cube_axes)

            plt.pause(0.1)

            neighbors = self.generate_neighbors(current_state)
            best_neighbor = None
            best_value = float('-inf')

            for neighbor in neighbors:
                neighbor_value = self.calculate_objective(neighbor)
                if neighbor_value > best_value:
                    best_value = neighbor_value
                    best_neighbor = neighbor
            
            if sideways_count >= max_sideways_move or best_value < current_value:
                plt.ioff()
                fig2 = plt.figure(figsize=(12, 6))
                fig2.suptitle('Initial and Final States')

                gs_init_final = fig2.add_gridspec(2, 5)

                axes_initial = [fig2.add_subplot(gs_init_final[0, i]) for i in range(5)]
                axes_final = [fig2.add_subplot(gs_init_final[1, i]) for i in range(5)]

                self.visualize_state(initial_state, axes=axes_initial)
                self.visualize_state(current_state, axes=axes_final)

                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds() * 1000

                fig2.text(0.5, 0.05, f'Final Objective Value: {best_value} | Duration: {duration} ms | Iteration: {iteration}', ha='center', fontsize=10)

                for ax in axes_initial:
                    ax.set_title('Initial State', fontsize=8)
                for ax in axes_final:
                    ax.set_title('Final State', fontsize=8)

                plt.show()
                return current_state, iteration
            
            if best_value == current_value:
                sideways_count += 1
            else:
                sideways_count = 0

            current_state = best_neighbor
            current_value = best_value

    def random_restart_hill_climbing(self, max_restart):
        all_state = []
        for i in range(max_restart):
            title = f"Restart {i + 1}"
            final_state , iteration = self.steepest_ascent_hill_climbing(title)
            print("Num of iteration for restart ", i+1 , ": " , iteration)
            all_state.append([final_state,iteration])

        temp = float("-inf")
        selected_index = -1
        for k in range(len(all_state)):
            value = self.calculate_objective(all_state[k][0])

            if value > temp:
                temp = value
                selected_index = k
        
        return all_state[selected_index][0], all_state[selected_index][1]
    
    def stochastic_hill_climbing(self, max_iteration = 100): 
        current_state = self.generate_random_initial_state()
        initial_state = current_state.copy()
        current_value = self.calculate_objective(current_state)
        iteration = 1
        iterations = []
        objective_values = []
        
        start_time = datetime.now()

        plt.ion() 
        fig= plt.figure(figsize=(10, 8))
        gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[1, 2])

        ax1 = fig.add_subplot(gs[0])
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Objective Value')
        ax1.set_title('Stochastic Hill Climbing Objective Value over Iterations')

        gs2 = gs[1].subgridspec(1, 5)
        cube_axes = [fig.add_subplot(gs2[0, i]) for i in range(5)]

        self.visualize_state(current_state,axes=cube_axes)
        plt.pause(0.1)

        while iteration < max_iteration:
            iterations.append(iteration)
            objective_values.append(current_value)
             
            ax1.plot(iterations, objective_values, color='blue')

            for ax in cube_axes:
                ax.clear()
            self.visualize_state(current_state, axes=cube_axes)
            plt.pause(0.1)
            
            neighbors= self.generate_neighbors(current_state)
            random_neighbor = random.choice(neighbors)

            neighbor_value = self.calculate_objective(random_neighbor)
            if neighbor_value > current_value:
                current_state = random_neighbor
                current_value = neighbor_value
            iteration += 1
        plt.ioff()
        fig2 = plt.figure(figsize=(12, 6))
        fig2.suptitle('Initial and Final States')

        gs_init_final = fig2.add_gridspec(2, 5)

        axes_initial = [fig2.add_subplot(gs_init_final[0, i]) for i in range(5)]
        axes_final = [fig2.add_subplot(gs_init_final[1, i]) for i in range(5)]

        self.visualize_state(initial_state, axes=axes_initial)
        self.visualize_state(current_state, axes=axes_final)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds() * 1000

        fig2.text(0.5, 0.05, f'Final Objective Value: {current_value} | Duration: {duration} ms | Iteration: {iteration}', ha='center', fontsize=10)

        for ax in axes_initial:
            ax.set_title('Initial State', fontsize=8)
        for ax in axes_final:
            ax.set_title('Final State', fontsize=8)

        plt.show()
        return current_state, iteration