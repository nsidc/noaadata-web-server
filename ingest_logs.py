import pathlib as path
import country_codes
from misc import RawLogFields, ProcessedLogFields

# Create a TypedDict with the fields we will use in our script
def get_log_lines() -> list[str]:
    """Get log entries as a list of strings.
    
    From /share/logs/noaa-web/download.log.
    """
    ...

def lines_to_raw_fields(log_lines: list[str]) -> list[RawLogFields]:
    """Convert log lines into self describing data structures."""
    ...

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
    log_dicts = process_raw_fields(log_dicts_raw)
    write_log_dicts_to_file(log_dicts)

if __name__ == '__main__':
    main()
