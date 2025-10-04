import copy
import numpy as np

from .check_bound import check_bound


class FireFly:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        self.ffGamma = 1            # Light Absorption Coefficient
        self.beta0 = 2            # Attraction Coefficient Base Value
        self.ffAlpha = 0.2          # Mutation Coefficient
        self.alpha_damp = 0.98    # Mutation Coefficient Damping Ratio
        # Uniform Mutation Range
        self.delta = 0.05 * (whh.VarMax - whh.VarMin)
        self.m = 2
        if np.isscalar(whh.VarMin) and np.isscalar(whh.VarMax):
            self.dmax = (whh.VarMax - whh.VarMin) * np.sqrt(whh.nVar)
        else:
            self.dmax = np.linalg.norm(whh.VarMax - whh.VarMin)

    def run(self, whh, pop, newpop):
        temppop = copy.deepcopy(newpop)
        for i in range(whh.nPop):
            temppop[i].Cost = np.inf
            for j in range(whh.nPop):
                if pop[j].Cost < pop[i].Cost:
                    rij = np.linalg.norm(
                        pop[i].Position - pop[j].Position) / self.dmax
                    beta = self.beta0 * np.exp(-self.ffGamma * rij ** self.m)
                    e = self.delta * np.random.uniform(-1, +1, whh.VarSize)
                    # e=delta*randn(VarSize);

                    newpop[i].Position = pop[i].Position + beta * np.random.rand(
                        whh.VarSize) * (pop[j].Position - pop[i].Position) + self.ffAlpha * e

                    newpop[i].Position = check_bound(
                        newpop[i].Position, whh.VarMin, whh.VarMax)

                    newpop[i].Cost = whh.CostFunction(newpop[i].Position)

                    if newpop[i].Cost <= temppop[i].Cost:
                        temppop[i] = copy.deepcopy(newpop[i])
                        if temppop[i].Cost <= whh.BestSol.Cost:
                            whh.BestSol.Position = temppop[i].Position.copy()
                            whh.BestSol.Cost = temppop[i].Cost

        # Merge
        pop = np.append(pop, temppop)  # ok

        # Sort
        pop = np.array(sorted(pop, key=lambda a: a.Cost))

        # Truncate
        pop = pop[1: whh.nPop]

        self.ffAlpha = self.ffAlpha * self.alpha_damp
