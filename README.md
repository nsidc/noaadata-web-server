<img alt="NSIDC logo" src="https://nsidc.org/themes/custom/nsidc/logo.svg" width="150" />


# Noaa-web-server

Noaa-web-server is an NGINX server that hosts the NSIDC NOAA datasets. Metrics are run on these downloads using this repo: https://github.com/nsidc/noaadata-web-server-metrics

## Level of Support

* This repository is not actively supported by NSIDC but we welcome issue 
  submissions and pull requests in order to foster community contribution.

See the [LICENSE](LICENSE) for details on permissions and warranties. Please 
contact nsidc@nsidc.org for more information.

## Requirements

Docker + docker-compose

## Installation


## Usage


## Troubleshooting

If adding a new dataset that is not below `/NOAA/` it must be added to the `docker-compose.yml` under `volumes`. It will also need to be addressed in the `noaadata-web-server-metrics` repo in the `ingest_logs.py` file. 

## License

See [LICENSE](LICENSE).

## Code of Conduct

See [Code of Conduct](CODE_OF_CONDUCT.md).

## Credit

This software was developed by the National Snow and Ice Data Center with 
funding from multiple sources.
