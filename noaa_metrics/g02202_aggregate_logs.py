import pandas as pd

from noaa_metrics.aggregate_logs import (
    create_dataframe,
    downloads_by_dataset,
    downloads_by_day,
    downloads_by_tld,
)
from noaa_metrics.constants.paths import JSON_OUTPUT_FILEPATH, REPORT_OUTPUT_DIR
from noaa_metrics.misc import ProcessedLogFields


def filter_to_g02202(log_df: pd.DataFrame) -> pd.DataFrame:
    """Select only cdr dataset."""


def main():

    log_df = create_dataframe(JSON_OUTPUT_FILEPATH)

    by_dataset_df = downloads_by_dataset(log_df)
    by_day_df = downloads_by_day(log_df)
    by_location_df = downloads_by_tld(log_df)

    by_dataset_text = dataframe_as_text(by_dataset_df)
    by_day_text = dataframe_as_text(by_day_df)
    by_tld_text = dataframe_as_text(by_location_df)
    full_report = f"{by_dataset_text}\n\n{by_day_text}\n\n{by_tld_text}"
    breakpoint()
    email_full_report(full_report)


if __name__ == "__main__":
    main()
