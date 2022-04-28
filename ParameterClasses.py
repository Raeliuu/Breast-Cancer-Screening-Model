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
        if self.race == Races.White:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_W
            if therapy == Therapies.NO:
                self.transRateMatrix = Data.TRANS_MATRIX_N0_W
            if therapy == Therapies.BI:
                self.transRateMatrix = Data.TRANS_MATRIX_BI_W

        if self.race == Races.Black:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_B
            if therapy == Therapies.NO:
                self.transRateMatrix = Data.TRANS_MATRIX_N0_B
            if therapy == Therapies.BI:
                self.transRateMatrix = Data.TRANS_MATRIX_BI_B

        if self.race == Races.AIAN:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_AIAN
            if therapy == Therapies.NO:
                self.transRateMatrix = Data.TRANS_MATRIX_N0_AIAN
            if therapy == Therapies.BI:
                self.transRateMatrix = Data.TRANS_MATRIX_BI_AIAN

        if self.race == Races.Hispanic:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_H
            if therapy == Therapies.NO:
                self.transRateMatrix = Data.TRANS_MATRIX_N0_H
            if therapy == Therapies.BI:
                self.transRateMatrix = Data.TRANS_MATRIX_BI_H

        if self.race == Races.API:
            self.annualStateUtilities = Data.ANNUAL_STATE_UTILITY_API
            if therapy == Therapies.NO:
                self.transRateMatrix = Data.TRANS_MATRIX_N0_API
            if therapy == Therapies.BI:
                self.transRateMatrix = Data.TRANS_MATRIX_BI_API

        # annual state costs
        self.annualStateCosts = Data.ANNUAL_STATE_COST

        # discount rate
        self.discountRate = Data.DISCOUNT

