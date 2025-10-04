import copy
import numpy as np

from .BBO import BBO
from .DE import DE
from .FireFly import FireFly
from .HS import HS
from .PSO import PSO
from .SA import SA
from .IWO import IWO
from .TLBO import TLBO
from .problem_types import Problem, Individual
from .cost_function import cost_function


class FWHH:
    def __init__(self, RLAlpha=0.5,):

        self.algs_list = [
            SA,
            BBO,
            DE,
            FireFly,
            HS,
            PSO,
            TLBO,
            IWO,
        ]
        self.algs = []

        self.calls = {}
        self.first_run_flag = 0
        self.nAlg = len(self.algs_list)
        self.RLAlpha = RLAlpha
        self.BestCost = np.zeros(self.nAlg)
        self.WorstCost = 0
        self.lotCHList = np.array([])
        self.iterr = 0

        self.nVar = 0
        self.VarSize = 0
        self.VarMin = 0
        self.VarMax = 0
        self.MaxIt = 0
        self.nPop = 0

        self.BestSol = Individual(0)
        self.GlobalBest = None
        self.BestCostMaxiter = []
        self.problem = None
        self.pop = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.columns = None

    def data_set(self, X_train=None, y_train=None,
                 X_test=None, y_test=None):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.columns = X_train.columns.to_numpy()

    def problem_set(self, threshold=0.9, cost_function=cost_function):
        prb = Problem(
            n_var=len(self.columns),
            var_min=0, var_max=1,
            max_it=10, n_pop=10,
            cost_function=cost_function,
            threshold=threshold
        )
        self.GlobalBest = Individual(prb.nVar)
        self.nVar = prb.nVar
        self.VarSize = prb.VarSize
        self.VarMin = prb.VarMin
        self.VarMax = prb.VarMax
        self.MaxIt = prb.MaxIt
        self.nPop = prb.nPop
        self.problem = prb

    def algs_set(self):
        for i in range(len(self.algs_list)):
            a = self.algs_list[i](i)
            a.set_parameters(self.problem)
            self.algs.append(a)
            self.calls[self.algs[-1].__class__.__name__] = 0

    def CostFunction(self, x):
        return self.problem.CostFunction(
            x, self.X_train, self.y_train,
            self.X_test, self.y_test, self.problem.threshold
        )

    def pop_set(self):
        pop = np.array([Individual(self.problem.nVar)
                        for i in range(self.problem.nPop)])

        for i in range(self.problem.nPop):
            pop[i].Position = np.random.uniform(
                self.problem.VarMin,
                self.problem.VarMax,
                self.problem.VarSize
            )
            pop[i].Velocity = np.zeros(self.problem.VarSize)
            pop[i].Cost = self.CostFunction(pop[i].Position)
            pop[i].Best_Position = pop[i].Position
            pop[i].Best_Cost = pop[i].Cost
            if pop[i].Best_Cost < self.problem.BestSol.Cost:
                self.problem.GlobalBest.Position = pop[i].Best_Position
                self.problem.GlobalBest.Cost = pop[i].Best_Cost

        pop = np.array(sorted(pop, key=lambda a: a.Cost))
        self.problem.BestSol = copy.deepcopy(pop[0])
        self.problem.WorstCost = pop[-1].Cost
        self.pop = pop

    def first_run(self, problem, pop):
        for alg in self.algs:
            newpop = copy.deepcopy(pop)
            alg.run(self, pop, newpop)
            self.calls[alg.__class__.__name__] += 1

            # Update Best Cost
            self.BestCost[alg.algnum] = self.BestSol.Cost
            rewardTemp = self.BestSol.Cost - (-1)
            if rewardTemp > 0:
                alg.rewards = 1 / rewardTemp
            else:
                alg.rewards = abs(rewardTemp)

        return sorted(self.algs, key=lambda a: a.rewards)

    def results_get(self, best_sol):
        r = {}
        selected = best_sol.Position > self.problem.threshold
        selected_count = 0
        for k in selected:
            if k:
                selected_count += 1
        r["best_cost"] = best_sol.Cost
        r["selected_num"] = selected_count
        r["selected"] = self.columns[selected]
        return r

    def run(self):
        for i in range(self.MaxIt):
            self._run()

        return self.results_get(self.problem.BestSol)

    def _run(self):
        problem = self.problem
        pop = self.pop
        newpop = copy.deepcopy(pop)
        if not self.first_run_flag:
            self.algs = self.first_run(problem, pop)
            self.first_run_flag = 1

        chooseRandomic = np.random.rand(1)
        sumRewards = 0
        for i in range(self.nAlg):
            sumRewards = sumRewards + self.algs[i].rewards

        rewardsAve = sumRewards / self.nAlg

        if self.iterr < self.nAlg:
            numi = self.iterr
        elif chooseRandomic > self.RLAlpha:
            numi = np.random.randint(0, self.nAlg)
        elif chooseRandomic < self.RLAlpha:
            f = np.cumsum([i.rewards for i in self.algs])
            r = np.random.rand()
            if r > f[-1]:
                numi = f.size - 1
            else:
                numi = np.nonzero(r <= f)[0][0]

        lotCH = self.algs[numi].algnum
        self.lotCHList = np.append(self.lotCHList, lotCH)

        newpop = copy.deepcopy(pop)
        self.algs[numi].run(self, pop, newpop)
        self.calls[self.algs[numi].__class__.__name__] += 1

        self.BestCostMaxiter.append(self.BestSol.Cost)
        if self.iterr == 0:
            rewardsTemp = self.BestSol.Cost - (-1)
            if rewardsTemp > 0:
                self.algs[lotCH].rewards = 1 / rewardsTemp
            else:
                self.algs[lotCH].rewards = abs(rewardsTemp)
        elif self.iterr > 11 and self.BestCostMaxiter[self.iterr - 1] == self.BestCostMaxiter[self.iterr]:
            self.algs[lotCH].rewards = self.algs[lotCH].rewards - rewardsAve

        else:
            self.algs[lotCH].rewards = self.algs[lotCH].rewards + \
                abs(self.BestCostMaxiter[self.iterr] - self.BestCostMaxiter[self.iterr - 1])

        self.RLAlpha = self.RLAlpha + (1 / self.problem.MaxIt)
        self.algs = np.array(sorted(self.algs, key=lambda a: a.rewards))
        self.BestSolPerIter = self.BestSol

        self.iterr += 1
        self.problem.BestSol = copy.deepcopy(self.BestSol)
