import numpy as np

from .check_bound import check_bound


class PSO:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        self.w = 1            # Inertia Weight
        self.wdamp = 0.99     # Inertia Weight Damping Ratio
        self.c1 = 1.5         # Personal Learning Coefficient
        self.c2 = 2.0         # Global Learning Coefficient
        self.VelMax = 0.1 * (whh.VarMax - whh.VarMin)
        self.VelMin = -self.VelMax

    def run(self, whh, pop, newpop):
        for i in range(whh.nPop):
            # Update Velocity
            pop[i].Velocity = self.w * pop[i].Velocity + \
                self.c1 * np.random.rand(whh.VarSize) * (pop[i].Best_Position - pop[i].Position) + \
                self.c2 * np.random.rand(whh.VarSize) * (whh.GlobalBest.Position - pop[i].Position)

            # Apply Velocity Limits
            pop[i].Velocity = check_bound(
                pop[i].Velocity, self.VelMin, self.VelMax)

            # Update Position
            pop[i].Position = pop[i].Position + pop[i].Velocity

            # Velocity Mirror Effect
            IsOutside = np.append(
                np.where(pop[i].Position < whh.VarMin),
                np.where(pop[i].Position > whh.VarMax))
            pop[i].Velocity[IsOutside] = -pop[i].Velocity[IsOutside]

            # Apply Position Limits
            pop[i].Position = check_bound(
                pop[i].Position, whh.VarMin, whh.VarMax)

            # Evaluation
            pop[i].Cost = whh.CostFunction(pop[i].Position)

            # Update Personal Best
            if pop[i].Cost < pop[i].Best_Cost:
                pop[i].Best_Position = pop[i].Position
                pop[i].Best_Cost = pop[i].Cost

                # Update Global Best
                if pop[i].Best_Cost < whh.GlobalBest.Cost:
                    whh.GlobalBest = pop[i]

        for i in range(whh.nPop):
            if pop[i].Cost < whh.BestSol.Cost:
                whh.BestSol.Position = pop[i].Position.copy()
                whh.BestSol.Cost = pop[i].Cost
        self.w = self.w * self.wdamp
