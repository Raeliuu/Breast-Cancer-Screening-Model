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
        self.transRateMatrixRVG_NO = []     # list of beta distributions for mu2/(mu2+mu3) given known (mu2+mu3)
        self.transRateMatrixRVG_BI = []     # list of beta distributions for mu2/(mu2+mu3) given known (mu2+mu3)
        self.annualStateCostRVG = []  # list of gamma distributions for the annual cost of states
        self.annualStateUtilityRVG = []  # list of beta distributions for the annual utility of states
        self.annualTreatmentCostRVG = None   # gamma distribution for treatment cost

        # create gamma distributions for annual state cost
        for cost in Data.ANNUAL_STATE_COST:

            # if cost is zero, add a constant 0, otherwise add a gamma distribution
            if cost == 0:
                self.annualStateCostRVG.append(RVGs.Constant(value=0))
            else:
                # find shape and scale of the assumed gamma distribution
                # no data available to estimate the standard deviation, so we assumed st_dev=cost / 5
                fit_output = RVGs.Gamma.fit_mm(mean=cost, st_dev=cost / 5)
                # append the distribution
                self.annualStateCostRVG.append(
                    RVGs.Gamma(a=fit_output["a"],
                               loc=0,
                               scale=fit_output["scale"]))

        # create a gamma distribution for annual treatment cost
        if self.therapy == Therapies.NO:
            annual_cost = Data.NO_COST
        else:
            annual_cost = Data.NO_COST + Data.BI_COST
        fit_output = RVGs.Gamma.fit_mm(mean=annual_cost, st_dev=annual_cost / 5)
        self.annualTreatmentCostRVG = RVGs.Gamma(a=fit_output["a"],
                                                 loc=0,
                                                 scale=fit_output["scale"])

        # create beta distributions for annual state utility
        if self.race == Races.White:
            for utility in Data.ANNUAL_STATE_UTILITY_W:
                # if utility is zero, add a constant 0, otherwise add a beta distribution
                if utility == 0:
                    self.annualStateCostRVG.append(RVGs.Constant(value=0))
                else:
                    # find alpha and beta of the assumed beta distribution
                    # no data available to estimate the standard deviation, so we assumed st_dev=cost / 4
                    fit_output = RVGs.Beta.fit_mm(mean=utility, st_dev=utility / 4)
                    # append the distribution
                    self.annualStateUtilityRVG.append(
                        RVGs.Beta(a=fit_output["a"], b=fit_output["b"]))

        if self.race == Races.Black:
            for utility in Data.ANNUAL_STATE_UTILITY_B:
                # if utility is zero, add a constant 0, otherwise add a beta distribution
                if utility == 0:
                    self.annualStateCostRVG.append(RVGs.Constant(value=0))
                else:
                    # find alpha and beta of the assumed beta distribution
                    # no data available to estimate the standard deviation, so we assumed st_dev=cost / 4
                    fit_output = RVGs.Beta.fit_mm(mean=utility, st_dev=utility / 4)
                    # append the distribution
                    self.annualStateUtilityRVG.append(
                        RVGs.Beta(a=fit_output["a"], b=fit_output["b"]))

            if self.race == Races.Hispanic:
                for utility in Data.ANNUAL_STATE_UTILITY_H:
                    # if utility is zero, add a constant 0, otherwise add a beta distribution
                    if utility == 0:
                        self.annualStateCostRVG.append(RVGs.Constant(value=0))
                    else:
                        # find alpha and beta of the assumed beta distribution
                        # no data available to estimate the standard deviation, so we assumed st_dev=cost / 4
                        fit_output = RVGs.Beta.fit_mm(mean=utility, st_dev=utility / 4)
                        # append the distribution
                        self.annualStateUtilityRVG.append(
                            RVGs.Beta(a=fit_output["a"], b=fit_output["b"]))

            if self.race == Races.AIAN:
                for utility in Data.ANNUAL_STATE_UTILITY_AIAN:
                    # if utility is zero, add a constant 0, otherwise add a beta distribution
                    if utility == 0:
                        self.annualStateCostRVG.append(RVGs.Constant(value=0))
                    else:
                        # find alpha and beta of the assumed beta distribution
                        # no data available to estimate the standard deviation, so we assumed st_dev=cost / 4
                        fit_output = RVGs.Beta.fit_mm(mean=utility, st_dev=utility / 4)
                        # append the distribution
                        self.annualStateUtilityRVG.append(
                            RVGs.Beta(a=fit_output["a"], b=fit_output["b"]))

            if self.race == Races.API:
                for utility in Data.ANNUAL_STATE_UTILITY_API:
                    # if utility is zero, add a constant 0, otherwise add a beta distribution
                    if utility == 0:
                        self.annualStateCostRVG.append(RVGs.Constant(value=0))
                    else:
                        # find alpha and beta of the assumed beta distribution
                        # no data available to estimate the standard deviation, so we assumed st_dev=cost / 4
                        fit_output = RVGs.Beta.fit_mm(mean=utility, st_dev=utility / 4)
                        # append the distribution
                        self.annualStateUtilityRVG.append(
                            RVGs.Beta(a=fit_output["a"], b=fit_output["b"]))

    def get_new_parameters(self, rng):
        """
        :param rng: random number generator
        :return: a new parameter set
        """

        # create a parameter set
        param = Parameters(therapy=self.therapy, race=self.race)

        # create beta distributions for mu2/(mu2+mu3) given known (mu2+mu3)
        fit_output = RVGs.Beta.fit_mm(mean=0.5, st_dev=0.25)
        if self.race == Races.White:
            self.transRateMatrixRVG_NO = Data.TRANS_MATRIX_N0_W
            self.transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * Data.SUM_W_NO
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_W_NO - self.transRateMatrixRVG_NO[0][2]

            self.transRateMatrixRVG_BI = Data.TRANS_MATRIX_BI_W
            self.transRateMatrixRVG_BI[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_W_BI
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_W_BI - self.transRateMatrixRVG_BI[0][2]

        if self.race == Races.Black:
            self.transRateMatrixRVG_NO = Data.TRANS_MATRIX_N0_B
            self.transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_B_NO
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_B_NO - self.transRateMatrixRVG_NO[0][2]

            self.transRateMatrixRVG_BI = Data.TRANS_MATRIX_BI_B
            self.transRateMatrixRVG_BI[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_B_BI
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_B_BI - self.transRateMatrixRVG_BI[0][2]

        if self.race == Races.AIAN:
            self.transRateMatrixRVG_NO = Data.TRANS_MATRIX_N0_AIAN
            self.transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_AIAN_NO
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_AIAN_NO - self.transRateMatrixRVG_NO[0][2]

            self.transRateMatrixRVG_BI = Data.TRANS_MATRIX_BI_AIAN
            self.transRateMatrixRVG_BI[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_AIAN_BI
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_AIAN_BI - self.transRateMatrixRVG_BI[0][2]

        if self.race == Races.Hispanic:
            self.transRateMatrixRVG_NO = Data.TRANS_MATRIX_N0_H
            self.transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_H_NO
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_H_NO - self.transRateMatrixRVG_NO[0][2]

            self.transRateMatrixRVG_BI = Data.TRANS_MATRIX_BI_H
            self.transRateMatrixRVG_BI[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_H_BI
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_H_BI - self.transRateMatrixRVG_BI[0][2]

        if self.race == Races.API:
            self.transRateMatrixRVG_NO = Data.TRANS_MATRIX_N0_API
            self.transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_API_NO
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_API_NO - self.transRateMatrixRVG_NO[0][2]

            self.transRateMatrixRVG_BI = Data.TRANS_MATRIX_BI_API
            self.transRateMatrixRVG_BI[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * \
                                               Data.SUM_API_BI
            self.transRateMatrixRVG_NO[1][2] = Data.SUM_API_BI - self.transRateMatrixRVG_BI[0][2]

        # sample from gamma distributions that are assumed for annual state costs
        for dist in self.annualStateCostRVG:
            param.annualStateCosts.append(dist.sample(rng))

        # sample from the gamma distribution that is assumed for the treatment cost
        param.annualTreatmentCost = self.annualTreatmentCostRVG.sample(rng)

        # sample from beta distributions that are assumed for annual state utilities
        for dist in self.annualStateUtilityRVG:
            param.annualStateUtilities.append(dist.sample(rng))

        # return the parameter set
        return param
