import numpy as np

from .check_bound import check_bound
from .problem_types import Individual


class IWO:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        self.Smin = 0       # Minimum Number of Seeds
        self.Smax = 5       # Maximum Number of Seeds
        self.Exponent = 2           # Variance Reduction Exponent
        self.sigma_initial = 0.5    # Initial Value of Standard Deviation
        self.sigma_final = 0.001  # Final Value of Standard Deviation

    def run(self, whh, pop, newpop):
        # Update Standard Deviation
        sigma = ((whh.MaxIt - self.algnum) / (whh.MaxIt - 1))**self.Exponent * \
            (self.sigma_initial - self.sigma_final) + self.sigma_final

        # Get Best and Worst Cost Values
        Costs = [i.Cost for i in pop]

        BestCost = np.min(Costs)
        WorstCost = np.max(Costs)

        # Initialize Offsprings Population
        newpop = np.array([])

        # Reproduction
        for i in range(len(pop)):
            if WorstCost == BestCost:
                ratio = 0
                S = 0
            else:
                ratio = (pop[i].Cost - WorstCost) / (BestCost - WorstCost)
                S = np.floor(self.Smin + (self.Smax - self.Smin) * ratio)

            for j in range(int(S)):
               # Initialize Offspring
                newsol = Individual(whh.nVar)

                # Generate Random Location
                newsol.Position = pop[i].Position + \
                    sigma * np.random.randn(whh.VarSize)

                # Apply Lower/Upper Bounds
                newsol.Position = check_bound(
                    newsol.Position, whh.VarMin, whh.VarMax)

                # Evaluate Offsring
                newsol.Cost = whh.CostFunction(newsol.Position)

                # Add Offpsring to the Population
                newpop = np.append(newpop, newsol)  # ok

        # Merge Populations
        pop = np.append(pop, newpop)

        # Sort Population
        pop = np.array(sorted(pop, key=lambda a: a.Cost))

        # Competitive Exclusion (Delete Extra Members)
        if pop.size > whh.nPop:
            pop = pop[: whh.nPop]

        if pop[0].Cost < whh.BestSol.Cost:
            whh.BestSol.Position = pop[0].Position.copy()
            whh.BestSol.Cost = pop[0].Cost
