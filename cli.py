import datetime as dt

import click

# from nsidc0102.luigitasks.main import ProcessDateRange



class DateType(click.ParamType):
    name = 'date'

    def convert(self, value, param, ctx):
        try:
            return dt.datetime.strptime(value, '%Y-%m').date()
        except ValueError:
            self.fail(f'{value} is not a valid %Y-%m date')


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


if __name__ == '__main__':
    cli()
