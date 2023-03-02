import pandas as pd

from noaa_metrics.misc import ProcessedLogFields


def ingest_and_decode_json_file(JSON_OUTPUT_FILEPATH) -> str:
    return ""


def create_dataframe(log_json: str) -> pd.DataFrame:
    """Create dataframe from JSON file."""
    ...


def downloads_by_dataset(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by dataset.

    Counting distinct users, summing total volume, couting number of files.
    """
    ...


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
    log_df = ...

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
