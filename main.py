from hill_climbing import HillClimbingSolver
from simulated_annealing import SimulatedAnnealingSolver
from genetic_algorithm import GeneticAlgorithmSolver

def get_solver_choice():
    print("Choose an algorithm to solve the cube:")
    print("1: Hill Climbing")
    print("2: Simulated Annealing")
    print("3: Genetic Algorithm")
    choice = int(input("Enter the number of your choice: "))
    return choice

if __name__ == "__main__":
    choice = get_solver_choice()

    if choice == 1:
        print("Choose an Hill Climbibg algorithm to solve the cube:")
        print("1: Stepest Ascent Hill Climbing")
        print("2: Sideways Move Hill Climbing")
        print("3: Random Restart Hill Climbing")
        print("4: Stochastic Hill Climbing")

        hill_choice = int(input("Enter the number of your choice: "))
        solver = HillClimbingSolver()

        if(hill_choice == 1):
            solution,iteration  = solver.steepest_ascent_hill_climbing()
        elif(hill_choice == 2):
            solution, iteration = solver.sideways_move_hill_climbing()
        elif(hill_choice == 3):
            solution, iteration = solver.random_restart_hill_climbing(7)
        elif(hill_choice == 4):
            solution, iteration = solver.stochastic_hill_climbing(500)

        print("Final state:", solution)
        print("Iteration: ", iteration)
        print("Objective value:", solver.calculate_objective(solution))
    elif choice == 2:
        initial_state = SimulatedAnnealingSolver().generate_random_initial_state()
        solver = SimulatedAnnealingSolver(initial_state)
        solution = solver.simulated_annealing()
        print("Final state:", solution)
        print("Objective value:", solver.calculate_objective(solution))
    elif choice == 3:
        solver = GeneticAlgorithmSolver(50,100)
        solution = solver.run()
        print("Final state:", solution)
        print("Objective value:", solver.calculate_objective(solution))
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
 

