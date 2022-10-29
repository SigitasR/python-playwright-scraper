import argparse
from typing import Dict


def get_commandline_parameters() -> Dict:
    parser = argparse.ArgumentParser(description='Crawler parameters')
    parser.add_argument('--category', type=str, help='Category URL to crawl. Default: %(default)s',
                        default='gerimai/stiprieji-alkoholiniai-gerimai/viskis')
    parser.add_argument('--batch-size', type=int,
                        help='Number of product links to be crawled by single browser instance. '
                             'Smaller batches will require more browser instances. Default: %(default)s',
                        default=30)
    parser.add_argument('--headless', action='store_true',
                        help='Run browsers in headless mode.')

    args = parser.parse_args()

    return args.__dict__
