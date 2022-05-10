import InputData as D
import MultiCohortClasses as Cls
import MultiCohortSupport as Support
import ProbilisticParamClasses as P
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.SamplePaths as Path

N_COHORTS = 200              # number of cohorts
therapy = P.Therapies.NO  # selected therapy
race = P.Races.White

# create multiple cohort
multiCohortW = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=D.POP_SIZE,
    therapy=therapy,
    race=P.Races.White)

multiCohortW.simulate(sim_length=10)

# # plot the sample paths
# Path.plot_sample_paths(
#     sample_paths=multiCohort.multiCohortOutcomes.survivalCurves,
#     title='Survival Curves',
#     x_label='Time-Step (Year)',
#     y_label='Number Survived',
#     transparency=0.5)
#
# # plot the histogram of average survival time
# Hist.plot_histogram(
#     data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
#     title='Histogram of Mean Survival Time',
#     x_label='Mean Survival Time (Year)',
#     y_label='Count')
#
# Hist.plot_histogram(
#     data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
#     title='Histogram of Mean Survival Time',
#     x_label='Mean Survival Time (Year)',
#     y_label='Count')

# print the outcomes of this simulated cohort
Support.print_outcomes(multi_cohort_outcomes=multiCohortW.multiCohortOutcomes,
                       therapy_name=therapy, race=P.Races.White)

# create multiple cohort
multiCohortB = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=D.POP_SIZE,
    therapy=therapy,
    race=P.Races.Black)

multiCohortB.simulate(sim_length=10)

# print the outcomes of this simulated cohort
Support.print_outcomes(multi_cohort_outcomes=multiCohortB.multiCohortOutcomes,
                       therapy_name=therapy, race=P.Races.Black)

# create multiple cohort
multiCohortAIAN = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=D.POP_SIZE,
    therapy=therapy,
    race=P.Races.AIAN)

multiCohortAIAN.simulate(sim_length=10)

# print the outcomes of this simulated cohort
Support.print_outcomes(multi_cohort_outcomes=multiCohortAIAN.multiCohortOutcomes,
                       therapy_name=therapy, race=P.Races.AIAN)

# create multiple cohort
multiCohortH = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=D.POP_SIZE,
    therapy=therapy,
    race=P.Races.Hispanic)

multiCohortH.simulate(sim_length=10)

# print the outcomes of this simulated cohort
Support.print_outcomes(multi_cohort_outcomes=multiCohortH.multiCohortOutcomes,
                       therapy_name=therapy, race=P.Races.Hispanic)

# create multiple cohort
multiCohortAPI = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=D.POP_SIZE,
    therapy=therapy,
    race=P.Races.API)

multiCohortAPI.simulate(sim_length=10)

# print the outcomes of this simulated cohort
Support.print_outcomes(multi_cohort_outcomes=multiCohortAPI.multiCohortOutcomes,
                       therapy_name=therapy, race=P.Races.API)
