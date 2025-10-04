import numpy as np

from .check_bound import check_bound


class BBO:
    def __init__(self, n):
        self.algnum = n

    def set_parameters(self, whh):
        self.rewards = 0
        # Keep Rate
        self.KeepRate = 0.4
        # Number of Kept Habitats
        self.nKeep = round(self.KeepRate * whh.nPop)
        # Number of New Habitats
        self.bbonNew = whh.nPop - self.nKeep
        # Emmigration Rates
        self.bboMu = np.linspace(1, 0, whh.nPop)
        # Immigration Rates
        self.llambda = 1 - self.bboMu
        # alpha value
        self.bboAlpha = 0.9
        # PMutation value
        self.pMutation = 0.1
        # sigma value
        self.bboSigma = 0.02 * (whh.VarMax - whh.VarMin)

    def run(self, whh, pop, newpop):
        for i in range(whh.nPop):
            for k in range(whh.nVar):
                # Migration
                if np.random.rand() <= self.llambda[i]:
                    # Emmigration Probabilities
                    EP = self.bboMu
                    EP[i] = 0
                    EP = EP / sum(EP)

                    # Select Source Habitat
                    j = RouletteWheelSelection(EP)

                    # Migration
                    newpop[i].Position[k] = pop[i].Position[k] + \
                        self.bboAlpha * (pop[j].Position[k] - pop[i].Position[k])

                # Mutation
                if np.random.rand() <= self.pMutation:
                    newpop[i].Position[k] = newpop[i].Position[k] + \
                        self.bboSigma * np.random.randn()

            # Apply Lower and Upper Bound Limits
            newpop[i].Position = check_bound(
                newpop[i].Position, whh.VarMin, whh.VarMax)

            # Evaluation
            newpop[i].Cost = whh.CostFunction(newpop[i].Position)

        # Sort New Population
        newpop = np.array(sorted(newpop, key=lambda a: a.Cost))

        # Select Next Iteration Population
        pop = np.append(pop[0:self.nKeep], newpop[0:self.bbonNew])

        # Sort Population
        pop = np.array(sorted(pop, key=lambda a: a.Cost))

        # Update Best Solution Ever Found
        if pop[0].Cost < whh.BestSol.Cost:
            whh.BestSol.Position = pop[0].Position.copy()
            whh.BestSol.Cost = pop[0].Cost


def RouletteWheelSelection(P):
    r = np.random.rand()
    C = np.cumsum(P)
    return np.nonzero(r <= C)[0][0]
