import InputData as D
import SimPy.EconEval as Econ
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.SamplePaths as Path
import SimPy.Statistics as Stat


def print_outcomes(multi_cohort_outcomes, therapy_name, race):
    """ prints the outcomes of a simulated cohort
    :param multi_cohort_outcomes: outcomes of a simulated multi-cohort
    :param therapy_name: the name of the selected therapy
    :param race: the race of the simulated patient
    """
    # mean and prediction interval of patient survival time
    survival_mean_PI_text = multi_cohort_outcomes.statMeanSurvivalTime\
        .get_formatted_mean_and_interval(interval_type='p',
                                         alpha=D.ALPHA,
                                         deci=2)

    # mean and prediction interval text of time to invasive cancer
    time_to_Diagnosis_PI_text = multi_cohort_outcomes.statMeanTimeToDiagnosis\
        .get_formatted_mean_and_interval(interval_type='p',
                                         alpha=D.ALPHA,
                                         deci=2)

    # mean and prediction interval text of discounted total cost
    cost_mean_PI_text = multi_cohort_outcomes.statMeanCost\
        .get_formatted_mean_and_interval(interval_type='p',
                                         alpha=D.ALPHA,
                                         deci=0,
                                         form=',')

    # mean and prediction interval text of discounted total QALY
    utility_mean_PI_text = multi_cohort_outcomes.statMeanQALY\
        .get_formatted_mean_and_interval(interval_type='p',
                                         alpha=D.ALPHA,
                                         deci=2)

    # print outcomes
    print(therapy_name, '(', race, ')')
    print("  Estimate of mean survival time and {:.{prec}%} uncertainty interval:".format(1 - D.ALPHA, prec=0),
          survival_mean_PI_text)
    print("  Estimate of mean time to invasive and {:.{prec}%} uncertainty interval:".format(1 - D.ALPHA, prec=0),
          time_to_Diagnosis_PI_text)
    print("  Estimate of mean discounted cost and {:.{prec}%} uncertainty interval:".format(1 - D.ALPHA, prec=0),
          cost_mean_PI_text)
    print("  Estimate of mean discounted utility and {:.{prec}%} uncertainty interval:".format(1 - D.ALPHA, prec=0),
          utility_mean_PI_text)
    print("")


def plot_survival_curves_and_histograms(multi_cohort_outcomes_no, multi_cohort_outcomes_bi):
    """ plot the survival curves and the histograms of survival times
    :param multi_cohort_outcomes_no: outcomes of a multi-cohort simulated without screening
    :param multi_cohort_outcomes_bi: outcomes of a multi-cohort simulated with biennial screening
    """

    # get survival curves of both treatments
    sets_of_survival_curves = [
        multi_cohort_outcomes_no.survivalCurves,
        multi_cohort_outcomes_bi.survivalCurves
    ]

    # graph survival curve
    Path.plot_sets_of_sample_paths(
        sets_of_sample_paths=sets_of_survival_curves,
        title='Survival Curves',
        x_label='Simulation Time Step (year)',
        y_label='Number of Patients Alive',
        legends=['Without Screening', 'Biennial screening'],
        transparency=0.4,
        color_codes=['green', 'blue']
    )

    # histograms of survival times
    set_of_survival_times = [
        multi_cohort_outcomes_no.meanSurvivalTimes,
        multi_cohort_outcomes_bi.meanSurvivalTimes
    ]

    # graph histograms
    Hist.plot_histograms(
        data_sets=set_of_survival_times,
        title='Histograms of Average Patient Survival Time',
        x_label='Survival Time (year)',
        y_label='Counts',
        bin_width=0.25,
        x_range=[5.25, 17.75],
        legends=['Without Screening', 'Biennial screening'],
        color_codes=['green', 'blue'],
        transparency=0.5
    )

    # histograms of time to invasive cancer
    set_of_diagnosis_times = [
        multi_cohort_outcomes_no.meanTimeToDiagnosis,
        multi_cohort_outcomes_no.meanTimeToDiagnosis
    ]

    # graph histograms
    Hist.plot_histograms(
        data_sets=set_of_diagnosis_times,
        title='Histogram of Average Patient Time until Invasive Cancer',
        x_label='Time until Invasive Cancer (year)',
        y_label='Counts',
        bin_width=1,
        legends=['Without Screening', 'Biennial screening'],
        color_codes=['green', 'blue'],
        transparency=0.5
    )


