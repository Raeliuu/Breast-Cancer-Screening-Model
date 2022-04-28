from enum import Enum
import numpy as np
import SimPy.RandomVariateGenerators as RVGs


# simulation settings
POP_SIZE = 1000     # cohort population size
SIM_LENGTH = 25   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

class HealthStates(Enum):
    """ health states of patients with HIV """
    WELL = 0
    DCIS = 1
    LOCAL = 2
    REGIONAL = 3
    DISTANT = 4
    CANCER_DEATH = 5
    NATUAL_DEATH = 6


# transition rate matrix
SUM_W_NO =0.00313
SUM_W_BI =0.00434

TRANS_MATRIX_N0_W = [
    [0,   0.000142,    SUM_W_NO/2,    0,   0,   0,   0.0462],   # Well
    [0,   0,   SUM_W_NO/2,    0,   0,   0,   0.0462],   # DCIS
    [0,   0,   0,   0.00123,   0,   0,   0.0462],  # Local
    [0,   0,   0,   0,   0.000237,   0,   0.0462],  # Regional
    [0,   0,   0,   0,   0,   0.201,   0.0462]   # Distant
    ]

TRANS_MATRIX_BI_W =[
    [0,   0.000142,    SUM_W_BI/2,    0,   0,   0,   0.0462],   # Well
    [0,   0,   SUM_W_BI/2,    0,   0,   0,   0.0462],   # DCIS
    [0,   0,   0,   0.000731,   0,   0,   0.0462],  # Local
    [0,   0,   0,   0,   0.0000975,   0,   0.0462],  # Regional
    [0,   0,   0,   0,   0,   0.0829,   0.0462]   # Distant
    ]

SUM_B_NO =0.00229
SUM_B_BI =0.00317

TRANS_MATRIX_N0_B = [
    [0,   0.000122,   SUM_B_NO/2,    0,   0,   0,   0.0549],   # Well
    [0,   0,   SUM_B_NO/2,    0,   0,   0,   0.0549],   # DCIS
    [0,   0,   0,   0.00135,   0,   0,   0.0549],  # Local
    [0,   0,   0,   0,   0.000326,   0,   0.0549],  # Regional
    [0,   0,   0,   0,   0,   0.257,   0.0549]   # Distant
    ]

TRANS_MATRIX_BI_B =[
    [0,   0.000122,    SUM_B_BI/2,    0,   0,   0,   0.0549],   # Well
    [0,   0,   SUM_B_BI/2,    0,   0,   0,   0.0549],   # DCIS
    [0,   0,   0,   0.000798,   0,   0,   0.0549],  # Local
    [0,   0,   0,   0,   0.000134,   0,   0.0549],  # Regional
    [0,   0,   0,   0,   0,   0.106,   0.0549]   # Distant
    ]

SUM_AIAN_NO =0.00132
SUM_AIAN_BI =0.00183

TRANS_MATRIX_N0_AIAN = [
    [0,   0.0000880,    SUM_AIAN_NO/2,    0,   0,   0,   0.0482],   # Well
    [0,   0,   SUM_AIAN_NO/2,    0,   0,   0,   0.0482],   # DCIS
    [0,   0,   0,   0.000661,   0,   0,   0.0482],  # Local
    [0,   0,   0,   0,   0.000132,   0,   0.0482],  # Regional
    [0,   0,   0,   0,   0,   0.186,   0.0482]   # Distant
    ]

TRANS_MATRIX_BI_AIAN = [
    [0,   0.0000880,    SUM_AIAN_BI/2,    0,   0,   0,   0.0482],   # Well
    [0,   0,   SUM_AIAN_BI/2,    0,   0,   0,   0.0482],   # DCIS
    [0,   0,   0,   0.000392,   0,   0,   0.0482],  # Local
    [0,   0,   0,   0,   0.0000544,   0,   0.0482],  # Regional
    [0,   0,   0,   0,   0,   0.0766,   0.0482]   # Distant
    ]

SUM_H_NO =0.00132
SUM_H_BI =0.00183

TRANS_MATRIX_N0_H = [
    [0,   0.000123,    SUM_H_NO/2,    0,   0,   0,   0.0327],   # Well
    [0,   0,   SUM_H_NO/2,    0,   0,   0,   0.0327],   # DCIS
    [0,   0,   0,   0.000988,   0,   0,   0.0327],  # Local
    [0,   0,   0,   0,   0.000123,   0,   0.0327],  # Regional
    [0,   0,   0,   0,   0,   0.189,   0.0327]   # Distant
    ]

