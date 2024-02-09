import random
import math

def simulated_annealing(cost_func, initial_solution, temp, temp_min, alpha, max_iter):
    """
    Simulated Annealing algorithm for optimization problems.
    
    Args:
        cost_func (function): Cost function to minimize.
        initial_solution : Initial solution for the optimization problem.
        temp (float): Initial temperature.
        temp_min (float): Minimum temperature.
        alpha (float): Cooling rate.
        max_iter (int): Maximum number of iterations.
        
    Returns:
        best_solution : Best solution found by the algorithm.
        best_cost : Cost of the best solution found.
    """
    current_solution = initial_solution
    best_solution = current_solution
    current_cost = cost_func(current_solution)
    best_cost = current_cost
    
    while temp > temp_min:
        for _ in range(max_iter):
            new_solution = generate_neighbor(current_solution)
            new_cost = cost_func(new_solution)
            
            delta_cost = new_cost - current_cost
            if delta_cost < 0 or random.random() < math.exp(-delta_cost / temp):
                current_solution = new_solution
                current_cost = new_cost
                
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
        
        temp *= alpha
    
    return best_solution, best_cost

def generate_neighbor(solution):
    """
    Generates a neighboring solution by randomly modifying the given solution.
    For demonstration purposes, this function simply swaps two elements of the solution.
    """
    neighbor = solution.copy()
    idx1, idx2 = random.sample(range(len(solution)), 2)
    neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]
    return neighbor

# Example usage:
if __name__ == '__main__':
    # Define a simple cost function (e.g., total distance)
    def cost_function(solution):
        # Example: total distance in a TSP problem
        return sum(abs(solution[i] - solution[i+1]) for i in range(len(solution) - 1))

    # Define parameters
    initial_solution = [1, 2, 3, 4, 5]  # Initial solution
    temp = 100.0  # Initial temperature
    temp_min = 0.1  # Minimum temperature
    alpha = 0.99  # Cooling rate
    max_iter = 100  # Maximum number of iterations

    # Run simulated annealing
    best_solution, best_cost = simulated_annealing(cost_function, initial_solution, temp, temp_min, alpha, max_iter)
    print("Best Solution:", best_solution)
    print("Best Cost:", best_cost)
