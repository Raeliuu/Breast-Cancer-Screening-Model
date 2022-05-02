import InputData as D
import MultiCohortClasses as Cls
import MultiCohortSupport as Support
import ProbilisticParamClasses as P

N_COHORTS = 200  # number of cohorts
POP_SIZE = 1000  # population size of each cohort

# White
# create a multi-cohort to simulate without screening
multiCohortNo = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.NO,
    race=P.Races.White
)

multiCohortNo.simulate(sim_length=D.SIM_LENGTH)

# create a multi-cohort to simulate with biennial screening
multiCohortBi = Cls.MultiCohort(
    ids=range(N_COHORTS, 2*N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.BI,
    race=P.Races.White
)

multiCohortBi.simulate(sim_length=D.SIM_LENGTH)

# print the estimates for the mean survival time and mean time to invasive cancer
Support.print_outcomes(multi_cohort_outcomes=multiCohortNo.multiCohortOutcomes,
                       therapy_name=P.Therapies.NO,
                       race=P.Races.White)
Support.print_outcomes(multi_cohort_outcomes=multiCohortBi.multiCohortOutcomes,
                       therapy_name=P.Therapies.BI,
                       race=P.Races.White)

# draw survival curves and histograms
Support.plot_survival_curves_and_histograms(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                            multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                   multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                       multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

#Black
#create a multi-cohort to simulate without screening
multiCohortNo = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.NO,
    race=P.Races.Black
)

multiCohortNo.simulate(sim_length=D.SIM_LENGTH)

# create a multi-cohort to simulate with biennial screening
multiCohortBi = Cls.MultiCohort(
    ids=range(N_COHORTS, 2*N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.BI,
    race=P.Races.Black
)

multiCohortBi.simulate(sim_length=D.SIM_LENGTH)

#print the estimates for the mean survival time and mean time to invasive cancer
Support.print_outcomes(multi_cohort_outcomes=multiCohortNo.multiCohortOutcomes,
                       therapy_name=P.Therapies.NO,
                       race=P.Races.Black)
Support.print_outcomes(multi_cohort_outcomes=multiCohortBi.multiCohortOutcomes,
                       therapy_name=P.Therapies.BI,
                       race=P.Races.Black)

# draw survival curves and histograms
Support.plot_survival_curves_and_histograms(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                            multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                   multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                       multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# AIAN
# create a multi-cohort to simulate without screening
multiCohortNo = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.NO,
    race=P.Races.AIAN
)

multiCohortNo.simulate(sim_length=D.SIM_LENGTH)

# create a multi-cohort to simulate with biennial screening
multiCohortBi = Cls.MultiCohort(
    ids=range(N_COHORTS, 2*N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.BI,
    race=P.Races.AIAN
)

multiCohortBi.simulate(sim_length=D.SIM_LENGTH)

# print the estimates for the mean survival time and mean time to invasive cancer
Support.print_outcomes(multi_cohort_outcomes=multiCohortNo.multiCohortOutcomes,
                       therapy_name=P.Therapies.NO,
                       race=P.Races.AIAN)
Support.print_outcomes(multi_cohort_outcomes=multiCohortBi.multiCohortOutcomes,
                       therapy_name=P.Therapies.BI,
                       race=P.Races.AIAN)

# draw survival curves and histograms
Support.plot_survival_curves_and_histograms(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                            multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                   multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                       multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# Hispanic
# create a multi-cohort to simulate without screening
multiCohortNo = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.NO,
    race=P.Races.Hispanic
)

multiCohortNo.simulate(sim_length=D.SIM_LENGTH)

# create a multi-cohort to simulate with biennial screening
multiCohortBi = Cls.MultiCohort(
    ids=range(N_COHORTS, 2*N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.BI,
    race=P.Races.Hispanic
)

multiCohortBi.simulate(sim_length=D.SIM_LENGTH)

# print the estimates for the mean survival time and mean time to invasive cancer
Support.print_outcomes(multi_cohort_outcomes=multiCohortNo.multiCohortOutcomes,
                       therapy_name=P.Therapies.NO,
                       race=P.Races.Hispanic)
Support.print_outcomes(multi_cohort_outcomes=multiCohortBi.multiCohortOutcomes,
                       therapy_name=P.Therapies.BI,
                       race=P.Races.Hispanic)

# draw survival curves and histograms
Support.plot_survival_curves_and_histograms(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                            multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                   multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                       multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# API
# create a multi-cohort to simulate without screening
multiCohortNo = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.NO,
    race=P.Races.API
)

multiCohortNo.simulate(sim_length=D.SIM_LENGTH)

# create a multi-cohort to simulate with biennial screening
multiCohortBi = Cls.MultiCohort(
    ids=range(N_COHORTS, 2*N_COHORTS),
    pop_size=POP_SIZE,
    therapy=P.Therapies.BI,
    race=P.Races.API
)

multiCohortBi.simulate(sim_length=D.SIM_LENGTH)

# print the estimates for the mean survival time and mean time to invasive cancer
Support.print_outcomes(multi_cohort_outcomes=multiCohortNo.multiCohortOutcomes,
                       therapy_name=P.Therapies.NO,
                       race=P.Races.API)
Support.print_outcomes(multi_cohort_outcomes=multiCohortBi.multiCohortOutcomes,
                       therapy_name=P.Therapies.BI,
                       race=P.Races.API)

# draw survival curves and histograms
Support.plot_survival_curves_and_histograms(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                            multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                                   multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(multi_cohort_outcomes_no=multiCohortNo.multiCohortOutcomes,
                       multi_cohort_outcomes_bi=multiCohortBi.multiCohortOutcomes)