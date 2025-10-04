import copy
import numpy as np

from .problem_types import Individual
from .check_bound import check_bound


class SA:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        self.MaxSubIt = 20    # Maximum Number of Sub-iterations
        self.T0 = 0.1       # Initial Temp.
        self.T = self.T0
        self.saAlpha = 0.99     # Temp. Reduction Rate
        self.nMove = 5        # Number of Neighbors per Individual
        self.saMu = 0.5       # Mutation Rate
        # Mutation Range (Standard Deviation)
        self.saSigma = 0.1 * (whh.VarMax - whh.VarMin)

    def run(self, whh, pop, newpop):
        for subit in range(self.MaxSubIt):

            # Create and Evaluate New Solutions
            newpop = []
            for i in range(whh.nPop):
                t = []
                for j in range(self.nMove):
                    t.append(Individual(whh.nVar))
                newpop.append(np.array(t))
            newpop = np.array(newpop)

            for i in range(whh.nPop):
                for j in range(self.nMove):

                    # Create Neighbor
                    newpop[i, j].Position = SaMutate(
                        pop[i].Position.copy(),
                        self.saMu, self.saSigma,
                        whh.VarMin, whh.VarMax)
                    newpop[i, j].Best_Position = newpop[i, j].Position

                    # Evaluation
                    newpop[i, j].Cost = whh.CostFunction(newpop[i, j].Position)

            # Sort Neighbors
            newpop = newpop.reshape(newpop.size)
            newpop = np.array(
                sorted(newpop, key=lambda a: a.Cost))

            for i in range(whh.nPop):
                if newpop[i].Cost <= pop[i].Cost:
                    pop[i] = copy.deepcopy(newpop[i])

                else:
                    DELTA = (newpop[i].Cost - pop[i].Cost) / pop[i].Cost
                    P = np.exp(-DELTA / self.T)
                    if np.random.rand() <= P:
                        pop[i] = copy.deepcopy(newpop[i])

                # Update Best Solution Ever Found
                if pop[i].Cost <= whh.BestSol.Cost:
                    whh.BestSol.Position = pop[i].Position.copy()
                    whh.BestSol.Cost = pop[i].Cost

       # Store Best Cost Ever Found
        self.T = self.saAlpha * self.T
        self.saSigma = 0.98 * self.saSigma


def SaMutate(x, mu, sigma, VarMin, VarMax):

    A = np.random.rand(x.size) <= mu
    J = np.where(A == 1)[0]

    y = x
    y[J] = x[J] + sigma * np.random.randn(J.size)

    # Clipping
    y = check_bound(y, VarMin, VarMax)

    return y
