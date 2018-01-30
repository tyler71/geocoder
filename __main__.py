#!/usr/bin/env python3

import time
import argparse
import sys
import os
import configparser

from functools import partial

from utility.GeocodeAddress import GeocodeAddress
from utility.config import write_config
from utility.content_iterator import csv_iterator
from utility.output_formats import output_csv, output_json, output_python


def main():
    output_formats = {
        'python': output_python,
        'json':  output_json,
        'csv': output_csv,
    }
    parser = argparse.ArgumentParser(description="For each address in file, print Address, Latitude and Longitude of Address")
    parser.add_argument('-f', '--format',
                        choices=output_formats.keys(),
                        default='python',
                        help='Output format',)
    parser.add_argument('-c', '--column',
                        default='addresses',
                        help='Which header to parse, default "addresses"')
    parser.add_argument('--config', default=os.path.dirname(os.path.realpath(__file__)) + '/config')
    parser.add_argument('files', nargs='+')
    args = parser.parse_args()

    if os.path.isfile(args.config):
        config = configparser.ConfigParser()
        config.read(args.config)
        api_keys = dict(config['api_keys'])
    else:
        write_config(args.config)
        api_keys = dict()

    if args.format == 'csv':
        print('address', 'latitude', 'longitude', sep=',')

    geocoder = partial(GeocodeAddress, api_keys=api_keys)
    for file in args.files:
        for geo_obj in csv_iterator(geocoder, file, column=args.column):
            try:
                decoded = geo_obj.int()
            except LookupError:
                print('No Address found at {address}'.format(address=geo_obj.address), file=sys.stderr)
            except KeyboardInterrupt:
                print('Keyboard Interruption, exiting')
                sys.exit(1)

            geo_info = {
                'address': decoded.address,
                'latitude': decoded.latitude,
                'longitude': decoded.longitude,
            }
            print(output_formats[args.format](geo_info))
            time.sleep(0.2)


if __name__ == '__main__':
    main()
