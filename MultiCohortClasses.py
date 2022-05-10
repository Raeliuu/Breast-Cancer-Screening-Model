import numpy as np

import SimPy.Statistics as Stat
from MarkovModelClasses import Cohort
from ProbilisticParamClasses import ParameterGenerator


class MultiCohort:
    """ simulates multiple cohorts with different parameters """

    def __init__(self, ids, pop_size, therapy, race):
        """
        :param ids: (list) of ids for cohorts to simulate
        :param pop_size: (int) population size of cohorts to simulate
        :param therapy: selected therapy
        """
        self.ids = ids
        self.popSize = pop_size
        self.therapy = therapy
        self.race = race
        self.paramSets = []  # list of parameter sets each of which corresponds to a cohort
        self.multiCohortOutcomes = MultiCohortOutcomes()

    def __populate_parameter_sets(self):

        # create a parameter set generator
        param_generator = ParameterGenerator(therapy=self.therapy, race=self.race)

        # create as many sets of parameters as the number of cohorts
        for i in range(len(self.ids)):
            # create a new random number generator for each parameter set
            rng = np.random.RandomState(seed=i)
            # get and store a new set of parameter
            self.paramSets.append(param_generator.get_new_parameters(rng=rng))

    def simulate(self, sim_length):
        """ simulates all cohorts
        :param sim_length: simulation length
        """

        # create parameter sets
        self.__populate_parameter_sets()

        for i in range(len(self.ids)):
            # create a cohort
            cohort = Cohort(id=self.ids[i],
                            pop_size=self.popSize,
                            parameters=self.paramSets[i])

            # simulate the cohort
            cohort.simulate(sim_length=sim_length)

            # extract the outcomes of this simulated cohort
            self.multiCohortOutcomes.extract_outcomes(simulated_cohort=cohort)

        # calculate the summary statistics of outcomes from all cohorts
        self.multiCohortOutcomes.calculate_summary_stats()


class MultiCohortOutcomes:
    def __init__(self):

        self.survivalCurves = []  # list of survival curves from all simulated cohorts
        self.meanSurvivalTimes = []  # list of average patient survival time from each simulated cohort
        self.meanNCancer = []     # list of average number of diagnosis of invasive cancer from each simulated cohort
        self.meanCosts = []          # list of average patient cost from each simulated cohort
        self.meanQALYs = []          # list of average patient QALY from each simulated cohort
        self.nCancerDeath = []     # list of number of cancer death from each simulated cohort


        self.statMeanSurvivalTime = None    # summary statistics of average survival time
        self.statMeanNCancer = None      # summary statistics of average number of diagnosis of invasive cancer
        self.statNCancerDeath = None      # summary statistics of number of cancer death
        self.statMeanCost = None            # summary statistics of average cost
        self.statMeanQALY = None            # summary statistics of average QALY

    def extract_outcomes(self, simulated_cohort):
        """ extracts outcomes of a simulated cohort
        :param simulated_cohort: a cohort after being simulated"""

        # append the survival curve of this cohort
        self.survivalCurves.append(simulated_cohort.cohortOutcomes.nLivingPatients)

        # store mean survival time from this cohort
        self.meanSurvivalTimes.append(simulated_cohort.cohortOutcomes.statSurvivalTime.get_mean())
        # store mean number of invasive cancer from this cohort
        self.meanNCancer.append(simulated_cohort.cohortOutcomes.statNCancer.get_mean())
        # store total number of cancer death from this cohort
        self.nCancerDeath.append(simulated_cohort.cohortOutcomes.statNCancerDeath.get_total())
        # store mean cost from this cohort
        self.meanCosts.append(simulated_cohort.cohortOutcomes.statCost.get_mean())
        # store mean QALY from this cohort
        self.meanQALYs.append(simulated_cohort.cohortOutcomes.statUtility.get_mean())

    def calculate_summary_stats(self):
        """
        calculate the summary statistics
        """

        # summary statistics of mean survival time
        self.statMeanSurvivalTime = Stat.SummaryStat(name='Average survival time',
                                                     data=self.meanSurvivalTimes)
        # summary statistics of mean number of invasive cancer
        self.statMeanNCancer = Stat.SummaryStat(name='Average number of invasive breast cancer',
                                                data=self.meanNCancer)
        # summary statistics of total number of cancer death
        self.statNCancerDeath = Stat.SummaryStat(name = 'Total number of invasive cancer death',
                                                 data = self.nCancerDeath)

        # summary statistics of mean cost
        self.statMeanCost = Stat.SummaryStat(name='Average cost',
                                             data=self.meanCosts)
        # summary statistics of mean QALY
        self.statMeanQALY = Stat.SummaryStat(name='Average QALY',
                                             data=self.meanQALYs)
