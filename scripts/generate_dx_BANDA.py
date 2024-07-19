#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from cyclopts import App, Parameter
from typing_extensions import Annotated

from neurostatx.utils.preprocessing import merge_dataframes


# Initializing the app.
app = App(default_parameter=Parameter(negative=()))


@app.default()
def main(
    in_root_folder: Annotated[
        str,
        Parameter(
            help="BANDA Release 1.1 source directory path.",
            show_default=False,
            group="Essential Files Options",
        ),
    ],
    output: Annotated[
        str,
        Parameter(
            help="Output dataset filename and path.",
            show_default=False,
            group="Essential Files Options",
        ),
    ],
):
    """
    generate_dx.py is a script that reproduce the variables
    used in [1]. This script is specifically designed and hard-coded for the
    BANDA Release 1.1 dataset and is adapted in python
    from this R code [2].

    [1] Bernanke, J., Luna, A., Chang, L., Bruno, E., Dworkin, J., & Posner, J.
        (2022). Structural brain measures among children with and without ADHD
        in the Adolescent Brain and Cognitive Development Study cohort: A
        cross-sectional US population-based study. The Lancet Psychiatry, 9(3),
        222–231. https://doi.org/10.1016/S2215-0366(21)00505-8

    [2]
    https://github.com/jabernanke/lancet/blob/main/JB%20-%20consolidated%20for%20Lancet%20-%20final.R

    """

    # Load dataset for KSADS diagnosis data.
    ksads1 = pd.read_excel(f'{in_root_folder}/ksads_diagnoses01.xlsx')
    ksads2 = pd.read_excel(f'{in_root_folder}/ksads_diagnosesp201.xlsx')

    # Using only baseline data.
    ksads1 = ksads1.loc[ksads1["visit"] == "T1"]
    ksads2 = ksads2.loc[ksads2["visit"] == "T1"]
    ksads2.drop(columns=['collection_id',
                         'dataset_id', 'src_subject_id', 'interview_date',
                         'interview_age', 'sex', 'version_form', 'visit',
                         'adjustmentdisordercurrent', 'adjustmentdisorderpast',
                         'collection_title'], inplace=True)

    # Merging both datasets.
    ksads1 = merge_dataframes({'ksads1': ksads1, 'ksads2': ksads2},
                              index='subjectkey')

    # Little selector function where if any values in a row == 3 or 4
    # (just meet dx criteria or present severe), return 1
    # else 0.
    def selector(row):
        if 3 in row.values:
            return 1
        elif 4 in row.values:
            return 1
        return 0

    # Attention Deficit Hyperactivity Disorder.
    # Lumping together past and present ADHD.
    adhd_vars = [
        "adhdpast",
        "adhdcurrent",
        "adhdotherspeccurrent_dsm5",
        "adhdotherspecpast_dsm5",
        "adhdunspeccurrent_dsm5",
        "adhdunspecpast_dsm5",
    ]
    adhd_df = ksads1[adhd_vars]

    adhd_score = adhd_df.apply(selector, axis=1)

    # Anxiety disorders.
    # Using PD, agoraphobia, separation anxiety, social anxiety and
    # GAD (if one of them == 3 or 4, then 1 is returned).
    anx_vars = [
        "gadpast",
        "gadcurrent",
        "agoraphobiapast",
        "agoraphobiacurrent",
        "separationpast",
        "separationcurrent",
        "panicdisorderpast",
        "panicdisordercurrent",
        "socialphobiapast",
        "socialphobiacurrent",
        "anxietynospast",
        "anxietynoscurrent",
        "illnessanxietycurrent_dsm5",
        "illnessanxietypast_dsm5",
        "otherspecanxietycurrent_dsm5",
        "otherspecanxietypast_dsm5",
        "unspecanxietycurrent_dsm5",
        "unspecanxietypast_dsm5"
    ]
    anx_df = ksads1[anx_vars]

    anx_score = anx_df.apply(selector, axis=1)

    # Depressive disorders.
    # Using MDD present/past and DD present/past.
    dep_vars = ["mddpast",
                "mddcurrent",
                "depnospast",
                "depnoscurrent",
                "depressotherspeccurrent_dsm5",
                "depressotherspecpast_dsm5"]
    dep_df = ksads1[dep_vars]

    dep_score = dep_df.apply(selector, axis=1)

    # Obsessive-compulsive disorder.
    ocd_vars = [
        "ocdpast",
        "ocdcurrent",
        "ocdotherspeccurrent_dsm5",
        "ocdotherspecpast_dsm5",
        "ocdunspeccurrent_dsm5",
        "ocdunspecpast_dsm5"
    ]
    ocd_df = ksads1[ocd_vars]

    ocd_score = ocd_df.apply(selector, axis=1)

    # Oppositional defiant disorder.
    odd_vars = [
        "oddcurrent",
        "oddpast",
    ]
    odd_df = ksads1[odd_vars]

    odd_score = odd_df.apply(selector, axis=1)

    # Conduct disorder.
    cd_vars = [
        "conductcurrent",
        "conductpast",
        "disruptiveotherspeccurr_dsm5",
        "disruptiveotherspecpast_dsm5",
        "disruptiveunspeccurrent_dsm5",
        "disruptiveunspecpast_dsm5"
    ]
    cd_df = ksads1[cd_vars]

    cd_score = cd_df.apply(selector, axis=1)

    # Merging concatenated scores and fetching OCD, ODD, CD and PTSD at the
    # same time. All from the present variable.
    concat_output = pd.concat(
        [
            adhd_score,
            anx_score,
            cd_score,
            dep_score,
            odd_score,
            ocd_score,
        ],
        axis=1,
    )
    concat_output.index = ksads1.index
    concat_output.columns = [
        "ADHD",
        "AD",
        "CD",
        "DD",
        "ODD",
        "OCD",
    ]

    # Filtering df for values = 888 and considering them as NaNs.
    concat_output = concat_output.replace(888, np.nan)
    clean_output = concat_output.dropna()
    clean_output.to_excel(f"{output}", header=True, index=True)


if __name__ == "__main__":
    app()
