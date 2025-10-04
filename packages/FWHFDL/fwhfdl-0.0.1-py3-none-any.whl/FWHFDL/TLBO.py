import copy
import numpy as np

from .check_bound import check_bound
from .problem_types import Individual


class TLBO:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0

    def run(self, whh, pop, newpop):
        # Calculate Population Mean
        Mean = 0
        for i in range(whh.nPop):
            Mean = Mean + pop[i].Position
        Mean = Mean / whh.nPop

        # Select Teacher
        Teacher = pop[0]
        for i in range(1, whh.nPop):
            if pop[i].Cost < Teacher.Cost:
                Teacher = pop[i]

        # Teacher Phase
        for i in range(whh.nPop):
            # Create Empty Solution
            newsol = Individual(whh.nVar)

            # Teaching Factor
            TF = np.random.randint(1, 333)

            # Teaching (moving towards teacher)
            newsol.Position = pop[i].Position + \
                np.random.rand(whh.VarSize) * (Teacher.Position - TF * Mean)

            # Clipping
            newsol.Position = check_bound(
                newsol.Position, whh.VarMin, whh.VarMax)

            # Evaluation
            newsol.Cost = whh.CostFunction(newsol.Position)

            # Comparision
            if newsol.Cost < pop[i].Cost:
                pop[i] = copy.deepcopy(newsol)
                if pop[i].Cost < whh.BestSol.Cost:
                    whh.BestSol.Position = pop[i].Position.copy()
                    whh.BestSol.Cost = pop[i].Cost

        # Learner Phase
        for i in range(whh.nPop):

            A = np.array(range(whh.nPop))
            A = np.delete(A, i)
            j = A[np.random.randint(whh.nPop - 1)]

            Step = pop[i].Position - pop[j].Position
            if pop[j].Cost < pop[i].Cost:
                Step = -Step

            # Create Empty Solution
            newsol = Individual(whh.nVar)

            # Teaching (moving towards teacher)
            newsol.Position = pop[i].Position + \
                np.random.rand(whh.VarSize) * Step

            # Clipping
            newsol.Position = check_bound(
                newsol.Position, whh.VarMin, whh.VarMax)

            # Evaluation
            newsol.Cost = whh.CostFunction(newsol.Position)

            # Comparision
            if newsol.Cost < pop[i].Cost:
                pop[i] = copy.deepcopy(newsol)
                if pop[i].Cost < whh.BestSol.Cost:
                    whh.BestSol.Position = pop[i].Position.copy()
                    whh.BestSol.Cost = pop[i].Cost