TRANS_MATRIX_BI_H = [
    [0,   0.000123,    SUM_H_BI/2,    0,   0,   0,   0.0327],   # Well
    [0,   0,   SUM_H_BI/2,    0,   0,   0,   0.0327],   # DCIS
    [0,   0,   0,   0.000586,   0,   0,   0.0327],  # Local
    [0,   0,   0,   0,   0.0000508,   0,   0.0327],  # Regional
    [0,   0,   0,   0,   0,   0.0779,   0.0327]   # Distant
    ]

SUM_API_NO =0.00132
SUM_API_BI =0.00183

TRANS_MATRIX_N0_API = [
    [0,   0.0000551,    SUM_API_NO/2,    0,   0,   0,   0.0239],   # Well
    [0,   0,   SUM_API_NO/2,    0,   0,   0,   0.0239],   # DCIS
    [0,   0,   0,   0.000773,   0,   0,   0.0239],  # Local
    [0,   0,   0,   0,   0.000138,   0,   0.0239],  # Regional
    [0,   0,   0,   0,   0,   0.192,   0.0239]   # Distant
    ]

TRANS_MATRIX_BI_API = [
    [0,   0.0000551,    SUM_API_BI/2,    0,   0,   0,   0.0239],   # Well
    [0,   0,   SUM_API_BI/2,    0,   0,   0,   0.0239],   # DCIS
    [0,   0,   0,   0.000458,   0,   0,   0.0239],  # Local
    [0,   0,   0,   0,   0.0000568,   0,   0.0239],  # Regional
    [0,   0,   0,   0,   0,   0.0790,   0.0239]   # Distant
    ]


# annual cost of each health state
ANNUAL_STATE_COST = [
    0,         # Well
    3316.647,     # DCIS
    6194.600,     # Local
    10350.133,     # Regional
    17814.500      # Distant
    ]


# annual health utility of each health state
ANNUAL_STATE_UTILITY_W = [
    1,         # Well
    0.975,     # DCIS
    0.950,     # Local
    0.887,     # Regional
    0.814      # Distant
    ]

ANNUAL_STATE_UTILITY_B = [
    1,         # Well
    0.983 ,     # DCIS
    0.960,     # Local
    0.899,     # Regional
    0.817      # Distant
    ]

ANNUAL_STATE_UTILITY_AIAN = [
    1,         # Well
    0.976,     # DCIS
    0.950,     # Local
    0.887,     # Regional
    0.812      # Distant
    ]

ANNUAL_STATE_UTILITY_H = [
    1,         # Well
    0.978,     # DCIS
    0.945,     # Local
    0.852,     # Regional
    0.716      # Distant
    ]

ANNUAL_STATE_UTILITY_API = [
    1,         # Well
    0.976,     # DCIS
    0.950,     # Local
    0.887,     # Regional
    0.812      # Distant
    ]

# annual screening costs
NO_COST = 0
BI_COST = 151.19/2


rng = np.random.RandomState(seed=1)
fit_output = RVGs.Beta.fit_mm(mean=0.5, st_dev=0.25)

transRateMatrixRVG_NO = TRANS_MATRIX_N0_W.copy()
sum = TRANS_MATRIX_N0_W[0][2]+TRANS_MATRIX_N0_W[1][2]
transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng) * sum
transRateMatrixRVG_NO[1][2] = sum-transRateMatrixRVG_NO[0][2]
rng_2 = np.random.RandomState(seed=5)
transRateMatrixRVG_NO = TRANS_MATRIX_N0_W.copy()
sum = TRANS_MATRIX_N0_W[0][2]+TRANS_MATRIX_N0_W[1][2]
transRateMatrixRVG_NO[0][2] = RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng_2) * sum
transRateMatrixRVG_NO[1][2] = sum-transRateMatrixRVG_NO[0][2]
#
print(TRANS_MATRIX_N0_W[0][2])
print(TRANS_MATRIX_N0_W[1][2])
print(transRateMatrixRVG_NO[0][2])
print(transRateMatrixRVG_NO[1][2])
print((TRANS_MATRIX_N0_W[0][2] + TRANS_MATRIX_N0_W[1][2]))
# print(RVGs.Beta(a=fit_output["a"], b=fit_output["b"]).sample(rng))




