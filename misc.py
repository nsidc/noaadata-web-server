import datetime as dt
from typing import TypedDict

class RawLogFields(TypedDict):
    date: dt.date
    ip_address: str
    download_size: int
    file_path: str

class ProcessedLogFields(TypedDict):
    date: dt.date
    ip_address: str
    download_size: int
    dataset: str
    ip_location: str

