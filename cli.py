import datetime as dt

import click
import luigi

from nsidc0102 import regions
from nsidc0102.luigitasks.clean import CleanOutput, CleanSource, CleanStaged
from nsidc0102.luigitasks.main import ProcessDateRange

region_choices = ['all'] + sorted(set(regions.load().shortname))


class DateType(click.ParamType):
    name = 'date'

    def convert(self, value, param, ctx):
        try:
            return dt.datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            self.fail(f'{value} is not a valid %Y-%m-%d date')


@click.group()
def cli():
    pass


@cli.command(
    short_help='Create images from MODIS source data',
)
@click.option(
    '-w',
    '--workers',
    help='Number of Luigi workers to use',
    type=int,
    default=1,
    show_default=True,
)
@click.option(
    '-s',
    '--start-date',
    help='Start date (YYYY-MM-DD)',
    type=DateType(),
)
@click.option(
    '-e',
    '--end-date',
    help='End date (YYYY-MM-DD)',
    type=DateType(),
)
@click.option(
    '-r',
    '--region',
    help='Region to process',
    type=click.Choice(region_choices),
    default='all',
    show_default=True,
)
def process(workers, start_date, end_date, region):
    """Create images from MODIS source data."""
    luigi.build(
        [
            ProcessDateRange(
                start_date=start_date,
                end_date=end_date,
                region=region,
            )
        ],
        workers=workers,
    )


@cli.command(
    short_help='Clean up working directories',
)
@click.option(
    '-w',
    '--workers',
    help='Number of Luigi workers to use',
    type=int,
    default=1,
    show_default=True,
)
@click.option(
    '-s',
    '--start-date',
    help='Start date (YYYY-MM-DD)',
    type=DateType(),
)
@click.option(
    '-e',
    '--end-date',
    help='End date (YYYY-MM-DD)',
    type=DateType(),
)
@click.option(
    '-i',
    '--source',
    is_flag=True,
    help='Clean input MODIS data',
)
@click.option(
    '-o',
    '--output',
    is_flag=True,
    help='Clean output images',
)
@click.option(
    '-d',
    '--staged',
    is_flag=True,
    help='Clean output images',
)
def clean(workers, start_date, end_date, source, output, staged):
    """Clean up working directories."""
    tasks = []
    if source:
        tasks.append(CleanSource())
    if output:
        tasks.append(CleanOutput(start_date, end_date))
    if staged:
        tasks.append(CleanStaged(start_date, end_date))

    luigi.build(tasks, workers=workers)


if __name__ == '__main__':
    cli()
