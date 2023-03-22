import pandas as pd

from noaa_metrics.aggregate_logs import (
    create_dataframe,
    df_to_csv,
    downloads_by_dataset,
    downloads_by_day,
    downloads_by_tld,
    email_full_report,
    get_period_summary_stats,
)
from noaa_metrics.constants.paths import (
    CDR_REPORT_OUTPUT_FILEPATH,
    JSON_OUTPUT_FILEPATH,
    REPORT_OUTPUT_DIR,
)
from noaa_metrics.misc import ProcessedLogFields


def filter_to_g02202(log_df: pd.DataFrame) -> pd.DataFrame:
    """Select only cdr dataset."""
    # TODO: look into regex for other versions of this code
    cdr_df = log_df.loc[log_df["dataset"] == "G02202_V4"]
    return cdr_df


def main():

    log_df = create_dataframe(JSON_OUTPUT_FILEPATH)
    cdr_df = filter_to_g02202(log_df)

    summary_df = get_period_summary_stats(cdr_df)
    by_dataset_df = downloads_by_dataset(cdr_df)
    by_day_df = downloads_by_day(cdr_df)
    by_location_df = downloads_by_tld(cdr_df)

    # breakpoint()
    summary_csv = df_to_csv(
        summary_df, "NOAA CDR Requests for March 2023\n\n", CDR_REPORT_OUTPUT_FILEPATH
    )
    by_day_csv = df_to_csv(
        by_day_df, "\nTransfers by Day\n\n", CDR_REPORT_OUTPUT_FILEPATH
    )
    by_dataset_csv = df_to_csv(
        by_dataset_df, "\nTransfers by Dataset\n\n", CDR_REPORT_OUTPUT_FILEPATH
    )
    all_csv = df_to_csv(
        by_location_df, "\nTransfers by Domain\n\n", CDR_REPORT_OUTPUT_FILEPATH
    )

    email_full_report(
        "/tmp/noaa-cdr-march-2023.csv",
        "noaa-cdr-march-2023.csv",
        "NOAA CDR Downloads March 2023",
    )


if __name__ == "__main__":
    main()
