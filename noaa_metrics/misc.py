import datetime as dt
from dataclasses import dataclass


@dataclass
class RawLogFields:
    date: dt.date
    ip_address: str
    download_bytes: int
    file_path: str


@dataclass
class ProcessedLogFields:
    date: dt.date
    ip_address: str
    download_bytes: int
    dataset: str
    ip_location: str
