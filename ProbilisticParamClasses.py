import math
import scipy.stats as stat
import SimPy.RandomVariateGenerators as RVGs
from ParameterClasses import *  # import everything from the ParameterClass module


class Parameters:
    """ class to include parameter information to simulate the model """

    def __init__(self, therapy, race):

        self.therapy = therapy              # selected therapy
        self.race = race                    # patient's race
        self.initialHealthState = HealthStates.WELL     # initial health state
        self.annualTreatmentCost = 0        # annual treatment cost
        self.transRateMatrix = []                # transition probability matrix of the selected therapy
        self.annualStateCosts = []          # annual state costs
        self.annualStateUtilities = []      # annual state utilities at the first year
        self.discountRate = Data.DISCOUNT   # discount rate


class ParameterGenerator:
    """ class to generate parameter values from the selected probability distributions """

    def __init__(self, therapy, race):

        self.therapy = therapy
        self.race = race                    # patient's race
        self.probMatrixRVG = []     # list of dirichlet distributions for transition probabilities
        self.annualStateCostRVG = []  # list of normal distributions for the annual cost of states
        self.annualStateUtilityRVG = []  # list of uniform distributions for the annual utility of states

        # treatment cost
        if self.therapy == Therapies.NO:
            self.annualTreatmentCost = Data.NO_COST
        else:
            self.annualTreatmentCost = Data.NO_COST + Data.BI_COST

        # create Dirichlet distributions for transition probabilities
        j = 0
        if self.race == Races.White:
            if self.therapy == Therapies.NO:
                for probs in Data.TRANS_MATRIX_N0_W:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1
            else:
                for probs in Data.TRANS_MATRIX_BI_W:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1

        elif self.race == Races.Black:
            if self.therapy == Therapies.NO:
                for probs in Data.TRANS_MATRIX_N0_B:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1
            else:
                for probs in Data.TRANS_MATRIX_BI_B:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1

        elif self.race == Races.AIAN:
            if self.therapy == Therapies.NO:
                for probs in Data.TRANS_MATRIX_N0_AIAN:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1
            else:
                for probs in Data.TRANS_MATRIX_BI_AIAN:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1

        elif self.race == Races.Hispanic:
            if self.therapy == Therapies.NO:
                for probs in Data.TRANS_MATRIX_N0_H:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1
            else:
                for probs in Data.TRANS_MATRIX_BI_H:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1

        else:
            if self.therapy == Therapies.NO:
                for probs in Data.TRANS_MATRIX_N0_API:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1
            else:
                for probs in Data.TRANS_MATRIX_BI_API:
                    self.probMatrixRVG.append(RVGs.Dirichlet(a=probs, if_ignore_0s=True))
                    j += 1


        # create normal distributions for annual state cost
        for cost in Data.ANNUAL_STATE_COST[1:3]:
            self.annualStateCostRVG.append(RVGs.Normal(loc=cost, scale=cost/4))

        # create uniform distributions for annual state utility
        if self.race == Races.White:
            for utility in Data.ANNUAL_STATE_UTILITY_W:
                self.annualStateUtilityRVG.append(RVGs.Uniform(scale=utility, loc=0.5*utility))

        elif self.race == Races.Black:
            for utility in Data.ANNUAL_STATE_UTILITY_W:
                self.annualStateUtilityRVG.append(RVGs.Uniform(scale=utility, loc=0.5*utility))

        elif self.race == Races.Hispanic:
            for utility in Data.ANNUAL_STATE_UTILITY_W:
                self.annualStateUtilityRVG.append(RVGs.Uniform(scale=utility, loc=0.5*utility))

        elif self.race == Races.AIAN:
            for utility in Data.ANNUAL_STATE_UTILITY_W:
                self.annualStateUtilityRVG.append(RVGs.Uniform(scale=utility, loc=0.5*utility))

        else:
            for utility in Data.ANNUAL_STATE_UTILITY_W:
                self.annualStateUtilityRVG.append(RVGs.Uniform(scale=utility, loc=0.5*utility))


    def get_new_parameters(self, rng):
        """
        :param rng: random number generator
        :return: a new parameter set
        """

        # create a parameter set
        param = Parameters(therapy=self.therapy, race=self.race)

        # calculate transition probabilities
        prob_matrix = []  # probability matrix without background mortality added
        # for all health states
        for s in HealthStates:
            # if the current state is not death
            if s not in [HealthStates.CANCER_DEATH, HealthStates.NATUAL_DEATH]:
                # sample from the dirichlet distribution to find the transition probabilities between breast cancer states
                # fill in the transition probabilities out of this state
                prob_matrix.append(self.probMatrixRVG[s.value].sample(rng))

        # calculate transition rate between breast cancer states
        param.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix)

        # sample from normal distributions that are assumed for annual state costs
        param.annualStateCosts = [0]
        for dist in self.annualStateCostRVG:
            cost = dist.loc
            fit_cost = dist.sample(rng)
            if fit_cost < 0.5 * cost:
                new_cost = 0.5 * cost
            elif fit_cost > 1.5 * cost:
                new_cost = 1.5 * cost
            else:
                new_cost = fit_cost
            # append the distribution
            param.annualStateCosts.append(new_cost)
        param.annualStateCosts.append(0)
        param.annualStateCosts.append(0)

        # sample from uniform distributions that are assumed for annual state utilities
        for dist in self.annualStateUtilityRVG:
            utility = dist.loc
            fit_utility =dist.sample(rng)
            if fit_utility < 0.5 * utility:
                new_utility = 0.5 * utility
            elif fit_utility > min(1, 1.5 * utility):
                new_utility = min(1, 1.5 * utility)
            else:
                new_utility = fit_utility
            param.annualStateUtilities.append(new_utility)


        # return the parameter set
        return param
