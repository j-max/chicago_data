


def calculate_total_survey_score(progress_report_df):

    map_survey_scores = {
    "NOT ENOUGH DATA": 0,
    "VERY WEAK": 1,
    "WEAK": 2,
    "NEUTRAL": 3,
    "STRONG": 4,
    "VERY STRONG": 5
    }

    progress_report_df["score_school_survey_ambitious"] = progress_report_df["school_survey_ambitious"].map(map_survey_scores)
    progress_report_df["score_school_survey_effective"] = progress_report_df["school_survey_effective"].map(map_survey_scores)
    progress_report_df["score_school_survey_collaborative"] = progress_report_df["school_survey_collaborative"].map(map_survey_scores)
    progress_report_df["score_school_survey_involved"] = progress_report_df["school_survey_involved"].map(map_survey_scores)
    progress_report_df["score_school_survey_safety"] = progress_report_df["school_survey_safety"].map(map_survey_scores)

    progress_report_df["pr_total_survey_score"] = (
        progress_report_df["score_school_survey_ambitious"]
        + progress_report_df["score_school_survey_effective"]
        + progress_report_df["score_school_survey_collaborative"]
        + progress_report_df["score_school_survey_involved"]
        + progress_report_df["score_school_survey_safety"]
    )

    return progress_report_df