def print_comparative_outcomes(multi_cohort_outcomes_no, multi_cohort_outcomes_bi):
    """ prints average increase in survival time, discounted cost, and discounted utility
    under combination therapy compared to mono therapy
    :param multi_cohort_outcomes_no: outcomes of a multi-cohort simulated without screening
    :param multi_cohort_outcomes_bi: outcomes of a multi-cohort simulated with biennial screening
    """

    # increase in mean survival time with biennial screening with respect to no screening
    increase_mean_survival_time = Stat.DifferenceStatPaired(
        name='Increase in mean survival time',
        x=multi_cohort_outcomes_bi.meanSurvivalTimes,
        y_ref=multi_cohort_outcomes_no.meanSurvivalTimes)

    # estimate and PI
    estimate_PI = increase_mean_survival_time.get_formatted_mean_and_interval(interval_type='p',
                                                                              alpha=D.ALPHA,
                                                                              deci=2)
    print("Increase in mean survival time and {:.{prec}%} uncertainty interval:"
          .format(1 - D.ALPHA, prec=0),
          estimate_PI)

    # decrease in mean time until invasive cancer with biennial screening with respect to no screening
    decrease_mean_time_until_invasive_cancer = Stat.DifferenceStatPaired(
        name='Increase in mean survival time',
        x=multi_cohort_outcomes_bi.meanSurvivalTimes,
        y_ref=multi_cohort_outcomes_no.meanSurvivalTimes)

    # estimate and PI
    estimate_PI = decrease_mean_time_until_invasive_cancer.get_formatted_mean_and_interval(interval_type='p',
                                                                                           alpha=D.ALPHA,
                                                                                           deci=2)
    print("Decrease in mean time until invasive cancer and {:.{prec}%} uncertainty interval:"
          .format(1 - D.ALPHA, prec=0),
          estimate_PI)

    # increase in mean discounted cost under combination therapy with respect to mono therapy
    # paired not independent
    increase_mean_discounted_cost = Stat.DifferenceStatPaired(
        name='Increase in mean discounted cost',
        x=multi_cohort_outcomes_bi.meanCosts,
        y_ref=multi_cohort_outcomes_no.meanCosts)

    # estimate and PI
    estimate_PI = increase_mean_discounted_cost.get_formatted_mean_and_interval(interval_type='p',
                                                                                alpha=D.ALPHA,
                                                                                deci=2,
                                                                                form=',')
    print("Increase in mean discounted cost and {:.{prec}%} uncertainty interval:"
          .format(1 - D.ALPHA, prec=0),
          estimate_PI)

    # increase in mean discounted QALY under combination therapy with respect to mono therapy
    increase_mean_discounted_qaly = Stat.DifferenceStatPaired(
        name='Increase in mean discounted QALY',
        x=multi_cohort_outcomes_bi.meanQALYs,
        y_ref=multi_cohort_outcomes_no.meanQALYs)

    # estimate and PI
    estimate_PI = increase_mean_discounted_qaly.get_formatted_mean_and_interval(interval_type='p',
                                                                                alpha=D.ALPHA,
                                                                                deci=2)
    print("Increase in mean discounted utility and {:.{prec}%} uncertainty interval:"
          .format(1 - D.ALPHA, prec=0),
          estimate_PI)


def report_CEA_CBA(multi_cohort_outcomes_no, multi_cohort_outcomes_bi):
    """ performs cost-effectiveness and cost-benefit analyses
    :param multi_cohort_outcomes_mono: outcomes of a multi-cohort simulated without screening
    :param multi_cohort_outcomes_combo: outcomes of a multi-cohort simulated with biennial screening
    """

    # define two strategies
    no_screening_strategy = Econ.Strategy(
        name='No Screening',
        cost_obs=multi_cohort_outcomes_no.meanCosts,
        effect_obs=multi_cohort_outcomes_no.meanQALYs,
        color='green'
    )
    biennial_screening_strategy = Econ.Strategy(
        name='Biennial Screening',
        cost_obs=multi_cohort_outcomes_bi.meanCosts,
        effect_obs=multi_cohort_outcomes_bi.meanQALYs,
        color='blue'
    )

    # do CEA
    CEA = Econ.CEA(
        strategies=[no_screening_strategy, biennial_screening_strategy],
        if_paired=True
    )

    # show the cost-effectiveness plane
    CEA.plot_CE_plane(
        title='Cost-Effectiveness Analysis',
        x_label='Additional Discounted QALY',
        y_label='Additional Discounted Cost',
        fig_size=(6, 5),
        add_clouds=True,
        transparency=0.2)

    # report the CE table
    CEA.build_CE_table(
        interval_type='p',  # uncertainty (projection) interval
        alpha=D.ALPHA,
        cost_digits=0,
        effect_digits=2,
        icer_digits=2,
        file_name='CETable.csv')

    # CBA
    NBA = Econ.CBA(
        strategies=[no_screening_strategy, biennial_screening_strategy],
        wtp_range=(0, 50000),
        if_paired=True
    )
    # show the net monetary benefit figure
    NBA.plot_incremental_nmbs(
        title='Cost-Benefit Analysis',
        x_label='Willingness-To-Pay for One Additional QALY ($)',
        y_label='Incremental Net Monetary Benefit ($)',
        interval_type='p',
        show_legend=True,
        figure_size=(6, 5),
    )