from enum import Enum
import numpy as np
import InputData as Data
from InputData import HealthStates
import SimPy.Markov as Markov


class Therapies(Enum):
    """ no screening vs. biennial screening """
    NO = 0
    BI = 1


class Races(Enum):
    """ race of the patient (i.e., non-Hispanic Whites, non-Hispanic Black, non-Hispanic American Indian/Alaska
     Native (AIAN), Hispanic, and non-Hispanic Asian/Pacific Islander (API))"""
    White = 0
    Black = 1
    AIAN = 2
    Hispanic = 3
    API = 4


class Parameters:
    def __init__(self, therapy, race):

        # selected therapy
        self.therapy = therapy

        # race of the patients
        self.race = race

        # initial health state
        self.initialHealthState = HealthStates.WELL

        # annual treatment cost
        if self.therapy == Therapies.NO:
            self.annualTreatmentCost = Data.NO_COST
        else:
            self.annualTreatmentCost = Data.BI_COST

        # transition rate matrix and annual states utilities
        # transition probability matrix of the selected therapy
        self.transRateMatrix = []
        if self.race == Races.White:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_W
            if therapy == Therapies.NO:
                # calculate transition probabilities between breast cancer states
                prob_matrix_no = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_N0_W)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_no)
            if therapy == Therapies.BI:
                # calculate transition probabilities between breast cancer states
                prob_matrix_bi = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_BI_W)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_bi)

        if self.race == Races.Black:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_B
            if therapy == Therapies.NO:
                # calculate transition probabilities between breast cancer states
                prob_matrix_no = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_N0_B)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_no)
            if therapy == Therapies.BI:
                # calculate transition probabilities between breast cancer states
                prob_matrix_bi = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_BI_B)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_bi)

        if self.race == Races.AIAN:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_AIAN
            if therapy == Therapies.NO:
                # calculate transition probabilities between breast cancer states
                prob_matrix_no = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_N0_AIAN)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_no)
            if therapy == Therapies.BI:
                # calculate transition probabilities between breast cancer states
                prob_matrix_bi = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_BI_AIAN)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_bi)

        if self.race == Races.Hispanic:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_H
            if therapy == Therapies.NO:
                # calculate transition probabilities between breast cancer states
                prob_matrix_no = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_N0_H)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_no)
            if therapy == Therapies.BI:
                # calculate transition probabilities between breast cancer states
                prob_matrix_bi = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_BI_H)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_bi)

        if self.race == Races.API:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_API
            if therapy == Therapies.NO:
                # calculate transition probabilities between breast cancer states
                prob_matrix_no = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_N0_API)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_no)
            if therapy == Therapies.BI:
                # calculate transition probabilities between breast cancer states
                prob_matrix_bi = get_trans_prob_matrix(trans_matrix=Data.TRANS_MATRIX_BI_API)
                self.transRateMatrix = get_trans_rate_matrix(trans_prob_matrix=prob_matrix_bi)

        # annual state costs
        self.annualStateCosts = Data.ANNUAL_STATE_COST

        # discount rate
        self.discountRate = Data.DISCOUNT


def get_trans_prob_matrix(trans_matrix):
    """
    :param trans_matrix: transition matrix containing counts of transitions between states
    :return: transition probability matrix
    """

    # initialize transition probability matrix
    trans_prob_matrix = []

    # for each row in the transition matrix
    for row in trans_matrix:
        # calculate the transition probabilities
        prob_row = np.array(row)/sum(row)
        # add this row of transition probabilities to the transition probability matrix
        trans_prob_matrix.append(prob_row)

    return trans_prob_matrix

def get_trans_rate_matrix(trans_prob_matrix):

    # find the transition rate matrix
    trans_rate_matrix = Markov.discrete_to_continuous(
        trans_prob_matrix=trans_prob_matrix,
        delta_t=1)

    # calculate background mortality rate
    mortality_rate = -np.log(1 - Data.ANNUAL_PROB_BACKGROUND_MORT)

    # add background mortality rate
    for row in trans_rate_matrix:
        row.append(mortality_rate)

    # add 2 rows for breast cancer death and natural death
    trans_rate_matrix.append([0] * len(HealthStates))
    trans_rate_matrix.append([0] * len(HealthStates))

    return trans_rate_matrix



