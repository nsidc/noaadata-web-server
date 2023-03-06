import pandas as pd

from noaa_metrics.constants.paths import JSON_OUTPUT_FILEPATH
from noaa_metrics.misc import ProcessedLogFields


def create_dataframe(JSON_OUTPUT_FILEPATH) -> pd.DataFrame:
    """Create dataframe from JSON file."""
    log_df = pd.read_json(JSON_OUTPUT_FILEPATH)
    return log_df


def downloads_by_dataset(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by dataset.

    Counting distinct users, summing total volume, couting number of files.
    """
    by_dataset_df = ...
    return by_dataset_df


def downloads_by_day(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by date.

    Counting distinct users, summing total volume, couting number of files.
    """
    ...


def downloads_by_tld(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by date.

    Counting distinct users, summing total volume, couting number of files.
    """
    ...


def dataframe_as_text(by_dataset_df):
    ...


def email_full_report(full_report):
    ...


def main():

    log_df = create_dataframe(JSON_OUTPUT_FILEPATH)
    breakpoint()

    by_dataset_df = downloads_by_dataset(log_df)
    by_day_df = downloads_by_day(log_df)
    by_location_df = downloads_by_tld(log_df)

    by_dataset_text = dataframe_as_text(by_dataset_df)
    by_day_text = dataframe_as_text(...)
    by_tld_text = dataframe_as_text(...)
    full_report = f"{by_dataset_text}\n\n{by_day_text}\n\n{by_tld_text}"
    email_full_report(full_report)


if __name__ == "__main__":
    main()
