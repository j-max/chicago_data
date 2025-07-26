import sys
import os

import pandas as pd

base_dir = os.getcwd()
repo_name = "chicago_data"
root_path =base_dir.split(repo_name)[0] + repo_name 
sys.path.append(root_path)
from src.data_portal_api import get_portal_data
from src.schools.schools import calculate_total_survey_score

progress_report_2324= 'https://data.cityofchicago.org/resource/2dn2-x66j.json'
pr_df = get_portal_data(progress_report_2324)

school_profile_2324 = "https://data.cityofchicago.org/resource/cu4u-b4d9.json"
sp_df = get_portal_data(school_profile_2324)


def calculate_total_survey_score(progress_report_df: pd.DataFrame) -> pd.DataFrame:

    """
    Assign numerical values to school surveys in progress report

    Arguments: DataFrame: School progress report 
    """

    map_survey_scores = {
    "NOT ENOUGH DATA": 0,
    "VERY WEAK": 1,
    "WEAK": 2,
    "NEUTRAL": 3,
    "STRONG": 4,
    "VERY STRONG": 5
    }

    school_surveys = [
        "school_survey_ambitious",
        "school_survey_effective",
        "school_survey_collaborative",
        "school_survey_involved",
        "school_survey_safety"
    ] 
    
    for survey in school_surveys:
        progress_report_df["score" + "_" + survey] = progress_report_df[survey].map(map_survey_scores)

    progress_report_df["pr_total_survey_score"] = (
        progress_report_df["score_school_survey_ambitious"]
        + progress_report_df["score_school_survey_effective"]
        + progress_report_df["score_school_survey_collaborative"]
        + progress_report_df["score_school_survey_involved"]
        + progress_report_df["score_school_survey_safety"]
    )

    return progress_report_df


calculate_total_survey_score(pr_df)

pr_df.shape
pr_df.columns
# In the 2023-24 school year, there are 650 unique school ID's
pr_df["school_id"].nunique()

# There are 471 Elementary schools, 171 High Schools, and 8 Middle Schools
pr_df["primary_category"].value_counts()

########## Overall numbers ##########
list(pr_df.columns)

student_count_fields = [
    'student_count_total',
    'student_count_low_income',
    'student_count_special_ed',
    'student_count_english_learners',
    'student_count_black',
    'student_count_hispanic',
    'student_count_white',
    'student_count_asian',
    'student_count_native_american',
    'student_count_other_ethnicity',
    'student_count_asian_pacific',
    'student_count_multi',
    'student_count_hawaiian_pacific',
    'student_count_ethnicity_not'
]
 
# Average pop across all schools
sp_df["student_count_total"].astype(int).mean()

##### Population Numbers #####
sp_df["student_count_total"].astype(int).mean()

# Make all student count totals integers
for col in student_count_fields:
    print(col, sp_df[col].astype(int).mean())
    sp_df[col] = sp_df[col].astype(int)

sp_df.groupby("primary_category")[student_count_fields].mean()

########## Chase Elementary ##########
# Chase elemntary is the school down the block from me
chase = pr_df[pr_df["long_name"].str.contains("Chase")]

# Chase has a 41.2% chronic truancy percentage
chase["chronic_truancy_pct"]

# The average chronic trancy across cps is 45%, however.
pr_df["chronic_truancy_pct"].astype(float).mean()

