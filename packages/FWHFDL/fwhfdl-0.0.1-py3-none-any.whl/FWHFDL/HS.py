import numpy as np

from .problem_types import Individual
from .check_bound import check_bound


class HS:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        self.HMS = whh.nPop         # Harmony Memory Size
        self.nNew = 20        # Number of New Harmonies
        self.HMCR = 0.9       # Harmony Memory Consideration Rate
        self.PAR = 0.1        # Pitch Adjustment Rate
        self.FW = 0.02 * (whh.VarMax - whh.VarMin)    # Fret Width (Bandwidth)
        self.FW_damp = 0.995              # Fret Width Damp Ratio

    def run(self, whh, pop, newpop):
        # Initialize Array for New Harmonies
        NEW = np.array([Individual(whh.nVar) for i in range(self.nNew)])

        # Create New Harmonies
        for k in range(self.nNew):
            # Create New Harmony Position
            NEW[k].Position = np.random.uniform(
                whh.VarMin, whh.VarMax, whh.VarSize)
            for j in range(whh.nVar):
                if np.random.rand() <= self.HMCR:
                    # Use Harmony Memory
                    i = np.random.randint(0, self.HMS)
                    NEW[k].Position[j] = pop[i].Position[j]

              # Pitch Adjustment
                if np.random.rand() <= self.PAR:
                    # DELTA=FW*unifrnd(-1,+1);    # Uniform
                    DELTA = self.FW * np.random.randn()            # Gaussian (Normal)
                    NEW[k].Position[j] = NEW[k].Position[j] + DELTA

            # Apply Variable Limits
            NEW[k].Position = check_bound(
                NEW[k].Position, whh.VarMin, whh.VarMax)

            # Evaluation
            NEW[k].Cost = whh.CostFunction(NEW[k].Position)

        # Merge Harmony Memory and New Harmonies
        pop = np.append(pop, NEW)

        # Sort Harmony Memory
        pop = np.array(sorted(pop, key=lambda a: a.Cost))

        # Truncate Extra Harmonies
        pop = pop[1:self.HMS]

        self.FW = self.FW * self.FW_damp

        # Update Best Solution Ever Found
        if pop[0].Cost < whh.BestSol.Cost:
            whh.BestSol.Position = pop[0].Position.copy()
            whh.BestSol.Cost = pop[0].Cost
