from pathlib import Path
import datetime as dt

# import country_codes
from misc import RawLogFields, ProcessedLogFields


# Create a TypedDict with the fields we will use in our script
def get_log_lines() -> list[str]:
    """Get log entries as a list of strings.
    
    From /share/logs/noaa-web/download.log.
    """
    log_file = Path('/share/logs/noaa-web-all/integration/download.log')
    log_lines = []
    with open(log_file) as file:
        log_lines = [line.rstrip() for line in file]

    return log_lines


def lines_to_raw_fields(log_lines: list[str]) -> list[RawLogFields]:
    """Convert log lines into self describing data structures."""
    split_line = log_lines[0].split()
    date = dt.datetime.strptime(split_line[0].strip('['), '%d/%b/%Y:%H:%M:%S'),
    RawLogfields: RawLogFields = {
        date : date,
        ip_address : split_line[3],
        download_size : int(split_line[4]),
        file_path : split_line[4]
    }


def process_raw_fields(log_dicts_raw: list[RawLogFields]) -> list[ProcessedLogFields]:
    """Enrich raw log data to include relevant information."""
    ...

def write_log_dicts_to_file(log_dicts: list[ProcessedLogFields]) -> None:
    """Create monthly log processed data file."""
    # TODO: This should take a month.
    ...

#Read in the log file
def main():
    ...
    log_lines = get_log_lines()
    log_dicts_raw = lines_to_raw_fields(log_lines)
    breakpoint()
    log_dicts = process_raw_fields(log_dicts_raw)
    write_log_dicts_to_file(log_dicts)

if __name__ == '__main__':
    main()
