import datetime as dt

import click

class DateType(click.ParamType):
    name = 'date'

    def __init__(self, formats=None):
        self.formats = formats or [
            '%Y-%m-%d',
            '%Y%m%d',
        ]

    def __repr__(self):
        return 'Date'

    def get_metavar(self, param):
        formats_str = "|".join(self.formats)
        return f'[{formats_str}]'

    def convert(self, value, param, ctx):
        for fmt in self.formats:
            try:
                return dt.datetime.strptime(value, fmt).date()
            except ValueError:
                continue

        self.fail(f'{value} is not a valid date. Expected one of: {self.formats}')


@click.group()
def cli():
    pass


@cli.command(
    short_help='Generate NOAA downlaods metric report.',
)
@click.option(
    '-s',
    '--start-date',
    help='Start date (YYYY-MM)',
    type=DateType(),
)
@click.option(
    '-e',
    '--end-date',
    help='End date (YYYY-MM)',
    type=DateType(),
)
@click.option(
    '-m',
    '--mail-to',
    help='',
    type=click.Choice(region_choices),
    default='all',
    show_default=True,
)
def process(start_date, end_date, mail-to):
    """Generate NOAA downlaods metric report."""


if __name__ == '__main__':
    cli()
