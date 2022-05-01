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
    [99687.556,   312.444,    0,    0,   0],   # Well
    [0,   189.36,   123.084,    0,   0],   # Local
    [0,   0,   99.414,   23.67,   0],  # Regional
    [0,   0,   0,   1.37286,   22.29714]  # Distant
    ]

TRANS_MATRIX_BI_W =[
    [99566.21283,   433.787167,    0,    0,   0],   # Well
    [0,   360.7767103,   73.01045669,    0,   0],   # Local
    [0,   0,   63.2639861,   9.746470588,   0],  # Regional
    [0,   0,   0,   0.565295294,   9.181175294]  # Distant
    ]


TRANS_MATRIX_N0_B = [
    [99771.744,   228.256,    0,    0,   0],   # Well
    [0,   93.748,   134.508,    0,   0],   # Local
    [0,   0,   101.9,   32.608,   0],  # Regional
    [0,   0,   0,  1.369536,   31.238464]  # Distant
    ]

TRANS_MATRIX_BI_B =[
    [99683.09674,   316.9032645,    0,    0,   0],   # Well
    [0,   237.1163669,   79.78689764,    0,   0],   # Local
    [0,   0,   66.36007411,   13.42682353,   0],  # Regional
    [0,   0,   0,  0.563926588,   12.86289694]  # Distant
    ]



TRANS_MATRIX_N0_AIAN = [
    [99867.94,   132.06,    0,    0,   0],   # Well
    [0,   66.03,   66.03,    0,   0],   # Local
    [0,   0,   52.824,   13.206,   0],  # Regional
    [0,   0,   0,  0.818772,   12.387228]  # Distant
    ]

TRANS_MATRIX_BI_AIAN = [
    [99816.65216,   183.3478424,    0,    0,   0],   # Well
    [0,   144.1804408,   39.16740157,    0,   0],   # Local
    [0,   0,   33.72963687,   5.437764706,   0],  # Regional
    [0,   0,   0,  0.337141412,   5.100623294]  # Distant
    ]



TRANS_MATRIX_N0_H = [
    [99821.012,   178.988,    0,    0,   0],   # Well
    [0,   80.236,   98.752,    0,   0],   # Local
    [0,   0,   86.408,   12.344,   0],  # Regional
    [0,   0,   0,  0.814704,   11.529296]  # Distant
    ]

TRANS_MATRIX_BI_H = [
    [99751.49884,   248.5011632,    0,    0,   0],   # Well
    [0,   189.9238614,   58.57730184,    0,   0],   # Local
    [0,   0,   53.49447831,   5.082823529,   0],  # Regional
    [0,   0,   0,  0.335466353,   4.747357176]  # Distant
    ]


TRANS_MATRIX_N0_API = [
    [99823.488,   176.512,    0,    0,   0],   # Well
    [0,   99.288,   77.224,    0,   0],   # Local
    [0,   0,   63.434,   13.79,   0],  # Regional
    [0,   0,   0,  0.93772,   12.85228]  # Distant
    ]

TRANS_MATRIX_BI_API = [
    [99754.93644,   245.0635647,    0,    0,   0],   # Well
    [0,   199.2561527,   45.80741207,    0,   0],   # Local
    [0,   0,   40.12917678,   5.678235294,   0],  # Regional
    [0,   0,   0,  0.38612,   5.292115294]  # Distant
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
    1,         # Well
    0.950,     # Local
    0.887,     # Regional
    0.814,      # Distant
    ]

ANNUAL_STATE_UTILITY_B = [
    1,         # Well
    0.960,     # Local
    0.899,     # Regional
    0.817,      # Distant
    ]

ANNUAL_STATE_UTILITY_AIAN = [
    1,         # Well
    0.950,     # Local
    0.887,     # Regional
    0.812,      # Distant
    ]

ANNUAL_STATE_UTILITY_H = [
    1,         # Well
    0.945,     # Local
    0.852,     # Regional
    0.716,      # Distant
    ]

ANNUAL_STATE_UTILITY_API = [
    1,         # Well
    0.950,     # Local
    0.887,     # Regional
    0.812,      # Distant
    ]

# annual screening costs
NO_COST = 0
BI_COST = 151.19/2



