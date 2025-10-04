import numpy as np


class Individual:
    def __init__(self, nVar):
        self.Position = np.zeros(nVar)
        self.Cost = np.inf
        self.Velocity = np.zeros(nVar)
        self.Best_Position = np.zeros(nVar)
        self.Best_Cost = np.inf


class Problem:
    def __init__(self, n_var=0, var_min=0, var_max=0,
                 max_it=0, n_pop=0, cost_function=None,
                 threshold=0.9):
        # Number of Decision Variables
        self.nVar = n_var
        # Decision Variables Matrix Size
        self.VarSize = n_var
        # Decision Variables Lower Bound
        self.VarMin = var_min
        # Decision Variables Upper Bound
        self.VarMax = var_max
        self.MaxIt = max_it
        self.nPop = n_pop
        self.CostFunction = cost_function
        self.BestSol = Individual(n_var)
        self.GlobalBest = Individual(n_var)
        self.BestCostMaxiter = np.zeros(max_it)
        self.BestCost = np.zeros(max_it)
        self.WorstCost = 0
        self.threshold = threshold
