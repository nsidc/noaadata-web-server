import smtplib
from email.message import EmailMessage

import pandas as pd

from noaa_metrics.constants.paths import JSON_OUTPUT_FILEPATH, REPORT_OUTPUT_DIR
from noaa_metrics.misc import ProcessedLogFields


def create_dataframe(JSON_OUTPUT_FILEPATH) -> pd.DataFrame:
    """Create dataframe from JSON file."""
    log_df = pd.read_json(JSON_OUTPUT_FILEPATH)
    return log_df


def get_period_summary_starts(log_df: pd.DataFrame):
    """Collect stats for entire period."""
    ...


def downloads_by_dataset(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by dataset.

    Counting distinct users, summing total volume, couting number of files.
    """
    by_dataset_df = log_df.groupby("dataset").agg(
        {"ip_address": ["nunique"], "file_path": ["count"], "download_bytes": ["sum"]}
    )
    by_dataset_df.columns.set_levels(
        ["Distinct Users", "Files Sent", "Download Volume (MB)"], level=1, inplace=True
    )
    by_dataset_df.columns = by_dataset_df.columns.droplevel(0)
    by_dataset_df.index = by_dataset_df.index.rename("Dataset")
    by_dataset_df.loc["Total"] = by_dataset_df.sum()
    return by_dataset_df


def downloads_by_day(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by date.

    Counting distinct users, summing total volume, couting number of files.
    """
    log_df["date"] = log_df["date"].dt.strftime("%d %b %Y")
    by_day_df = log_df.groupby("date").agg(
        {"ip_address": ["nunique"], "file_path": ["count"], "download_bytes": ["sum"]}
    )
    by_day_df.columns.set_levels(
        ["Distinct Users", "Files Sent", "Download Volume (MB)"], level=1, inplace=True
    )
    by_day_df.columns = by_day_df.columns.droplevel(0)
    by_day_df.index = by_day_df.index.rename("Date")
    by_day_df.loc["Total"] = by_day_df.sum()
    return by_day_df


def downloads_by_tld(log_df: pd.DataFrame) -> pd.DataFrame:
    """Group log_df by date.

    Counting distinct users, summing total volume, couting number of files.
    """
    ...
    by_location_df = log_df.groupby("ip_location").agg(
        {"ip_address": ["nunique"], "file_path": ["count"], "download_bytes": ["sum"]}
    )
    by_location_df.columns.set_levels(
        ["Distinct Users", "Files Sent", "Download Volume (MB)"], level=1, inplace=True
    )
    by_location_df.columns = by_location_df.columns.droplevel(0)
    by_location_df.index = by_location_df.index.rename("Domain Type")
    by_location_df.loc["Total"] = by_location_df.sum()
    return by_location_df


def df_to_csv(df: pd.DataFrame, header: str):
    with open("/tmp/noaa-march-2023.csv", "a") as file:
        file.write(header)
        df.to_csv(file, header=True, index=True)


def email_full_report(full_report):
    msg = EmailMessage()
    msg["From"] = "archive@nusnow.colorado.edu"
    msg["To"] = "roma8902@colorado.edu"  # "ann.windnagel@colorado.edu"
    msg["Subject"] = "NOAA Downloads March 2023"

    with open(full_report) as fp:
        metrics_data = fp.read()
    msg.add_attachment(metrics_data, filename="noaa-march-2023.csv")
    with smtplib.SMTP("localhost") as s:
        s.send_message(msg)


def main():

    log_df = create_dataframe(JSON_OUTPUT_FILEPATH)

    by_dataset_df = downloads_by_dataset(log_df)
    by_day_df = downloads_by_day(log_df)
    by_location_df = downloads_by_tld(log_df)

    by_day_csv = df_to_csv(by_day_df, "Transfers by Day\n\n")
    by_dataset_csv = df_to_csv(by_dataset_df, "\nTransfers by Dataset\n\n")
    all_csv = df_to_csv(by_location_df, "\nTransfers by Domain\n\n")

    email_full_report("/tmp/noaa-march-2023.csv")
    ...


if __name__ == "__main__":
    main()
