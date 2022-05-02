from enum import Enum
import numpy as np
import SimPy.RandomVariateGenerators as RVGs


# simulation settings
POP_SIZE = 1000     # cohort population size
SIM_LENGTH = 25   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
# annual probability of background mortality (number per year per 100,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 4386.10/ 100000



class HealthStates(Enum):
    """ health states of patients with HIV """
    WELL = 0
    LOCAL = 1
    REGIONAL = 2
    DISTANT = 3
    CANCER_DEATH = 4
    NATUAL_DEATH = 5


# transition rate matrix

TRANS_MATRIX_N0_W = [
    [93751.120,   6248.880,    0,    0,   0],   # Well
    [0,   1782.045,   4466.835,    0,   0],   # Local
    [0,   0,   1465.142,   996.538,   0],  # Regional
    [0,   0,   0,   57.799,   415.601]  # Distant
    ]

TRANS_MATRIX_BI_W =[
    [91324.257,   8675.743,    0,    0,   0],   # Well
    [0,   6026.124,   2649.619,    0,   0],   # Local
    [0,   0,   1049.870,   410.339,   0],  # Regional
    [0,   0,   0,   23.800,   171.130]  # Distant
    ]


TRANS_MATRIX_N0_B = [
    [95434.880,   4565.120,    0,    0,   0],   # Well
    [0,   1301.873,   3263.247,    0,   0],   # Local
    [0,   0,   1962.139,   728.021,   0],  # Regional
    [0,   0,   0,  30.577,   621.583]  # Distant
    ]

TRANS_MATRIX_BI_B =[
    [93661.935,   6338.065,    0,    0,   0],   # Well
    [0,   4402.386,   1935.679,    0,   0],   # Local
    [0,   0,   1295.965,   299.773,   0],  # Regional
    [0,   0,   0,  12.590,   255.946]  # Distant
    ]



TRANS_MATRIX_N0_AIAN = [
    [97358.800,   2641.200,    0,    0,   0],   # Well
    [0,   753.213,   1887.987,    0,   0],   # Local
    [0,   0,   899.395,   421.205,   0],  # Regional
    [0,   0,   0,  26.115,   238.005]  # Distant
    ]

TRANS_MATRIX_BI_AIAN =[
    [96333.043,   3666.957,    0,    0,   0],   # Well
    [0,   2547.048,   1119.908,    0,   0],   # Local
    [0,   0,   609.911,   173.437,   0],  # Regional
    [0,   0,   0,  10.753,   98.002]  # Distant
    ]



TRANS_MATRIX_N0_H = [
    [96420.240,   3579.760,    0,    0,   0],   # Well
    [0,   1020.870,   2558.890,    0,   0],   # Local
    [0,   0,   1404.159,   570.881,   0],  # Regional
    [0,   0,   0,  37.678,   209.202]  # Distant
    ]

TRANS_MATRIX_BI_H = [
    [95029.977,   4970.023,    0,    0,   0],   # Well
    [0,   3452.151,   1517.872,    0,   0],   # Local
    [0,   0,   936.477,   235.069,   0],  # Regional
    [0,   0,   0,  15.515,   86.142]  # Distant
    ]


TRANS_MATRIX_N0_API = [
    [95098.729,   4901.271,    0,    0,   0],   # Well
    [0,   1397.736,   3503.535,    0,   0],   # Local
    [0,   0,   134.520,   781.629,   0],  # Regional
    [0,   0,   0,  53.151,   60.414]  # Distant
    ]

TRANS_MATRIX_BI_API = [
    [95098.729,   4901.271,    0,    0,   0],   # Well
    [0,   3404.397,   1496.875,    0,   0],   # Local
    [0,   0,   684.331,   231.817,   0],  # Regional
    [0,   0,   0,  15.764,   97.801]  # Distant
    ]


# annual cost of each health state
ANNUAL_STATE_COST = [
    0,         # Well
    6194.600,     # Local
    10350.133,    # Regional
    17814.500,    # Distant
    0,            # Death
    0
    ]


# annual health utility of each health state
ANNUAL_STATE_UTILITY_W = [
    0.731,         # Well
    0.950,     # Local
    0.887,     # Regional
    0.814,      # Distant
    ]

ANNUAL_STATE_UTILITY_B = [
    0.814,         # Well
    0.960,     # Local
    0.899,     # Regional
    0.817,      # Distant
    ]

ANNUAL_STATE_UTILITY_AIAN = [
    0.738,         # Well
    0.950,     # Local
    0.887,     # Regional
    0.812,      # Distant
    ]

ANNUAL_STATE_UTILITY_H = [
    0.676,         # Well
    0.945,     # Local
    0.852,     # Regional
    0.716,      # Distant
    ]

ANNUAL_STATE_UTILITY_API = [
    0.738,         # Well
    0.950,     # Local
    0.887,     # Regional
    0.812,      # Distant
    ]

# annual screening costs
NO_COST = 0
BI_COST = 151.19/2



