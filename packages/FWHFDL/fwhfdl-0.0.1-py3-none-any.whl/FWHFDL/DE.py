import copy
import numpy as np

from .check_bound import check_bound


class DE:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        self.beta_min = 0.2   # Lower Bound of Scaling Factor
        self.beta_max = 0.8   # Upper Bound of Scaling Factor
        self.pCR = 0.2        # Crossover Probability

    def run(self, whh, pop, newpop):
        for ide in range(whh.nPop):
            x = pop[ide].Position
            A = np.random.choice(whh.nPop, whh.nPop, replace=False)
            A = np.delete(A, np.where(A == ide))

            a = A[0]
            b = A[1]
            c = A[2]

            # Mutation
            # beta=unifrnd(beta_min,beta_max);
            beta = np.random.uniform(self.beta_min, self.beta_max, whh.VarSize)
            y = pop[a].Position + beta * (pop[b].Position - pop[c].Position)

            y = check_bound(y, whh.VarMin, whh.VarMax)

            # Crossover
            z = np.zeros(x.size)
            j0 = np.random.randint(x.size)
            for j in range(x.size):
                if j == j0 or np.random.rand() <= self.pCR:
                    z[j] = y[j]
                else:
                    z[j] = x[j]

            it = self.algnum
            newpop[it].Position = z
            newpop[it].Cost = whh.CostFunction(newpop[it].Position)

            if newpop[it].Cost < pop[ide].Cost:
                pop[ide] = copy.deepcopy(newpop[it])

                if pop[ide].Cost < whh.BestSol.Cost:
                    whh.BestSol.Position = pop[ide].Position.copy()
                    whh.BestSol.Cost = pop[ide].Cost
